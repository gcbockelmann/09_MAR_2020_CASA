# MODULO CONTABILIDAD


# Hace que panda muestre 2 puntos decimales para los float.
#pd.options.display.float_format = '${:,.2f}'.format


###########################################################################################################################################################

def inicia_df_de_transacciones():
    #
    global df
    #
    # Inicializa 
    indice_dataframe = []
    #
    #import pandas as pd
    list_of_columns = ['Liquida','Operado','Comprobante','Numero','Cantidad','Especie', 'Precio','Importe','Saldo','Referencia']
    # 
    #Crea el dataframe 
    df=pd.DataFrame(index = indice_dataframe, columns=list_of_columns)
    #
    # Agrega una fila al dataframe
    #df = df.append({'Liquida':0,'Operado':0,'Comprobante':0,'Numero':0,'Cantidad':0,'Especie':0, 'Precio':0,'Importe':0,'Saldo':0,'Referencia':0}, ignore_index=True)
    #
    return

#inicia_df_de_transacciones()
    

#### COMPROBANTE COMPRA NORMAL #############################################################################################################################
def crea_comprobante_compra_normal(fecha_liquida, fecha_operado, nro_comprobante, cantidad, especie, precio, importe, referencia):
    global df
    importe = -abs(importe)
    df = df.append({'Liquida':fecha_liquida,'Operado':fecha_operado,'Comprobante':'COMPRA_NORMAL','Numero':nro_comprobante,'Cantidad':cantidad,'Especie':especie, 'Precio':precio,'Importe':importe,'Saldo':0,'Referencia':0}, ignore_index=True)
    return

def crea_comprobante_compra_trading(fecha_liquida, fecha_operado, nro_comprobante, cantidad, especie, precio, importe, referencia):
    global df
    importe = -abs(importe)
    df = df.append({'Liquida':fecha_liquida,'Operado':fecha_operado,'Comprobante':'COMPRA_TRADING','Numero':nro_comprobante,'Cantidad':cantidad,'Especie':especie, 'Precio':precio,'Importe':importe,'Saldo':0,'Referencia':0}, ignore_index=True)
    return


def crea_comprobante_compra_x_ejercicio_prima(fecha_liquida, fecha_operado, nro_comprobante, cantidad, especie, precio, importe, referencia):
    global df
    importe = -abs(importe)
    df = df.append({'Liquida':fecha_liquida,'Operado':fecha_operado,'Comprobante':'COMPRA_X_EJERCICIO_PRIMA','Numero':nro_comprobante,'Cantidad':cantidad,'Especie':especie, 'Precio':precio,'Importe':importe,'Saldo':0,'Referencia':0}, ignore_index=True)
    return

def crea_comprobante_venta(fecha_liquida, fecha_operado, nro_comprobante, cantidad, especie, precio, importe, referencia):
    global df
    cantidad = -abs(cantidad)
    importe = abs(importe)
    df = df.append({'Liquida':fecha_liquida,'Operado':fecha_operado,'Comprobante':'VENTA','Numero':nro_comprobante,'Cantidad':cantidad,'Especie':especie, 'Precio':precio,'Importe':importe,'Saldo':0,'Referencia':0}, ignore_index=True)
    return


def crea_comprobante_dividendos_en_efectivo(fecha_liquida, fecha_operado, nro_comprobante, cantidad, especie, precio, importe, referencia):
    global df
    cantidad = 0
    importe = abs(importe)
    df = df.append({'Liquida':fecha_liquida,'Operado':fecha_operado,'Comprobante':'DIVIDENDOS_EN_EFECTIVO','Numero':nro_comprobante,'Cantidad':cantidad,'Especie':especie, 'Precio':precio,'Importe':importe,'Saldo':0,'Referencia':0}, ignore_index=True)
    return

def crea_comprobante_venta_trading(fecha_liquida, fecha_operado, nro_comprobante, cantidad, especie, precio, importe, referencia):
    global df
    cantidad = -abs(cantidad)
    importe = abs(importe)
    df = df.append({'Liquida':fecha_liquida,'Operado':fecha_operado,'Comprobante':'VENTA_TRADING','Numero':nro_comprobante,'Cantidad':cantidad,'Especie':especie, 'Precio':precio,'Importe':importe,'Saldo':0,'Referencia':0}, ignore_index=True)
    return

##############################################################################################################################
# FUNCIONES QUE EXTRAEN PRECIOS DEL DOLAR_LIBRE Y DEL USDARS_PPP Y LAS ASIGNAN A UN DATAFRAME PORQUE SIRVEN DE INPUT A LA FUNCION DE FORMATEO DE TRANSACCIONES
##############################################################################################################################

#########################################################################################################
# FUNCION QUE DEVUELVE EL PRECIO DEL DOLAR_LIBRE A UNA DETERMINADA FECHA
#########################################################################################################

def precio_del_dolar_libre_a_una_fecha(fecha):  
    #global df, b
    #
    df = open_excel(original_source + "\ONLINE", "USDARS_LIBRE", ".xlsx")
    df = df.set_index("Fecha")
    #
    b = fecha # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #print(b)
    #
    #
    if b in df.index:
       # Arma una serie y busca por el indice de la serie que es una string
       #
       output = df["tc_nominal"][b]
       return output       
    else:
       return "NA"  

#precio_del_dolar_libre_a_una_fecha("2020-01-28")

############################################################################################################
# FUNCION QUE DEVUELVE EL PRECIO DEL TIPO DE CAMBIO USDARS_PPP A UNA DETERMINADA FECHA, USANDO SERIE ONLINE
############################################################################################################

def precio_del_tipo_de_cambio_USDARS_PPP_a_una_fecha(fecha):  
    global df, b
    #
    df = open_excel(original_source + "\ONLINE", "USDARS_PPP", ".xlsx")
    df = df.set_index("Fecha")
    #
    b = fecha # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #print(b)
    #
    #
    if b in df.index:
       # Arma una serie y busca por el indice de la serie que es una string
       #
       output = df["tc_real"].loc[b]
       #output = list(df["tc_real"][b])
       return output      
    else:
       return "NA"  

#precio_del_tipo_de_cambio_USDARS_PPP_a_una_fecha("2020-02-07")


#########################################################################################################
# FUNCION QUE ASIGNA A UN DATAFRAME DE TRANSACCIONES EL PRECIO DEL DOLAR_LIBRE PARA CADA TRANSACCION
#########################################################################################################

def asigna_dolar_libre_a_df(df, columna):
    lista_de_fechas_de_operaciones = list(df[columna])
    lista_de_precios_del_dolar =[]
    for fecha in lista_de_fechas_de_operaciones:
        lista_de_precios_del_dolar.append(precio_del_dolar_libre_a_una_fecha(fecha))
    df["USDARS_LIBRE"]= pd.Series(lista_de_precios_del_dolar)
    return df
    #return lista_de_precios_del_dolar

#df2=asigna_dolar_libre_a_df(df, "Liquida")


#########################################################################################################
# FUNCION QUE ASIGNA A UN DATAFRAME DE TRANSACCIONES EL PRECIO DEL USDARS_PPP PARA CADA TRANSACCION
#########################################################################################################

def asigna_USDARS_PPP_a_df(df, columna):
    lista_de_fechas_de_operaciones = list(df[columna])
    lista_de_precios_del_USDARS_PPP =[]
    for fecha in lista_de_fechas_de_operaciones:
        lista_de_precios_del_USDARS_PPP.append(precio_del_tipo_de_cambio_USDARS_PPP_a_una_fecha(fecha))
    df["USDARS_PPP"]= pd.Series(lista_de_precios_del_USDARS_PPP)
    return df

#df2=asigna_USDARS_PPP_a_df(df, "Liquida")

#########################################################################################################
# FUNCION QUE SIRVE PARA CALCULAR EL COSTO UNITARIO 
#########################################################################################################

# Funcion que sirve para calcular el costo unitario
# Se la utiliza para calcular la columna costo unitario en un dataframe de transacciones
def calculates_cost(quantity, cost):
    if quantity >0:
       return (cost/quantity)
    else:
       return 0 

################################################################################################################
############################### FORMATEA EL DATAFRAME DE TRANSACCIONES AGREGANDO DATOS DE TIPOS DE CAMBIO
################################################################################################################

def formato_df_de_transacciones(df):
    #
    # Setea formatos de columnas con un tipo de dato para poder operarlas
    df['Cantidad'] = df['Cantidad'].astype(int)
    df['Importe'] = df['Importe'].astype(int)
    #
    # CALCULOS CON TIPO DE CAMBIO USDARS_LIBRE
    #
    #Agrega el precio del dolar libre a la fecha de cada operacion
    # Se usa la fecha de operacion para poder evaluar si la toma de decisiones fue correcta o no.
    # Si se usara para dolarizar la operacion y tributar impuestos, probablemente habria que tomar la fecha de liquidacion.
    df=asigna_dolar_libre_a_df(df, "Operado")
    #df2=asigna_dolar_libre_a_df(df2, "Operado")
    #
    # Calcula el importe en USD
    df["Importe_en_USD"]=(df["Importe"]/df["USDARS_LIBRE"])
    #
    #Crea la columna de Costo Unitario en USD
    df["Costo_Unitario_en_USD"]=0
    #
    #df2["Costo_Unitario_en_USD"].loc[0]=calculates_cost(df2["Cantidad"].loc[0],df2["Costo_en_USD"].loc[0])
    #
    # Completa la columna de costo unitario en USD
    for i in df.index:
        df["Costo_Unitario_en_USD"].loc[i]=calculates_cost(df["Cantidad"].loc[i],df["Importe_en_USD"].loc[i])
    #
    # CALCULOS CON TIPO DE CAMBIO USDARS_PPP
    #    
    #Agrega el precio del USDARS_PPP a la fecha de cada operacion
    # Se usa la fecha de operacion para poder evaluar si la toma de decisiones fue correcta o no.
    # Si se usara para dolarizar la operacion y tributar impuestos, probablemente habria que tomar la fecha de liquidacion.
    df=asigna_USDARS_PPP_a_df(df, "Operado")
    #
    # Calcula el importe en USDARS_PPP
    df["Importe_en_USDARS_PPP"]=(df["Importe"]/df["USDARS_PPP"])
    #
    #Crea la columna de Costo Unitario en USDARS_PPP
    df["Costo_Unitario_en_USDARS_PPP"]=0
    #
    # Completa la columna de costo unitario en USDARS_PPP
    for i in df.index:
        df["Costo_Unitario_en_USDARS_PPP"].loc[i]=calculates_cost(df["Cantidad"].loc[i],df["Importe_en_USDARS_PPP"].loc[i])
    return df



################################################################################################################
#### FUNCION QUE FILTRA UN DATAFRAME DE TRANSACCIONES POR TICKER
##############################################################################################################

def filtra_dataframe_de_transacciones_por_ticker(df, ticker):
    df2 = df[df["Especie"]==ticker]
    return df2

#filtra_dataframe_de_transacciones_por_ticker(df, "PAMP")

#df[df["Especie"]=="PAMP"]

################################################################################
###### FORMULA FUNDAMENTAL PARA EL CALCULO DEL COSTO FIFO
##############################################################################

def FiFo(dfg):
    if dfg[dfg['CS'] < 0]['Cantidad'].count():
        subT = dfg[dfg['CS'] < 0]['CS'].iloc[-1]
        dfg['Cantidad'] = np.where((dfg['CS'] + subT) <= 0, 0, dfg['Cantidad'])
        dfg = dfg[dfg['Cantidad'] > 0]
        if (len(dfg) > 0):
            dfg['Cantidad'].iloc[0] = dfg['CS'].iloc[0] + subT
    return dfg

################################################################################################################
############################## ARMA MATRIZ DE COSTO FIFO DE INVENTARIO  PARA UN TICKER  ########################
################################################################################################################

def arma_matriz_costo_fifo_por_ticker(df,ticker):
    #
    # Aplica un filtro al df de transacciones
    df_particular = filtra_dataframe_de_transacciones_por_ticker(df, ticker)
    #df_particular = df[df["Especie"]==ticker]
    #
    # A Borrar porque ya la funcion formateo formatea estas columnas
    #df_particular['Cantidad'] = df_particular['Cantidad'].astype(int)
    #df_particular['Importe'] = df_particular['Importe'].astype(int)
    #
    # Arma columnas auxiliares para calcular el inventario final
    df_particular['PN'] = np.where(df_particular['Cantidad'] > 0, 'P', 'N')
    df_particular['CS'] = df_particular.groupby(['Especie', 'PN'])['Cantidad'].cumsum()
    #
    # Aplica una formula FiFo y agrupa, y no se bien como lo hace pero calcula el inventario final de un metodo FIFO
    dfR = df_particular.groupby(['Especie'], as_index=False)\
    .apply(FiFo) \
    .drop(['CS', 'PN'], axis=1) \
    .reset_index(drop=True)
    #
    # RECALCULA LAS COLUMNAS EN ARS
    dfR.rename(columns = {'Importe':'Costo_ARS'}, inplace=True)
    dfR.rename(columns = {'Precio':'Costo_Unitario_ARS'}, inplace=True)
    dfR["Costo_ARS"]=dfR["Costo_Unitario_ARS"]*dfR["Cantidad"]
    #
    # RECALCULA LAS COLUMNAS EN USDARS_LIBRE
    dfR.rename(columns = {'Importe_en_USD':'Costo_USD'}, inplace=True)
    #dfR.rename(columns = {'Precio':'Costo_Unitario_USD'}, inplace=True)
    dfR["Costo_USD"]=-dfR["Costo_Unitario_en_USD"]*dfR["Cantidad"]
    dfR["Costo_Unitario_en_USD"]=-dfR["Costo_Unitario_en_USD"]
    #
    # RECALCULA LAS COLUMNAS EN USDARS_PPP
    dfR.rename(columns = {'Importe_en_USDARS_PPP':'Costo_USDARS_PPP'}, inplace=True)
    dfR.rename(columns = {'Costo_Unitario_en_USDARS_PPP':'Costo_Unitario_USDARS_PPP'}, inplace=True)
    dfR["Costo_USDARS_PPP"]=-dfR["Costo_Unitario_USDARS_PPP"]*dfR["Cantidad"]
    dfR["Costo_Unitario_USDARS_PPP"]=-dfR["Costo_Unitario_USDARS_PPP"]
    #
    return dfR
    

#df2=arma_matriz_costo_fifo_por_ticker(df,"PAMP")




######################################################################################################################################
#### FUNCION QUE ASIGNA A UN DF DE TENENCIA/COSTOS, EL PRECIO A UNA FECHA PARA DETERMINAR LA RENTABILIDAD A UNA FECHA DE CADA OPERACION
######################################################################################################################################
def asigna_precio_actual_a_cada_transaccion(df_de_tenencia, fecha):
    # Como asigna precios a una fecha, la operacion de compra deberia estar en inventario a esa fecha, esta funcion deberia aplicarse a las matrices de tenencia a una fecha.
    #global df
    mykeys = list(df_de_tenencia["Especie"])
    #
    df_de_tenencia['Precio_de_Cierre']=crea_lista_de_precios_del_portfolio(mykeys, fecha)
    #df['Valor']=portfolio['Cantidad']*portfolio['Precio_de_Cierre']
    #df = portfolio 
    return df_de_tenencia

#asigna_precio_actual_a_cada_transaccion(df, "2020-02-07")

#################################################################################################################
#### ARMA Y GRABA ARCHIVOS DE COSTOS Y RENDIMIENTOS POR OPERACION
##################################################################################################################

def arma_y_graba_matriz_de_costos_y_rentabilidades_por_ticker(df_de_transacciones, ticker, fecha_de_valorizacion):
    #
    # Arma matriz de costos para ese ticker
    df2=arma_matriz_costo_fifo_por_ticker(df_de_transacciones,ticker)
    #  
    #
    # En ARS
    asigna_precio_actual_a_cada_transaccion(df2, fecha_de_valorizacion)
    df2.rename(columns = {'Precio_de_Cierre':'Precio_Actual_ARS'}, inplace=True)
    df2["Valor_ARS"]=(df2["Precio_Actual_ARS"]*df2["Cantidad"])
    df2["%_ARS"]=((df2["Valor_ARS"]/df2["Costo_ARS"])-1)*100
    #
    # En USD
    df2["Precio_Actual_USDARS_LIBRE"]=precio_del_dolar_libre_a_una_fecha(fecha_de_valorizacion)
    df2["Precio_Actual_USD"]=(df2["Precio_Actual_ARS"]/df2["Precio_Actual_USDARS_LIBRE"])
    df2["Valor_USD"]=(df2["Precio_Actual_USD"]*df2["Cantidad"])
    df2["%_USD"]=((df2["Valor_USD"]/df2["Costo_USD"])-1) * 100
    #
    # En USDARS_PPP
    #
    df2["Precio_Actual_USDARS_PPP"]=precio_del_tipo_de_cambio_USDARS_PPP_a_una_fecha(fecha_de_valorizacion)
    df2["Precio_Actual_USDARS_PPP"]=(df2["Precio_Actual_ARS"]/df2["Precio_Actual_USDARS_PPP"])
    df2["Valor_USDARS_PPP"]=(df2["Precio_Actual_USDARS_PPP"]*df2["Cantidad"])
    df2["%_USDARS_PPP"]=((df2["Valor_USDARS_PPP"]/df2["Costo_USDARS_PPP"])-1)*100
    #
    # GRABA LA MATRIZ
    #
    writer = pd.ExcelWriter(original_source + '/PORTFOLIO/COSTOS_' + ticker +'' + '.xlsx', engine='xlsxwriter')
    #
    # Graba la matriz a una tab especifica
    df2.to_excel(writer, sheet_name=ticker)
    #
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    #

#arma_y_graba_matriz_de_costos_y_rentabilidades_por_ticker(transacciones, "PAMP", "2020-02-10")
#arma_y_graba_matriz_de_costos_y_rentabilidades_por_ticker(transacciones, "CTIO", "2020-02-07")
#arma_y_graba_matriz_de_costos_y_rentabilidades_por_ticker(transacciones, "TXAR", "2020-02-07")
#arma_y_graba_matriz_de_costos_y_rentabilidades_por_ticker(transacciones, "SAMI", "2020-02-07")





################################################################################################################
############################## GRABA MATRIZ DE COSTO FIFO DE INVENTARIO  PARA UN TICKER  ########################
################################################################################################################

def graba_matriz_de_costos(df, ticker):
    #
    df2 = arma_matriz_costo_fifo_por_ticker(df,ticker)  
    #
    writer = pd.ExcelWriter(original_source + '/PORTFOLIO/COSTOS_' + ticker +'' + '.xlsx', engine='xlsxwriter')
    #
    # Write each dataframe to a different worksheet.
    df2.to_excel(writer, sheet_name='Transacciones')
    #
    #df2.to_excel(writer, sheet_name='USDARS_LIBRE')
    #df3.to_excel(writer, sheet_name='USDARS_PPP')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


#graba_matriz_de_costos(df, "PAMP")
#graba_matriz_de_costos(df, "TXAR")
#graba_matriz_de_costos(df, "CTIO")
#graba_matriz_de_costos(df, "GGAL")


################################################################################################################
############################### PREPARA LOS DATOS PARA ARMAR UN PORTFOLIO
################################################################################################################

def arma_lista_de_cantidades_del_portfolio_final(df):
    #
    lista_de_cantidades_finales = []
    filtro = df.drop_duplicates(subset='Especie', keep='last')
    lista_tickers = list(filtro["Especie"])
    for ticker in lista_tickers:
        # aplica
        df3 = df[df["Especie"]==ticker]
        df3['Cantidad'] = df3['Cantidad'].astype(int)
        df3['Importe'] = df3['Importe'].astype(int)
        df3['PN'] = np.where(df3['Cantidad'] > 0, 'P', 'N')
        df3['CS'] = df3.groupby(['Especie', 'PN'])['Cantidad'].cumsum()
        dfR = df3.groupby(['Especie'], as_index=False)\
        .apply(FiFo) \
        .drop(['CS', 'PN'], axis=1) \
        .reset_index(drop=True)
        lista_de_cantidades_finales.append(dfR["Cantidad"].sum())
    return lista_de_cantidades_finales

#arma_lista_de_cantidades_del_portfolio_final(df)


def arma_lista_de_tickers_actuales_en_portafolio(df):
    #
    # Arma un filtro del df por la columna Especie y remuve los duplicados
    filtro = df.drop_duplicates(subset='Especie', keep='last')
    # Arma una lista con los datos de la columna Especie sin duplicados
    lista_tickers = list(filtro["Especie"])
    return lista_tickers

#arma_lista_de_tickers_actuales_en_portafolio(df)


def convert_two_lists_into_a_dictionary(keys, values):
    dictionary = dict(zip(keys, values))
    return dictionary

#convert_two_lists_into_a_dictionary(arma_lista_de_tickers_actuales_en_portafolio(df), arma_lista_de_cantidades_del_portfolio_final(df))


################################################################################################################
############################## ARMA VECTOR DE COSTOS EN PESOS ##################################################
################################################################################################################

def arma_lista_de_costos_de_tenencia(df):
    #
    lista_de_costos_de_tenencia = []
    filtro = df.drop_duplicates(subset='Especie', keep='last')
    lista_tickers = list(filtro["Especie"])
    for ticker in lista_tickers:
        # Filtra la matriz por ticker
        df2=arma_matriz_costo_fifo_por_ticker(df,ticker)
        #
        Costo_total_para_el_security = df2["Costo_ARS"].sum()
        lista_de_costos_de_tenencia.append(-Costo_total_para_el_security)
    return lista_de_costos_de_tenencia

#arma_lista_de_costos_de_tenencia(df)

################################################################################################################
############################## ARMA VECTOR DE COSTOS EN DOLARES ################################################
################################################################################################################

def arma_lista_de_costos_de_tenencia_en_usd(df):
    #
    lista_de_costos_de_tenencia = []
    filtro = df.drop_duplicates(subset='Especie', keep='last')
    lista_tickers = list(filtro["Especie"])
    for ticker in lista_tickers:
        # Filtra la matriz por ticker
        df2=arma_matriz_costo_fifo_por_ticker(df,ticker)
        #
        Costo_total_para_el_security = df2["Costo_USD"].sum()
        lista_de_costos_de_tenencia.append(-Costo_total_para_el_security)
    return lista_de_costos_de_tenencia

#arma_lista_de_costos_de_tenencia_en_usd(df)
#arma_lista_de_costos_de_tenencia_en_usd(df2)



################################################################################################################
############################## ARMA VECTOR DE COSTOS EN USDARS_PPP #############################################
################################################################################################################


def arma_lista_de_costos_de_tenencia_en_usdars_ppp(df):
    #
    lista_de_costos_de_tenencia = []
    filtro = df.drop_duplicates(subset='Especie', keep='last')
    lista_tickers = list(filtro["Especie"])
    for ticker in lista_tickers:
        # Filtra la matriz por ticker
        df2=arma_matriz_costo_fifo_por_ticker(df,ticker)
        #
        Costo_total_para_el_security = df2["Costo_USDARS_PPP"].sum()
        lista_de_costos_de_tenencia.append(-Costo_total_para_el_security)
    return lista_de_costos_de_tenencia

#arma_lista_de_costos_de_tenencia_en_usdars_ppp(df)
#arma_lista_de_costos_de_tenencia_en_usdars_ppp(df2)


################################################################################################################
############################### FUNCIONES O METODOS ADICIONALES
################################################################################################################

# Mira la cantidad de acciones totales
#df["Cantidad"].sum()

# Filtrar la matriz por un security
#df3 = df[df["Especie"]=="TXAR"]


####################################################################################
### FUNCION QUE ACTUALIZA EL COSTO UNITARIO A PARTIR DE UN IMPORTE Y UNAS CANTIDADES
####################################################################################

def actualiza_el_precio_unitario(importe, cantidad):
    if cantidad != 0:
       precio_unitario = abs(importe/cantidad)
    else:
       precio_unitario = 0
    return precio_unitario

#actualiza_el_precio_unitario(10000, 0)

##############################################################################################
### FUNCION QUE ACTUALIZA LA COLUMNA PRECIO DE UN DATAFRAME APLICANDO UNA FORMULA, ROW BY ROW.
##############################################################################################

def calcula_precio_unitario_con_muchos_decimales(dataframe):
    #
    df = dataframe
    for i in df.index:
        df["Precio"].loc[i]=actualiza_el_precio_unitario(df["Importe"].loc[i],df["Cantidad"].loc[i])
    #
    return df


#calcula_precio_unitario_con_muchos_decimales(df)



##############################################################################################
### FUNCION QUE ABRE UN ARCHVIO DE TRANSACCIONES DE BULL MARKET BROKERS
##############################################################################################

def abre_transacciones_bmb_archivo_excel(nombre_del_archivo):
    # Setea la variable global df
    global df
    #
    #Lee el archivo de excel especificando el simbolo para miles y decimales
    df = pd.read_excel(arma_path(original_source + "",nombre_del_archivo , ".xlsx"), sheet_name=0,thousands='.',decimal=',')
    #
    # Setea como indice la columna liquida
    df=df.set_index("Liquida")
    #
    # Transforma la columna de index a datetime
    df.index = pd.to_datetime(df.index, format="%d/%m/%y")
    #
    # Resetea el indice
    df = df.reset_index()
    #
    # Setea como indice la columna Operado
    df=df.set_index("Operado")
    #
    # Transforma la columna de index a datetime
    df.index = pd.to_datetime(df.index, format="%d/%m/%y")
    #
    # Resetea el indice
    df = df.reset_index()
    #
    # Rellena los Nan
    # similar a 
    #df["Numero"] = df["Numero"].fillna(0)
    df["Numero"] = df["Numero"].replace(np.nan, "") 
    #
    # Elimina las filas que no tienen valor en la columna liquida
    df = df[df.Liquida.notnull()]
    #
    # Reemplaza los Nan de la columna Referencia por ""
    df["Referencia"] = df["Referencia"].replace(np.nan, "") 
    #
    # Reemplaza los Nan de la columna Especie por ""
    df["Especie"] = df["Especie"].replace(np.nan, "") 
    #
    # RESETEA EL INDICE PARA QUE QUEDE EN NUMEROS SUCESIVOS EN CASO DE HABER BORRADO FILAS INTERMEDIAS
    ## PUEDE QUE FALTE ORDENAR EL INDICE POR FECHA - 
    #
    # Setea como indice la columna liquida
    df=df.set_index("Liquida")
    #
    # Resetea el indice
    df = df.reset_index()
    #
    # Remueve los puntos.
    #df["Importe"] = df["Importe"].replace('.', '') 
    #
    #Setea las columnas al tipo que queramos
    df["Importe"]=df["Importe"].astype(float)
    df["Numero"]=df["Numero"].astype(int)
    df["Cantidad"]=df["Cantidad"].astype(int)


#abre_transacciones_bmb_archivo_excel("BMB")


################################################################################
################################################################################
################################################################################
# CONOCIMIENTOS INTERESANTES PARA APRENDER

### CONOCIMIENTO IMPORTANTEE
# Para filtrar por la columna Especie los valores que sean iguales a Nan 
#df = df[df.Especie.isnull()]
# Para filtrar por la columna Especie los valores que sean distintos de Nan 
#df = df[df.Especie.notnull()]


################################################################################
################################################################################
################################################################################

#### PARA OTRA FUNCION TENENCIA A UNA FECHA DETERMINADA


def filtra_un_dataframe_de_transacciones_hasta_una_fecha(df, fecha_de_corte): 
    #
    # Filtra por una determinada fecha
    return df[df["Liquida"]<="2020-02-10"]



#filtra_un_dataframe_de_transacciones_hasta_una_fecha(df, "2020-02-10")
       


################################################################################
################################################################################
################################################################################

#FUNCIONES DE AUTOFIT PARA PODER GRABAR EN EXCEL CON FORMATO
# FUNCION QUE SIRVE PARA EL AUTOFIT DE COLUMNAS DE EXCEL (AJUSTAR A SELECCION) AJUSTA EL WIDTH
def get_col_widths(dataframe):
    # First we find the maximum length of the index column   
    idx_max = max([len(str(s)) for s in dataframe.index.values] + [len(str(dataframe.index.name))])
    # Then, we concatenate this to the max of the lengths of column name and its values for each column, left to right
    return [idx_max] + [max([len(str(s)) for s in dataframe[col].values] + [len(col)]) for col in dataframe.columns]


################################################################################
################################################################################
################################################################################

def graba_matriz_de_transacciones(df, nombre_del_archivo_a_grabar):
    #
    #GRABA EL ARCHIVO , SETEANDO FORMATOS DE COLUMNAS, AUTOFIT
    writer = pd.ExcelWriter(original_source + nombre_del_archivo_a_grabar + '.xlsx', engine='xlsxwriter')
    #
    df.to_excel(writer, sheet_name='Transacciones_BMB')
    workbook  = writer.book
    worksheet = writer.sheets['Transacciones_BMB']
    #format1 = workbook.add_format({'num_format': '#.##0,00'})
    #format1 = workbook.add_format({'num_format': '#,##0;(#,##0)'})})
    #format1 = workbook.add_format({'num_format': '#,##0;(#,##0)'})})
    format1 = workbook.add_format({'num_format': '0.00'})
    get_col_widths(df)
    #
    # 
    for i, width in enumerate(get_col_widths(df)):
        worksheet.set_column(i, i, width)
    #
    # Setea la columna B a ancho 18 (contiene fecha)
    worksheet.set_column('B:B', 18, format1)
    # Setea la columna C a ancho 18
    worksheet.set_column('C:C', 18, format1)
    # Graba el archivo
    writer.save()

#graba_matriz_de_transacciones(df, "transacciones")

################################################################################
################################################################################
################################################################################

def arma_matriz_de_transacciones_a_una_fecha(dataframe, fecha_de_corte_inclusive, nombre_del_archivo_a_grabar):
    global df
    df = filtra_un_dataframe_de_transacciones_hasta_una_fecha(dataframe, fecha_de_corte_inclusive)
    # 
    # Graba el archivo
    graba_matriz_de_transacciones(dataframe, nombre_del_archivo_a_grabar)

#arma_matriz_de_transacciones_a_una_fecha(df, "2020-02-10", "BMB_05")


