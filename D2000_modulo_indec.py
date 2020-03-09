# MODULO INDEC2
#

# Abre la serie del CPI
#df = open_excel("C:\GCB_CAPITAL2\INPUT_MANUAL", "ARG", ".xlsx")

# Transforma la serie en serie de tiempo
#df= serie_de_tiempo(df)

# Calcula la diferencia entre el ultimo punto de la serie y el anterior
#df["prueba"]=df["CPI"].diff()

# Calcula la diferencia porcentual entre el ultimo punto de la serie y el anterior
#df["cpi_monthly_variation"]=df["CPI"].pct_change()

# importa calendario
import calendar
# Muestra los dias que incluye cada mes
#df['days_in_month'] = df.index.map(lambda val: calendar.monthrange(val.year, val.month)[1])





# Calcula la variacion diaria 
#df['daily_variation'] = (1+df["cpi_monthly_variation"])**(1/df["days_in_month"])


#--------------------------------------------------------------------



#start_date = df.index.min() - pd.DateOffset(day=1)
#end_date = df.index.max() + pd.DateOffset(day=31)

#dates = pd.date_range(start_date, end_date, freq='D')
#dates.name = 'Fecha'

# Para rellenar con none
#df2 = df.reindex(dates, method=None)


# Para rellelar con el ultimo dato valido hasta el proximo valido
#df3 = df.reindex(dates, method='backfill')
#df3= df3.reset_index()
# Dias transcurridos del mes
#df3['Nro_de_dia'] = df3['Fecha'].map(lambda x: str(x)[8:10])
#df3['Nro_de_dia']=df3['Nro_de_dia'].astype(int)
#df3['days_in_month']=df3['days_in_month'].astype(int)
#df3["Comp"]=(df3['daily_variation'])**(df3['Nro_de_dia']/df3['days_in_month'])
#df3["CPI_new"]=df3["CPI"]/(df3["Comp"])
#df3=df3.set_index("Fecha")
#df3["CPI"] = None
#df3["CPI"]=df["CPI"]
#df3["CPI_ultimate"]= 0
#df3=df3.fillna(0)
#filter = (df3['CPI'] != 0)
#df3.loc[filter, 'CPI_ultimate'] = df3['CPI']

#filter = (df3['CPI'] == 0)
#df3.loc[filter, 'CPI_ultimate'] = df3['CPI_new']

#save_file_generico(df3, "C:\GCB_CAPITAL2\OUTPUT", "CPI_ARG_", "PRUEBA", ".xlsx")

def transform_monthly_serie_to_daily_series(panda_dataframe_time_series, series_name):
    # tiene que ser una serie de tiempo
    # que tenga los datos asignados al ultimo dia de cada mes
    #
    df["monthly_variation"]=df[series_name].pct_change()    
    # importa calendario
    import calendar
    # Muestra los dias que incluye cada mes
    df['days_in_month'] = df.index.map(lambda val: calendar.monthrange(val.year, val.month)[1])
    # Calcula la variacion diaria 
    df['daily_variation'] = (1+df["monthly_variation"])**(1/df["days_in_month"])
    #
    start_date = df.index.min() - pd.DateOffset(day=1)
    end_date = df.index.max() + pd.DateOffset(day=31)
    dates = pd.date_range(start_date, end_date, freq='D')
    dates.name = 'Fecha'
    # Para rellenar con none
    df2 = df.reindex(dates, method=None)
    # Para rellelar con el ultimo dato valido hasta el proximo valido
    df3 = df.reindex(dates, method='backfill')
    df3= df3.reset_index()
    # Dias transcurridos del mes
    df3['Nro_de_dia'] = df3['Fecha'].map(lambda x: str(x)[8:10])
    df3['Nro_de_dia']=df3['Nro_de_dia'].astype(int)
    df3['days_in_month']=df3['days_in_month'].astype(int)
    df3["Factor_de_capitalizacion"]=(df3['daily_variation'])**((df3['days_in_month']-df3['Nro_de_dia'])/df3['days_in_month'])
    #df3[series_name+"_new"]=df3[series_name]/(df3["Factor_de_capitalizacion"])
    df3[series_name+"_new"]=df3[series_name]/(df3['daily_variation']**(df3['days_in_month']-df3['Nro_de_dia']))
    df3=df3.set_index("Fecha")
    #
    # 
    #
    df3[series_name] = None
    #df3[series_name]=df["CPI"]
    df3[series_name + "_definitivo"]= 0
    df3=df3.fillna(0)
    filter = (df3[series_name] != 0)
    df3.loc[filter, series_name + "_definitivo"] = df3[series_name]
    filter = (df3[series_name] == 0)
    df3.loc[filter, series_name + "_definitivo"] = df3[series_name+"_new"]
    return df3

#df2= transform_monthly_serie_to_daily_series(df, "CPI")

#save_file_generico(df2, "C:\GCB_CAPITAL2\CPI", "CPI_ARG", "", ".xlsx")


def arma_cpi_pais(pais):
    # Abre la serie del CPI
    df = open_excel(original_source + "\INPUT_MANUAL", pais, ".xlsx")
    # Transforma la serie en serie de tiempo
    df= serie_de_tiempo(df)
    #
    #
    df2= transform_monthly_serie_to_daily_series(df, "CPI")
    #
    # ARMA EL DATAFRAME DE OUTPUT
    # 
    df3 = df2[['CPI_new', ]]
    #
    df3.rename(columns = {'CPI_new':'CPI'}, inplace=True)
    #
    # Calcula la diferencia porcentual entre el ultimo punto de la serie y el anterior
    #df3["cpi_monthly_variation"]=df3["CPI"].pct_change()
    #
    save_file_generico(df3, original_source + "\CPI", "CPI_"+pais, "", ".xlsx")

#arma_cpi_pais("ARG")
#arma_cpi_pais("USA")

#df1 = open_excel(original_source + "\INPUT_MANUAL", "ARG", ".xlsx")
#df1= serie_de_tiempo(df)
# Crea un dataframe solo con la columna CPI (muy distinto a solo poner un par de corchetes y se transforma en una serie
#df1 = df1[["CPI"]]
#df2= open_excel(original_source + "\INPUT_MANUAL", "USA", ".xlsx")
#df2= serie_de_tiempo(df2)
#df2 = df2[["CPI"]]

#df3 = df1.merge(df2)

#merge=pd.merge(df1, df2, how='outer', left_index=True, right_index=True)  
#merge.rename(columns = {'CPI_x':'CPI_ARG'}, inplace=True)
#merge.rename(columns = {'CPI_y':'CPI_USA'}, inplace=True)



# Calcula la diferencia porcentual entre el ultimo punto de la serie y el anterior solo para la columna CPI_x
#merge["cpi_monthly_variation_ARG"]=merge["CPI_ARG"].pct_change()
# Calcula la diferencia porcentual entre el ultimo punto de la serie y el anterior solo para la columna CPI_y
#merge["cpi_monthly_variation_USA"]=merge["CPI_USA"].pct_change()

# Calcula el diferencial mensual de inflacion
#merge['Monthly_CPI_Differential_USD_ARS'] = merge["cpi_monthly_variation_ARG"]-merge["cpi_monthly_variation_USA"]


#merge['Monthly_CPI_Differential_USD_ARS'] = merge["cpi_monthly_variation_ARG"]-merge["cpi_monthly_variation_USA"]
#merge['Factor'] = merge['Monthly_CPI_Differential_USD_ARS']+1

#merge['Theoretic_Monthly_PPP_USD_ARS'] = merge['Monthly_CPI_Differential_USD_ARS'].shift(-1)
#merge['Accumulated_Factor'] = merge['Factor'].cumprod()


#
#merge['USDARS']=0
# convert column "USDARS" to float
#merge = merge.astype({"USDARS": np.float16})
#merge['USDARS'].ix["2002-01-31"]=2.050
#merge['USDARS'].loc["2002-01-31"]=2.050
#merge.ix["2002-01-31"]
#merge=merge.reset_index()
#merge[
#merge.at[480,"USDARS"] = 2.050
#merge["USDARS"].loc[480]=2.050
#merge.loc[480]


#merge.ix[(merge["Fecha"] == "2002-01-31")]
#posicion_indice=list(merge.index[(merge["Fecha"] == "2002-01-31")].values)
#valor_indice=posicion_indice[0]

# Para obtener la posicion de la fecha
#merge["Fecha"][(merge["Fecha"] == "2002-01-31")]


# Itera multiplicando por la columna factor
#for i in range(481, len(merge)):
#    merge.loc[i, 'USDARS'] = (merge.loc[i-1, 'USDARS'] * merge.loc[i, 'Factor']) 

# Vuelve a setear la serie como serie de tiempo
#merge.set_index("Fecha")

#save_file_generico(merge, original_source + "\CPI", "USDARS_PPP", "", ".xlsx")






#merge.index[merge['Fecha'] == "2002-01-31"]

#merge["Theoretic_Monthly_PPP_USD_ARS"]=0
#merge["Theoretic_Monthly_PPP_USD_ARS"]["2001-12-31"]= 2.05

#merge['Theoretic_Monthly_PPP_USD_ARS']["2001-12-31"]= 2.05

#merge.loc[(merge["Fecha"] == "2001-01-31") & (df["C"] == 900), "A"]



def genera_tipo_de_cambio_de_paridad(cod_pais_1, cod_pais_2, fecha_base_de_tipo_de_cambio):
    #
    df1 = open_excel(original_source + "\INPUT_MANUAL", "CPI_"+ cod_pais_1 + "_MANUAL", ".xlsx")
    df1= serie_de_tiempo(df)
    # Crea un dataframe solo con la columna CPI (muy distinto a solo poner un par de corchetes y se transforma en una serie
    df1 = df1[["CPI"]]
    df2= open_excel(original_source + "\INPUT_MANUAL", "CPI_"+ cod_pais_2 + "_MANUAL", ".xlsx")
    df2= serie_de_tiempo(df2)
    df2 = df2[["CPI"]]
    #
    merge=pd.merge(df1, df2, how='outer', left_index=True, right_index=True)  
    merge.rename(columns = {'CPI_x':'CPI_'+cod_pais_1}, inplace=True)
    merge.rename(columns = {'CPI_y':'CPI_'+cod_pais_2}, inplace=True)
    # Calcula la diferencia porcentual entre el ultimo punto de la serie y el anterior solo para la columna CPI_x
    merge["cpi_monthly_variation_"+cod_pais_1]=merge["CPI_"+cod_pais_1].pct_change()
    # Calcula la diferencia porcentual entre el ultimo punto de la serie y el anterior solo para la columna CPI_y
    merge["cpi_monthly_variation_"+cod_pais_2]=merge["CPI_"+cod_pais_2].pct_change()
    #
    #
    # Calcula el diferencial mensual de inflacion
    #
    currency_cod_1 = transforma_pais_en_moneda(cod_pais_1)
    currency_cod_2 = transforma_pais_en_moneda(cod_pais_2)
    #
    merge['Monthly_CPI_Differential_' + currency_cod_2 + '_' + currency_cod_1] = merge["cpi_monthly_variation_"+cod_pais_1]-merge["cpi_monthly_variation_"+cod_pais_2]
    merge['Factor'] = merge['Monthly_CPI_Differential_' + currency_cod_2 + '_' + currency_cod_1]+1
    #
    # FILAS A BORRAR
    #merge['Theoretic_Monthly_PPP_USD_ARS'] = merge['Monthly_CPI_Differential_' + currency_cod_2 + '_' + currency_cod_1].shift(-1)
    #merge['Accumulated_Factor'] = merge['Factor'].cumprod()
    #
    # Prepara la columna con el tipo de cambio teorico
    #
    merge[currency_cod_2 + currency_cod_1]=0
    #
    # convert column "USDARS" to float
    #merge = merge.astype({"USDARS": np.float16})
    #merge['USDARS'].ix["2002-01-31"]=2.050
    #
    # Carga en memoria la serie del tipo de cambio 
    #
    df4 = open_excel(original_source + "\CURRENCIES", "USDARS", ".xlsx")
    df4 = df4.set_index("Fecha")
    #
    # Busca el tipo de cambio de la fecha base a ser ajustado por inflacion 
    #
    # MODO 1 - Funcionaba cuando se sacaba una lista porque habia multiples datos para una misma fech
    #df4["2002-01-31"]
    #
    # a
    #valores = df4[fecha_base_de_tipo_de_cambio]["tc_nominal"]
    #valores[0]
    #
    # MODO 2 - 
    #
    valores = df4.ix[fecha_base_de_tipo_de_cambio]["tc_nominal"]
    #
    # Asigna el tipo de cambio a la fecha correspondiente en la columna
    #
    # FUNCIONABA CON MODO 1
    #merge[currency_cod_2 + currency_cod_1].loc[fecha_base_de_tipo_de_cambio]=float(valores[0])
    # MODO 2
    merge[currency_cod_2 + currency_cod_1].loc[fecha_base_de_tipo_de_cambio]=float(valores)
    #
    # Verifica que el valor haya cambiado al tipo de cambio en la fecha 
    #merge.ix["2002-01-31"]
    #
    merge=merge.reset_index()
    #
    # Busca el nro de posicion en el indice de la fecha correspondiente al tipo de cambio nominal con el que se empezo a ajustar
    posicion_indice=list(merge.index[(merge["Fecha"] == fecha_base_de_tipo_de_cambio)].values)
    # Muestra el numero de posicion
    valor_indice=posicion_indice[0]
    #
    # Itera multiplicando por la columna factor
    for i in range((valor_indice+1), len(merge)):
        merge.loc[i, currency_cod_2 + currency_cod_1] = (merge.loc[i-1, 'USDARS'] * merge.loc[i, 'Factor']) 
    # Vuelve a setear la serie como serie de tiempo
    #
    merge=merge.set_index("Fecha")
    #
    # Graba la matriz
    save_file_generico(merge, original_source + "\CPI", currency_cod_2 + currency_cod_1+"_PPP", "_MONTHLY", ".xlsx")



#genera_tipo_de_cambio_de_paridad("ARG", "USA", "2002-01-31")
#genera_tipo_de_cambio_de_paridad("ARG", "USA", "2018-05-31")

def transforma_pais_en_moneda(cod_pais):
    # Transforma en alpha-3 code. Tambien existe Alpha-2 code que serian 2 letras.
    dictionary = {'ARG':'ARS', 
    'AUS':'AUD', 
    'BRA':'BRL',
    'BOL':'BOB',
    'CAN':'CAD',
    'CHE':'CHF',
    'CHL':'CLP',
    'CHN':'CNY',
    'COL':'COP',
    'DEU':'EUR',
    'ECU':'ECS',
    'FRA':'EUR',
    'GBR':'GBP',
    'GRC':'EUR',
    'IND':'INR',
    'JPN':'JPY',
    'MEX':'MXN',
    'PRY':'PYG',
    'RUS':'RUB',
    'TUR':'TRY',
    'URY':'UYU',
    'USA':'USD'}
    return dictionary[cod_pais]

#transforma_pais_en_moneda("ARG")


def prepara_USDARS_a_partir_del_USDARS_LIBRE():
    df = open_excel(original_source + "\CURRENCIES", "USDARS_LIBRE", ".xlsx")
    df = df.set_index("Fecha")
    df["Especie"]="USDARS"
    # Eliminacion de duplicados del indice
    #
    # 1. Reseteo el indice para poder operar sobre las columnas    
    df = df.reset_index()
    # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
    df = df.drop_duplicates(subset='Fecha', keep='last')
    # 3. Vuelvo a establecer la columna fecha como indice
    df = df.set_index('Fecha', inplace=False)
    #
    # Renombra columnas
    #df.rename(columns = {'':'CPI_'+cod_pais_2}, inplace=True)
    #
    # Graba el dataframe
    save_file_generico(df, original_source + "\CURRENCIES", "USDARS", "", ".xlsx")


#prepara_USDARS_a_partir_del_USDARS_LIBRE()



def prepara_serie_diaria_de_tipo_de_cambio_ppp(cod_moneda1, cod_moneda2, fecha_del_ultimo_punto):
    import datetime
    # Carga el archivo con la serie mensual
    df1 = open_excel(original_source + "\CPI", cod_moneda1+cod_moneda2+"_PPP_MONTHLY", ".xlsx")
    # Transforma en serie de tiempo
    df1= serie_de_tiempo(df)
    # Transforma la serie en diaria
    df2= transform_monthly_serie_to_daily_series(df1, "USDARS")
    #
    #
    # SET END DATE
    end_year = int(fecha_del_ultimo_punto[0:4])
    end_month = int(fecha_del_ultimo_punto[6:7])
    end_day =  int(fecha_del_ultimo_punto[8:10])
    #
    # CHECK END DATE
    #print(fecha_del_ultimo_punto)
    #print(fecha_del_ultimo_punto)
    #print(fecha_del_ultimo_punto)
    #
    end = datetime.datetime(end_year, end_month, end_day+1)
    #
    #
    df3 = df2[df2.index<end]
    #
    #
    # ARMA EL FORMATO DE LA SERIE DIARIA
    #
    df3.rename(columns = {cod_moneda1+cod_moneda2+"_definitivo":cod_moneda1+cod_moneda2+"_PPP"}, inplace=True)
    #
    df4 = df3[[ cod_moneda1+cod_moneda2+"_PPP" ]] 
    df4["Especie"] = cod_moneda1+cod_moneda2+"_PPP"
    df4.rename(columns = {cod_moneda1+cod_moneda2+"_PPP":"tc_real"}, inplace=True)
    #
    save_file_generico(df4, original_source + "\CURRENCIES", cod_moneda1+cod_moneda2, "_PPP", ".xlsx")
    #
    return

#df3 = prepara_serie_diaria_de_tipo_de_cambio_ppp("USD", "ARS", "2020-02-05")

