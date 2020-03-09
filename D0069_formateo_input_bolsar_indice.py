
def formateo_input_bolsar_indice(df):
    # Toma un dataframe y la transforma poniendo los nombres correctos a las columnas
    # Transforma el indice para poder operar sobre las columnas
    df=df.reset_index()
    #
    # EL FORMATO DE INPUT ES EL CRUDO DE BOLSAR/BYMA
    #
    #Columna 1: Fecha (Indice) seteado cuando se secciono el archivo original
    #Columna 2: Especie
    #Columna 3: Vencimiento
    #Columna 4: Tipo de Serie
    #Columna 5: Cierre_del_dia
    #Columna 6:            <<<<<< FALTA
    #Columna 7: Apertura
    #Columna 8: Maximo
    #Columna 9: Minimo
    #Columna10: Volumen_Nominal
    #Columna11: Monto_Negociado
    #Columna12: Nro_Operaciones
    #
    # EL FORMATO DE OUTPUT GENERAL DE LA SPCH
    #
    #Columna 1: Fecha (Indice)
    #Columna 2: Especie
    #Columna 3: Vencimiento
    #Columna 4: Tipo de Serie
    #Columna 5: Cierre_del_dia
    #Columna 6: Variacion_%
    #Columna 7: Apertura
    #Columna 8: Maximo
    #Columna 9: Minimo
    #Columna10: Volumen_Nominal
    #Columna11: Monto_Negociado
    #Columna12: Nro_Operaciones
    #
    #
    # PREPARADO DEL OUTPUT
    #
    # INSERTA LA COLUMNAS QUE FALTAN AL DATAFRAME
    if "Variación %" not in df:
        df.insert(5, "Variacion_%", "any")
    #
    #### FORMATEO DEL NOMBRE DE LAS COLUMNAS
    #
    df.rename(columns = {'Especie':'Especie'}, inplace=True)
    #df.rename(columns = {'Fecha':'Fecha'}, inplace=True)
    df.rename(columns = {'Vencimiento':'Vencimiento'}, inplace=True)
    df.rename(columns = {'Tipo de Serie':'Tipo_de_Serie'}, inplace=True)
    df.rename(columns = {'Cierre del día':'Cierre_del_dia'}, inplace=True)
    df.rename(columns = {'Cierre_del_día':'Cierre_del_dia'}, inplace=True)
    df.rename(columns = {'Último':'Cierre_del_dia'}, inplace=True)
    #   df['Variación %']= 0
    df.rename(columns = {'Variación %':'Variacion_%'}, inplace=True)
    df.rename(columns = {'Apertura':'Apertura'}, inplace=True)
    df.rename(columns = {'Máximo':'Maximo'}, inplace=True)
    df.rename(columns = {'Mínimo':'Minimo'}, inplace=True)
    df.rename(columns = {'Volumen Nominal':'Volumen_Nominal'}, inplace=True)
    df.rename(columns = {'Monto Negociado':'Monto_Negociado'}, inplace=True)
    df.rename(columns = {'N° Oper':'Nro_Operaciones'}, inplace=True)      
    #
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False) 
    #
    # Establece con formato de bolsar el indice
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y")
    #
    return (df)


#formateo_input_bolsar_indice(df)


#df = open_file_spch("C:\GCB_CAPITAL\SPCH", "SERIE_CORRIENTE_BOLT" , ".xlsx")
#df2 = open_file_versatil("C:\GCB_CAPITAL\INPUT", "BOLT", ".xlsx")


#df2 = serie_de_tiempo(df2)
#df2 = formateo_input_bolsar(df2)

#list(df.columns) == list(df2.columns)