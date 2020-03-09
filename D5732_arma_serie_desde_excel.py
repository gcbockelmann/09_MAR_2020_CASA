
def open_excel(loc, ticker, ext, tab=0):
    ### Esta funcion abre un archivo de excel con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    print (path)
    df = pd.read_excel(path, sheetname=tab)
    return (df)

# Abre el excel de estados financieros del ticker
open_excel("C:\GCB_CAPITAL", "FS_TXAR", ".xlsx")


def crea_df_de_puntos(df, concepto):
    """ Toma una dataframe de estados financieros y devuelve un vector de evolucion de una variable financiera"""
    #
    # Crea una lista vacia de fechas
    lista_de_fechas = []
    # Crea una lista vacia de valores
    lista_de_valores = []
    #
    # Donde 0 y 1 son las posiciones del index en las que estan las fechas y los valores respectivamente, hace un for loop para armar listas con las fechas y los valores.
    for i in list(df.columns):
        # Agrega a la lista vacia las fechas que tiene el dataframe en la fila llamada "Close_date"
        lista_de_fechas.append(df[i].loc['Close_date'])
        # Agrega a la lista vacia los importes que tiene el dataframe en la fila llamada "LTM_NI"
        lista_de_valores.append(df[i].loc[concepto])
    #
    # Imprime en pantalla la lista de fechas
    #print (lista_de_fechas)
    # Imprime en pantalla la lista de valores
    #print (lista_de_valores)
    #
    # Crea un dataframe llamado evolucion
    evolucion = pd.DataFrame() #Crea una matriz de pandas
    # Agrega la columna Fecha al dataframe con valor por default igual a 0 (cero)
    #evolucion["Fecha"] = 0
    # Agrega la columna Fecha al dataframe con valor por default igual a ""
    evolucion["Fecha"] = ""
    # Agrega la columna concepto al dataframe con valor por default igual a ""
    evolucion[concepto] = ""
    #
    # 
    # Chequea que el largo de lista de fechas sea el mismo que lista de valores
    len(lista_de_fechas) == len(lista_de_valores)
    # Agrega al dataframe evolucion, una por una la fecha y un valor
    for i in range(0, (len(lista_de_fechas))):
        evolucion = evolucion.append({'Fecha': lista_de_fechas[i], concepto: lista_de_valores[i] }, ignore_index=True)     
    #
    # Establece la fecha como el indice de dataframe
    evolucion = evolucion.set_index('Fecha', inplace=False) # Sete el indice como la columna Fecha
    # Establece el formato del indice en formato datetime
    evolucion.index = pd.to_datetime(evolucion.index, format="%Y-%m-%d") # Convertimos el indice en date time con el formato ANO-MES-DIA
    # Convierte la columna "concepto" en punto flotante
    evolucion[concepto] = evolucion[concepto].astype(float) # Convierte la columna de concepto a punto flotante 
    return evolucion


#crea_df_de_puntos(df, 'LTM_NI')
#crea_df_de_puntos(df, 'Common_Equity')
#crea_df_de_puntos(df, 'Net_Debt')
#crea_df_de_puntos(df, 'EBITDA')
#crea_df_de_puntos(df, 'LTM_EBITDA')

######################################################################################################################################
# CONOCIMIENTOS POSIBLEMENTE UTILES
# Agrega una row al dataframe , pero para esto tenes que saber la cantidad de columnas que tiene el df
#df = df.append({'2001Q1': 23, '2001Q2': 'Riti', '2001Q3': 'Login', '2001Q4': 'Login'}, ignore_index=True)
#####################################################################################################################################

##################################################################################################################
################### HASTA ACA ARME UN DATAFRAME LLAMADO EVOLUCION CON LOS PUNTOS DE DATOS EN LA COLUMNA CONCEPTO #
##################################################################################################################

evolucion = crea_df_de_puntos(df, 'LTM_NI')
evolucion = crea_df_de_puntos(df, 'Common_Equity')
evolucion = crea_df_de_puntos(df, 'Net_Debt')
evolucion = crea_df_de_puntos(df, 'EBITDA')
evolucion = crea_df_de_puntos(df, 'LTM_EBITDA')


# Abre el mkt cap_usd_ppp file del ticker
open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "TXAR", ".xlsx")


def agrega_serie_al_data_frame(df, evolucion, concepto):
    global value
    evolucion.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(evolucion.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #
    # Mergea la matriz evolucion con el df de mkt cap_usd_ppp
    merge = pd.merge(df, evolucion, how='outer', left_index=True, right_index=True) # mergea las dos dataframes e incorpora la columna "capital"
    # 
    merge.loc[:,concepto] = merge.loc[:,concepto].fillna(0) #completa la columna capital los NA y los reemplaza por 0
    #
    # Renombra la matriz merge a df
    df = merge
    # Agrega una columna C que tiene todos valores NaN
    df['C'] = np.nan #agrega nan en toda la columna C 
    # Ordena el indice de manera descendente 
    df = df.sort_index(axis=0, level=None, ascending=False) # Da vuelta el indice
    #
    # Muestra el head del df
    df.head(1).index[-1] # muestra el head
    intermedio2 = str(df.head(2).index) # Convierte a string
    anteultima_fecha = intermedio2[30:40] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    df=df.fillna(0)  #completo con 0 los nan de la columna C mayuscula.
    #
    # ITERA SOBRE EL DATAFRAME
    value = 0 # inicializa la variable value en cero para luego poder iterar
    # La variable value es utilizada por la formula calculate
    df.loc[anteultima_fecha:, 'C'] = df.loc[anteultima_fecha:].apply(lambda row: float(calculate(*row[[concepto]])), axis=1)  # Itera sobre la columna capital utilizando la formula calculate
    df=df.drop([concepto], axis=1)  #elimina la columna concepto que es donde habiamos colocado los puntos
    df=df.sort_index(axis=0, level=None, ascending=True) #Reordena el dataframe
    #
    #
    # Crea una lista de filas del dataframe a borrar
    lista_de_filas_a_borrar = []
    # Eliminar las filas del df que 
    #
    # Identifica las filas del df a borrar
    for i in evolucion.index:
        a = df['Cierre_del_dia'].loc[i]
        if a == 0:
           lista_de_filas_a_borrar.append(i)
    #
    # Elimina las filas en la matriz df
    for i in lista_de_filas_a_borrar:
        df.drop(pd.Timestamp(i), inplace=True)
    df=df.rename(columns={'C': concepto}) #
    return df


b = agrega_serie_al_data_frame(df, evolucion, 'LTM_NI')
b = agrega_serie_al_data_frame(df, evolucion, 'Common_Equity')
b = agrega_serie_al_data_frame(df, evolucion, 'Net_Debt')

d = agrega_serie_al_data_frame(c, evolucion, 'EBITDA')
d = agrega_serie_al_data_frame(df, evolucion, 'LTM_EBITDA')

def calculate(mul):
    # Esta funcion calcula el capital con calculo iterativo
    global value
    if mul == 0: 
       value = value
    else:
       value = mul    
    return value


PARA ANUALIZAR EL QUARTER
#df=df.rename(columns={'C': 'Quarter_Net_Income_M_ARS'}) #
#df['Annualized_Net_Income_M_ARS']=df['Quarter_Net_Income_M_ARS']*4
#df['Annual_EPS_(Quaterly_annualized)']=df['Annualized_Net_Income_M_ARS']/df['Capital'] 
#df['PE_ratio']=df['Cierre_del_dia']/df['Annual_EPS_(Quaterly_annualized)'] 

PARA CALCULAR EL PRICE TO EARNINGS
df['Annual_EPS_(LTM_NI)']=df['LTM_NI']/df['Capital'] 
df['PE_ratio']=df['Cierre_del_dia']/df['Annual_EPS_(LTM_NI)'] 
chart_series_de_dataframe(df , "PE_ratio")

PARA CALCULAR EL PRICE TO EARNINGS
df['BVPS']=df['Common_Equity']/df['Capital'] 
chart_series_de_dataframe(df , "BVPS")

PARA CALCULAR EV
df['EV']=(df['Mkt_Cap_Close_ARS']+df['Net_Debt'])
df['EV/EBITDA']=(df['Mkt_Cap_Close_ARS']+df['Net_Debt'])/df['EBITDA'] 
chart_series_de_dataframe(df , "EV/EBITDA")



# Graba el archivo
save_file("C:\GCB_CAPITAL\OUTPUT", "TXAR3", ".xlsx")







def add_serie_to_dataframe(ticker, serie, df):
    # Abre los estados financieros del ticker
    name = "FS_" + str(ticker)
    df2 = open_excel("C:\GCB_CAPITAL", name, ".xlsx") 
    evolucion = crea_df_de_puntos(df2, serie)    
    # Abre la serie historica a la cual agregar la datos financieros
    return agrega_serie_al_data_frame(df, evolucion, serie)


PARA CALCULAR EV
open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "TXAR", ".xlsx")
df = add_serie_to_dataframe("TXAR", "Net_Debt", df)
df['EV']=(df['Mkt_Cap_Close_ARS']+df['Net_Debt'])
df = add_serie_to_dataframe("TXAR", "LTM_EBITDA", df)
df['EV/EBITDA']=(df['EV'])/df['LTM_EBITDA'] 
chart_series_de_dataframe(df , "EV/EBITDA")

PARA CALCULAR PE
df = add_serie_to_dataframe("TXAR", "LTM_NI", df)
df['Annual_EPS_(LTM_NI)']=df['LTM_NI']/df['Capital'] 
df['PE_ratio']=df['Cierre_del_dia']/df['Annual_EPS_(LTM_NI)'] 
chart_series_de_dataframe(df , "PE_ratio")

PARA CALCULAR PS
df = add_serie_to_dataframe("TXAR", "LTM_Revenue", df)
df['Annual_SPS_(LTM_Revenue)']=df['LTM_Revenue']/df['Capital'] 
df['PS_ratio']=df['Cierre_del_dia']/df['Annual_SPS_(LTM_Revenue)'] 
chart_series_de_dataframe(df , "PS_ratio")

PARA CALCULAR BVPS
df = add_serie_to_dataframe("TXAR", "Common_Equity", df)
df['BVPS']=df['Common_Equity']/df['Capital'] 
df['P/BVPS_ratio']=df['Cierre_del_dia']/df['BVPS'] 
chart_series_de_dataframe(df , "P/BVPS_ratio")


PARA CALCULAR P/FCFPS
df = add_serie_to_dataframe("TXAR", "LTM_FCF", df) 
df['EV/LTM_FCF_ratio']=df['EV']/df['LTM_FCF'] 
chart_series_de_dataframe(df , "EV/LTM_FCF_ratio")

PARA CALCULAR 1/ EV/LTM_FCF
df['LTM_FCF/EV_ratio']=df['LTM_FCF']/df['EV'] 
chart_series_de_dataframe(df , "LTM_FCF/EV_ratio")


###### ARMA EL DATAFRAME ANUAL
year_quarter = 0
if "2018Q1" in df.columns:
   year_quarter += 1

if "2018Q2" in df.columns:
   year_quarter += 2

if "2018Q3" in df.columns: 
   year_quarter += 3

if "2018Q4" in df.columns:
   year_quarter += 4

df2 = pd.DataFrame()

df2['2018'] = df["2018Q1"] + df["2018Q2"] + df["2018Q3"] + df["2018Q4"]


#################
heading = pd.DataFrame
income_statement = pd.DataFrame
balance_sheet_nominal_anual = pd.DataFrame
cash_flow = pd.DataFrame
 
########################## NOMINAL DEL PERIODO TRIMESTRAL
heading_nominal_trimestral = pd.DataFrame
income_statement_nominal_trimestral = pd.DataFrame
balance_sheet_nominal_trimestral = pd.DataFrame
cash_flow_nominal_trimestral = pd.DataFrame



########################## NOMINAL DEL PERIODO ANUAL
heading_nominal_anual = pd.DataFrame
income_statement_nominal_anual = pd.DataFrame
balance_sheet_nominal_anual = pd.DataFrame
cash_flow_nominal_anual = pd.DataFrame

year = 2018

list_of_columns = []

# Verifica que tenga los 4 quarters historicos el DataFrame del ano correspondiente
if (str(year)+"Q1") in df.columns and (str(year)+"Q2") in df.columns and (str(year)+"Q3") in df.columns and (str(year)+"Q4") in df.columns:     
   list_of_columns.append(str(year))


open_excel("C:\GCB_CAPITAL", "FS_TXAR", ".xlsx")


# Controla si estan estos anios en el dataframe y agrega los anios completos en la lista de columnas para crear un dataframe
list_of_columns = []
years = [2018, 2019]
for i in years:
    if (str(i)+"Q1") in df.columns and (str(i)+"Q2") in df.columns and (str(i)+"Q3") in df.columns and (str(i)+"Q4") in df.columns:     
       list_of_columns.append(str(i))

# Crea un DataFrame
df2 = pd.DataFrame()
# Agrega las columnas al DataFrame
df2 = pd.DataFrame(columns=list_of_columns)
# Agrega el indice
df2 = pd.DataFrame(index=indice)

conceptos_estandarizados_estado_de_resultados = []
conceptos_estandarizados_balance_sheet = []
conceptos_estandarizados_cash_flow = []

conceptos_estandarizados_estado_de_resultados = []



##################################################################################################
## CODIGO ABRE UN ARCHIVO EXCEL Y ARMA DATAFRAME Y LUEGO ARMA EL DF ANUAL ESTANDARIZADO
#####################################################################################################3

open_excel("C:\GCB_CAPITAL", "FS_TXAR", ".xlsx")
df_bs = pd.DataFrame()

# Controla si estan estos anios en el dataframe y agrega los anios completos en la lista de columnas para crear un dataframe
list_of_columns = []
years = [2018, 2019]
for i in years:
    if (str(i)+"Q1") in df.columns and (str(i)+"Q2") in df.columns and (str(i)+"Q3") in df.columns and (str(i)+"Q4") in df.columns:     
       list_of_columns.append(str(i))


# Crea el DataFrame df_bs con los conceptos estandarizados del BS como indice y los anuales como columnas
df_bs = pd.DataFrame(index = conceptos_estandarizados_balance_sheet, columns=list_of_columns)

# HASTA ACA TENGO UN DATAFRAME PARA CARGAR LOS VALORES

##### DATAFRAME PARA MOSTRAR VISUALMENTE MAS FACIL
# Crea una serie a partir del diccionario
nombres = pd.Series(nombres_conceptos_estandarizados_balance_sheet) 
df_bs_show = df_bs
df_bs_show['Concepto'] = pd.Series(nombres_conceptos_estandarizados_balance_sheet) 


conceptos_bs = pd.Series(nombres_conceptos_estandarizados_balance_sheet)

list_of_columns = []
list_of_columns.append(conceptos_bs)

df_bs_show = pd.DataFrame(index = conceptos_estandarizados_balance_sheet, columns=list_of_columns))


##### DATAFRAME PARA MOSTRAR VISUALMENTE MAS FACIL AGREGA COLUMNA CON EL NOMBRE DE LOS CONCEPTOS
# Crea un DataFrame con el indice de los conceptos estandarizados del BS
df_bs_show = pd.DataFrame(index = conceptos_estandarizados_balance_sheet)
# Agrega la columna Concepto y mapea con el nombre de los conceptos.
df_bs_show['Concepto'] = pd.Series(nombres_conceptos_estandarizados_balance_sheet) 




#ABRE EL ARCHIVO CON LOS DATOS y lo carga en df
open_excel("C:\GCB_CAPITAL", "FS_TXAR", ".xlsx")
# Controla si estan estos anios en el dataframe y agrega los anios completos en la lista de columnas para crear un dataframe
list_of_columns = []
years = ["2018", "2019"]
for i in years:
    if (str(i)+"Q1") in df.columns and (str(i)+"Q2") in df.columns and (str(i)+"Q3") in df.columns and (str(i)+"Q4") in df.columns:     
       list_of_columns.append(str(i))
       df_bs_show[i] = 0



Metrica del IS
# Agrega el concepto RI18 al indice del DataFrame
df_bs_show = df_bs_show.append(pd.Series(name='RI18'))

if 'RI18' in df.index:
   df_bs_show['2018']['RI18']=df['2018Q1']['RI18']+df['2018Q2']['RI18']+df['2018Q3']['RI18']+df['2018Q4']['RI18']

# Metrica del BS
if 'BI0001' in df.index:
   df_bs_show['2018']['BI0001']=df['2018Q4']['BI0001']
if 'RI216' in df.index:
   df_bs_show['2018']['RI216']=df['2018Q4']['RI216']




df_bs_show['Concepto'] = pd.Series(

nombres = nombres_conceptos_estandarizados_balance_sheet  + nombres_conceptos_estandarizados_estado_de_resultado + nombres_conceptos_estandarizados_cash_flow

nombres_conceptos_estandarizados_balance_sheet 
nombres_conceptos_estandarizados_estado_de_resultado
nombres_conceptos_estandarizados_cash_flow



 

