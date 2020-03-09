
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

# Crea una lista vacia de fechas
lista_de_fechas = []
# Crea una lista vacia de valores
lista_de_valores = []

# Donde 0 y 1 son las posiciones del index en las que estan las fechas y los valores respectivamente, hace un for loop para armar listas con las fechas y los valores.
for i in list(df.columns):
    # Agrega a la lista vacia las fechas que tiene el dataframe en la fila llamada "Close_date"
    lista_de_fechas.append(df[i].loc['Close_date'])
    # Agrega a la lista vacia los importes que tiene el dataframe en la fila llamada "LTM_NI"
    lista_de_valores.append(df[i].loc['LTM_NI'])

# Imprime en pantalla la lista de fechas
print (lista_de_fechas)
# Imprime en pantalla la lista de valores
print (lista_de_valores)

# Crea un dataframe llamado evolucion
evolucion = pd.DataFrame() #Crea una matriz de pandas

# Agrega la columna Fecha al dataframe con valor por default igual a 0 (cero)
#evolucion["Fecha"] = 0
# Agrega la columna Fecha al dataframe con valor por default igual a ""
evolucion["Fecha"] = ""
# Agrega la columna concepto al dataframe con valor por default igual a ""
evolucion["concepto"] = ""

# Chequea que el largo de lista de fechas sea el mismo que lista de valores
len(lista_de_fechas) == len(lista_de_valores)

# Agrega al dataframe evolucion, una por una la fecha y un valor
for i in range(0, (len(lista_de_fechas))):
    evolucion = evolucion.append({'Fecha': lista_de_fechas[i], 'concepto': lista_de_valores[i] }, ignore_index=True)     

# Establece la fecha como el indice de dataframe
evolucion = evolucion.set_index('Fecha', inplace=False) # Sete el indice como la columna Fecha
# Establece el formato del indice en formato datetime
evolucion.index = pd.to_datetime(evolucion.index, format="%Y-%m-%d") # Convertimos el indice en date time con el formato ANO-MES-DIA
# Convierte la columna "concepto" en punto flotante
evolucion['concepto'] = evolucion['concepto'].astype(float) # Convierte la columna de concepto a punto flotante 

######################################################################################################################################
# CONOCIMIENTOS POSIBLEMENTE UTILES
# Agrega una row al dataframe , pero para esto tenes que saber la cantidad de columnas que tiene el df
#df = df.append({'2001Q1': 23, '2001Q2': 'Riti', '2001Q3': 'Login', '2001Q4': 'Login'}, ignore_index=True)
#####################################################################################################################################

##################################################################################################################
################### HASTA ACA ARME UN DATAFRAME LLAMADO EVOLUCION CON LOS PUNTOS DE DATOS EN LA COLUMNA CONCEPTO #
##################################################################################################################

evolucion.tail(1).index # para buscar la ultima fecha de la serie
intermedio = str(evolucion.tail(1).index) # Transformamos en una variable string
b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING

# Abre el mkt cap_usd_ppp file del ticker
open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "TXAR", ".xlsx")

# Mergea la matriz evolucion con el df de mkt cap_usd_ppp
merge = pd.merge(df, evolucion, how='outer', left_index=True, right_index=True) # mergea las dos dataframes e incorpora la columna "capital"
# 
merge.loc[:,'concepto'] = merge.loc[:,'concepto'].fillna(0) #completa la columna capital los NA y los reemplaza por 0

# Renombra la matriz merge a df
df = merge
# Agrega una columna C que tiene todos valores NaN
df['C'] = np.nan #agrega nan en toda la columna C 
# Ordena el indice de manera descendente 
df = df.sort_index(axis=0, level=None, ascending=False) # Da vuelta el indice

# Muestra el head del df
df.head(1).index[-1] # muestra el head
intermedio2 = str(df.head(2).index) # Convierte a string
anteultima_fecha = intermedio2[30:40] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
df=df.fillna(0)  #completo con 0 los nan de la columna C mayuscula.

global value
value = 0 

def calculate(mul):
    # Esta funcion calcula el capital con calculo iterativo
    global value
    if mul == 0: 
       value = value
    else:
       value = mul    
    return value

df.loc[anteultima_fecha:, 'C'] = df.loc[anteultima_fecha:].apply(lambda row: float(calculate(*row[['concepto']])), axis=1)  # Itera sobre la columna capital utilizando la formula calculate
df=df.drop(['concepto'], axis=1)  #elimina la columna concepto que es donde habiamos colocado los puntos
df=df.sort_index(axis=0, level=None, ascending=True) #Reordena el dataframe

PARA ANUALIZAR EL QUARTER
#df=df.rename(columns={'C': 'Quarter_Net_Income_M_ARS'}) #
#df['Annualized_Net_Income_M_ARS']=df['Quarter_Net_Income_M_ARS']*4
#df['Annual_EPS_(Quaterly_annualized)']=df['Annualized_Net_Income_M_ARS']/df['Capital'] 
#df['PE_ratio']=df['Cierre_del_dia']/df['Annual_EPS_(Quaterly_annualized)'] 

PARA ANUALIZAR EL QUARTER
df=df.rename(columns={'C': 'LTM_NI'}) #
df['Annual_EPS_(LTM_NI)']=df['LTM_NI']/df['Capital'] 
df['PE_ratio']=df['Cierre_del_dia']/df['Annual_EPS_(LTM_NI)'] 



# Crea una lista de filas del dataframe a borrar
lista_de_filas_a_borrar = []
# Eliminar las filas del df que 

# Identifica las filas del df a borrar
for i in evolucion['Fecha']:
    a = df['Cierre_del_dia'].loc[i]
    if a == 0:
       lista_de_filas_a_borrar.append(i)

# Elimina las filas en la matriz df
for i in lista_de_filas_a_borrar:
    df.drop(pd.Timestamp(i), inplace=True)

# GRaba el archivo
save_file("C:\GCB_CAPITAL\OUTPUT", "TXAR3", ".xlsx")

chart_series_de_dataframe(df , "PE_ratio")
