
def prepara_input_merval(source_path, nombre_del_archivo, ext, save_location, tab=0):
    #
    global df
    #
    open_excel(source_path, nombre_del_archivo, ext, tab)
    """ Genera los archivos de input para agregar a la SPCH de los indices"""
    df.columns = ["Indices", "Fecha", "Apertura", "Minimo", "Maximo", "Cierre_del_dia"]
    #
    df = serie_de_tiempo(df)
    #    
    #formateo_input_bolsar_indice(df)
    #
    if 'Variacion_%' in df:
       df=df.drop(['Variacion_%'], axis=1)
    #
    # AGREGA LA COLUMNA ESPECIE
    df['Especie']="S&P_Merval"
    #
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    #df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    #    
    #
    filename = str("^MERV")     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (save_location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()



#prepara_input_merval("C:\GCB_CAPITAL2\BOLSAR", "2020-01-16_TODO", ".xlsx", "C:\GCB_CAPITAL2\INPUT", "Indices")

