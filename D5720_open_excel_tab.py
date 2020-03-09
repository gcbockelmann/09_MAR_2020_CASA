




open_excel("C:\GCB_CAPITAL", "TXAR", ".xlsx", "REPORTADO")

# Asigna el valor de la fila 2 como header de las columnas
df.columns = df.iloc[2]

# Remueve la fila 2 de la matriz
df.drop(df.index[2])


# Remueve desde la fila 2 hasta la fila 4 (no inclusive) de la matriz
df.drop(df.index[2:4])


# Remueve desde la fila 0 hasta la fila 6 (no inclusive) de la matriz
df = df.drop(df.index[0:6])

#Remueve de la fila 1 hasta el final
df = df.drop(df.index[1:])

# Muestra los nombres de las columnas de la matriz
df.columns


# Le cambia el nombre a las columnas con nan
df = df.rename(columns=str).rename(columns={'nan':'columna_a'})

# Borra la columna_a del dataframe
df.drop(['columna_a'], axis='columns', inplace=True)

# Borra las columnas a partir de la columna 5 en adelante
df.drop(df.columns[4:],axis=1,inplace=True) # la cuarta columna de 2001Q4 no la toca

# Pone fechas en el dataframe
df["2001Q1"].loc[6] = "2001-03-31"
df["2001Q2"].loc[6] = "2001-06-30"
df["2001Q3"].loc[6] = "2001-09-30"
df["2001Q4"].loc[6] = "2001-12-31"

# Resetea el indice, lo vuelve a setear renumerando desde cero
df = df.reset_index(drop=True)

df2 = df.reset_index()

############## NO se bien que hace
df = df2.set_index('index')

# Agrega una row al dataframe sin especificar las columnas ni nada
df = df.append(pd.Series(), ignore_index=True)

# Agrega valores al dataframe
df["2001Q1"].loc[1] = 10
df["2001Q2"].loc[1] = 12
df["2001Q3"].loc[1] = 14
df["2001Q4"].loc[1] = 16

################### HASTA ACA ARME EL DATAFRAME DF CON LOS PUNTOS DE DATOS
########################################################################

save_file("C:\GCB_CAPITAL\OUTPUT", "TXAR2", ".xlsx")

open_excel("C:\GCB_CAPITAL\OUTPUT", "SERIE_CORRIENTE_TXAR2", ".xlsx")

###################################################################


# Crea una lista vacia
lista_de_fechas = []
lista_de_valores = []
# Agrega a la lista vacia las fechas que tiene el dataframe

# Donde 0 y 1 son las posiciones del index en las que estan las fechas y los valores respectivamente, hace un for loop para armar listas con las fechas y los valores.
for i in list(df.columns):
    lista_de_fechas.append(df[i].loc[0])
    lista_de_valores.append(df[i].loc[1])

# Imprime en pantalla la lista de fechas
print (lista_de_fechas)
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

for i in range(0, (len(lista_de_fechas))):
    evolucion = evolucion.append({'Fecha': lista_de_fechas[i], 'concepto': lista_de_valores[i] }, ignore_index=True)     

evolucion = evolucion.set_index('Fecha', inplace=False) # Sete el indice como la columna Fecha
evolucion.index = pd.to_datetime(evolucion.index, format="%Y-%m-%d") # Convertimos el indice en date time con el formato ANIO-MES-DIA
evolucion['concepto'] = evolucion['concepto'].astype(float) # Convierte la columna de concepto a punto flotante 

######################################################################################################################################
# CONOCIMIENTOS POSIBLEMENTE UTILES
# Agrega una row al dataframe , pero para esto tenes que saber la cantidad de columnas que tiene el df
#df = df.append({'2001Q1': 23, '2001Q2': 'Riti', '2001Q3': 'Login', '2001Q4': 'Login'}, ignore_index=True)
#####################################################################################################################################

##############################################################################################################
################### HASTA ACA ARME UN DATAFRAME LLAMADO EVOLUCION CON LOS PUNTOS DE DATOS EN LA COLUMNA CONCEPTO
###############################################################################################

evolucion.tail(1).index # para buscar la ultima fecha de la serie
intermedio = str(evolucion.tail(1).index) # Transformamos en una variable string
b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING


#open_file_spch("C:\GCB_CAPITAL\SPCH", filename, ".xlsx") #abre la spch
#open_file_spch("C:\GCB_CAPITAL\SPCH", "SERIE_CORRIENTE_TXAR", ".xlsx") #abre la spch
open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "TXAR", ".xlsx")

merge = pd.merge(df, evolucion, how='outer', left_index=True, right_index=True) # mergea las dos dataframes e incorpora la columna "capital"
merge.loc[:,'concepto'] = merge.loc[:,'concepto'].fillna(0) #completa la columna capital los NA y los reemplaza por 0

df = merge
df['C'] = np.nan #agrega nan en toda la columna C  
df = df.sort_index(axis=0, level=None, ascending=False) # Da vuelta el indice

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
df=df.rename(columns={'C': 'Quarter_Net_Income_M_ARS'}) #
df['Annualized_Net_Income_M_ARS']=df['Quarter_Net_Income_M_ARS']*4
df['Annual_EPS_(Quaterly_annualized)']=df['Annualized_Net_Income_M_ARS']/df['Capital'] 
df['PE_ratio']=df['Cierre_del_dia']/df['Annual_EPS_(Quaterly_annualized)'] 
save_file("C:\GCB_CAPITAL\OUTPUT", "TXAR3", ".xlsx")


#chart_series_de_dataframe(df , "PE_ratio", "2012-01-04", "2019-09-13")