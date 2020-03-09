



def paint_index(ticker):
    ### GRAFICA LOS ULTIMOS 1000 puntos del Precio de Cierre del Indice
    ### Si el indice esta en formato datetime, al correr este codigo las fechas aparecen en el eje x automaticamente
    global df
    #
    #
    # Da la orden de graficar los ultimos 1000 puntos de la serie
    ax = df[['Cierre_del_dia']].iloc[-1000:].plot(color ='k', linestyle = '-', figsize =(12,12), linewidth = 1 ) #18,12 es grande
    #
    # Define el titulo como una variable string
    title = "Serie de Precios Corrientes Historicos de " + ticker + " en ARS"
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
    y_label = "En ARS"
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
    location = original_source + "16_CHART_INDEX"
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
    extension = "_2018-08-23"
    #
    # Path es el todo la linea para llegar al archivo
    path = location + slash + file_name + extension
    #print (path)
    #
    # Graba en formato png. Fijarse que no hay que poner la extension.
    # A Modo de Ejemplo seria: plt.savefig('C:\GCB_CAPITAL\myfig')
    plt.savefig(path)
    #
    plt.close()
    #
    # 
    plt.show() #lo desactivo solo para guardar todos los charts/ 
    # Save Transparent Figure
    #fig.savefig("foo.png") #, transparent=True)
    #

    return


#paint_index("^MERV")

#################################
##FUNCION QUE DEBERIA HACER TODO CARGAR EN MEMORIA, ARREGLAR LA SERIE

def chart_index(ticker):
    loc = original_source + "SPCH"
    file_name_part1 = "SERIE_CORRIENTE_"
    file_name = file_name_part1 + ticker
    ext = ".xlsx"    
    open_index_file_spch(loc, file_name, ext)
    global df
    paint_index(ticker)
    return


#chart_index("^MERV")








