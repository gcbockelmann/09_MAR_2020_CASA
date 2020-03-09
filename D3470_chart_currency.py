##FUNCION GRAFICA LA SERIE LARGA DEL MKT CAP EN USD
def paint_currency(ticker, puntos):
    ### GRAFICA LOS ULTIMOS N puntos del tipo de cambio
    ### Si el indice esta en formato datetime, al correr este codigo las fechas aparecen en el eje x automaticamente
    global df, cur
    #
    # ABRE EL DATAFRAME DE CURRENCIES
    #
    open_file_currency(ticker)
    #
    df = cur
    #
    #
    # VERIFICA SI LA SERIE ES UN TIPO DE CAMBIO REAL O NOMINAL
    if ticker == "USDARS_BCRA":  
       serie = "tc_nominal"
       tipo_de_cambio = "nominal"
    elif ticker == "USDARS_LIBRE":
       serie = "tc_nominal"
       tipo_de_cambio = "nominal"
    elif ticker == "USDARS_PPP":
       serie = "tc_real"
       tipo_de_cambio = "bilateral real"
    else:
       serie = "tc_nominal"
       tipo_de_cambio = "nominal"
    #
    #  Calcula las Moving Average y los suma a la df
    #
    if serie == "tc_nominal":
       df["MA200"] = df.tc_nominal.rolling(200).mean()
       df["MA100"] = df.tc_nominal.rolling(100).mean()
       df["MA50"] = df.tc_nominal.rolling(50).mean()
       df["MA25"] = df.tc_nominal.rolling(25).mean()
    elif serie == "tc_real":
       df["MA200"] = df.tc_real.rolling(200).mean()
       df["MA100"] = df.tc_real.rolling(100).mean()
       df["MA50"] = df.tc_real.rolling(50).mean()
       df["MA25"] = df.tc_real.rolling(25).mean()
    else:
       print ("Problema con la serie no es ni real ni nominal")
    #
    #
    # DEFINE EL RANGO DEL CHART
    # 
    puntos = -1*int(puntos)
    #
    #
    #Rango inicial. La serie puede identificarse como 0 (el primer dato de la serie) o como un numero negativo comenzando desde el final de la serie
    rango_inicial = puntos
    #
    #Rango final. La serie puede identificarse como 0 (el primer dato de la serie) o como un numero negativo comenzando desde el final de la serie
    # 0 es el final de la serie pero se debe completar ni con "" ni con 0
    rango_final = -1
    #
    #
    # GRAFICA
    #
    # Da la orden de graficar el rango
    ax = df[[serie]].iloc[rango_inicial:rango_final].plot(color ='k', linestyle = '-', figsize =(12,12), linewidth = 1 ) #18,12 es grande
    #
    #
    # Activa las medias moviles o las desactiva
    #
    df['MA200'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
    df['MA100'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA50'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA25'].iloc[rango_inicial:rango_final].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #
    #
    # Define el titulo como una variable string
    title = "Tipo de cambio " + tipo_de_cambio + " " + ticker
    plt.title(title)
    #    
    #    
    # Add a legend
    #
    #plt.legend('off')
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
    x_label = "Fecha"
    #
    #Define el xlabel, x=1 estaria en el limite inferior derecho, x=0.50 estaria casi en el medio
    plt.xlabel(x_label, fontsize=9, x=0.50, y=0.10)
    #
    #Define el label del eje y como una variable string
    y_label = "en ARS por USD"
    #
    #Define el ylabel, y=1 estaria en el limite superior, y=0.50 estaria casi en el medio
    plt.ylabel(y_label, fontsize=9, x=0.10, y=0.50)
    #
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
    # AGREGA FOOTNOTE
    #plt.text(0.5, 0.5, "Fuente: BCRA, GCB CAPITAL", fontsize=12, horizontalalignment='center', verticalalignment='center')
    plt.annotate('Fuente: BCRA, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    #
    #
    # PROBLEMA
    import matplotlib.dates as mdates
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d '))
    #
    # Save Figure
    #
    # Location jamas termina con una barra
    location = "C:\GCB_CAPITAL\CURRENCIES"
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
    plt.show()  # lo desactive para poder grabar todos los archivos
    return

#paint_currency("USDARS_LIBRE", "1000") #Ultimos 1000 puntos
#paint_currency("USDARS_LIBRE", "261") #Ultimo año
#paint_currency("USDARS_LIBRE", "0")  #Serie Historica

#paint_currency("USDARS_BCRA", "1000") #Ultimos 1000 puntos
#paint_currency("USDARS_BCRA", "261") #Ultimo año
#paint_currency("USDARS_BCRA", "0")  #Serie Historica

#open_file_currency("USDARS_PPP")
#paint_currency("USDARS_PPP", "1000") #Ultimos 1000 puntos
#paint_currency("USDARS_PPP", "261") #Ultimo año
#paint_currency("USDARS_PPP", "0")  #Serie Historica

