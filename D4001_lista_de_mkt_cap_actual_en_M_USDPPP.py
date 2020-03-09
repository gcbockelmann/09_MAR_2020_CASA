def lista_mkt_cap_actual_en_M_USDPPP(lista2):
    """ lista """
    global df, mkt_cap_actual_en_M_USDPPP
    #
    #
    mkt_cap_actual_en_M_USDPPP = pd.DataFrame()
    #
    for ticker in lista2:
        ############### CARGA EL DATAFRAME DEL TICKER
        #   
        #
        # Location jamas termina con una barra
        location = original_source + "MARKET_CAP_USDPPP"
        #
        # Slash es la barra
        slash = str("//")
        #
        # Filename parte 1 es un nombre que le agrega el programa a los archivos
        file_name_parte1 = "MKT_CAP_USD_"
        #
        # Filename parte 2 es el ticker
        file_name_parte2 = ticker
        #
        # file_name es el total del nombre del archivo incluyendo al ticker que lo identifica                             
        file_name = file_name_parte1 + file_name_parte2     
        #
        # Extension es la extension del archivo
        extension = ".xlsx"
        #
        # Path es el todo la linea para llegar al archivo
        path = location + slash + file_name + extension
        #print (path)
        #
        #open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "AGRO", ".xlsx")
        open_file_mkt_cap_usdppp(location, ticker, extension)
        #    
        #
        # Extension es la extension del archivo
        #
        df.tail(1).index # para buscar la ultima fecha de la serie
        intermedio = str(df.tail(1).index) # Transformamos en una variable string
        b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
        ultima_fecha_mkt_cap_en_USDPPP = str(b)
        #
        #
        mkt_cap_usdppp = df.loc[ultima_fecha_mkt_cap_en_USDPPP, 'Mkt_Cap_Close_USD_PPP']
        #
        mkt_cap_actual_en_M_USDPPP = mkt_cap_actual_en_M_USDPPP.append({'Ticker': ticker, 'Fecha': ultima_fecha_mkt_cap_en_USDPPP, 'Mkt_Cap_USDPPP': mkt_cap_usdppp }, ignore_index=True)   
        #
        #        
        #
        pass







lista = ["AGRO", "ALUA", "AUSO", "BBAR", "BHIP", "BMA", "BOLT", "BPAT", "BRIO", "BYMA", "CADO", "CAPX", "CEPU", "CGPA2", "COME", "CRES", "CTIO", "CVH", "DGCU2", "EDN", "ESME", "FERR", "GCLA", "GGAL", "HARG", "INTR", "INVJ", "LEDE", "LOMA", "METR", "MIRG", "MOLA", "MOLI", "OEST", "PAMP", "PATA","RICH","SAMI", "SUPV", "TECO2", "TGNO4", "TGSU2", "TRAN", "TXAR", "VALO", "YPFD"]
lista_mkt_cap_actual_en_M_USDPPP(lista)
print (mkt_cap_actual_en_M_USDPPP)
