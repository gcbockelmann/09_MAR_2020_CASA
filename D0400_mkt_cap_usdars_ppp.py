

#####################################################33
#HACER UN CHART DEL MARKET CAP EN USDARS_PPP
##########################################33

cur = 0 # define a cur como una variable global

def open_file_versatil(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    print (path)
    df = pd.read_excel(path)
    return (df)

###########################################################
# Tratamiento a la serie USDPPP
#open_file_versatil("C:\GCB_CAPITAL\CURRENCIES", "USDARS_PPP", ".xlsx")
#serie_de_tiempo(df)
#df.columns = ['USDARS_PPP', 'W', 'X', 'Y']
#df.drop
# Drop the column with label 'A'

#df.drop('W', axis=1, inplace=True)
#df.drop('X', axis=1, inplace=True)
#df.drop('Y', axis=1, inplace=True)


######## FUNCION CREA MATRIZ USDPPP
#
cur = 0 # define a cur como una variable global

def update_mkt_cap_usdppp(ticker25):
    # Esta funcion crea una matriz de mkt cap usdppp
    # Y graba la matriz en un subdirectorio MKT CAP USDPPP
    global df, cur
    #
    # Carga la matriz de USDARS_PPP
    #
    cur = open_file_versatil(original_source + "\CURRENCIES", "USDARS_PPP", ".xlsx")
    cur = df
    cur = serie_de_tiempo(cur)
    # Crea una matriz solo con la columna "tc_real"
    cur = cur[['tc_real']]
    #
    #
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
    open_file_mkt_cap_usd(original_source + "\MARKET_CAP_USD", ticker25, ".xlsx")
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
    save_file_mkt_cap_usdppp(ticker25)
    #
    return df

def save_file_mkt_cap_usdppp(ticker26):
    ### Esta funcion toma la df global y la graba en un archivo con el nombre MKT_CAP_USDPPP_ticker en el subdirectorio especificado
    global df
    location = original_source + "\MARKET_CAP_USDPPP"                                 
    filename = str("MKT_CAP_USDPPP_" + ticker26)     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()
    return

#save_file_mkt_cap_usdppp("AGRO")
#save_file_mkt_cap_usdppp("SAMI")




#update_mkt_cap_usdppp("AGRO")
#update_mkt_cap_usdppp("ALUA")
#update_mkt_cap_usdppp("AUSO")
#update_mkt_cap_usdppp("BBAR")
#update_mkt_cap_usdppp("BHIP")
#update_mkt_cap_usdppp("BMA")
#update_mkt_cap_usdppp("BOLT")
#update_mkt_cap_usdppp("BPAT")
#update_mkt_cap_usdppp("BRIO")
#update_mkt_cap_usdppp("BYMA")
#update_mkt_cap_usdppp("CADO")
#update_mkt_cap_usdppp("CAPX")
#update_mkt_cap_usdppp("CEPU")
#update_mkt_cap_usdppp("CGPA2")
#update_mkt_cap_usdppp("COME")
#update_mkt_cap_usdppp("CRES") #FALTA MAL LOS SPLITS REVISAR TODO
#update_mkt_cap_usdppp("CTIO")
#update_mkt_cap_usdppp("CVH")
#update_mkt_cap_usdppp("DGCU2")
#update_mkt_cap_usdppp("EDN") #FALTA LA SERIE LARGA DE BOLSAR
#update_mkt_cap_usdppp("ESME")
#update_mkt_cap_usdppp("FERR")
#update_mkt_cap_usdppp("GCLA")
#update_mkt_cap_usdppp("GGAL")
#update_mkt_cap_usdppp("HARG")
#update_mkt_cap_usdppp("INTR")
#update_mkt_cap_usdppp("INVJ")
#update_mkt_cap_usdppp("LEDE")
#update_mkt_cap_usdppp("LOMA")
#update_mkt_cap_usdppp("METR")
#update_mkt_cap_usdppp("MIRG")
#update_mkt_cap_usdppp("MOLA")
#update_mkt_cap_usdppp("MOLI")
#update_mkt_cap_usdppp("OEST")
#update_mkt_cap_usdppp("PAMP")
#update_mkt_cap_usdppp("PATA")
#update_mkt_cap_usdppp("RICH")
#update_mkt_cap_usdppp("SAMI")
#update_mkt_cap_usdppp("SUPV")
#update_mkt_cap_usdppp("TECO2")
#update_mkt_cap_usdppp("TGNO4")
#update_mkt_cap_usdppp("TGSU2")
#update_mkt_cap_usdppp("TRAN")
#update_mkt_cap_usdppp("TXAR")
#update_mkt_cap_usdppp("VALO")
#update_mkt_cap_usdppp("YPFD")



def open_file_mkt_cap_usdppp(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel mkt_cap_ars_ticker, con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = "MKT_CAP_USDPPP_" + str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    print (path)
    df = pd.read_excel(path)   
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    return

#PRUEBA
#open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "AGRO", ".xlsx")
#open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "BOLT", ".xlsx")
#open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "TXAR", ".xlsx")


