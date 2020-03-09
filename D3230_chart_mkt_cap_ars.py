
### FUNCION PAINT_MKT_CAP_ARS: DIBUJA LA EVOLUCION DEL MKT CAP EN PESOS
def paint_mkt_cap_ars(ticker):
    ### GRAFICA LOS N  puntos del Market Cap
    ### Si el indice esta en formato datetime, al correr este codigo las fechas aparecen en el eje x automaticamente
    global df
    #
    # Establece el rango del chart
    #
    rango = -1000 #debe ser un numero negativo
    #
    # Da la orden de graficar los ultimos 1000 puntos de la serie
    ax = df[['Mkt_Cap_ARS']].iloc[rango:].plot(color ='k', linestyle = '-', figsize =(12,12), linewidth = 1 ) #18,12 es grande
    #
    # Calcula las Moving Average y los suma a la df
    #
    df["MA200"] = df.Mkt_Cap_ARS.rolling(200).mean()
    df["MA100"] = df.Mkt_Cap_ARS.rolling(100).mean()
    df["MA50"] = df.Mkt_Cap_ARS.rolling(50).mean()
    df["MA25"] = df.Mkt_Cap_ARS.rolling(25).mean()
    #
    # Activa las medias moviles o las desactiva
    #
    df['MA200'].iloc[rango:].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
    df['MA100'].iloc[rango:].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA50'].iloc[rango:].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA25'].iloc[rango:].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #
    #
    # Define el titulo como una variable string
    title = "Evolucion Mkt Cap de " + ticker + " en M ARS"
    plt.title(title)
    #    
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
    y_label = "Mkt Cap en M ARS"
    #
    #Define el ylabel, y=1 estaria en el limite superior, y=0.50 estaria casi en el medio
    plt.ylabel(y_label, fontsize=9, x=0.10, y=0.50)
    #
    # Add a legend
    #
    plt.legend('off')
    #
    #plt.axis('on') 
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
    #
    # Save Figure
    #
    # Location jamas termina con una barra
    location = original_source + "11_CHART_MKT_CAP_ARS"
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
    #
    ##### ESTAS ULTIMAS DOS ES PARA QUE LOS CHARTS NO QUEDEN EN MEMORIA
    #
    #plt.cla()
    #
    #
    #plt.close(fig)
    plt.close()
    #
    return

#paint_mkt_cap_ars("AGRO")
#paint_mkt_cap_ars("ALUA")
#paint_mkt_cap_ars("TXAR")
#paint_mkt_cap_ars("SAMI")
#paint_mkt_cap_ars("SUPV")


### FUNCION OPEN FILE MKT CAP ARS Y LO CARGA EN LA MATRIZ DF
def open_file_mkt_cap_ars(loc, ticker, ext):
    ### Esta funcion abre un archivo de excel mkt_cap_ars_ticker, con el nombre y ubicacion especificados y lo carga en la matriz df
    global df
    location = str(loc)                                 
    filename = "MKT_CAP_ARS_" + str(ticker)     
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
    #Establece como indice a la columna de fecha para poder cruzarla contra otros dataframes y con inplace=False hace caer la columna de la matriz
    df = df.set_index('Fecha', inplace=False)
    df.index = pd.to_datetime(df.index, format="%d/%m/%Y") 
    return (df)

#PRUEBA
#open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", "AGRO", ".xlsx")
#open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", "BOLT", ".xlsx")
#open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", "TXAR", ".xlsx")

### FUNCION OPEN FILE MKT CAP ARS Y LO CARGA EN LA MATRIZ DF
def chartmktcapars(ticker2):
    ### Esta funcion abre un archivo el archivo de excel mkt_cap_ars correspondiente a ese ticker y lo carga en la matriz df
    global df
    # Location jamas termina con una barra
    location = original_source + "MARKET_CAP_ARS"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "MKT_CAP_ARS_"
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ticker2
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
    open_file_mkt_cap_ars(location, ticker2, extension)
    #    
    # Dibuja
    #
    paint_mkt_cap_ars(ticker2)
    #
    return 



#chartmktcapars("AGRO")
#chartmktcapars("ALUA")
#chartmktcapars("AUSO")
#chartmktcapars("BBAR")
#chartmktcapars("BHIP")
#chartmktcapars("BMA")
#chartmktcapars("BOLT")
#chartmktcapars("BPAT")
#chartmktcapars("BRIO")
#chartmktcapars("BYMA")
#chartmktcapars("CADO")
#chartmktcapars("CAPX")
#chartmktcapars("CEPU")
#chartmktcapars("CGPA2")
#chartmktcapars("COME")
#chartmktcapars("CRES") #FALTA MAL LOS SPLITS REVISAR TODO
#chartmktcapars("CTIO")
#chartmktcapars("CVH")
#chartmktcapars("DGCU2")
#chartmktcapars("EDN") #FALTA LA SERIE LARGA DE BOLSAR
#chartmktcapars("ESME")
#chartmktcapars("FERR")
#chartmktcapars("GCLA")
#chartmktcapars("GGAL")
#chartmktcapars("HARG")
#chartmktcapars("INTR")
#chartmktcapars("INVJ")
#chartmktcapars("LEDE")
#chartmktcapars("LOMA")
#chartmktcapars("METR")
#chartmktcapars("MIRG")
#chartmktcapars("MOLA")
#chartmktcapars("MOLI")
#chartmktcapars("OEST")
#chartmktcapars("PAMP")
#chartmktcapars("PATA")
#chartmktcapars("RICH")
#chartmktcapars("SAMI")
#chartmktcapars("SUPV")
#chartmktcapars("TECO2")
#chartmktcapars("TGNO4")
#chartmktcapars("TGSU2")
#chartmktcapars("TRAN")
#chartmktcapars("TXAR")
#chartmktcapars("VALO")
#chartmktcapars("YPFD")

