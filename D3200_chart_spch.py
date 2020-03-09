
### FUNCION PAINT: DIBUJA SERIE DE PRECIOS CORRIENTES HISTORICOS EN ARS POR ACCION
def paint(ticker):
    ### GRAFICA LOS ULTIMOS N puntos del Precio de Cierre
    ### Si el indice esta en formato datetime, al correr este codigo las fechas aparecen en el eje x automaticamente
    global df
    #
    # Establece el rango del chart
    #
    rango = -1000 #debe ser un numero negativo
    #
    #if rango_str == int:
    #   rango = (rango_str + ":")    
    #elif rango_str == "todos":
    #   rango = ":"
    #else:
    #   rango = ":"
    #
    #
    #
    # Da la orden de graficar el rango (definido por los ultimos n puntos de la serie)
    #
    ax = df[['Cierre_del_dia']].iloc[rango:].plot(color ='k', linestyle = '-', figsize =(12,12), linewidth = 1 ) #18,12 es grande  #prueba
    #
    # Calcula las Moving Average y los suma a la df
    #
    df = pd.DataFrame(df.Cierre_del_dia)
    df["MA200"] = df.Cierre_del_dia.rolling(200).mean()
    df["MA100"] = df.Cierre_del_dia.rolling(100).mean()
    df["MA50"] = df.Cierre_del_dia.rolling(50).mean()
    df["MA25"] = df.Cierre_del_dia.rolling(25).mean()
    #
    # Activa las medias moviles o las desactiva
    #
    df['MA200'].iloc[rango:].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
    df['MA100'].iloc[rango:].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA50'].iloc[rango:].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #df['MA25'].iloc[rango:].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #
    # Define el titulo como una variable string
    title = "Serie de Precios Corrientes Historicos de " + ticker + " en ARS por Accion"
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
    y_label = "ARS por accion"
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
    location = original_source + "10_CHART_SPCH"
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
    plt.savefig(path)
    # 
    #plt.show() #lo desactivo solo para guardar todos los charts/ 
    #
    ##### ESTAS ULTIMAS DOS ES PARA QUE LOS CHARTS NO QUEDEN EN MEMORIA
    #
    # Clear axis . pero entonces no deja rastrear que figura o que funcion es la que no tiene close
    #plt.cla()
    #
    #
    #plt.close(fig)    
    #plt.close()
    #
    return



#################################
##FUNCION QUE DEBERIA HACER TODO CARGAR EN MEMORIA, ARREGLAR LA SERIE

def chart(ticker):
    loc = original_source + "SPCH"
    file_name_part1 = "SERIE_CORRIENTE_"
    file_name = file_name_part1 + ticker
    ext = ".xlsx"    
    open_file_spch(loc, file_name, ext)
    global df
    paint(ticker)
    return



#PRUEBA    
#chart("AGRO")
#chart("ALUA")
#MISSING chart("APBR")
#chart("AUSO")
#chart("BBAR")
#chart("BHIP")
#chart("BMA")
#chart("BOLT")
#chart("BPAT")
#chart("BRIO")
#chart("BYMA")
#chart("CADO")
#chart("CAPX")
#chart("CEPU")
#chart("CGPA2")
#chart("COME")
#chart("CRES")
#chart("CTIO")
#chart("CVH")
#chart("DGCU2")
#chart("EDN")
#chart("ESME")
#chart("FERR")
#chart("GCLA")
#chart("GGAL")
#chart("HARG")
#chart("INTR")
#chart("INVJ")
#chart("LEDE")
#chart("LOMA")
#chart("METR")
#chart("MIRG")
#chart("MOLA")
#chart("MOLI")
#chart("OEST")
#chart("PAMP")
#chart("PATA")
#chart("RICH")
#chart("SAMI")
#chart("SUPV")
#chart("TECO2")
#chart("TGNO4")
#chart("TGSU2")
#chart("TRAN")
#chart("TXAR")
#MISSING chart("TS")
#chart("VALO")
#chart("YPFD")
