


def open_index_file_bolsar(loc, ticker, ext):
    #
    ### Esta funcion abre un archivo de excel recien bajado de bolsar con el nombre y ubicacion especificados y lo carga en la matriz df
    ### Ademas de cargarlo asigna el nombre que nosotros queremos a cada una de las columnas del archvio de bolsar
    global df
    location = str(loc)                                 
    filename = str(ticker)     
    extension = str(ext)    
    #
    #
    open_excel(location, ticker, extension)
    serie_de_tiempo(df)
    formateo_input_bolsar_indice(df)
    #
    ####FORMATEO DEL ARCHIVO
    #df.rename(columns = {'Especie':'Especie'}, inplace=True)
    #df.rename(columns = {'Fecha':'Fecha'}, inplace=True)
    #df.rename(columns = {'Vencimiento':'Vencimiento'}, inplace=True)
    #df.rename(columns = {'Tipo de Serie':'Tipo_de_Serie'}, inplace=True)
    #df.rename(columns = {'Cierre del día':'Cierre_del_día'}, inplace=True)
    #df.rename(columns = {'Variación %':'Variación_%'}, inplace=True)
    #df.rename(columns = {'Máximo':'Máximo'}, inplace=True)
    #df.rename(columns = {'Mínimo':'Mínimo'}, inplace=True)
    #if 'Variacion_%' in df:
    #   df=df.drop(['Variacion_%'], axis=1)
    #
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    #df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    #    
    return df


### PRUEBA
#open_index_file_bolsar("C:\GCB_CAPITAL2\INPUT", "^MERV", ".xlsx")

### FUNCION OPEN INDEX FILE SPCH: ABRE UN ARCHIVO DE EXCEL CON LA SPCH Y LO CARGA EN LA MATRIZ DF
def open_index_file_spch(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel spch, con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = str(ticker)     
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
    # pandas drop a column with drop function    
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    formateo_input_bolsar_indice(df)
    return (df)


#open_index_file_spch("C:\GCB_CAPITAL2\SPCH", "SERIE_CORRIENTE_^MERV", ".xlsx")

#save_file("C:\GCB_CAPITAL\OUTPUT", "^MERV", ".xlsx")





### ACTUALIZA SERIE DE PRECIOS CORRIENTE HISTORICA
def update_indice(ticker):
    ### Esta funcion actualiza la serie de precios corrientes historica de un indice indicado como ticker con la data nueva de bolsar
    ### El ticker se debe ingresar como una string
    global df
    filename2 = str ("SERIE_CORRIENTE_" + ticker)   
    #borrar print (filename2) 
    ispch = open_index_file_spch(original_source + "\SPCH", filename2 , ".xlsx")
    idata = open_index_file_bolsar(original_source + "\INPUT", ticker, ".xlsx")
    #Estas dos renombre de columnas ya fueron puestas en la funcion open file spch y se podrian borrar
    #
    # Inserta en la posicion de columna 4 una columna llamada "Variacion" con el string "any"
    #idata.insert(4,'Variación_%',"any")
    idata.rename(columns = {'Último':'Cierre_del_día'}, inplace = True) 
    #idata.rename(columns = {'Variación_%':'Variacion_%'}, inplace = True) 
    #ispch= ispch.drop(['Variación_%'], axis=1)
    #ispch.rename(columns = {'Variacion %':'Variación_%'}, inplace = True) 
    ispch.rename(columns = {'Mínimo':'Minimo'}, inplace = True) 
    ispch.rename(columns = {'Máximo':'Maximo'}, inplace = True) 
    ispch.rename(columns = {'Cierre_del_día':'Cierre_del_dia'}, inplace = True) 
    #ispch= ispch.drop(['Variacion_%'], axis=1)
    #estas proximas 2 filas tambien quedaron obsoletas.
    #ispch = spch.set_index('Fecha')
    #idata = data.set_index('Fecha')
    #Para checkear que las 2 listas de nombres son iguales > al devolver True.
    print (ispch.columns)
    print (idata.columns)
    if list(ispch.columns) == list(idata.columns):
       #Esta funcion concatena dos dataframes (supongo que de igual cantidad y mismo nombre de columnas) y luego dropea las rows duplicadas
       #la matriz a grabar se pone en df para poder nutrir a la funcion de guardado
       df = pd.concat([ispch,idata]).drop_duplicates()
       df['Especie']= "S&P_Merval"
       #df = df.drop(['Variacion_%'], axis=1)
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
       save_file_generico(df, original_source + "\OUTPUT\INDICES", "SERIE_CORRIENTE_", ticker, ".xlsx")
    else:
       print ("Problema la lista de nombres de columnas no coincide")
    return

#update_indice("^MERV")



