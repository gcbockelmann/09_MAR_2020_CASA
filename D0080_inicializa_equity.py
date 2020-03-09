


def inicializa_equity(ticker):
    #
    global df
    #
    open_excel("C:\GCB_CAPITAL2\INPUT", ticker, ".xlsx")
    #
    df=serie_de_tiempo(df)
    #
    df=formateo_input_bolsar_equity(df)
    #
    save_file_generico(df, "C:\GCB_CAPITAL2\OUTPUT\INICIALIZA", "SERIE_CORRIENTE_", ticker , ".xlsx")
    print ("Se debe copiar este archivo a la carpeta SPCH para cuando se quiera actualizar la base de datos haya una serie historica")
    #
    return




#inicializa_equity("AGRO")
#open_excel("C:\GCB_CAPITAL2\INPUT", "AGRO", ".xlsx")
#df = df.set_index("Fecha")