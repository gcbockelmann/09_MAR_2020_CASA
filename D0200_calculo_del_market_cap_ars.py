############################################ 
###   MODULO DE SPLITS
###


actual = 0 #Es una variable global que contiene al capital actual

def capital_actual(ticker):
    # El capital actual se carga en Millones de ARS
    global actual
    if ticker == "AGRO":
       actual = 100         
    elif ticker == "ALUA":
       actual = 2800     
    elif ticker == "AUSO":
       actual = 88.384092
    elif ticker == "BBAR":
       actual = 612.66
    elif ticker == "BHIP":
       actual = 1500
    elif ticker == "BMA":
       actual = 669.663
    elif ticker == "BOLT":
       actual = 1700      
    elif ticker == "BPAT":
       actual = 719.145  
    elif ticker == "BRIO":
       actual = 4315.5  
    elif ticker == "BYMA":
       actual = 76.25  
    elif ticker == "CADO":
       actual = 123.2
    elif ticker == "CAPX":
       actual = 179.802282
    elif ticker == "CEPU":
       actual = 1514.022
    elif ticker == "CGPA2":
       actual = 333.281049
    elif ticker == "COME":
       actual = 1510
    elif ticker == "CRES":
       actual = 494
    elif ticker == "CTIO":
       actual = 409.907
    elif ticker == "CVH":
       actual = 181
    elif ticker == "DGCU2":
       actual = 202.351
    elif ticker == "EDN":
       actual = 877.128
    elif ticker == "ESME":
       actual = 58.936904
    elif ticker == "FERR":
       actual = 534
    elif ticker == "GCLA":
       actual = 106.776004
    elif ticker == "GGAL":
       actual = 1426.765
    elif ticker == "HARG":
       actual = 352.056899
    elif ticker == "INTR":
       actual = 121.085807
    elif ticker == "INVJ":
       actual = 538.267868
    elif ticker == "LEDE":
       actual = 439.714
    elif ticker == "LOMA":
       actual = 59.642649
    elif ticker == "METR":
       actual = 569.171
    elif ticker == "MIRG":
       actual = 18
    elif ticker == "MOLA":
       actual = 49.082
    elif ticker == "MOLI":
       actual = 201.415
    elif ticker == "OEST":
       actual = 160
    elif ticker == "PAMP":
       actual = 1875
    elif ticker == "PATA":
       actual = 500
    elif ticker == "RICH":
       actual = 80.751087
    elif ticker == "SAMI":
       actual = 71.150988
    elif ticker == "SUPV":
       actual = 456.722
    elif ticker == "TECO2":
       actual = 2168.909384
    elif ticker == "TGNO4":
       actual = 439.374
    elif ticker == "TGSU2":
       actual = 780.894
    elif ticker == "TRAN":
       actual = 444.674
    elif ticker == "TXAR":
       actual = 4517.094
    elif ticker == "VALO":
       actual = 849.512
    elif ticker == "YPFD":
       actual = 392.4
    else:
       print("Ticker no identificado")
    return

#capital_actual("AGRO")
#capital_actual("ALUA")
#capital_actual("AUSO")
#capital_actual("BOLT")
#actual

value = 0 # Es una variable global que se va a utilizar para iterar la evolucion del capital hacia atras 



def capital_historico(ticker):
    global splits
    splits = pd.DataFrame() #Crea una matriz de pandas
    if ticker == "AGRO":
       splits = splits.append({'Fecha': '2019-04-26', 'capital': 75 }, ignore_index=True)     
       splits = splits.append({'Fecha': '2017-10-23', 'capital': 48 }, ignore_index=True)
       splits = splits.append({'Fecha': '2014-01-14', 'capital': 24 }, ignore_index=True)
       splits = splits.append({'Fecha': '2004-08-17', 'capital': 10.85 }, ignore_index=True)
       splits = splits.append({'Fecha': '2001-06-25', 'capital': 7.25 }, ignore_index=True)
    elif ticker == "ALUA":
       splits = splits.append({'Fecha': '2015-05-18', 'capital': 2500 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2011-12-29', 'capital': 1943 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2009-06-30', 'capital': 1518 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2008-10-21', 'capital': 1320 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2005-12-09', 'capital': 1120 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2003-12-22', 'capital': 700 }, ignore_index=True)
       splits = splits.append({'Fecha': '2003-02-06', 'capital': 510 }, ignore_index=True)
    elif ticker == "AUSO":
       splits = splits.append({'Fecha': '2012-12-20', 'capital': 175.396394 }, ignore_index=True)   
    elif ticker == "BBAR":
       splits = splits.append({'Fecha': '2017-07-03', 'capital': 536.361 }, ignore_index=True)
       splits = splits.append({'Fecha': '2009-09-18', 'capital': 471.361 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2004-10-13', 'capital': 368.128 }, ignore_index=True) 
    elif ticker == "BHIP":
       splits = splits.append({'Fecha': '2000-01-01', 'capital': 1500 }, ignore_index=True)    
    elif ticker == "BMA":
       splits = splits.append({'Fecha': '2017-07-12', 'capital': 608.943 }, ignore_index=True)  
       splits = splits.append({'Fecha': '2003-12-18', 'capital': 455.242 }, ignore_index=True)
       splits = splits.append({'Fecha': '2003-01-31', 'capital': 64.41 }, ignore_index=True)            
    elif ticker == "BOLT":
       splits = splits.append({'Fecha': '2019-04-04', 'capital': 1250 }, ignore_index=True)
       splits = splits.append({'Fecha': '2018-05-09', 'capital': 840 }, ignore_index=True)
       splits = splits.append({'Fecha': '2017-06-07', 'capital': 600 }, ignore_index=True)
       splits = splits.append({'Fecha': '2016-06-29', 'capital': 450 }, ignore_index=True)
       splits = splits.append({'Fecha': '2015-08-25', 'capital': 350 }, ignore_index=True)
       splits = splits.append({'Fecha': '2015-05-18', 'capital': 250 }, ignore_index=True)
       splits = splits.append({'Fecha': '2011-04-28', 'capital': 200 }, ignore_index=True)
       splits = splits.append({'Fecha': '2010-04-21', 'capital': 130 }, ignore_index=True)
       splits = splits.append({'Fecha': '2009-04-21', 'capital': 100 }, ignore_index=True)
       splits = splits.append({'Fecha': '2008-04-18', 'capital': 76.345688 }, ignore_index=True)        
    elif ticker == "BPAT":
       splits = splits.append({'Fecha': '2008-12-01', 'capital': 719.145 }, ignore_index=True) 
    elif ticker == "BRIO":
       splits = splits.append({'Fecha': '2018-07-31', 'capital': 2157.75 }, ignore_index=True)  
       splits = splits.append({'Fecha': '2016-08-17', 'capital': 1078.875 }, ignore_index=True)  
    elif ticker == "BYMA":
       splits = splits.append({'Fecha': '2017-12-01', 'capital': 76.25 }, ignore_index=True) 
    elif ticker == "CADO":
       splits = splits.append({'Fecha': '2017-09-20', 'capital': 110 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2016-10-20', 'capital': 100 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2014-07-01', 'capital': 56.59492 }, ignore_index=True)
       splits = splits.append({'Fecha': '2010-01-15', 'capital': 35 }, ignore_index=True)  
    elif ticker == "CAPX":
       splits = splits.append({'Fecha': '2008-04-07', 'capital': 59.934094 }, ignore_index=True) 
    elif ticker == "CEPU":
       splits = splits.append({'Fecha': '2017-02-02', 'capital': 189.253 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2016-11-02', 'capital': 199.742 }, ignore_index=True) 
    elif ticker == "CGPA2":
       splits = splits.append({'Fecha': '2000-12-28', 'capital': 333.281049 }, ignore_index=True) 
    elif ticker == "COME":
       splits = splits.append({'Fecha': '2018-05-08', 'capital': 1584.1 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2017-11-09', 'capital': 1452.386 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2016-11-30', 'capital': 1359.919 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2012-11-27', 'capital': 260.512 }, ignore_index=True) 
    elif ticker == "CRES":
       splits = splits.append({'Fecha': '1998-12-31', 'capital': 124.259392}, ignore_index=True) 
       splits = splits.append({'Fecha': '1998-12-31', 'capital': 124.259392}, ignore_index=True) 
    elif ticker == "CTIO":
       splits = splits.append({'Fecha': '2012-11-22', 'capital': 383.13315 }, ignore_index=True) 
    elif ticker == "CVH":
       splits = splits.append({'Fecha': '2017-08-31', 'capital': 181 }, ignore_index=True) 
    elif ticker == "DGCU2":
       splits = splits.append({'Fecha': '1999-09-01', 'capital': 202.351 }, ignore_index=True) 
    elif ticker == "EDN":
       splits = splits.append({'Fecha': '2007-04-30', 'capital': 877.128 }, ignore_index=True) 
    elif ticker == "ESME":
       splits = splits.append({'Fecha': '2009-12-28', 'capital': 43.431764 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2009-03-06', 'capital': 34.723189 }, ignore_index=True)
    elif ticker == "FERR":
       splits = splits.append({'Fecha': '2018-12-20', 'capital': 411 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2018-01-02', 'capital': 311 }, ignore_index=True) 
       splits = splits.append({'Fecha': '2016-12-16', 'capital': 234 }, ignore_index=True)
       splits = splits.append({'Fecha': '2015-12-16', 'capital': 188 }, ignore_index=True)
       splits = splits.append({'Fecha': '2014-12-02', 'capital': 160 }, ignore_index=True)
       splits = splits.append({'Fecha': '2012-03-19', 'capital': 134 }, ignore_index=True)
       splits = splits.append({'Fecha': '2011-11-09', 'capital': 113 }, ignore_index=True)
    elif ticker == "GCLA":
       splits = splits.append({'Fecha': '2017-08-29', 'capital': 287.418584 }, ignore_index=True) 
    elif ticker == "GGAL":
       splits = splits.append({'Fecha': '2018-09-04', 'capital': 1410.265 }, ignore_index=True)
       splits = splits.append({'Fecha': '2018-06-26', 'capital': 1300.265 }, ignore_index=True)
       splits = splits.append({'Fecha': '2013-09-09', 'capital': 1241.407 }, ignore_index=True)
       splits = splits.append({'Fecha': '2004-05-12', 'capital': 1092.407 }, ignore_index=True)       
    elif ticker == "HARG":
       splits = splits.append({'Fecha': '1999-11-29', 'capital': 50 }, ignore_index=True)
    elif ticker == "INTR":
       splits = splits.append({'Fecha': '2019-03-26', 'capital': 86.085807 }, ignore_index=True)
       splits = splits.append({'Fecha': '2018-01-16', 'capital': 60.372486 }, ignore_index=True)
       splits = splits.append({'Fecha': '2016-07-28', 'capital': 38.872732 }, ignore_index=True)
       splits = splits.append({'Fecha': '2013-09-10', 'capital': 34.385191 }, ignore_index=True)
       splits = splits.append({'Fecha': '2010-06-25', 'capital': 26.131336 }, ignore_index=True)
    elif ticker == "INVJ":
       splits = splits.append({'Fecha': '2017-12-11', 'capital': 432.610472 }, ignore_index=True)
       splits = splits.append({'Fecha': '2016-05-11', 'capital': 367.990379 }, ignore_index=True)
       splits = splits.append({'Fecha': '2014-05-29', 'capital': 315.42092 }, ignore_index=True)
    elif ticker == "LEDE":
       splits = splits.append({'Fecha': '1992-01-03', 'capital': 439.714 }, ignore_index=True)
    elif ticker == "LOMA":
       splits = splits.append({'Fecha': '2017-11-03', 'capital': 59.642649 }, ignore_index=True)
    elif ticker == "METR":
       splits = splits.append({'Fecha': '1994-11-24', 'capital': 560.171}, ignore_index=True)
    elif ticker == "MIRG":
       splits = splits.append({'Fecha': '2016-10-24', 'capital': 6 }, ignore_index=True)
    elif ticker == "MOLA":
       splits = splits.append({'Fecha': '2017-06-21', 'capital': 49.082 }, ignore_index=True)
    elif ticker == "MOLI":
       splits = splits.append({'Fecha': '2015-10-29', 'capital': 250.497 }, ignore_index=True)
    elif ticker == "OEST":
       splits = splits.append({'Fecha': '2007-06-25', 'capital': 80 }, ignore_index=True)
    elif ticker == "PAMP":
       splits = splits.append({'Fecha': '2019-03-15', 'capital': 2078 }, ignore_index=True)
       splits = splits.append({'Fecha': '2018-03-16', 'capital': 1938 }, ignore_index=True)
       splits = splits.append({'Fecha': '2017-02-22', 'capital': 1696 }, ignore_index=True)
       splits = splits.append({'Fecha': '2007-09-13', 'capital': 1526.194242 }, ignore_index=True)
       splits = splits.append({'Fecha': '2006-05-16', 'capital': 446 }, ignore_index=True)
    elif ticker == "PATA":
       splits = splits.append({'Fecha': '2013-02-27', 'capital': 50 }, ignore_index=True)
       splits = splits.append({'Fecha': '2006-12-11', 'capital': 23 }, ignore_index=True)
    elif ticker == "RICH":
       splits = splits.append({'Fecha': '2017-12-26', 'capital': 80.751087 }, ignore_index=True)
    elif ticker == "SAMI":
       splits = splits.append({'Fecha': '2018-05-07', 'capital': 64.423488 }, ignore_index=True)
       splits = splits.append({'Fecha': '2012-11-16', 'capital': 15.25 }, ignore_index=True)
       splits = splits.append({'Fecha': '2009-08-25', 'capital': 7.625 }, ignore_index=True)
    elif ticker == "SUPV":
       splits = splits.append({'Fecha': '2017-08-25', 'capital': 363.777 }, ignore_index=True)
    elif ticker == "TECO2":
       splits = splits.append({'Fecha': '2018-05-07', 'capital': 1200 }, ignore_index=True)
       splits = splits.append({'Fecha': '2018-02-08', 'capital': 984.380978 }, ignore_index=True)
    elif ticker == "TGNO4":
       splits = splits.append({'Fecha': '2008-10-21', 'capital': 351.499185 }, ignore_index=True)
    elif ticker == "TGSU2":
       splits = splits.append({'Fecha': '1994-05-16', 'capital': 780.894 }, ignore_index=True)
    elif ticker == "TRAN":
       splits = splits.append({'Fecha': '2006-03-31', 'capital': 436.226295 }, ignore_index=True)
       splits = splits.append({'Fecha': '2005-04-27', 'capital': 360.198818 }, ignore_index=True)
    elif ticker == "TXAR":
       splits = splits.append({'Fecha': '2012-03-06', 'capital': 347.468771 }, ignore_index=True)
    elif ticker == "VALO":
       splits = splits.append({'Fecha': '2017-06-08', 'capital': 0.0001 }, ignore_index=True)
    elif ticker == "YPFD":
       splits = splits.append({'Fecha': '1993-07-08', 'capital': 392.4 }, ignore_index=True)
    else:
       print("Ticker no identificado")
       return
    splits = splits.set_index('Fecha', inplace=False) # Sete el indice como la columna Fecha
    splits.index = pd.to_datetime(splits.index, format="%Y-%m-%d") # Convertimos el indice en date time con el formato ANIO-MES-DIA
    splits['capital'] = splits['capital'].astype(float) # Convierte la columna de capital a punto flotante 
    return

##PRUEBA
#capital_historico("AGRO")
#capital_historico("ALUA")
#capital_historico("BOLT")




def update_mkt_cap_ars(ticker):
    # Esta funcion crea una matriz de mkt cap ars armando el capital por medio de una iteracion utilizando un dataframe con fechas e importes de splits
    # Y graba la matriz en un subdirectorio MKT CAP ARS
    global df, actual, value, splits, original_source
    #
    # Capital historico asigna a la variable splits un array con los valores y las fechas de split del capital en Millones.
    capital_historico(ticker)
    #
    # Capital actual asigna a la variable actual el valor actual del capital para ese ticker en Millones.        
    capital_actual(ticker)
    #
    ###############SERIA BUENO QUE ABRA LA SERIE QUE CORRESPONDE
    filename = str("SERIE_CORRIENTE_" + ticker)  
    open_file_spch(original_source+"SPCH", filename, ".xlsx") #abre la spch
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
    save_file_mkt_cap_ars(original_source+"MARKET_CAP_ARS", ticker, ".xlsx")
    return
    

def save_file_mkt_cap_ars(loc, ticker, ext):
    ### Esta funcion toma la df global y la graba en un archivo con el nombre MKT_CAP_ARS_ticker en el subdirectorio especificado
    global df
    location = str(loc)                                 
    filename = str("MKT_CAP_ARS_" + ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()
    return


def calculate(mul):
    # Esta funcion calcula el capital con calculo iterativo
    global value
    if mul == 0: 
       value = value
    else:
       value = mul    
    return value

### FUNCION OPEN FILE MKT CAP ARS Y LO CARGA EN LA MATRIZ DF
def open_file_mkt_cap_ars(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel mkt_cap_ars_ticker, con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = "MKT_CAP_ARS_" + str(ticker)     
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
    return (df)

#PRUEBA
#open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", "AGRO", ".xlsx")
#open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", "BOLT", ".xlsx")
#open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", "TXAR", ".xlsx")
 






###PRUEBA
#update_mkt_cap_ars("AGRO")
#update_mkt_cap_ars("ALUA")
#update_mkt_cap_ars("AUSO")
#update_mkt_cap_ars("BBAR")
#update_mkt_cap_ars("BHIP")
#update_mkt_cap_ars("BMA")
#update_mkt_cap_ars("BOLT")
#update_mkt_cap_ars("BPAT")
#update_mkt_cap_ars("BRIO")
#update_mkt_cap_ars("BYMA")
#update_mkt_cap_ars("CADO")
#update_mkt_cap_ars("CAPX")
#update_mkt_cap_ars("CEPU")
#update_mkt_cap_ars("CGPA2")
#update_mkt_cap_ars("COME")
#update_mkt_cap_ars("CRES") #FALTA MAL LOS SPLITS REVISAR TODO
#update_mkt_cap_ars("CTIO")
#update_mkt_cap_ars("CVH")
#update_mkt_cap_ars("DGCU2")
#update_mkt_cap_ars("EDN") 
#update_mkt_cap_ars("ESME")
#update_mkt_cap_ars("FERR")
#update_mkt_cap_ars("GCLA")
#update_mkt_cap_ars("GGAL")
#update_mkt_cap_ars("HARG")
#update_mkt_cap_ars("INTR")
#update_mkt_cap_ars("INVJ")
#update_mkt_cap_ars("LEDE")
#update_mkt_cap_ars("LOMA")
#update_mkt_cap_ars("METR")
#update_mkt_cap_ars("MIRG")
#update_mkt_cap_ars("MOLA")
#update_mkt_cap_ars("MOLI")
#update_mkt_cap_ars("OEST")
#update_mkt_cap_ars("PAMP")
#update_mkt_cap_ars("PATA")
#update_mkt_cap_ars("RICH")
#update_mkt_cap_ars("SAMI")
#update_mkt_cap_ars("SUPV")
#update_mkt_cap_ars("TECO2")
#update_mkt_cap_ars("TGNO4")
#update_mkt_cap_ars("TGSU2")
#update_mkt_cap_ars("TRAN")
#update_mkt_cap_ars("TXAR")
#update_mkt_cap_ars("VALO")
#update_mkt_cap_ars("YPFD")
