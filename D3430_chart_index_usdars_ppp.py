

## FALTA

def paint_index_usdars_ppp(ticker):
    global df
    #
    # Da la orden de graficar todos los puntos de la serie
    ax = df[['Cierre_del_dia_USDPPP']].plot(color ='k', linestyle = '-', figsize =(12,12), linewidth = 1 ) #18,12 es grande
    #
    #
    # Calcula las Moving Average y los suma a la df
    #
    df["MA200"] = df.Cierre_del_dia_USDPPP.rolling(200).mean()
    df["MA100"] = df.Cierre_del_dia_USDPPP.rolling(100).mean()
    df["MA50"] = df.Cierre_del_dia_USDPPP.rolling(50).mean()
    df["MA25"] = df.Cierre_del_dia_USDPPP.rolling(25).mean()
    #
    # Activa las medias moviles o las desactiva
    #
    #df['MA200'].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
    #df['MA100'].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA50'].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA25'].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #
    #
    # Define el titulo como una variable string
    title = "Evolucion del Indice " + ticker + " en USDARS_PPP"
    plt.title(title)
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
    y_label = "En USDARS_PPP"
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
    location = original_source + "18_CHART_INDEX_USDARS_PPP"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "INDICE_"
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
    #plt.close()
    #
    # Graba en formato png. Fijarse que no hay que poner la extension.
    # A Modo de Ejemplo seria: plt.savefig('C:\GCB_CAPITAL\myfig')
    plt.savefig(path)
    plt.show()  # lo desactive para poder grabar todos los archivos
    return



#paint_index_usdars_ppp("^MERV")


#open_index_file_spch("C:\GCB_CAPITAL\INDICES_USD", "SERIE_CORRIENTE_^MERV", "_USD.xlsx")

def chart_index_usdars_ppp(ticker12):
    ### Esta funcion abre un archivo el archivo de excel correspondiente a un indice ticker y lo carga en la matriz df
    global df
    # Location jamas termina con una barra
    location = original_source + "INDICES_USDPPP"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "SERIE_CORRIENTE_"
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ticker12
    #
    # file_name es el total del nombre del archivo incluyendo al ticker que lo identifica                             
    file_name = file_name_parte1 + file_name_parte2     
    #
    # Extension es la extension del archivo
    extension = "_USDPPP.xlsx"
    #
    # Path es el todo la linea para llegar al archivo
    path = location + slash + file_name + extension
    #print (path)
    #
    open_index_file_spch(location, file_name, extension )
    #open_file_mkt_cap_usd(location, ticker5, extension)
    #    
    # Dibuja
    #
    paint_index_usdars_ppp(ticker12)
    #
    return

#chart_index_usdars_ppp("^MERV")
