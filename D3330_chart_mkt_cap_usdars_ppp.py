
def open_file_mkt_cap_usdppp(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel mkt_cap_ars_ticker, con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = "MKT_CAP_USDPPP_" + str(ticker)     
    extension = str(ext)
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)
    print (path)
    df = pd.read_excel(path)   
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    return

#PRUEBA
#open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "AGRO", ".xlsx")
#open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "BOLT", ".xlsx")
#open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", "TXAR", ".xlsx")


#############################
#########DISENO CHART VERSATIL
########3
#####################

### FUNCION PAINT_MKT_CAP_USD: DIBUJA LA SERIE QUE NOS INDICA
def paint_mkt_cap_usdppp(ticker):
    ### GRAFICA LOS ULTIMOS N puntos de la Serie indicada
    ### Si el indice esta en formato datetime, al correr este codigo las fechas aparecen en el eje x automaticamente
    #
    global df
    #
    # Establece el rango del chart
    #
    #Rango inicial. La serie puede identificarse como 0 (el primer dato de la serie) o como un numero negativo comenzando desde el final de la serie
    rango_inicial = 0
    #
    #Rango final. La serie puede identificarse como 0 (el primer dato de la serie) o como un numero negativo comenzando desde el final de la serie
    # 0 es el final de la serie pero se debe completar ni con "" ni con 0
    rango_final = -1
    #
    #
    # Da la orden de graficar los ultimos n puntos de la serie
    ax = df[['Mkt_Cap_USDPPP']].iloc[rango_inicial:rango_final].plot(color ='k', linestyle = '-', figsize =(12,12), linewidth = 1 ) #18,12 es grande
    #
    # Calcula las Moving Average y los suma a la df
    #
    df["MA200"] = df.Mkt_Cap_USDPPP.rolling(200).mean()
    df["MA100"] = df.Mkt_Cap_USDPPP.rolling(100).mean()
    df["MA50"] = df.Mkt_Cap_USDPPP.rolling(50).mean()
    df["MA25"] = df.Mkt_Cap_USDPPP.rolling(25).mean()
    #
    # Activa las medias moviles o las desactiva
    #
    #df['MA200'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
    #df['MA100'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA50'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA25'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #
    #
    # Define el titulo como una variable string
    title = "Evolucion Mkt Cap de " + ticker + " en M USDARS_PPP"
    plt.title(title)
    #    
    # Situa la leyenda arriba a la izquierda (loc=2)
    plt.legend(loc=2)
    #    
    # Pone los labels del eje x de forma vertical
    plt.xticks(rotation='vertical')
    #
    # Define el margen de cuan pegados estan los labels entre si del eje x. cuanto mas pequeno empieza a ser neceseario mostrar mas detalle en los labels.
    plt.margins(0.1)
    #
    #Distancia desde el fondo del chart (corre la altura del eje x en el dibujo. Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.25)
    #
    #Define el label del eje x como una variable string
    x_label = "fecha"
    #
    #Define el xlabel, x=1 estaria en el limite inferior derecho, x=0.50 estaria casi en el medio
    plt.xlabel(x_label, fontsize=9, x=0.50, y=0.10)
    #
    #Define el label del eje y como una variable string
    y_label = "Mkt Cap en M USDARS_PPP"
    #
    #Define el ylabel, y=1 estaria en el limite superior, y=0.50 estaria casi en el medio
    plt.ylabel(y_label, fontsize=9, x=0.10, y=0.50)
    #
    # Add a legend
    #
    plt.legend('off')
    #
    plt.axis('on') 
    #Dibuja una recta horizontal en y = 600 de color azul
    #plt.axhline(y = 600, xmin = 0, xmax = 250000)
    ##Dibuja una recta horizontal en y = 0 de color rojo
    #plt.axhline(color = 'r')
    plt.grid(True)
    plt.grid(color = 'k') #r=red b=blue g=green y=yellow c=cian w=white m=magenta k=black
    plt.grid(linestyle = ':') # '-' = linea solida, '--' = linea a rayas,'-.' = puntos y rayas, ':' = linea punteada,
    plt.grid(linewidth=1) # 1 es lo mas finito, 20 es grueso
    plt.text(500, 300, "Más texto", fontsize = 200)
    #
    # Define que el formato de los numeros del eje y sean con coma para separar los miles  
    ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #
    # Save Figure
    #
    # Location jamas termina con una barra
    location = original_source + "13_CHART_MKT_CAP_USDARS_PPP"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = ""
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ticker
    #
    # file_name es el total del nombre del archivo incluyendo al ticker que lo identifica                             
    file_name = file_name_parte1 + file_name_parte2     
    #
    # Extension es la extension del archivo
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    extension = "_" + str(b)
    #
    # Path es el todo la linea para llegar al archivo
    path = location + slash + file_name + extension
    #print (path)
    #
    # Graba en formato png. Fijarse que no hay que poner la extension.
    # A Modo de Ejemplo seria: plt.savefig('C:\GCB_CAPITAL\myfig')
    plt.savefig(path)
    #plt.show()  # lo desactive para poder grabar todos los archivos
    return

#paint_mkt_cap_usdppp("AGRO")
#paint("ALUA", "Mkt_Cap_USDPPP")
#paint("BOLT", "Mkt_Cap_USDPPP")




### FUNCION OPEN FILE MKT CAP ARS Y LO CARGA EN LA MATRIZ DF
def chartmktcapusdppp(ticker50):
    ### Esta funcion abre un archivo el archivo de excel mkt_cap_usd correspondiente a ese ticker y lo carga en la matriz df
    global df
    # Location jamas termina con una barra
    location = original_source + "MARKET_CAP_USDPPP"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "MKT_CAP_USDPPP_"
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ticker50
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
    open_file_mkt_cap_usdppp(location, ticker50, extension)
    #    
    # Dibuja
    #
    paint_mkt_cap_usdppp(ticker50)
    #
    return

#chartmktcapusdppp("AGRO")
#chartmktcapusdppp("ALUA")
##MISSING chartmktcapusdppp("APBR")
#chartmktcapusdppp("AUSO")
#chartmktcapusdppp("BBAR")
#chartmktcapusdppp("BHIP")
#chartmktcapusdppp("BMA")
#chartmktcapusdppp("BOLT")
#chartmktcapusdppp("BPAT")
#chartmktcapusdppp("BRIO")
#chartmktcapusdppp("BYMA")
#chartmktcapusdppp("CADO")
#chartmktcapusdppp("CAPX")
#chartmktcapusdppp("CEPU")
#chartmktcapusdppp("CGPA2")
#chartmktcapusdppp("COME")
#chartmktcapusdppp("CRES")
#chartmktcapusdppp("CTIO")
#chartmktcapusdppp("CVH")
#chartmktcapusdppp("DGCU2")
#chartmktcapusdppp("EDN")
#chartmktcapusdppp("ESME")
#chartmktcapusdppp("FERR")
#chartmktcapusdppp("GCLA")
#chartmktcapusdppp("GGAL")
#chartmktcapusdppp("HARG")
#chartmktcapusdppp("INTR")
#chartmktcapusdppp("INVJ")
#chartmktcapusdppp("LEDE")
#chartmktcapusdppp("LOMA")
#chartmktcapusdppp("METR")
#chartmktcapusdppp("MIRG")
#chartmktcapusdppp("MOLA")
#chartmktcapusdppp("MOLI")
#chartmktcapusdppp("OEST")
#chartmktcapusdppp("PAMP")
#chartmktcapusdppp("PATA")
#chartmktcapusdppp("RICH")
#chartmktcapusdppp("SAMI")
#chartmktcapusdppp("SUPV")
#chartmktcapusdppp("TECO2")
#chartmktcapusdppp("TGNO4")
#chartmktcapusdppp("TGSU2")
#chartmktcapusdppp("TRAN")
#chartmktcapusdppp("TXAR")
#MISSING chartmktcapusdppp("TS")
#chartmktcapusdppp("VALO")
#chartmktcapusdppp("YPFD")
