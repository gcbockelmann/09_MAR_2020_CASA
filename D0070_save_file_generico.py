def save_file_generico(matriz, save_location, nombre_archivo_pre_ticker, ticker, ext):
    ### Esta funcion toma la df global y la graba en un archivo con el nombre SERIE_CORRIENTE_ticker en el subdirectorio especificado
    location = str(save_location)                                 
    filename = str(nombre_archivo_pre_ticker + ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    matriz.to_excel(path_writer, 'DataFrame')
    path_writer.save()
    return

#save_file_generico(df, "C:\GCB_CAPITAL\OUTPUT", "GENERICO", "AGRO", ".xlsx")

# utiliza el open_file_versatil del archivo B04 e initializa una serie corriente nueva
# inicializa una nueva serie corriente que antes no existia