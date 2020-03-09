def serie_de_tiempo(matriz):
    global df
    if 'Fecha' in df:
       #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
       df = df.set_index('Fecha', inplace=False)
    else:
       print ("El DataFrame df no tiene una columna llamada Fecha para establecer como datetime index") 
    return df      

#serie_de_tiempo(df)