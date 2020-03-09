def open_file_currency(name_part):
    ### Esta funcion abre un archivo de currency
    global cur
    # Location jamas termina con una barra
    location = original_source + "\CURRENCIES"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = ""
    #
    # Filename parte 2 es el name_part
    file_name_parte2 = name_part
    #
    # file_name es el total del nombre del archivo incluyendo al ticker que lo identifica                             
    file_name = file_name_parte1 + file_name_parte2     
    print (file_name)
    #
    # Extension es la extension del archivo
    extension = ".xlsx"
    #
    # Path es el todo la linea para llegar al archivo
    path = location + slash + file_name + extension
    #
    cur = pd.read_excel(path)
    #
    ####FORMATEO DEL ARCHIVO
    cur = cur.set_index('Fecha', inplace=False)
    #df.rename(columns = {'TIPO DE CAMBIO DEFINITIVO':'TC'}, inplace=True)      
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    #cur = cur.set_index('Fecha', inplace=False)
    #cur.index = cur.to_datetime(df.index, format="%d/%m/%Y") 
    #cur.drop([3])  #elimina la columna fuente en caso de ser necesaria.
    return

#open_file_currency("USDARS_LIBRE")

#cur = cur.drop(['FUENTE'], axis=1)

#df y cur

#merge=pd.merge(df, cur, how='inner', left_index=True, right_index=True) # Agrega una columna a la derecha de la Mkt Cap Ars que se llama USDARS_LIBRE

#merge['Mkt_Cap_USD'] = merge['Mkt_Cap_ARS'] / merge['USDARS_LIBRE']  # Genera y asigna una columna calculada a merge

#df = merge

def save_file_mkt_cap_usd(ticker3):
    ### Esta funcion toma la df global y la graba en un archivo con el nombre MKT_CAP_USD_ticker en el subdirectorio especificado
    global df
    location = original_source + "\MARKET_CAP_USD"                                 
    filename = str("MKT_CAP_USD_" + ticker3)     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()
    return

#save_file_mkt_cap_usd("SAMI")

def update_mkt_cap_usd(ticker4):
    # Esta funcion crea una matriz de mkt cap usd
    # Y graba la matriz en un subdirectorio MKT CAP USD
    global df, cur
    open_file_currency("USDARS_LIBRE")
    cur = cur.drop(['FUENTE'], axis=1)
    cur = cur.drop(['Especie'], axis=1)
    open_file_mkt_cap_ars(original_source + "\MARKET_CAP_ARS", ticker4, ".xlsx")
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
    save_file_mkt_cap_usd(ticker4)
    return

### FUNCION OPEN FILE MKT CAP USD Y LO CARGA EN LA MATRIZ DF
def open_file_mkt_cap_usd(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel mkt_cap_ars_ticker, con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = "MKT_CAP_USD_" + str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    print (path)
    df = pd.read_excel(path)
    #### FORMATEO
    df.rename(columns = {'Especie':'Especie'}, inplace=True)
    df.rename(columns = {'Fecha':'Fecha'}, inplace=True)
    df.rename(columns = {'Vencimiento':'Vencimiento'}, inplace=True)
    df.rename(columns = {'Tipo de Serie':'Tipo_de_Serie'}, inplace=True)
    df.rename(columns = {'Último':'Cierre_del_día'}, inplace=True)
    df.rename(columns = {'Variacion %':'Variación_%'}, inplace=True)
    df.rename(columns = {'Apertura':'Apertura'}, inplace=True)
    df.rename(columns = {'Máximo':'Máximo'}, inplace=True)
    df.rename(columns = {'Mínimo':'Mínimo'}, inplace=True)
    df.rename(columns = {'Volumen Nominal':'Volumen_Nominal'}, inplace=True)
    df.rename(columns = {'Monto Negociado':'Monto_Negociado'}, inplace=True)
    df.rename(columns = {'N° Oper':'Nro_Operaciones'}, inplace=True)      
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    return

#PRUEBA
#open_file_mkt_cap_usd("C:\GCB_CAPITAL\MARKET_CAP_USD", "AGRO", ".xlsx")
#open_file_mkt_cap_usd("C:\GCB_CAPITAL\MARKET_CAP_USD", "BOLT", ".xlsx")
#open_file_mkt_cap_usd("C:\GCB_CAPITAL\MARKET_CAP_USD", "TXAR", ".xlsx")

###PRUEBA
#update_mkt_cap_usd("AGRO")
#update_mkt_cap_usd("ALUA")
#update_mkt_cap_usd("AUSO")
#update_mkt_cap_usd("BBAR")
#update_mkt_cap_usd("BHIP")
#update_mkt_cap_usd("BMA")
#update_mkt_cap_usd("BOLT")
#update_mkt_cap_usd("BPAT")
#update_mkt_cap_usd("BRIO")
#update_mkt_cap_usd("BYMA")
#update_mkt_cap_usd("CADO")
#update_mkt_cap_usd("CAPX")
#update_mkt_cap_usd("CEPU")
#update_mkt_cap_usd("CGPA2")
#update_mkt_cap_usd("COME")
#update_mkt_cap_usd("CRES") #FALTA MAL LOS SPLITS REVISAR TODO
#update_mkt_cap_usd("CTIO")
#update_mkt_cap_usd("CVH")
#update_mkt_cap_usd("DGCU2")
#update_mkt_cap_usd("EDN") #FALTA LA SERIE LARGA DE BOLSAR
#update_mkt_cap_usd("ESME")
#update_mkt_cap_usd("FERR")
#update_mkt_cap_usd("GCLA")
#update_mkt_cap_usd("GGAL")
#update_mkt_cap_usd("HARG")
#update_mkt_cap_usd("INTR")
#update_mkt_cap_usd("INVJ")
#update_mkt_cap_usd("LEDE")
#update_mkt_cap_usd("LOMA")
#update_mkt_cap_usd("METR")
#update_mkt_cap_usd("MIRG")
#update_mkt_cap_usd("MOLA")
#update_mkt_cap_usd("MOLI")
#update_mkt_cap_usd("OEST")
#update_mkt_cap_usd("PAMP")
#update_mkt_cap_usd("PATA")
#update_mkt_cap_usd("RICH")
#update_mkt_cap_usd("SAMI")
#update_mkt_cap_usd("SUPV")
#update_mkt_cap_usd("TECO2")
#update_mkt_cap_usd("TGNO4")
#update_mkt_cap_usd("TGSU2")
#update_mkt_cap_usd("TRAN")
#update_mkt_cap_usd("TXAR")
#update_mkt_cap_usd("VALO")
#update_mkt_cap_usd("YPFD")

#cur = 0 # define a cur como una variable global
