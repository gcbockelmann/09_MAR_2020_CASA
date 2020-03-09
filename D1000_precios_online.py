

## PRECIOS ONLINE


def ultimo_precio_operado_de_un_equity_traido_de_yahoo(ticker):
    import pandas_datareader as web
    import datetime
    import requests
    session= requests.Session()
    session.verify = False # SSL   verification will be turned OFF, requests will give you an InsecureR questWarning
    global df
    start = datetime.datetime(2020, 1, 1)
    end = datetime.date.today()
    df = web.DataReader(ticker, 'yahoo', start, end, session=session)
    return df

#ultimo_precio_operado_de_un_equity_traido_de_yahoo("TXAR.BA")


### ACTUALIZA SERIE DE PRECIOS SPCH CON EL ULTIMO PRECIO ONLINE DE YAHOO FINANCE
def update_last_price(ticker):
    global df, df2
    #dictionary = {"ALUA":"ALUA.BA", "CTIO":"CTIO.BA", "TXAR":"TXAR.BA"}        
    dictionary = {'AGRO':'AGRO.BA', 
    'ALUA':'ALUA.BA',
    'APBR':'APBR.BA', 
    'AUSO':'AUSO.BA',
    'BBAR':'BBAR.BA',
    'BHIP':'BHIP.BA',
    'BMA':'BMA.BA',
    'BOLT':'BOLT.BA', 
    'BPAT':'BPAT.BA', 
    'BRIO6':'BRIO.BA', 
    'BRIO':'BRIO.BA', 
    'BYMA':'BYMA.BA', 
    'CADO':'CADO.BA', 
    'CAPX':'CAPX.BA', 
    'CARC':'CARC.BA', 
    'CECO2':'CECO".BA', 
    'CELU':'CELU.BA', 
    'CEPU':'CEPU.BA', 
    'CGPA2':'CGPA.BA', 
    'COME':'COME.BA', 
    'CRES':'CRES.BA', 
    'CTIO':'CTIO.BA', 
    'CVH':'CVH.BA', 
    'DGCU2':'DGCU2.BA', 
    'DOME':'DOME.BA', 
    'DYCA':'DYCA.BA', 
    'EDN':'EDN.BA', 
    'FERR':'FERR.BA', 
    'FIPL':'FIPL.BA', 
    'GAMI':'GAMI.BA', 
    'GARO':'GARO.BA', 
    'GBAN':'GBAN.BA', 
    'GCLA':'GCLA.BA', 
    'GGAL':'GGAL.BA', 
    'GOLD':'GOLD.BA',
    'GRIM':'GRIM.BA',
    'HARG':'HARG.BA', 
    'HAVA':'HAVA.BA', 
    'INDU':'INDU.BA', 
    'INTR':'INTR.BA', 
    'INVJ':'INVJ.BA', 
    'IRCP':'IRCP.BA', 
    'IRSA':'IRSA.BA', 
    'LEDE':'LEDE.BA', 
    'LOMA':'LOMA.BA', 
    'LONG':'LONG.BA', 
    'METR':'METR.BA', 
    'MIRG':'MIRG.BA', 
    'MOLA5':'MOLA5.BA', 
    'MOLA':'MOLA.BA', 
    'MOLI5':'MOLI5.BA', 
    'MOLI':'MOLI.BA', 
    'MORI':'MORI.BA', 
    'OEST':'OEST.BA', 
    'PAMP':'PAMP.BA', 
    'PATA':'PATA.BA', 
    'PATY':'PATY.BA', 
    'PGR':'PGR.BA', 
    'POLL':'POLL.BA', 
    'RICH':'RICH.BA', 
    'RIGO':'RIGO.BA', 
    'ROSE':'ROSE.BA', 
    'SAMI':'SAMI.BA', 
    'SEMI':'SEMI.BA', 
    'SUPV':'SUPV.BA', 
    'TECO2':'TECO2.BA', 
    'TGLT':'TGLT.BA', 
    'TGNO4':'TGNO4.BA', 
    'TGSU2':'TGSU2.BA', 
    'TRAN':'TRAN.BA', 
    'TS':'TS.BA', 
    'TXAR':'TXAR.BA', 
    'VALO':'VALO.BA', 
    'YPFD':'YPFD.BA'}
    ultimo_precio_operado_de_un_equity_traido_de_yahoo(dictionary[ticker])
    df2 = df
    #
    #
    ### 
    ### El ticker se debe ingresar como una string
    open_file_spch(original_source + "\SPCH", "SERIE_CORRIENTE_"+ticker, ".xlsx")
    #
    ispch = df
    idata = df2
    #
    #Para checkear que las 2 listas de nombres son iguales > al devolver True.
    df2=df2.reset_index()
    df2.rename(columns = {'Date':'Fecha'}, inplace=True)
    df2.rename(columns = {'High':'Maximo'}, inplace=True)
    df2.rename(columns = {'Low':'Minimo'}, inplace=True)
    df2.rename(columns = {'Open':'Apertura'}, inplace=True)
    df2.rename(columns = {'Close':'Cierre_del_dia'}, inplace=True)
    df2.rename(columns = {'Volume':'Volumen_Nominal'}, inplace=True)
    df2.rename(columns = {'Adj Close':'Adj_Close'}, inplace=True)
    df2 = df2.set_index("Fecha")
    df2 = df2.drop(columns=['Adj_Close'])
    df = pd.concat([df2,df],sort=False).drop_duplicates()    
    df = df.sort_index()       
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
    #
    # Eliminacion de duplicados del indice
    #
    # 1. Reseteo el indice para poder operar sobre las columnas    
    df = df.reset_index()
    # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
    df = df.drop_duplicates(subset='Fecha', keep='last')
    # 3. Vuelvo a establecer la columna fecha como indice
    df = df.set_index('Fecha', inplace=False)
    df["Especie"]=ticker
    #
    save_file_generico(df, original_source + "ONLINE\SPCH", "SERIE_CORRIENTE_", ticker, ".xlsx")

#update_last_price("AGRO")
#update_last_price("ALUA")
#MISSING update_last_price("APBR")
#update_last_price("AUSO")
#update_last_price("BBAR")
#update_last_price("BHIP")
#update_last_price("BMA")
#update_last_price("BOLT")
#update_last_price("BPAT")
#update_last_price("BRIO")
#update_last_price("BYMA")
#update_last_price("CADO")
#update_last_price("CAPX")
#update_last_price("CARC")
#update_last_price("CECO2")
#update_last_price("CELU")
#update_last_price("CEPU")
#update_last_price("CGPA2")
#update_last_price("COME")
#update_last_price("CRES")
#update_last_price("CTIO")
#update_last_price("CVH")
#update_last_price("DGCU2")
#update_last_price("DOME")
#update_last_price("DYCA")
#update_last_price("EDLH")
#update_last_price("EDN")
#update_last_price("EDSH")
#update_last_price("EMDE")
#update_last_price("ESME")
#update_last_price("FERR")
#update_last_price("FIPL")
#update_last_price("GAMI")
#update_last_price("GARO")
#update_last_price("GBAN")
#update_last_price("GCLA")
#update_last_price("GGAL")
#update_last_price("GRIM")
#update_last_price("HARG")
#update_last_price("HAVA")
#update_last_price("INDU")
#update_last_price("INTR")
#update_last_price("INVJ")
#update_last_price("IRCP")
#update_last_price("IRSA")
#update_last_price("LEDE")
#update_last_price("LOMA")
#update_last_price("LONG")
#update_last_price("METR")
#update_last_price("MIRG")
#update_last_price("MOLA")
#update_last_price("MOLI")
#update_last_price("MORI")
#update_last_price("OEST")
#update_last_price("PAMP")
#update_last_price("PATA")
#update_last_price("PATY")
#update_last_price("PGR")
#update_last_price("POLL")
#update_last_price("RICH")
#update_last_price("RIGO")
#update_last_price("ROSE")
#update_last_price("SAMI")
#update_last_price("SEMI")
#update_last_price("SUPV")
#update_last_price("TECO2")
#update_last_price("TGLT")
#update_last_price("TGNO4")
#update_last_price("TGSU2")
#update_last_price("TRAN")
#MISSING update_last_price("TS")
#update_last_price("TXAR")
#update_last_price("VALO")
#update_last_price("YPFD")

def calculate(mul):
    # Esta funcion calcula el capital con calculo iterativo
    global value
    if mul == 0: 
       value = value
    else:
       value = mul    
    return value

def update_online_mkt_cap_ars(ticker, input_subdirectory, output_subdirectory):
    # Esta funcion crea una matriz de mkt cap ars armando el capital por medio de una iteracion utilizando un dataframe con fechas e importes de splits
    # Y graba la matriz en un subdirectorio MKT CAP ARS
    global df, actual, value, splits
    #
    # Capital historico asigna a la variable splits un array con los valores y las fechas de split del capital en Millones.
    capital_historico(ticker)
    #
    # Capital actual asigna a la variable actual el valor actual del capital para ese ticker en Millones.        
    capital_actual(ticker)
    #
    ###############SERIA BUENO QUE ABRA LA SERIE QUE CORRESPONDE
    filename = str("SERIE_CORRIENTE_" + ticker)  
    open_file_spch(input_subdirectory, filename, ".xlsx") #abre la spch
    merge = pd.merge(df, splits, how='outer', left_index=True, right_index=True) # mergea las dos dataframes e incorpora la columna "capital"
    merge.loc[:,'capital'] = merge.loc[:,'capital'].fillna(0) #completa la columna capital los NA y los reemplaza por 0
    df = merge
    df['C'] = np.nan #agrega nan en toda la columna C    
    value = actual
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    df.loc[b, 'C'] = value #Asigna a la fecha (b) que es la que obtuvimos antes el valor actual del capital
    df = df.sort_index(axis=0, level=None, ascending=False) # Da vuelta el indice
    df.head(1).index[-1] # muestra el head
    intermedio2 = str(df.head(2).index) # Convierte a string
    anteultima_fecha = intermedio2[30:40] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    df=df.fillna(0)  #completo con 0 los nan de la columna C mayuscula.
    df.loc[anteultima_fecha:, 'C'] = df.loc[anteultima_fecha:].apply(lambda row: float(calculate(*row[['capital']])), axis=1)  # Itera sobre la columna capital utilizando la formula calculate
    df=df.drop(['capital'], axis=1) 
    df=df.sort_index(axis=0, level=None, ascending=True)
    df=df.rename(columns={'C': 'Capital'})
    df['Mkt_Cap_ARS']=df['Cierre_del_dia']*df['Capital']
    #
    #### AGREGA COLUMNAS DEL MKT CAP EN ARS
    #
    df['Mkt_Cap_Open_ARS']=df['Apertura']*df['Capital']
    df['Mkt_Cap_Max_ARS']=df['Maximo']*df['Capital']    
    df['Mkt_Cap_Min_ARS']=df['Minimo']*df['Capital']
    df['Mkt_Cap_Close_ARS']=df['Cierre_del_dia']*df['Capital']
    #df['Mkt_Cap_ARS']=df['Cierre_del_dia']*df['Capital']  #parece que hay que borrrarla
    df['Volumen_%_Capital']=(df['Volumen_Nominal']/1000000)/df['Capital']
    # 
    df['Volumen_Nominal_Ajustado']=(actual*df['Volumen_%_Capital']*1000000)
    # 
    save_file_mkt_cap_ars(output_subdirectory, ticker, ".xlsx")
    return


#update_online_mkt_cap_ars("AGRO", original_source + "\ONLINE\SPCH", original_source + "\ONLINE\MKT_CAP_ARS")
#update_online_mkt_cap_ars("BBAR", original_source + "\ONLINE\SPCH", original_source + "\ONLINE\MKT_CAP_ARS")
#update_online_mkt_cap_ars("TXAR", original_source + "\ONLINE\SPCH", original_source + "\ONLINE\MKT_CAP_ARS")

#arma_df_con_mercado_americano("GGAL", "2020-01-01", "2020-01-24")
#graba_matriz_mercado_americano("GGAL", "2020-01-01", "2020-01-24")

#graba_matriz_mercado_americano("GGAL", "2020-01-01", "2020-01-24", original_source +"\INPUT\ONLINE", "AMERICANO_", ".xlsx")
#update_mercado_americano("GGAL", original_source + "INPUT\ONLINE", ("AMERICANO_" + "GGAL"), ".xlsx", original_source + "SPCH_AMERICANO", "AMERICANO_" + "GGAL", ".xlsx", original_source + "ONLINE\SPCH_AMERICANO", "AMERICANO_", ".xlsx")


# UPDATEA LA SERIE DE UN ADR AMERICANO CON LOS ULTIMOS PRECIOS ONLINE
def update_online_mercado_americano(ticker,date): 
    #
    #
    b = int(date[8:10])
    #print (b)
    day_date = "{:02d}".format(b+1)
    total_date = date[0:8]+day_date
    #print(total_date)
    graba_matriz_mercado_americano(ticker, "2020-01-01", total_date, original_source +"\INPUT_ONLINE", "AMERICANO_", ".xlsx")
    update_mercado_americano(ticker, original_source + "INPUT_ONLINE", ("AMERICANO_" + ticker), ".xlsx", original_source + "SPCH_AMERICANO", "AMERICANO_" + ticker, ".xlsx", original_source + "ONLINE\SPCH_AMERICANO", "AMERICANO_", ".xlsx")
    return


#update_online_mercado_americano("GGAL","2020-01-24")




def update_ccl_equities_online(ticker, source_path_american_serie_file, name_part1_american_serie_file, ext_american_serie_file, source_path_local_serie_file, name_part1_local_serie_file, ext_local_serie_file):
    # ARMA GGAL_CCL
    #
    # Abre serie del ADR
    df = open_excel(source_path_american_serie_file, name_part1_american_serie_file, ext_american_serie_file)
    df = serie_de_tiempo(df)
    adr = df
    adr['factor_de_conversion']=10
    #
    # Abre serie spch local
    df = open_file_spch( source_path_local_serie_file, name_part1_local_serie_file, ext_local_serie_file)
    #
    #
    merge=pd.merge(adr, df, how='inner', left_index=True, right_index=True)  
    merge['tc_nominal'] = merge['Cierre_del_dia']*merge['factor_de_conversion'] / merge['Close']  # Genera y asigna una columna calculada a merge 
    # Pone el correcto nombre a la especie
    merge['Especie']= ("USDARS_CCL_"+ticker)
    #Arma un dataframe solo con las columnas que me interesan
    merge=merge[['tc_nominal','Especie']]
    # Renombra la matriz a df para poder grabarla
    df=merge
    #
    # GRABA EL ARCHIVO
    #
    location = original_source + "\ONLINE"                                 
    filename = str("USDARS_CCL_"+ticker)     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()

#update_ccl_equities_online("GGAL", original_source + "\ONLINE\SPCH_AMERICANO", "AMERICANO_"+ "GGAL",  ".xlsx", original_source + "ONLINE\SPCH", "SERIE_CORRIENTE_"+ "GGAL", ".xlsx")

def update_ccl_equity_online(ticker):
    # Funcion que 
    update_ccl_equities_online(ticker, original_source + "\ONLINE\SPCH_AMERICANO", "AMERICANO_"+ ticker,  ".xlsx", original_source + "ONLINE\SPCH", "SERIE_CORRIENTE_"+ ticker, ".xlsx")
    return
     
#update_ccl_equity_online("GGAL")


def actualiza_dolar_libre_online(ticker):
    global df
    # Abre serie de tipo de cambio libre historica
    df = open_excel(original_source + "\CURRENCIES","USDARS_LIBRE",".xlsx")
    df = serie_de_tiempo(df)
    #
    # BUSCA EL ULTIMO PUNTO DE LA SERIE ORIGINAL
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #print (b)
    #
    serie_original = df
    #
    #Abre serie de tipo de cambio con la que actualizar
    df = open_excel(original_source + "\ONLINE","USDARS_CCL_"+ticker,".xlsx")
    df = serie_de_tiempo(df)
    df = df[df.index>b]
    puntos_nuevos = df
    #
    # Cambia el nombre a la columna para que la especie vaya a parar a la columna FUENTE
    #
    puntos_nuevos.rename(columns={"Especie":"FUENTE"}, inplace=True)
    #
    #ARMA LA NUEVA MATRIZ
    #
    #
    df=pd.concat([serie_original, puntos_nuevos]).drop_duplicates()
    #
    df["Especie"]="USDARS_LIBRE"
    #
    # ELIMINA DUPLICADOS DEL INDICE
    #
    # Eliminacion de duplicados del indice
    #
    # 1. Reseteo el indice para poder operar sobre las columnas    
    df = df.reset_index()
    # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
    df = df.drop_duplicates(subset='Fecha', keep='last')
    # 3. Vuelvo a establecer la columna fecha como indice
    df = df.set_index('Fecha', inplace=False)
    #
    #
    ## GRABA EL ARCHIVO
    #
    location = original_source + "\ONLINE"                                 
    filename = str("USDARS_LIBRE")     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()

#actualiza_dolar_libre_online("GGAL")




def update_online_mkt_cap_usd(ticker4):
    # Esta funcion crea una matriz de mkt cap usd
    # Y graba la matriz en un subdirectorio especificado
    global df, cur
    cur = open_excel(original_source + "\ONLINE", "USDARS_LIBRE", ".xlsx")
    cur = serie_de_tiempo(cur)
    #open_file_currency("USDARS_LIBRE")
    cur = cur.drop(['FUENTE'], axis=1)
    cur = cur.drop(['Especie'], axis=1)
    open_file_mkt_cap_ars(original_source + "\ONLINE\MKT_CAP_ARS", ticker4, ".xlsx")
    merge=pd.merge(df, cur, how='inner', left_index=True, right_index=True) # Agrega una columna a la derecha de la Mkt Cap Ars que se llama USDARS_LIBRE
    merge['Mkt_Cap_USD'] = merge['Mkt_Cap_ARS'] / merge['tc_nominal']  # Genera y asigna una columna calculada a merge
    #
    ######## PASA EL RESTO DE LAS COLUMNAS A USD
    #
    merge['Mkt_Cap_Open_USD'] = merge['Apertura']*merge['Capital'] / merge['tc_nominal']
    merge['Mkt_Cap_Max_USD'] = merge['Maximo']*merge['Capital'] / merge['tc_nominal']
    merge['Mkt_Cap_Min_USD'] = merge['Minimo']*merge['Capital'] / merge['tc_nominal']
    merge['Mkt_Cap_Close_USD'] = merge['Cierre_del_dia']*merge['Capital'] / merge['tc_nominal']
    #
    #######
    df = merge
    #
    # Eliminacion de duplicados del indice
    #
    # 1. Reseteo el indice para poder operar sobre las columnas    
    df = df.reset_index()
    # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
    df = df.drop_duplicates(subset='Fecha', keep='last')
    # 3. Vuelvo a establecer la columna fecha como indice
    df = df.set_index('Fecha', inplace=False)
    #  
    #
    # GRABA LA MATRIZ
    #
    location = original_source + "\ONLINE\MKT_CAP_USD"                                 
    filename = str("MKT_CAP_USD_" + ticker4)     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()
    #
    return


#update_online_mkt_cap_usd("AGRO")
#update_online_mkt_cap_usd("BBAR")
#update_online_mkt_cap_usd("TXAR")

#UPDATEAR MANUALMENTE EL USDARS_PPP
def prepara_serie_online_diaria_de_tipo_de_cambio_ppp(cod_moneda1, cod_moneda2, fecha_del_ultimo_punto):
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
    save_file_generico(df4, original_source + "\ONLINE", cod_moneda1+cod_moneda2, "_PPP", ".xlsx")
    #
    return

#df3 = prepara_serie_online_diaria_de_tipo_de_cambio_ppp("USD", "ARS", "2020-02-07")



def update_online_mkt_cap_usdppp(ticker25):
    # Esta funcion crea una matriz de mkt cap usdppp
    # Y graba la matriz en un subdirectorio 
    global df, cur
    #
    # Carga la matriz de USDARS_PPP
    #
    cur = open_excel(original_source + "\ONLINE", "USDARS_PPP", ".xlsx")
    cur = serie_de_tiempo(cur)
    #
    # Crea una matriz solo con la columna "tc_real"
    cur = cur[['tc_real']]
    #
    # QUEDO OBSOLETO DESDE QUE CREE UNA MATRIZ SOLO CON UNA COLUMNA 
    #cur.columns = ['tc_real', 'W', 'X', 'Y', 'Especie']
    # Drop the column with label 'A'
    #if 'W' in cur:
    #   cur.drop('W', axis=1, inplace=True)
    #if 'X' in cur:
    #   cur.drop('X', axis=1, inplace=True)
    #if 'Y' in cur:
    #   cur.drop('Y', axis=1, inplace=True)
    #if 'Especie' in cur:
    #   cur.drop('Especie', axis=1, inplace=True)
    #cur.head()
    #
    # Carga la matriz de USDARS_PPP
    #
    open_file_mkt_cap_usd(original_source + "\ONLINE\MKT_CAP_USD", ticker25, ".xlsx")
    #
    #
    #
    merge=pd.merge(df, cur, how='inner', left_index=True, right_index=True) # Agrega una columna a la derecha de la Mkt Cap Usd que se llama USDARS_PPP
    merge['Mkt_Cap_USDPPP'] = merge['Mkt_Cap_ARS'] / merge['tc_real']  # Genera y asigna una columna calculada a merge
    #
    ######## PASA EL RESTO DE LAS COLUMNAS A USD_PPP
    #
    merge['Mkt_Cap_Open_USD_PPP'] = merge['Mkt_Cap_Open_ARS'] / merge['tc_real'] 
    merge['Mkt_Cap_Max_USD_PPP'] = merge['Mkt_Cap_Max_ARS'] / merge['tc_real']
    merge['Mkt_Cap_Min_USD_PPP'] = merge['Mkt_Cap_Min_ARS'] / merge['tc_real']
    merge['Mkt_Cap_Close_USD_PPP'] = merge['Mkt_Cap_Close_ARS'] / merge['tc_real']
    #
    #######
    df = merge
    if 'W' in df:
       df.drop('W', axis=1, inplace=True)
    #
    # GRABA LA MATRIZ
    #
    location = original_source + "\ONLINE\MKT_CAP_USDPPP"                                 
    filename = str("MKT_CAP_USDPPP_" + ticker25)     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()
    #
    return df

#update_online_mkt_cap_usdppp("AGRO")
#update_online_mkt_cap_usdppp("BBAR")
#update_online_mkt_cap_usdppp("TXAR")


def update_online_de_un_ticker(ticker, fecha):
    #
    # Actualiza la serie en precios online
    update_last_price(ticker)
    #
    # Actualiza la serie de mkt cap ARS online
    update_online_mkt_cap_ars(ticker, original_source + "\ONLINE\SPCH", original_source + "\ONLINE\MKT_CAP_ARS")
    #
    # Actualiza el dolar libre online 
    exec(open(original_source+"D1003_online_actualiza_dolar_libre.py").read())
    #
    # Actualiza la serie de mkt cap USD online
    #update_online_mkt_cap_usd("AGRO")
    #
    # Actualiza la serie de tipo de cambio UDSARS_PPP online
    exec(open(original_source+"D2000_modulo_indec.py").read())
    prepara_serie_online_diaria_de_tipo_de_cambio_ppp("USD", "ARS", fecha)
    #
    # Actualiza la serie de mkt cap USDARS_PPP online
    update_online_mkt_cap_usdppp(ticker)
    

#update_online_de_un_ticker("TXAR", "2020-02-11")

#Funcion que copia la serie historica en el directorio online

def inicializa_un_nuevo_dia_online_spch():
    global original_source
    import os
    directory_source = (original_source+"\SPCH")
    directory_destiny = (original_source + "ONLINE\SPCH")
    import shutil
    for filename in os.listdir(directory_source):
        if filename.endswith(".xlsx"):
           shutil.copy( directory_source + "\\" + filename, directory_destiny)
           print(filename)
        else:
           return ("Problema")


#inicializa_un_nuevo_dia_online_spch()

def inicializa_un_nuevo_dia_online_currencies():
    global original_source
    import os
    directory_source = (original_source+"\CURRENCIES")
    directory_destiny = (original_source + "ONLINE")
    import shutil
    for filename in os.listdir(directory_source):
        if filename.endswith(".xlsx"):
           shutil.copy( directory_source + "\\" + filename, directory_destiny)
           print(filename)
        else:
           print ("Problema con "+filename )

#inicializa_un_nuevo_dia_online_currencies()
