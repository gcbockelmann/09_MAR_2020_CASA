
# Crea un diccionario de ISINs. 12 caracteres. los 2 primeros corresponden al codigo de pais.
#isin = {"ARP6823S1295":"Mirgor S.A.", "US00206R1023":"AT&T", "ARALUA010258":"Aluar S.A.", "ARSIDE010029":"Ternium Argentina S.A."}

# Crea un diccionario de Paises
#country = {"AR":"Argentina", "US":"United States"}

# Crea un diccionario de Stock Exchanges
#stock_exchange = {"ARG":"Argentina"}

# Crea un diccionario de Currencies
#currency = {"ARS":"Pesos de Argentina", "USD":"United States Dollars"}


#entity_number = {"1":"Mirgor S.A."}

#estado_contable es un vector

# El security va a tener un isin y con eso ya esta identificado, tipo de security (fixed income, renta variable, fideicomiso, opcion, swap, etc), subyacente, 
#security = {}

#instrumento = es una clase? no. es un tipo de instrumento.
# Asset class es otra cosa
# Instrument type?
# 


def calculate(vector):
    #
    global ticker
    global datos_empresa
    #
    ############################################# CARGA LAS VARIABLES DEL BALANCE SHEET, ESTADO DE RESULTADOS Y CASH FLOW
    #
    vector['RI1'] = vector['BI0001']
    vector['RI2'] = vector['BI0002']
    vector['RI3'] = vector['BI0003']
    vector['RI68'] = vector['BI0068']
    vector['RI68'] = vector['BI0068']
    vector['RI4'] = vector['BI0004']
    vector['RI7'] = vector['BI0007']
    vector['RI196'] = vector['BI0196']
    vector['RI8'] = vector['BI0008']
    vector['RI158'] = vector['BI0158']
    vector['RI260'] = vector['BI0260']
    vector['RI73'] = vector['BI0073']
    vector['RI266'] = vector['BI0266']
    vector['RI69'] = vector['BI0069']
    #Other Long-Term Assets & Investments es un titulo no  deberia tener un codigo.
    vector['RI69'] = vector['BI0069']
    vector['RI33'] = vector['BI0033']
    vector['RI31i'] = vector['BI0031_I'] ####POSIBLE PROBLEMA
    vector['RI32i'] = vector['BI0032_I'] ####POSIBLE PROBLEMA
    vector['RI6'] = vector['BI0006']
    vector['RI70'] = vector['BI0070']
    vector['RI71'] = vector['BI0071']
    vector['RI72'] = vector['BI0072']
    vector['RI34'] = vector['BI0034']
    vector['RI5'] = vector['BI0005']
    vector['RI9'] = vector['BI0009']
    vector['RI75'] = vector['BI0075']
    vector['RI35'] = vector['BI0035']
    vector['RI38'] = vector['BI0038']
    vector['RI181'] = vector['BI0181']
    vector['RI216'] = vector['BI0216']
    vector['RI60'] = vector['BI0060']
    vector['RI130'] = vector['BI0130']
    vector['H1467'] = vector['RI6']-vector['RI181']-vector['RI216']
    #vector['H1621'] = vector['']
    #
    # ESTADO DE RESULTADOS
    #
    vector['RI12'] = vector['BI0012']
    vector['RI41'] = vector['BI0041']
    vector['RI189'] = vector['BI0189']
    vector['RI649'] = vector['BI0649']
    vector['RI13'] = vector['BI0013']
    # D&A
    vector['RI14'] = vector['BI0014']
    vector['RI178'] = vector['BI0178']
    # Pretax Income
    vector['RI15'] = vector['BI0015']
    vector['RI61'] = vector['BI0061']
    vector['RI17'] = vector['BI0017']
    vector['RI170'] = vector['BI0170']
    #Net income after minority Interest
    vector['RI16'] = vector['BI0016']
    vector['RI49'] = vector['BI0049']
    vector['RI18'] = vector['BI0018']
    vector['RI47'] = vector['BI0047']
    vector['RI46'] = vector['BI0046']
    vector['RI190'] = vector['RI61']-vector['RI62']
    vector['RI55'] = vector['BI0055']
    #
    # PRIMERAS VARIABLES OBTENIDAS DE OTRO LADO
    #
    #vector['H1602'] = vector['']
    # Market Section
    # Calculo del maximo
    vector['RI22'] = get_max_price(ticker, str(vector['reporting_year']),"12", "31")
    #
    vector['RI23'] = get_min_price(ticker, str(vector['reporting_year']),"12", "31")
    #
    #Calculo de la variable RI24, toma el precio historico
    if get_price(ticker, str(vector['reporting_year']),"12", "31") == "NA":
       vector['RI24'] = 0
    else:
       vector['RI24'] = get_price(ticker, str(vector['reporting_year']),"12", "31")
    # 
    # 
    vector['H1200'] = vector['RI7']   
    #
    # Calcula la Land and Improvements base del calculo del Land Inflation
    vector['H1439'] = vector['RI260']
    #
    # Calcula la Construction in Progress utilizada el Global Depreciating Assets
    vector['H1231'] = vector['RI266']
    #vector['H1201'] = (vector['H1200']-vector['H1439']-vector['H1231'])
    #vector['H1202'] = vector['RI14']-vector['RI65']
    #vector['H1201'] = vector['H1200']
    #vector['H1005'] = vector['H1201']/vector['H1202']     #es la que causa el problema
    #  
    #
    # SYSTEM CONSTANTS
    #
    #vector['Year']=0
    vector['Year'] = vector['reporting_year']
    #print (vector['Year'])
    #
    if datos_empresa["CCLASS"]=="I":
       vector['FRMCLASS']=0
    else:
       vector['FRMCLASS']=1       
    #
    # coloca el Gdp corriente
    if get_gdp_corriente(str(vector['reporting_year']),"12", "31") == "NA":
       vector['gdp_precios_corrientes']= 0
    else:
       vector['gdp_precios_corrientes']= get_gdp_corriente(str(vector['reporting_year']),"12", "31")
    #
    #if str(vector['reporting_year']-1) in df_show:
    #   a = extrae(str(vector['Year']-1), 'gdp_precios_corrientes')  
    #   vector['H1616']=vector['gdp_precios_corrientes']/a
    #else:
    #   vector['H1616']= 1.30
    #
    if str(vector['reporting_year']-1) in df_show:
       a = extrae(str(vector['reporting_year']-1), 'gdp_precios_corrientes')  
       vector['H1502GDP']=(vector['gdp_precios_corrientes'])/a
    else:
       vector['H1502GDP']=1.3060
    #
    ######################################################## GLOBAL NON DEPRECIATING ASSETS - CARGA LAS VARIABLES QUE SON FACILMENTE COPIA DE OTRAS
    # Comienza a calcular las variables desde abajo hacia arriba    
    #
    # Calcula la "Other Assets less Deferred Charges"
    vector['H1419']=vector['RI69']
    #
    # Calcula esta variable auxiliar
    vector['H1423']=vector['H1419']
    #
    #
    #Calcula esta variable auxiliar
    vector['H1413']=vector['H1423']
    #
    #Calcula "Industrial Receivables"
    vector['H1409']=vector['RI2']
    #
    #Calcula "Other Current Assets"                                   "(-) Investment & Other Charges"
    vector['H1412']=vector['RI68']
    #
    vector['H1414']=vector['RI69']+vector['RI33']+vector['RI31i']+vector['RI32i']
    #
    # Calcula "Monetary Assets"
    vector['H1430']=vector['RI1']+vector['H1409']+vector['H1412'] #+vector['H1429']
    #
    # Calcula Lmonetary Liabs Excluding Debt
    vector['H1418']=vector['RI70']+vector['RI71']+vector['RI72']
    #
    #
    #
    # Calcula la "Other Assets - Long-Term"
    vector['H1417'] = vector['H1419']
    #
    # FALTA LA H1449 PORQUE EL CALCULO DE LA INFLATION ADJUSTED LAND (H1449) NECESITA CALCULAR PREVIAMENTE H1439(land), H1011(years), H1809GP(gross plant growth)
    #
    # 
    #
    # Calcula "Inflation Adjusted Inventories"
    vector['H1445']=vector['RI3']
    #
    # Calcula "Investment & Advances"
    vector['H1422']=vector['RI32i']
    #
    # Calcula "Net Monetary Assets"
    vector['H1441']=vector['H1430']-vector['H1418']    
    #
    #
    #
    #
    # GLOBAL DEPRECIATING ASSETS
    #    
    vector['H1200'] = vector['RI7']
    #
    #
    #vector['H1102'] = "Viene definida por un input anterior"
    #
    #
    #
    ###################################################################################### GROSS PLANT LIFE
    # Calcula el valor de la mediana y llega muy bien al valor de la variable H1011
    #
    #vector['Year']  
    #vector['H1006'] = str(vector['Year']-1)
    from statistics import median
    #if str(vector['Year']-1) in df_show:
    #   a = extrae(str(vector['Year']-1, 'H1005')
    #else:
    #   a = 0
    #if str(vector['Year']-2) in df_show:
    #   b = extrae(str(vector['Year']-2), 'H1005')
    #else:
    #   b = 0
    #vector['H1006'] = median([vector['H1005'],a,b])
    vector['H1201'] = (vector['H1200']-vector['H1439']-vector['H1231']) 
    vector['H1202'] = (vector['RI14']-vector['RI65']) 
    #vector['H1102'] = 0
    vector['H1005'] = (vector['H1201']/vector['H1202']) 
    #
    # Calculo del Gross Plant life median
    vector['H1001'] = 4
    vector['H1003'] = 30
    vector['H1002'] = round(((vector['H1001']+vector['H1003'])/2),3)
    # Calculo de la Gross Plant Life Mediana
    from statistics import median
    #vector['H1006'] = 9.71                                       # FALTA REVEEER MEDIANA CON HISTORIA 
    #
    # Arma el vector para la mediana historica "H1006"   
    #     
    if str(vector['reporting_year']-1) in df_show:
       a = extrae(str(vector['reporting_year']-1), 'H1005')  
       #print(a)
    else:
       a = 0
    if str(vector['reporting_year']-2) in df_show:
       b = extrae(str(vector['reporting_year']-2), 'H1005')
       #print(b)
    else:
       b = 0
    # Para la mediana tengo que armar una lista
    lista_para_mediana =[vector['H1005'],a,b]    
    if str(vector['reporting_year']-1) in df_show and str(vector['reporting_year']-2) in df_show:   
       vector['H1006'] = median(lista_para_mediana)
    else:
       vector['H1006']=vector['H1005']
    #
    #
    #vector['H1006'] = vector['H1005'] + extrae(str(vector['reporting_year']-1), 'H1005')+ extrae(str(vector['reporting_year']-2), 'H1005')
    #vector['H1006'] = ("Columna"+str(int(columna)-1))['H1005']
    #vector['H1006'] = vector['H1005']+ 2 anios anteriores
    # Para la mediana tengo que armar una lista
    lista_para_mediana =[vector['H1006'],vector['H1001'],vector['H1003']]
    #vector['H1007'] = median(lista_para_mediana)
    vector['H1007']=max(min(vector['H1006'],vector['H1003']),vector['H1001'])   
    import math
    #vector['H1011'] = math.ceil(vector['H1007'])
    vector['H1011']=round(vector['H1007'],0) 
    #
    # 
    #
    vector['H1022'] = vector['H1021']
    vector['H1014'] = vector['H1022']+vector['H1023']+vector['H1024']+vector['RI542']
    vector['H1081'] = 40.00
    #
    # Vida de Machinery Life depende de la industria
    # MIRG = 9 , TXAR = 17
    #
    #vector['H1082'] = 17.00
    #
    if datos_empresa["GICS Global Industry Code Display"]=="Household Appliances":
        vector['H1082'] = 9.00
    elif datos_empresa["GICS Global Industry Code Display"]=="Steel":
        vector['H1082'] = 17.00
    #
    #
    #vector['H1083'] = 9.00
    #
    if datos_empresa["GICS Global Industry Code Display"]=="Household Appliances":
        vector['H1083'] = 9.00
    elif datos_empresa["GICS Global Industry Code Display"]=="Steel":
        vector['H1083'] = 17.00
    #
    vector['H1084'] = 5.00
    vector['H1085'] = 25.00
    vector['H1086'] = 15.00
    vector['H1087'] = 5.00
    vector['H1222'] = (vector['H1022']/vector['H1081'])+(vector['H1023']/vector['H1082'])+(vector['H1024']/vector['H1083'])+(vector['RI542']/vector['H1084'])+(vector['RI543']/vector['H1085'])+(vector['RI545']/vector['H1087'])
    vector['H1002'] = 17.00
    if vector['AVG'] >0:
       vector['H1015'] = vector['H1002']
    else:
       if vector['H1222'] !=0:
          vector['H1015'] = (vector['H1014']/vector['H1222'])
       else:
          vector['H1015'] = 1
    #
    #
    ######################################################################################## INTANGIBLES FIX FACTSHEET
    #
    #
    if vector['LIC_METHOD']==0:
       vector['HT1323'] = 0
    else:
       vector['HT1323'] = vector['RI537']+vector['RI536B']  
    vector['HT1348'] = vector['HT1323'] 
    vector['HT1307'] = vector['HT1348'] 
    #
    # Mediana historica para el calculo de la HT1331
    #
    # Arma el vector para la mediana historica del calculo de la "HT1331" en base a la "HT1330"   
    #     
    if str(vector['reporting_year']-1) in df_show:
       a = extrae(str(vector['reporting_year']-1), 'HT1330')  
       #print(a)
    else:
       a = 0
    if str(vector['reporting_year']-2) in df_show:
       b = extrae(str(vector['reporting_year']-2), 'HT1330')
       #print(b)
    else:
       b = 0
    # Para la mediana tengo que armar una lista
    lista_para_mediana =[vector['HT1330'],a,b]    
    vector['HT1331'] = median(lista_para_mediana)
    #
    #
    #
    vector['HT1483'] = vector['RI33']-vector['RI204']
    #
    ###################################################################################   OPERATING LEASES
    #
    vector['H1013'] = vector['H1007']
    #
    #
    vector['H2110_S'] = 7.90714263916016    # MANUAL INPUT
    vector['H2102'] = 599.76    # MANUAL INPUT    
    #
    #
    # Calculo de la variable H1243
    #
    import numpy
    tasa = (vector['H2110_S']/100)
    #print(tasa)
    periodo = round(vector['H1013'],0)
    #print(periodo)
    pago = -vector['RI47']
    #print(pago)
    vector['H1243'] = numpy.pv(tasa, periodo, pago)
    #
    #
    #
    #
    vector['H1221'] = vector['H1243']  
    #
    vector['H1242']=vector['H1221']
    #
    #vector['H1243']=vector['H1242']
    #
    import math
    #Esta tirando error siguiente es 505
    if vector['RI47'] >= 1:
       # (((((Vector2008['H2110_S']/100))*-Vector2008['H2102'])+Vector2008['BI0047']))
       if ((vector['H2110_S']/100))*(-vector['H2102'])+vector['BI0047'] >=1:
          vector['H1239'] = (math.log(vector['RI47'])-math.log((((((vector['H2110_S']/100))*-vector['H2102'])+vector['BI0047']))))/(math.log((1+(vector['H2110_S']/100))))
       else:
          #print("Problema en alguna variable distinta a la RI47")
          vector['H1239'] = 1
    else:
       #print("Problema en la RI47 menor o igual que 1")
       vector['H1239'] = 1
    #
    #
    ######################################################################### GLOBAL INFLATION ADJUSTED CASH FLOW
    #print("Prueba -Arranca el calculo de global inflation cash flow")
    #
    vector['H1622']=(vector['RI3']*vector['H1621']/100)
    #
    # Calcula el vector H1628 que depende del vector del anio anterior por ser LIFO Charge to inventories
    if str(vector['reporting_year']-1) in df_show:
       vector['H1628']=extrae(str(vector['reporting_year']-1), 'H1622')  
    else:
       vector['H1628']= 0
    #
    # PPI - PRODUCER PRICE INDEX
    # Calcula el vector H1620 que depende del vector del anio anterior por ser algo con los indices de precios del productor
    #if str(vector['reporting_year']-1) in df_show:
    #   if (extrae(str(vector['reporting_year']-1),'SYSC3')-1) != 0:
    #      vector['H1620']=((vector['SYSC3']/extrae(str(vector['reporting_year']-1), 'SYSC3'))-1)*100
    #else:
    #   vector['H1620']= 1
    #
    vector['H1620'] =100*(get_ppi_inflation(str(vector['reporting_year']),"12","31"))
    #
    #
    # FILA 340
    #
    vector['H1623']=-(vector['H1628']*vector['H1620'])/100
    #
    # Calcula el vector H1442 que depende del vector del anio anterior por ser algo con net monetary holding assets
    if str(vector['reporting_year']-1) in df_show:
       vector['H1442']=extrae(str(vector['reporting_year']-1), 'H1441')
    else:
       vector['H1442']= 0
    #
    # FILA 350
    #
    # Change in GNP Deflator
    # Formula original reemplazada por otra para input de GDP_corriente
    vector['H1616']=(vector['H1502GDP']-1)*100
    #
    #
    vector['H1617']=(-vector['H1442'])*vector['H1616']/100
    # 
    vector['H1612']=vector['RI15'] 
    #
    #
    vector['H1608']=vector['BI0018']
    #
    vector['H1605']=vector['RI17'] 
    #
    vector['H1602']=(vector['H1605']*vector['H1601'])/100
    #
    vector['H1653']=vector['RI55'] 
    #
    vector['H1609']=vector['H1608']-vector['H1605']+vector['H1602']-vector['H1653']
    #
    vector['H1615']=max(0, vector['H1609']+vector['RI14']+vector['H1612'])/10
    #
    vector['H1626']=vector['H1615']
    #
    #print (vector['H1617'])
    if vector['H1296']==0:
       vector['H1619']=0
    elif vector['H1296']==1:
       if vector['H1617'] == 0:
          vector['H1619']=min( vector['H1615'] , 0)
       else:
          vector['H1619']=min( vector['H1615'] , abs(vector['H1617']) )*(vector['H1617']/abs(vector['H1617']))
    #
    if vector['H1289']==0:
       vector['H1629']=0
    elif vector['H1289']==1:
       if vector['H1623'] != 0:
          vector['H1629']=min( abs(vector['H1623']) , vector['H1626'] )*(vector['H1623']/abs(vector['H1623']))
       else:
          vector['H1629']=0
    #
    #
    #if vector['H1289']==1:
    #   vector['H1629']=-vector['H1289']*(min(abs(vector['H1623']),abs(vector['H1626']*vector['H1623']/(abs(vector['H1623'])))))
    #else:
    #   vector['H1629']=0
    # vector['H1629']=0
    #
    # Non-Earning Cash Flow
    vector['H1659']=vector['RI14']+vector['RI47']+vector['RI49']+vector['H1612']+vector['H1619']+vector['H1629']
    #
    #
    vector['H1697']=vector['H1609']+vector['H1659']
    #
    ################################################################################################ PROJECT LIFE
    #
    # Calcula Current $ Gross Capitalized R&D
    vector['H1252']=0 #buscarla en numero de fila 722 formula complicada
    #
    # Calcula la "Implied Depreciation of Leased Assets for Project Life"
    vector['H1042']=vector['H1221']/vector['H1013']
    #
    #
    #
    #
    ############################################################## BOUNDED HISTORIC GROWTH RATE
    #print("Prueba -Arranca el calculo de bounded historic growth rate")
    #
    #
    # Calcula el vector "H1502" - Constant Currency Adjustment Factor - de la Bounded Historic Growth Rate
    if str(vector['reporting_year']-1) in df_show:
       vector['H1502']=(extrae(str(vector['reporting_year']-1), 'H1502'))*vector['H1502GDP']                                          
    else:
       #vector['H1502']=12089.665104137     #Para anio 2018    
       # Cambiar el vector de la 1502 por vector['H1502']=3379.93530
       # vector['H1502']=12089.665104137
       #
       vector['H1502']=3379.9353027 # Para anio 2002                  
    #
    #
    # Calcula la H1032 "Life - Capitalized R&D"
    vector['H1032'] = 5    # El modelo es activa 5 anios de investigacion y desarrollo  >>>> INPUT
    # 
    # Calcula la H1043 "Implied Amortization of Capitalized R&D for Project Life" 
    vector['H1043'] = 0
    #
    #
    #
    #
    ##################################################################################### INDUSTRY HISTORIC GROWTH RATE
    #print("Prueba -Arranca el calculo de indutry historic growth rate")
    # Industry Historic Growth Rate
    #
    #vector['H1800']= 1.7                                            # DEBE SER UN INPUT??
    # Poner la H1800 en 1.9 para que de bien el ano2002
    #vector['H1800']=1.7 # prueba para ver si da bien la tab del ano 2002.   ###################################### INPUT MANUAL
    vector['H1800']=100*(get_historic_industry_growth(str(vector['reporting_year']),"12","31"))
    #
    #
    #
    # 
    #
    #################################################################### CALCULOS DE TASAS DE CRECIMIENTO DE LA GROSS PLANT PARA PODER HACER EL LAND INFLATION ADJUSTMENT
    #
    # Calcula "Historic Growth Rate Upper Limit" de la Bounded Historic Growth Rate -
    vector['H1804']=30
    #
    # Calcula "Historic Growth Rate Lower Limit" de la Bounded Historic Growth Rate -
    vector['H1803']=-5
    #
    # Calcula la variable H1802GP de la Bounded Historic Growth Rate tomando como base la H1829GP del ano anterior
    if str(vector['reporting_year']-1) in df_show:
       vector['H1802GP']= extrae(str(vector['reporting_year']-1), 'H1829GP') 
    else:
       # En caso de ser el primer anio de analisis, esta variable es igual a la de la industria.
       vector['H1802GP']= vector['H1800']
    #
    # Calcula la H1809GP de la Bounded Historic Growth Rate - 
    if min(max(vector['H1802GP'],vector['H1803']),vector['H1804']) <= 0:
       vector['H1809GP']=11
    else:    
       vector['H1809GP']=min(max(vector['H1802GP'],vector['H1803']),vector['H1804'])
    #

    ###################################################################################################################################

    #

    #
    #
    ################################################################## CALCULO DEL LAND INFLATION ADJUSTMENT_VERSION ############################
    #print("Prueba -Arranca el calculo de land inflation adjustment")
    # Esta variable requiere previamente haber calculado la H1809GP.
    #
    # Si esta desactivado el ajuste por inflacion la H1295 es igual a 0
    #
    # Verifica los inputs de la funcion
    #print ("H1439")
    #print (int(vector['H1439']))    
    #print ("H1011 - Years")
    #print (int(vector['H1011']))
    #print ("H1809GP - Growth")
    #print (float(vector['H1809GP']))
    #
    if vector['H1295'] == 1:
       # Ajuste por inflacion encendido
       #
       #layers = arma_lista_de_capex_layers(vector['H1439'], 5, 22.4)
       #layers = arma_lista_de_capex_layers(vector['H1439'], int(vector['H1011']), 22.4)
       #
       # Arma la lista de capex layers
       layers = arma_lista_de_capex_layers(vector['H1439'], int(vector['H1011']), float(vector['H1809GP']))
       # Imprime la lista de capex layers
       #print(layers)
       #
       #a =(get_ppi_inflation(str(vector['reporting_year']),"12","31"))
       #print(a)
       #
       # Arma una lista de inflacion vacia 
       lista_de_inflacion = []
       #
       for i in range (0,int(vector['H1011'])):
           #print (i)
           #print(100*get_ppi_inflation((str( int(vector['reporting_year'])-i)),"12","31"))
           lista_de_inflacion.append(100*get_ppi_inflation((str( int(vector['reporting_year'])-i)),"12","31"))         
       #
       # Da vuelta el orden de la lista (reverse)
       lista_de_inflacion = lista_de_inflacion[::-1]
       #
       # Imprime la lista de inflacion
       #print(lista_de_inflacion)
       #
       if np.nan in lista_de_inflacion:
          # Valor provisorio para la H1449
          vector['H1449']=vector['H1439']
       else: 
          # Valor bien calculado de la H1449
          vector['H1449']=devuelve_total_ajustado_con_inflacion_compuesta(lista_de_inflacion, layers)
       #
       # Valor provisorio
       #vector['H1449']=vector['H1439']
       #
    else:
       # Ajuste por inflacion apagado
       vector['H1449']=vector['H1439']
    #
    ###############################################################################################################################
    # Calcula la variable H1425 - EL AJUSTE NETO - Que tambien esta en la hojita de Non-depreciating assets
    #
    # Si esta desactivado el ajuste por inflacion la H1295 es igual a 0
    if vector['H1295'] == 0:
       vector['H1425']=0
    else:
       vector['H1425']=(vector['H1449']-vector['H1439'])
    #
    ###############################################################################################################################
    #
    # Calcula Non-Depreciating Assets
    vector['H1497']=vector['H1441']+vector['H1422']+vector['H1445']+vector['H1449']+vector['H1417']          
    #
    #
    ##############################################Estos calculos pueden seguir despues del calculo de la land inflation adjustment
    # Estas variables son de la pagina Bounded Historic GRowth Rate pero debe ser calculada despues del land inflation adjustment y de la gross plant inflation adjustment
    #
    vector['H1823']= vector['H1800']
    vector['H1825']= vector['H1823']
    vector['H1827']= vector['H1825']
    vector['H1829']= vector['H1827']
    vector['H1802']= vector['H1800']
    #
    # Calcula la H1809 "Historic Growth Rate of Depreciating Assets" de la pagina Bounded Historic GRowth Rate pero debe ser calculada despues del land inflation adjustment y de la gross plant inflation adjustment
    vector['H1809'] = min(max(vector['H1802'],vector['H1803']),vector['H1804']) 
    #    #
    ############################################################################### CFROI Audit And Valuation
    #ESTA TAB ENTERA TIENE QUE IR DESPUES DEL CALCULO DEL INFLATION ADJUSTMENT H1449
    #
    vector['H1499']=vector['H1497']
    #
    vector['H1699']=vector['H1697']
    #
    #
    vector['ROIUIVFLR']=-0.01  
    #
    #
    vector['H2425']=5
    vector['H2425G']=5
    #
    # Market Value of Investments
    vector['H2440']= 0
    #
    # Value of Existing Assets
    vector['H2460']=49.97
    #vector['H2460']=  
           #valor presente de H2415 CFROI, la tasa
           #               de H2450 Replacement CFROI used in valuation 
           #               de H2416 CFROI futuro    
           #               de H2417 Growth Existing   
           #               de H2418 Normalized GRowth Rate used in valuation 
           #               de H2488 Sustainable Growth Rate
           #               de H2424 Non-depreciating Assets
           #               de H2423 Inflation Adjustment Gross Investment
           #               de H4405 DR as 1 yr rate
           #               de H2437 CFROI Fadefactor
           #               de H2425 ROI hold period
           #               de H1055 Asset Project Life
           #               de H2430 ROI exponential fade rate
           #               de H4431 Exponential Fade windows year
           #               de H2427 ROI FADE to
           #               de H2428 Growth fade to
           #               de H2429 Disc rate fade to
           #               de HS2450 Replacement CFROI Override pseudoscalar 
           #               de FOVRH2437 Sensitivity:Fade 
           #               de H2425G Growth Fade Window         
    vector['H2468']=-24.16
    vector['HS2450']=0
    vector['H2441']=vector['H2460']+vector['H2468']+vector['HS2450']
    #
    # Value of Future Assets
    vector['H2442']=-29.10
    #
    vector['H2443']=vector['H2441']+vector['H2442']+vector['H2440']
    #
    vector['H5400_USED']=0
    #
    vector['H5425']=26.1
    #
    vector['H5428']=1
    #
    vector['H5402']=min(vector['H5425'],vector['H5425']*(1-vector['H5400_USED']/100)+(vector['H5400_USED']/100*vector['H5428']))
    #
    vector['H2420']=1
    #
    vector['H5407']=vector['H5402']/vector['H2420']
    #
    vector['H2159']=vector['H5407']
    #
    vector['H2421']=vector['H2159']*vector['H2420']
    #
    vector['H2444']=vector['H2443']-vector['H2421']
    #
    vector['H2446']=vector['H2444']*vector['H2132_OR']
    #
    vector['H2447']=vector['H2444']-vector['H2446']
    # 
    vector['H1107']=vector['RI25']
    # Agregar al vector generico de columnas la RI27. despues de la RI25.
    vector['H1109']=vector['RI27']
    if vector['H1107'] != 0 and vector['H1109'] != 0:
       vector['H1111']=vector['H1107']*vector['H1109']
    else:
       vector['H1111']=vector['RI25']
    #
    vector['H2445']=vector['H2447']/vector['H1111']
    #
    #TERMINA CFROI AUDIT
    #
    #####################################################################################################################################################
    # Calcula la variable H1206 GROSS PLANT INFLATION ADJUSTMENT - si la H1394 del ajuste inflacionario es cero entonces es cero.
    #
    #if vector['H1394']==0:
    #   vector['H1206']=0
    #else:
    #   #vector['H1206']=vector['H1201']*(vector['H1102']-1)
    #   year=vector['reporting_year']
    #   #print(year)
    #   life_ = int(round(vector['H1011'],0))
    #   #print(life_)
    #   #vector['H1206']=f_dcf(year, 12, vector['H1011'], 22.4, vector['H1201'])  
    #   #vector['H1206']=f_dcf(year, 12, life_, , vector['H1201'])  
    #   #vector['H1206']=f_dcf(year, 12, life_, vector['H1809GP'], vector['H1201'])
    #
    #vector['H1207']=0
    #vector['H1207']=vector['H1201']+vector['H1206']
    #    
    #
    ######################################### CALCULO DE LA VARIABLE H1101
    #Esta variable es el land inflation factor
    #
    vector['H1101'] = vector['H1102']
    if vector['H1449'] !=0:
       vector['H1101']=vector['H1449']/vector['H1439']
    else:
       vector['H1101']=1
    #
    #
    ########################################## CALCULO DE LA VARIABLE H1102
    #Esta variable iguala el gross plant inflation factor al land inflation factor
    #
    #vector['H1102']=vector['H1207']/vector['H1201']
    vector['H1102']=vector['H1101']
    #
    ######################################### CALCULO DE LA VARIABLE H1207
    #Esta variable es la Gross Plant Adjusted (inflated)
    #
    vector['H1207']=vector['H1201']*vector['H1102']
    #
    #######################################################################
    ######################################### CALCULO DE LA VARIABLE H1206
    #Esta variable es la Gross Plant Inflation Adjustment
    #
    vector['H1206']=vector['H1207']-vector['H1201']
    #
    #######################################################################
    #Calcula el Depreciating Assets
    # Variable H1297 que depende de la H1243
    vector['H1297']=vector['H1207']+vector['H1231']+vector['H1243']
    #
    #Calcula el Inflation Adjusted GRoss Investment para el CFROI AUDIT u otra Tab
    vector['H1500']=vector['H1499']+vector['H1297']
    #
    # Calcula la H1504 para la Bounded Historic GRowth Rate
    if vector['H1502'] !=0:
       vector['H1504']=vector['H1500']/vector['H1502']
    else:
       vector['H1504']=1
    #
    #
    #
    #######################################################################
    #
    #
    # 
    #
    #
    #Como esta variable Depreciable Asset Sum for Project Life depende de la Inflation Adjusted Gross Plant debe estar aca abajo. 
    #esta variable es parte de la hojita PROJECT LIFE
    #
    if vector['LIC_METHOD']==0:
       vector['H1046']=vector['H1207']+vector['H1221']+vector['H1252']
    else:
       vector['H1046']=vector['H1207']+vector['H1221']+vector['H1252']+vector['HT1323']
    #
    #
    #
    ############################################################ CALCULO H1505GP hojita Bounded Historic Growth Rate
    #Como esta variable  depende de la Inflation Adjusted Gross Plant debe estar aca abajo. 
    #
    vector['H1501GP']=vector['H1207']
    #
    if vector['H1502'] !=0:
       vector['H1505GP']=vector['H1501GP']/vector['H1502']
    else:
       vector['H1505GP']=1
    #
    #######################################################################
    #
    # Calcula el vector "H1506". Si la clase es industrial la entorna con la Gross Plant.
    if vector['CCLASS']=="I":
       vector['H1506GPB']=vector['H1505GP']  
    else:
       vector['H1506GPB']=vector['H1504']  
    #
    #
    # Calcula el vector "H1508GPB". Toma el vector "H1506GPB" y lo divide por la cantidad de acciones
    if vector['CCLASS']=="I":
       vector['H1508GPB']=vector['H1506GPB']/vector['H1111'] 
    else:
       vector['H1508GPB']=vector['H1506GPB']/vector['H1111']      
    #
    # Calcula el vector "H1821GPB" usando el del anio anterior siempre que este disponible
    if str(vector['reporting_year']-1) in df_show:
       vector['H1821GPB']=vector['H1508GPB']/extrae(str(vector['reporting_year']-1), 'H1508GPB') 
    else:
       vector['H1821GPB']=1
    #
    vector['H1821GPA']=vector['H1821GPB']
    #
    vector['H1821GP']=vector['H1821GPA']
    #
    if vector['H1821GP']>=0.75:
       vector['H1823GP']=max(min(vector['H1821GP'],(1+(vector['H1804']/100))),(1+(vector['H1803']/100)))
    else:
       vector['H1823GP']=max(min(vector['H1821GP'],(1+(vector['H1804']/100))),(1+(vector['H1803']/100)))
    #
    vector['H1825GP']=math.log(vector['H1823GP'])
    #
    #
    # Calcula el promedio de los ultimos 7 anios
    # Primero checkea que existan los vectores
    #
    if str(vector['reporting_year']-6) in df_show and str(vector['reporting_year']-5) in df_show and str(vector['reporting_year']-4) in df_show and str(vector['reporting_year']-3) in df_show and str(vector['reporting_year']-2) in df_show and str(vector['reporting_year']-1) in df_show:
       import statistics
       list_for_mean = []
       list_for_mean.append(extrae(str(vector['reporting_year']-6), 'H1825GP'))
       list_for_mean.append(extrae(str(vector['reporting_year']-5), 'H1825GP'))
       list_for_mean.append(extrae(str(vector['reporting_year']-4), 'H1825GP'))
       list_for_mean.append(extrae(str(vector['reporting_year']-3), 'H1825GP'))
       list_for_mean.append(extrae(str(vector['reporting_year']-2), 'H1825GP'))
       list_for_mean.append(extrae(str(vector['reporting_year']-1), 'H1825GP'))
       list_for_mean.append(vector['H1825GP'])
       vector['H1827GP'] = statistics.mean(list_for_mean)
    else: 
       vector['H1827GP'] = "NA"
    #
    #
    if vector['H1827GP'] == "NA":
       vector['H1829GP']= 0
    else:
       vector['H1829GP']=100*(math.exp(vector['H1827GP'])-1)*100
    #
    #
    #En final de project life a copiarrrrrrrrrrrrrrr
    vector['H1041']=vector['H1207']/vector['H1007']
    #
    vector['H1045']=vector['H1041']+vector['H1042']
    #
    vector['H1051']=vector['H1046']/vector['H1045']
    #
    vector['H1053']=round(vector['H1051'],0)
    #
    vector['H1055']=round(vector['H1051'],0)
    #
    vector['H1056']=round(vector['H1051'],1)  #Eliminar la misma varible del CFROI AUdit
    #
    # CALCULO DE LA VARIABLE H2312
    #
    #    
    #Ejemplo de formula Rate
    #Solution = np.rate(6, 10000, 500, 200)  
    vector['H2312'] = 100*np.rate(vector['H1056'], vector['H1699'],  -vector['H1500'],  vector['H1499'])  
    #
    # CALCULO DE LA VARIABLE H2415T3
    #vector['H2415T3']=vector['ROIUIVFLR'] 
    #
    from statistics import median
    # Mediana para el calculo de la H2415T3
    # Arma el vector para la mediana del calculo de la "H2415T3" en base a la "H2312"   
    #     
    if str(vector['reporting_year']-1) in df_show:
       a = extrae(str(vector['reporting_year']), 'H2312')  
       #print(a)
    else:
       a = 0
    if str(vector['reporting_year']-2) in df_show:
       b = extrae(str(vector['reporting_year']-1), 'H2312')
       #print(b)
    else:
       b = 0
    # Para la mediana tengo que armar una lista
    lista_para_mediana =[6.10,a,b]    
    vector['H2415T3']=max(vector['ROIUIVFLR'], median(lista_para_mediana))
    # 
    # Es un problema porque calcula una mediana en vase al CFROI de la variable H2312 no solo del año actual y pasado sino del año futuro.
    # por eso recomiendo armar un segundo funcion de calculo que haga los calculos con variables habiendo recorrido ya todos los anos de valuacion. o sea que vuelva a repasar el df...todos loa anos
    #from statistics import median
    #A la formula mediana hay que entregarle una lista de numeros
    #
    #
    #
    #
    # ------------------------------------------------------------------------
    #
    # CALCULO DE LA VARIABLE H2312   - PUEDE QUE NO VAYA ACA-
    if datos_empresa["Designated Last Reported Year (MLASTM)"]==vector['reporting_year']:
       vector['H2415T2']=vector['H2312']
    else: 
       vector['H2415T2']="NA"
    #
    #vector['H2415T2']=0
    #
    if vector['H2415T2']=="NA":
       vector['H2415']=vector['H2415T3']
    else:
       vector['H2415']=vector['H2415T2']
    #
    #
    #
    # CALCULO DE LA VARIABLE 2415 - PUEDE QUE NO VAYA ACA-
    #
    #if str(vector['reporting_year'])=="NA":
    #   vector['H2415']=vector['H2415T2']
    #else:
    #   vector['H2415']=vector['H2415T3']    
    #---------------------------------------------------------------------------
    #
    #
    #
    vector['H2313']=vector['H2312']
    vector['H2316']=vector['H2312']
    vector['H2416']=vector['H2312']
    #
    #
    #
    #
    # Calcula el vector "H1810"
    if abs(vector['H1809GP'])>0.001:
       vector['H1810'] = (vector['H1207']*vector['H1809GP']/100)/((((1+(vector['H1809GP']/100))**vector['H1011'])-1)*(1+(vector['H1809GP']/100)))
        #+IF(ABS(U1410)>0,001;(U672*U1410/100)/((POWER((1+(U1410/100));U1037)-1)*(1+(U1410/100)));U672/U1037
    else:
        vector['H1810'] = vector['H1207']/vector['H1011']
    #
    # Calcula el vector "H1822"
    if abs(vector['H1809GP'])>0.001 and vector['H1006']>0:
       vector['H1822'] = (vector['H1207']*vector['H1809GP']/100)/ ((((1+(vector['H1809GP']/100))**vector['H1006'])-1)*(1+(vector['H1809GP']/100)))
    else:
       vector['H1822'] = 1
    #
    #
    ########################################################################################### NORMALIZED GROWTH RATE
    #
    #
    #
    #
    #
    # 
    #
    vector['H1611']=0
    vector['H2107']=0
    vector['H1639']=0
    vector['RI641']=0
    vector['H1812']=vector['RI15']+vector['H1611']+vector['RI47']+vector['H2107']+vector['H1639']+vector['RI641']
    vector['H1813']=vector['H1699']-vector['H1812']
    vector['H1961']=vector['H1813']
    vector['H1253']=0
    vector['H1253_ENP']=0
    vector['HT1810']=0
    vector['H1850']=0
    vector['H1811']=vector['H1810']+vector['H1253']+vector['H1253_ENP']+vector['HT1810']+vector['H1850']
    # De la hojita Normalized Growth Rate
    vector['H1919_O']=vector['RI65']
    vector['H1919']=vector['H1919_O']
    # Esta formula es mas compleja para financieras.
    vector['H1931']=vector['H1961']-vector['H1811']
    vector['H1836C']=vector['H1931']
    vector['H1503_USED']=-(vector['H1931']-vector['H1500'])
    vector['H1503']=(vector['H1500']-vector['H1836C'])
    # Normalized GRowth Rate CAp
    vector['H1913_CAP']=100 
    #
    vector['H1859A']=min(vector['H1913_CAP'],100*vector['H1931']/vector['H1503_USED'])
    #
    vector['H1913_FLR']=-20
    #
    vector['H1913']=min(vector['H1913_CAP'],max(vector['H1913_FLR'],100*vector['H1836C']/vector['H1503_USED']))
    #
    #
    # Arma el vector para la mediana historica del calculo de la "H1860"
    #     
    if str(vector['reporting_year']-1) in df_show and str(vector['reporting_year']-2) in df_show:
       a = extrae(str(vector['reporting_year']-1), 'H1913')  
       b = extrae(str(vector['reporting_year']-2), 'H1913')
       lista_para_mediana =[vector['H1913'],a,b]    
       vector['H1860']=median(lista_para_mediana)
    else:
       vector['H1860']= vector['H1913']
    #
    vector['H1869']= vector['H1913']
    vector['H2418']= max(-0.01,vector['H1869'])
    #
    #
    #
    ### HOJITA BOUNDED HISTORICAL GROWTH RATE
    #
    #
    if vector['H1111'] !=0:
       vector['H1506GP']= vector['H1504']/vector['H1111']
    else:
       vector['H1506GP']= "NA"
    #
    #
    #vector['H1102']= "DCF"
    vector['H1103']= "DCF"
    vector['H1104']= "DCF"
    #vector['H1101']= "DCF"
    # 
    #
    #
    vector['H1501']= vector['H1501GP']
    #
    #
    if vector['H1502'] !=0:
       vector['H1505']= vector['H1501']/vector['H1502']
    else:
       vector['H1505']= "NA"
    #
    vector['H1506B']= vector['H1505']
    #
    vector['H2417']= max(0, vector['H1809'])
    vector['H1105']= "DCF"
    vector['H1108']= "DCF"
    #
    ##################################################################################################################################################################
    #
    # TAB DEBT AUDIT 
    #
    vector['H1407']= vector['RI34']+ vector['RI9']
    #
    #
    vector['H1408']= 0
    vector['H2101']= vector['H1407']-vector['H1408']
    #
    #
    vector['H2438']=vector['RI25']*vector['RI24']
    #
    #
    vector['H5423']=vector['H2438']
    #
    vector['H2102']=vector['H1221']/2
    #
    vector['H2103']=vector['H2102']
    #
    vector['H2105']=vector['H2101']+vector['H2103']
    #
    vector['H2155']=vector['H2105']
    #
    vector['H1864']=100*(1+vector['H1860']/100)*(1+vector['H1616']/100)-1
    #
    vector['H2157']=vector['H2105']
    #
    vector['H2132']=0
    #
    vector['H2132N']=1-vector['H2132']
    #
    vector['H5420']= 0
    #
    vector['H2158']= 0
    #
    vector['H2446M']= 0
    #
    vector['H5425']= vector['H2157']
    #
    vector['H5423']=vector['H5425']+vector['H2438']+vector['H2446M']
    #
    vector['H3021H']=100*vector['H5425']/(vector['H5425']+vector['H2438'])/1
    #
    vector['H2159']= 0
    #
    #vector['H2421']=vector['H2159']*vector['H2420']
    #
    vector['H2490']=vector['H2438']+vector['H2421']+vector['H2446M']

    #
    vector['H5400']= 0
    #
    vector['H5410']= 0
    #
    vector['H5412']= 0
    #
    vector['H5413']=vector['H5412']-vector['H5410']
    #
    vector['H5415']= -1*vector['H5413']*100
    #
    vector['H5400S']=100-vector['H5400']
    #
    vector['H5426']=(1+vector['H5415']/100)*vector['H5425']
    #
    vector['H5427']=40
    #
    vector['H2504']= 0
    #
    vector['H2492']=vector['H2504']+vector['H2440']
    #
    if vector['H2492'] !=0:
       vector['H2494']=vector['H2490']/vector['H2492']
    else:
       vector['H2494']=0
    #
    vector['H5435']= 0
    #
    vector['H5428']=vector['H2492']*vector['H5427']/100+min(vector['H5435'],vector['H5425'])*(1-vector['H5427']/100)
    #
    vector['H5433']=min(vector['H5425'],vector['H5428'])
    #
    vector['H5429']=vector['H5433']*vector['H5415']/100
    #
    # HOJITA COMPANY SPECIFIC DISCOUNT RATE
    #
    # Economic Leverage Implied from Credit Rating. Si es financiera se usa este leverage para el diferencial sino se usa la H2408
    vector['H2405']=0.25
    # Industrial Economic Leverage for Discount Rate
    #vector['H2408']=0.66
    # 
    #Market Capitalization using 3 Month Avg. Price. (for Discount Rate)
    #
    #Provisoriamente uso el mkt cap... pero deberia usar un precio de los ultmis 3 meses.
    vector['H2403_DR']=vector['H2438']
    #Provisoriamente uso el mkt cap... pero deberia usar un precio de los ultmis 3 meses.
    vector['H2403']=vector['H2438']
    #
    vector['H2404']=vector['H2155']
    vector['H2408']=vector['H2404']/(vector['H2404']+vector['H2403_DR'])
    #
    #
    if vector['FRMCLASS']==1:
       vector['H2407']=vector['H2405']
    else:
       vector['H2407']=vector['H2408']   
    #
    #
    # HOJITA ADICIONALES
    vector['H1136']=vector['RI21'] 
    vector['H0009']=vector['RI19'] 
    vector['H2107']=vector['H1136']+vector['H0009']
    #
    #
    #
    # HOJITA eCAP AUDIT
    #
    vector['H4188']=0
    #
    if vector['H4188']==1: 
       vector['H4205']=10
    else: 
       vector['H4205']=5
    #
    # Calculo de la H4182A
    if vector['H4188']==1: 
       vector['H4182A']=0
    else: 
       vector['H4182A']=0
    #
    # Calculo de la H4182
    if vector['H2312']>=8: 
       vector['H4182']=1
    else: 
       vector['H4182']=0
    #
    # Calculo de la H4187A
    if vector['H4182A']==5: 
       vector['H4187A']=5
    else: 
       vector['H4187A']=0
    #
    vector['DIP278']=0    
    #
    # Calculo del Vector H4185
    #vector['H2312']=5.30
    lista = []
    #
    if str(vector['reporting_year']-6) in df_show and str(vector['reporting_year']-5) in df_show and str(vector['reporting_year']-4) in df_show and str(vector['reporting_year']-3) in df_show and str(vector['reporting_year']-2) in df_show and str(vector['reporting_year']-1) in df_show:
       list_for_standard_deviation = []
       list_for_standard_deviation.append(extrae(str(vector['reporting_year']-6), 'H2312'))
       list_for_standard_deviation.append(extrae(str(vector['reporting_year']-5), 'H2312'))
       list_for_standard_deviation.append(extrae(str(vector['reporting_year']-4), 'H2312'))
       list_for_standard_deviation.append(extrae(str(vector['reporting_year']-3), 'H2312'))
       list_for_standard_deviation.append(extrae(str(vector['reporting_year']-2), 'H2312'))
       list_for_standard_deviation.append(extrae(str(vector['reporting_year']-1), 'H2312'))
       list_for_standard_deviation.append(vector['H2312'])
       vector['H4185']=np.std(list_for_standard_deviation)
    else:
       vector['H4185']=0
    #
    # Calculo del Vector H4184
    if str(vector['reporting_year']-6) in df_show and str(vector['reporting_year']-5) in df_show and str(vector['reporting_year']-4) in df_show and str(vector['reporting_year']-3) in df_show and str(vector['reporting_year']-2) in df_show and str(vector['reporting_year']-1) in df_show:
       import statistics
       list_for_average = []
       list_for_average.append(extrae(str(vector['reporting_year']-6), 'H2312'))
       list_for_average.append(extrae(str(vector['reporting_year']-5), 'H2312'))
       list_for_average.append(extrae(str(vector['reporting_year']-4), 'H2312'))
       list_for_average.append(extrae(str(vector['reporting_year']-3), 'H2312'))
       list_for_average.append(extrae(str(vector['reporting_year']-2), 'H2312'))
       list_for_average.append(extrae(str(vector['reporting_year']-1), 'H2312'))
       list_for_average.append(vector['H2312'])
       vector['H4184']=statistics.mean(list_for_average)
    else:
       vector['H4184']=1
    #
    vector['H4186']=vector['H4185']/vector['H4184']    
    #
    #
    # Calculo de la H4187C
    if vector['H4186']<=vector['DIP278']:
       vector['H4187C']=0
    else: 
       vector['H4187C']=1
    #
    #
    #Calculo de la Base Discount
    #
    vector['H2489']=6.76
    vector['FIN_MKT_COE']=4.65
    vector['DR_FLAG']=0
    vector['H2412G']=5.53
    vector['FIN_MKT_COEG']=6.37
    vector['H2412']=6.76
    #
    vector['H4186']=4.02
    vector['H4182A']=0
    vector['H4184A']=0
    vector['H4185A']=5.3
    if vector['H4182A'] <4:
       vector['H4186A']=vector['H4186']
    else:
       vector['H4186A']=vector['H4185A']/vector['H4184A']
    #
    vector['H2312ADJ']=0
    # 
    vector['H2409']=0
    vector['H2410']=0
    vector['H2411']=6.20
    vector['H2413']=12.96
    #
    vector['DR_GROUP']=2
    #
    vector['DIP205']=0.4 
    #
    vector['DIP78']=0.25
    #
    if vector['DR_GROUP']==4:
       vector['H2497']=vector['DIP205']
    else:
       vector['H2497']=vector['DIP78']
    #
    if get_msci(str(vector['reporting_year']),"12", "31") == "NA":
       vector['H2498_WI']= 0
    else:
       vector['H2498_WI']= get_msci(str(vector['reporting_year']),"12", "31")
    #vector['H2498_WI']
    #
    vector['H2498_WI_BASE']=1420.90
    #
    vector['FX09']=3.33
    #
    if vector['H2498_WI']>0:
       vector['H2498_N']=(5000*(1+(vector['H2498_WI']/vector['H2498_WI_BASE'])-1))*vector['FX09']
    else:
       vector['H2498_N']=0
    #
    vector['H2498']=vector['H2498_N']
    #

   

######## FUNCION QUE CHECKEA QUE EL VECTOR EXISTA ########################
def exist(year):
    return eval("Columna"+year)    

######## FUNCION QUE PERMITE OBTENER DATOS DE OTROS VECTORES ##############
def extrae(year, concepto):
     # Recibe como inputs el anio del vector en formato string y el concepto en formato string 
     return eval("Vector"+year)[concepto]

#extrae("2018", 'H1202')

###########################################################################


