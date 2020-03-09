
def open_excel(loc, ticker, ext, tab=0):
    ### Esta funcion abre un archivo de excel con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    print (path)
    df = pd.read_excel(path, sheet_name=tab)
    return (df)

# Abre el excel de estados financieros del ticker
#open_excel("C:\GCB_CAPITAL", "FS_TXAR", ".xlsx")
#open_excel("C:\GCB_CAPITAL\BOLSAR", "2020-01-16_TODO", ".xlsx", "Indices")





def arma_path(loc, file_name, ext):
    location = str(loc)                                 
    filename = str(file_name)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    return path

#arma_path("C:\GCB_CAPITAL\BOLSAR", "2020-01-16_TODO", ".xlsx")

#df = pd.read_excel(arma_path("C:\GCB_CAPITAL\BOLSAR", "2020-01-16_TODO", ".xlsx"), sheet_name=0)