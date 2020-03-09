
### FUNCION OPEN FILE SPCH: ABRE UN ARCHIVO DE EXCEL CON LA SPCH Y LO CARGA EN LA MATRIZ DF
def open_file_spch(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel spch, con el nombre y ubicacion especificados y lo carga en la matriz df
    #
    # EL FORMATO DE OUTPUT GENERAL LA SPCH
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
    global df
    #
    # ARMA EL PATH PARA PODER LEER EL ARCHIVO
    #
    location = str(loc)                                 
    filename = str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    #
    print (path)
    #
    df = pd.read_excel(path)
    #
    #### FORMATEO
    df.rename(columns = {'Especie':'Especie'}, inplace=True)
    df.rename(columns = {'Fecha':'Fecha'}, inplace=True)
    df.rename(columns = {'Vencimiento':'Vencimiento'}, inplace=True)
    df.rename(columns = {'Tipo de Serie':'Tipo_de_Serie'}, inplace=True)
    df.rename(columns = {'Último':'Cierre_del_dia'}, inplace=True)
    df.rename(columns = {'Cierre_del_día':'Cierre_del_dia'}, inplace=True)
    df.rename(columns = {'Variación %':'Variacion_%'}, inplace=True)
    df.rename(columns = {'Variación_%':'Variacion_%'}, inplace=True)
    df.rename(columns = {'Apertura':'Apertura'}, inplace=True)
    df.rename(columns = {'Máximo':'Maximo'}, inplace=True)
    df.rename(columns = {'Mínimo':'Minimo'}, inplace=True)
    df.rename(columns = {'Volumen Nominal':'Volumen_Nominal'}, inplace=True)
    df.rename(columns = {'Monto Negociado':'Monto_Negociado'}, inplace=True)
    df.rename(columns = {'N° Oper':'Nro_Operaciones'}, inplace=True)      
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    return (df)

#open_file_spch("C:\GCB_CAPITAL2\SPCH", "SERIE_CORRIENTE_AGRO", ".xlsx")

