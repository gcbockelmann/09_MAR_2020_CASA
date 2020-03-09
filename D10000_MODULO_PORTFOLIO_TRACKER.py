

#import pandas as pd
#list_of_columns = ['Cantidad']

# Inicializa 

#indice_dataframe = []

# Indice puede ser integer o string

#componentes_portfolio = ["AGRO","ALUA"]

#df=pd.DataFrame(index = componentes_portfolio, columns=list_of_columns)



#################


#cantidades = {"AGRO":2, "ALUA":2}
#acquisition_date = {"AGRO":"2019-02-02", "ALUA":"2019-02-02"}
#costo_acumulado = {"AGRO":30, "ALUA":60}

#df['Cantidad']=pd.Series(cantidades)
#df['Fecha_de_adquisicion']=pd.Series(adquisition_date)
#df['Costo_Unitario']=0


#df['Base_de_Costo']=pd.Series(costo_acumulado)
#df['Costo_Unitario']=df['Base_de_Costo']/df['Cantidad']

#df['Precio_de_Cierre']=0


#def arma_portfolio(a,b,c,d,e,f,g)
#    global df
    


########### FUNCION QUE DEVUELVE LA ULTIMA FECHA OPERADA DE UN TICKER

def ultima_fecha_operada(ticker):
    global df
    file_name = "SERIE_CORRIENTE_"+ ticker
    open_file_spch(original_source + "SPCH", file_name, ".xlsx")
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    return b



#ultima_fecha_operada("AGRO")



########### FUNCION QUE DEVUELVE EL ULTIMO PRECIO DE LA ULTIMA OPERACION DE UN TICKER

def ultimo_precio_de_cierre(ticker):
    global df, b
    file_name = "SERIE_CORRIENTE_"+ ticker
    open_file_spch(original_source + "SPCH", file_name, ".xlsx")
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #print(b)
    #
    #
    end_day_number= int(b[8:10])
    end_month_number= int(b[5:7])
    end_year_number = int(b[0:4])
    #
    #print(end_day_number)
    #print(end_month_number)
    #print(end_year_number)
    #
    #
    # Arma la fecha de finalizacion
    #end = datetime.datetime(end_year_number,end_month_number, end_day_number)
    #
    # Arma una serie y busca por el indice de la serie que es una string
    return df["Cierre_del_dia"][b]

#ultimo_precio_de_cierre("AGRO")


###############################33
# NO SE BIEN QUE HACE - FUNCION NO TERMINADA

#def arma_lista_de_fechas_de_precio():
#    global df, lista_de_fechas
#    lista_de_fechas_de_precio = []
#    for ticker in componentes_portfolio:
#        lista_de_fechas.append(ultima_fecha_operada(ticker))
#    return lista_de_fechas_de_precio
        
#new_dict = dict(zip(indice_dataframe, lista_de_fechas))

#df['Fecha_de_precio']=pd.Series(new_dict)



########################################################################
#### FUNCION QUE CREA UN PORTFOLIO PERO SIN TRANSACCIONES SUBYACENTES
########################################################################

#tickers_portfolio1 = ["AGRO","ALUA","ALEX"]
#cantidades_portfolio1 = {"AGRO":0, "ALUA":1, "ALEX":0}

#a = list(cantidades_portfolio1.values())


#for i in range(0,(len(a))):
#      if a[i] == 0: 
#         print(i)
#         del tickers_portfolio1[i-1]        
#      else:
#         pass
       
       

########################################################################################
# FUNCION QUE CHECKEA QUE LAS CANTIDADES NO PUEDEN SER CERO
################################################################################

def is_portfolio(quantities):
    if 0 in list(quantities.values()):
       return False
    else:
       return True

#is_portfolio(cantidades_portfolio1)



#####################################################################################################################
# FUNCION QUE CHECKEA SI LAS PONDERACIONES SON COHERENTES CON LAS DE UN PORTFOLIO. La ponderacion no puede ser zero.#
#####################################################################################################################

def check_if_weights_is_zero(quantities):
    if 0 in list(quantities.values()):
       return ("Las cantidades incluyen un componente con ponderacion igual a cero")
    else:
       return 

#check_if_weights_is_zero(cantidades_portfolio1)



##################################################################### 
#### TICKERS EN UNA LISTA Y CANTIDADES EN UN DICCIONARIO.
#### DEBEN SER DE IGUAL LONGITUD
############################################################################

       
#tickers_portfolio1 = ["AGRO","ALUA","ALEX"]
#cantidades_portfolio1 = {"AGRO":1, "ALUA":1, "ALEX":1}

##################################################################################################
#### FUNCION OBSOLETA - QUE CREA UN PORTAFOLIO A PARTIR DE LOS TICKERS Y LAS CANTIDADES  - BORRAR
##################################################################################################


def create_portfolio(tickers_list, quantities):
    global df
    #
    if len(tickers_list)==len(quantities):
       #     
       if is_portfolio(quantities):
          componentes_portfolio = tickers_list
          #          
          lista_de_valor_de_cantidades = list(quantities.values())
          #
          list_of_columns = ['Cantidad']    
          #
          df=pd.DataFrame(index = componentes_portfolio, columns=list_of_columns)
          #
          # Transforma el diccionario quantities a una serie y la aplica a la columna Cantidad
          df['Cantidad']=pd.Series(quantities)
          #
          return df
       else: 
          return ("Problema: Las cantidades incluyen un ticker con ponderacion igual a cero") 
    else:
       return ("Problema: Las listas de ticker y el diccionario de cantidades no tienen la misma longitud")

#create_portfolio(tickers_portfolio1, cantidades_portfolio1)



####################################################################################
### FUNCION QUE DEVUELVE EL PRECIO EN PESOS DE UN TICKER A UNA DETERMINADA FECHA
###################################################################################

def precio_del_ticker_a_una_fecha(ticker, fecha):  
    global df, b
    file_name = "SERIE_CORRIENTE_"+ ticker
    open_file_spch(original_source + "ONLINE/SPCH", file_name, ".xlsx")
    #
    #
    b = fecha # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #print(b)
    #
    #
    if b in df.index:
       # Arma una serie y busca por el indice de la serie que es una string
       #
       #
       return df["Cierre_del_dia"][b]
    else:
       return "NA"  

#precio_del_ticker_a_una_fecha("AGRO", "2020-02-10")


#########################################################################################################
### FUNCION QUE CREA LA LISTA DE PRECIOS DE LOS TICKERS INCLUIDOS EN UN PORTFOLIO A UNA FECHA DETERMINADA
#########################################################################################################

def crea_lista_de_precios_del_portfolio(tickers_portfolio, fecha):
    global precios_portfolio
    precios_portfolio=[]    
    for ticker in tickers_portfolio:        
        precios_portfolio.append(precio_del_ticker_a_una_fecha(ticker, fecha))
    return precios_portfolio

#crea_lista_de_precios_del_portfolio(tickers_portfolio1, "2019-12-02")



#tickers_portfolio1 = ["AGRO","ALUA"]
#cantidades_portfolio1 = {"AGRO":1, "ALUA":1}

#tickers_portfolio1 = ["GOLD","PAMP", "SAMI", "TXAR"]
#cantidades_portfolio1 = {"GOLD":3500, "PAMP":1500, "SAMI":6800, "TXAR":215000}






#############################################################################################################################
# Haciendo que los portafolios no importa en que orden entregue las cantidades y los tickers , siempre se muestren iguales

#list_of_securities_supported_by_this_software = []

# Esta es la lista de securities soportados por este software y en la que se van a mostrar en el portafolio. En vez de ticker, la identificacion podria ser por ISIN u otra identificacion
#list_of_securities_supported_by_this_software = ["BMA", 
#"PAMP", 
#"SAMI", 
#"TXAR",
#"GOLD", 
#]

# Toma la lista y la modifica ordenandola por orden alfabetico
#list_of_securities_supported_by_this_software.sort()
# En este caso no hace falta porque queremos que la estructura se muestre tickers locales, y luego CEDEARs.

#Creo un dictionario vacio para cada 
#d = {}
#cantidades_portfolio1 = {"GOLD":3500, "PAMP":1500, "SAMI":6800, "TXAR":215000}

# Devuelve la lista de keys de un diccionario, para que no sea necesario tener que entregar una lista de los securities y un diccionario de cantidades.
# Con el diccionario de cantidades y sus keys seria suficiente.
# Veamos como

# Creamos un diccionario de cantidades
#cantidades_portfolio1 = {"GOLD":3500, "PAMP":1500, "SAMI":6800, "TXAR":215000}
# Crea una lista de keys 
#mykeys = list(cantidades_portfolio1.keys())

# Crea una lista de cantidades
#list(cantidades_portfolio1.values())

# Crea una lista con las cantidades correspondientes a la lista mykeys
#[cantidades_portfolio1[x] for x in mykeys]


#list_of_securities_supported_by_this_software = ["BMA", 
#"PAMP", 
#"SAMI", 
#"TXAR",
#"GOLD", 
#]

# Genera un diccionario llamado d con las keys de todos los securities soportados por el software
#d = dict.fromkeys(list_of_securities_supported_by_this_software, 0)

#Verifica que todos las llaves de un diccionario cantidades_portfolio1 esten en el diccionario d
#set(cantidades_portfolio1.keys()).issubset(d)

#Actualiza el diccionario d con la informacion del diccionario cantidades_portfolio1
#d.update(cantidades_portfolio1)


# Remueve todos los valores llave x  que tengan cantidades(y) iguales a cero
#d2 = {x:y for x,y in d.items() if y!=0}

##########################################################################################
#### FUNCION QUE CREA UN PORTAFOLIO A PARTIR DE UN DICCIONARIO DE TICKERS Y LAS CANTIDADES
#########################################################################################

list_of_securities_supported_by_this_software = ["BMA", 
"CTIO",
"GGAL", 
"PAMP", 
"SAMI", 
"TXAR",
"GOLD", 
]




def create_portfolio(dictionary_of_quantities):
    # Esta funcion toma un diccionario de tickers y cantidades
    # y lo compara con la lista de securities soportada por el software
    # Si todos los tickers estan dentro de la lista procede a verificar que las cantidades sean distintas de 0
    #
    global df, list_of_securities_supported_by_this_software
    #
    # Toma el diccionario y lo mapea al diccionario permitido por el software
    #
    # ATENCION: La lista de securities soportada por el software debe updatearse manualmente.
    #list_of_securities_supported_by_this_software = ["BMA", 
#"CTIO",
#"GGAL", 
#"PAMP", 
#"SAMI", 
#"TXAR",
#"GOLD", 
#]
    #
    # Genera un diccionario llamado d con las keys de todos los securities soportados por el software
    d = dict.fromkeys(list_of_securities_supported_by_this_software, 0)
    #
    #Verifica que todos las llaves de un diccionario cantidades_portfolio1 esten en el diccionario d
    if set(dictionary_of_quantities.keys()).issubset(d):
       #Actualiza el diccionario d con la informacion del diccionario cantidades_portfolio1
       d.update(dictionary_of_quantities)
       # Remueve todos los valores llave x  que tengan cantidades(y) iguales a cero
       d2 = {x:y for x,y in d.items() if y!=0}
    #
    else: 
       return ("Problema: Tickers no incluidos en el diccionario list_of_securities_supported_by_this_software")
    #
    #
    #
    ##### A PARTIR DE ACA YA TENEMOS UN DICCIONARIO PERMITIDO POR EL SOFTWARE Y TIENE EL ORDEN CORRECTO PARA LOS SECURITIES Y LAS CANTIDADES
    #
    # Crea una lista de keys 
    mykeys = list(d2.keys())
    #
    #
    #
    # Crea una lista con las cantidades correspondientes a la lista mykeys
    myquantities = [d2[x] for x in mykeys]
    #
    # Asigna a ticker_list la lista de llaves del dictionario
    tickers_list = mykeys
    #
    # Asigna a quantities la lista de las cantidades correspondientes a la lista de llaves del dictionario
    quantities = myquantities
    #
    if len(tickers_list)==len(d2):
       #     
       if is_portfolio(d2):
          componentes_portfolio = tickers_list
          #          
          lista_de_valor_de_cantidades = list(d2.values())
          #
          list_of_columns = ['Cantidad']    
          #
          df=pd.DataFrame(index = componentes_portfolio, columns=list_of_columns)
          #
          # Transforma el diccionario quantities a una serie y la aplica a la columna Cantidad
          df['Cantidad']=pd.Series(d2)
          #
          return df
       else: 
          return ("Problema: Las cantidades incluyen un ticker con ponderacion igual a cero") 
    else:
       return ("Problema: Las listas de ticker y el diccionario de cantidades no tienen la misma longitud")

#cantidades_portfolio1 = {"PAMP":3400, "GOLD":1500, "SAMI":6800, "TXAR":215000}
#cantidades_portfolio1 = {"GOLD":1500, "PAMP":3400, "SAMI":6800, "TXAR":215000}
#cantidades_portfolio1 = {"SAMI":6800, "PAMP":3400, "GOLD":1500, "TXAR":215000}
#cantidades_portfolio1 = {"TXAR":215000, "SAMI":6800, "PAMP":3400, "GOLD":1500 }


#create_portfolio(cantidades_portfolio1)

#########################################################################################################
# FUNCION QUE ASIGNA LOS PRECIOS DE CIERRE A LA COLUMNA DEL PORTFOLIO                                   #
#########################################################################################################

def valoracion_portfolio(portfolio, fecha):
    global df
    mykeys = list(portfolio.index)
    #
    portfolio['Precio_de_Cierre']=crea_lista_de_precios_del_portfolio(mykeys, fecha)
    portfolio['Valor']=portfolio['Cantidad']*portfolio['Precio_de_Cierre']
    df = portfolio 
    return df

#valoracion_portfolio(df, "2020-01-15")

#########################################################################################################
# AGREGA EL COSTO FIFO A LA TENENCIA DEL PORTAFOLIO
#########################################################################################################

def arma_diccionario_de_costos(lista_de_tickers, lista_de_costos):
    #
    new_dict = dict(zip(lista_de_tickers, lista_de_costos))
    return new_dict

#arma_diccionario_de_costos(arma_lista_de_tickers_actuales_en_portafolio(df),costos)


def agrega_costo_fifo_a_portafolio(dataframe, diccionario_de_costos):
    #
    dataframe['Costo'] = pd.Series(diccionario_de_costos)
    #
    return dataframe


#agrega_costo_fifo_a_portafolio(df, costos)

#########################################################################################################
# AGREGA EL COSTO FIFO EN USD A LA TENENCIA DEL PORTAFOLIO
#########################################################################################################

def arma_diccionario_de_costos_en_usd(lista_de_tickers, lista_de_costos):
    #
    new_dict = dict(zip(lista_de_tickers, lista_de_costos))
    return new_dict

#arma_diccionario_de_costos_en_usd(arma_lista_de_tickers_actuales_en_portafolio(df),costos_en_usd)

def agrega_costo_fifo_en_usd_a_portafolio(dataframe, diccionario_de_costos):
    #
    dataframe['Costo_en_USD'] = pd.Series(diccionario_de_costos)
    #
    return dataframe


#agrega_costo_fifo_en_usd_a_portafolio(df, costos_en_usd)

def agrega_costo_fifo_en_usdars_ppp_a_portafolio(dataframe, diccionario_de_costos):
    #
    dataframe['Costo_en_USDARS_PPP'] = pd.Series(diccionario_de_costos)
    #
    return dataframe


#agrega_costo_fifo_en_usdars_ppp_a_portafolio(df, costos_en_usdars_ppp)


#########################################################################################################
# CALCULA LA VALORIZACION TOTAL DEL PORTFOLIO
#########################################################################################################

#df['Valor'].sum()






#######################################################################################################
### EJEMPLO DE PORTAFOLIO Y VALORIZACION


# Crea el diccionario de las cantidades
#cantidades_portfolio1 = {"GOLD":3500, "PAMP":1500, "SAMI":6800, "TXAR":215000}

# Crea un portfolio con la funcion de creacion de portafolios
#portfoliox = create_portfolio(cantidades_portfolio1)

# Valoriza el portfoliox a la fecha especificada
#portfoliox_value = valoracion_portfolio(portfoliox, "2020-01-28")
# Imprime en pantalla el df
#portfoliox_value

# Calcula el valor total del portafolio
#portfoliox['Valor'].sum()



##################################################################################################################
########## ARMA DATAFRAME DE PORTFOLIO Y LO VALORIZA EN ARS  ####################################################
#################################################################################################################


def valorizacion_actual_del_portfolio_en_pesos(fecha):
    global df
    global quantities
    create_portfolio(quantities)
    agrega_costo_fifo_a_portafolio(df, lista_de_costos_en_ars)
    valoracion_portfolio(df, fecha)
    df["Costo"]=-df["Costo"]
    df["Res.Acumulado"]=df["Valor"]-df["Costo"]
    df["ARS_%"]=((df["Valor"]/df["Costo"])-1)*100
    return df


#valorizacion_actual_del_portfolio_en_pesos("2020-02-07")

##################################################################################################################
########## ARMA DATAFRAME DE PORTFOLIO Y LO VALORIZA EN USDARS_LIBRE  ############################################
##################################################################################################################

def valorizacion_actual_del_portfolio_en_usd(df):
    global df2
    open_file_currency("USDARS_LIBRE")
    a=list(cur["tc_nominal"].tail(1))
    a[0]
    df["USDARS_LIBRE"]=a[0]
    #
    # Arma un segundo dataframe solo con las cantidades
    df2 = df[["Cantidad"]]
    #
    agrega_costo_fifo_en_usd_a_portafolio(df2, costos_en_usd)
    #
    df2["Costo_en_USD"]=-df2["Costo_en_USD"]
    #
    df2["Precio_en_USD"] = df["Precio_de_Cierre"]/a[0]
    #
    df2["Valor_en_USD"]=df2["Precio_en_USD"]*df2["Cantidad"] 
    #
    df2["Res.Acumulado_en_USD"]=df2["Valor_en_USD"]-df2["Costo_en_USD"]
    #
    df2["USD_%"]=((df2["Valor_en_USD"]/df2["Costo_en_USD"])-1)*100
    #
    return df2
    
#valorizacion_actual_del_portfolio_en_usd(df)

##################################################################################################################
########## ARMA DATAFRAME DE PORTFOLIO Y LO VALORIZA EN USDARS_PPP  ##############################################
#################################################################################################################

def valorizacion_actual_del_portfolio_en_usdars_ppp(df):
    global df3
    open_file_currency("USDARS_PPP")
    a=list(cur["tc_real"].tail(1))
    a[0]
    df["USDARS_PPP"]=a[0]
    #
    # Arma un segundo dataframe solo con las cantidades
    df2 = df[["Cantidad"]]
    #
    agrega_costo_fifo_en_usdars_ppp_a_portafolio(df2, costos_en_usdars_ppp)
    #
    df2["Costo_en_USDARS_PPP"]=-df2["Costo_en_USDARS_PPP"]
    #
    df2["Precio_en_USDARS_PPP"] = df["Precio_de_Cierre"]/a[0]
    #
    df2["Valor_en_USDARS_PPP"]=df2["Precio_en_USDARS_PPP"]*df2["Cantidad"] 
    #
    df2["Res.Acumulado_en_USDARS_PPP"]=df2["Valor_en_USDARS_PPP"]-df2["Costo_en_USDARS_PPP"]
    #
    df2["USDARS_PPP%"]=((df2["Valor_en_USDARS_PPP"]/df2["Costo_en_USDARS_PPP"])-1)*100
    #
    df3=df2
    #
    return df3
    
#valorizacion_actual_del_portfolio_en_usdars_ppp(df)

###################################################################################
###############GRABA LOS 3 DATAFRAMES A UN EXCEL ################################
##################################################################################

def guarda_posicion():
    global df,df2,df3
    writer = pd.ExcelWriter(original_source + 'PORTFOLIO/POSICION_ACTUAL.xlsx', engine='xlsxwriter')
    # Write each dataframe to a different worksheet.
    df.to_excel(writer, sheet_name='ARS')
    df2.to_excel(writer, sheet_name='USDARS_LIBRE')
    df3.to_excel(writer, sheet_name='USDARS_PPP')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

#guarda_posicion()

