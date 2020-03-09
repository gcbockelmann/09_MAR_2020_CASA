def secciona_tab_de_equities_de_bolsar(source_location, nombre_del_archivo, ext, tab, save_location):
    """ Genera los archivos de input para agregar a la SPCH"""
    #
    global df 
    #
    # Abre un excel con la ubicacion, el nombre, la extension y en la tab especificada
    open_excel(source_location, nombre_del_archivo, ext, tab)
    #
    # Crea una lista vacia
    lista_de_nombres_de_tickers = []
    #
    # Crea un segundo dataframe quitando los duplicados de la columna Especie
    matriz_de_tickers_unicos = df.drop_duplicates(subset='Especie', keep='first')
    #
    # Corre un loop que por cada diferente valor en el indice que tome el valor de la columna Especie y que lo cargue a la lista
    for i in matriz_de_tickers_unicos['Especie'].index:  
        lista_de_nombres_de_tickers.append(matriz_de_tickers_unicos['Especie'].loc[i])
    #
    # Corre un loop que por cada ticker en la lista, cree una matriz igual solo a ese ticker en la columna especie
    # que luego grabe esa matriz en un excel en el subdirectorio, y con la extesion y con el nombre del ticker.
    #
    for i in lista_de_nombres_de_tickers:
        dfi = df[df.Especie == i]   
        # No conviene darle tratamiento de serie de tiempo aun porque conviene cambiarle el nombre a las columnas primero pero lo hacemos para evitar el agregado de columnas innecesarias
        if "Fecha" in dfi:
           # Si el dataframe no tiene una columna llamada fecha puede ser porque esta sea el indice, en ese caso no es necesario setearlo como serie de tiempo.
           dfi = serie_de_tiempo(dfi)                       
        filename = str("" + i)     
        extension = ".xlsx"
        #En una variable string la doble blackslash \\ resulta en una sola \
        path = (save_location + "\\" + filename + extension)  
        print (path)  
        path_writer = pd.ExcelWriter(path)
        dfi.to_excel(path_writer, 'DataFrame')
        path_writer.save()


#secciona_tab_de_equities_de_bolsar("C:\GCB_CAPITAL2\BOLSAR", "2020-01-16_TODO", ".xlsx", 0, "C:\GCB_CAPITAL2\INPUT")

