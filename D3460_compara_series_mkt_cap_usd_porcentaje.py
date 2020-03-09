### FUNCION PAINT_MKT_CAP_USD: DIBUJA LA EVOLUCION DEL MKT CAP EN USD
def paint(ticker1, ticker2):
    ### GRAFICA LOS ULTIMOS N puntos del Market Cap en USD
    ### Si el indice esta en formato datetime, al correr este codigo las fechas aparecen en el eje x automaticamente
    #
    global df, df1, df2, df3, df4
    #
    ######## ABRE LA SERIE df2 con ticker 2
    #
    # Location jamas termina con una barra
    location = original_source + "MARKET_CAP_USD"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "MKT_CAP_USD_"
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
    open_file_mkt_cap_usd(location, ticker2, extension)
    #
    df2 = df
    #
    ######## ABRE LA SERIE df con ticker 1
    #
    # Location jamas termina con una barra
    location = original_source + "MARKET_CAP_USD"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "MKT_CAP_USD_"
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ticker1
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
    open_file_mkt_cap_usd(location, ticker1, extension)
    #
    df1 = df
    #
    ######################
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
    #####################################################################
    #
    #
    #
    #df1 ALUA
    df1.drop(df1.columns.difference(['Mkt_Cap_USD']), 1, inplace=True)
    #
    #df2 TXAR
    df2.drop(df2.columns.difference(['Mkt_Cap_USD']), 1, inplace=True)
    #
    df3=pd.merge(df1, df2, how='inner', left_index=True, right_index=True) # Agrega una columna a la derecha de
    #
    df3['pct1'] = (df3['Mkt_Cap_USD_x'] / df3['Mkt_Cap_USD_x'].shift(1))-1
    df3['Acc.Serie1_sum1'] = (df3['pct1'] +1)
    df3['Acc.Prod1'] = df3['Acc.Serie1_sum1'].cumprod(skipna = True)
    df3['Acc.Prod1'] = (df3['Acc.Prod1']*100)
    df3['Renta.Acc.1'] = df3['Acc.Prod1']-100
    #
    #
    df3['pct2'] = (df3['Mkt_Cap_USD_y'] / df3['Mkt_Cap_USD_y'].shift(1))-1
    df3['Acc.Serie2_sum1'] = (df3['pct2'] +1)
    df3['Acc.Prod2'] = df3['Acc.Serie2_sum1'].cumprod(skipna = True)
    df3['Acc.Prod2'] = (df3['Acc.Prod2']*100)
    df3['Renta.Acc.2'] = df3['Acc.Prod2']-100
    #
    df4 = df3
    #  
    #
    #
    #ax.plot(label = ticker1)
    # Agrega la otra serie al chart
    #    
    #
    #
    ########  PONE LABEL A LA SERIE
    #
    # Setea como eje a la Serie que nosotros queremos
    df3[ticker1] = df3['Renta.Acc.1'] #Porque solo me deja asignar el eje ax a una serie del dataframe, y luego no me deja cambiarle el nombre al label.
    ax = df3[[ticker1]].iloc[rango_inicial:rango_final].plot.line(x=None, label = ticker1, color ='r', linestyle = '-', figsize =(12,12), linewidth = 1 )
    #
    #
    # Agrega una Segunda Serie al eje 
    df3['Renta.Acc.2'].iloc[rango_inicial:rango_final].plot(ax=ax, label = ticker2, color ='b', linestyle = '-', linewidth = 1, ) #18,12 es grande
    #
    #
    #
    # Pone los labels del eje x de forma vertical
    plt.xticks(rotation='vertical')
    #
    #
    #
    # MEDIAS MOVILES
    #
    # Calcula las Moving Average y los suma a la df
    #
    #df["MA200"] = df.Mkt_Cap_USD.rolling(200).mean()
    #df["MA100"] = df.Mkt_Cap_USD.rolling(100).mean()
    #df["MA50"] = df.Mkt_Cap_USD.rolling(50).mean()
    #df["MA25"] = df.Mkt_Cap_USD.rolling(25).mean()
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
    title = "Comparacion de Rentabilidad Acumulada de " + ticker1 + " y de " + ticker2
    plt.title(title)
    #    
    # Situa la leyenda arriba a la izquierda (loc=2)
    plt.legend(loc=2)
    # Otra forma de poner la leyenda pero esta vez relacionada con el eje y1
    ax.legend(loc=2)
    # Add a legend que no parece funcionar
    #plt.legend('off')
    #
    # EJE X - HORIZONTAL
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
    # EJE Y - VERTICAL
    #
    #Define el label del eje y como una variable string
    y_label = "Rentabilidad Acumulada en %"
    #
    #Define el ylabel, y=1 estaria en el limite superior, y=0.50 estaria casi en el medio
    plt.ylabel(y_label, fontsize=9, x=0.10, y=0.50)
    #
    ###########################################################################################
    # ESTABLECE LOS MAXIMOS Y MINIMOS PARA EL EJE Y Y LA DISTANCIA ENTRE TICKS
    #
    # Establece el maximo punto para el eje y .. En serie porcentual 1400 seria 1400 %
    #y_eje = mpl.ticker.MultipleLocator(base=1400) # this locator puts ticks at regular intervals
    #ax.yaxis.set_major_locator(y_eje)
    #
    #
    if df3['Renta.Acc.2'].max() < df3['Renta.Acc.1'].max():
       ymax = df3['Renta.Acc.1'].max()
    else:
       ymax = df3['Renta.Acc.2'].max()
    #
    if df3['Renta.Acc.2'].min() < df3['Renta.Acc.1'].min():
       ymin = df3['Renta.Acc.2'].min()
    else:
       ymin = df3['Renta.Acc.1'].min()
    #
    #
    # Establece el minimo, maximo, y distancia entre ticks del eje y
    #el np.arange se lo usa para definir una lista de (minimo, maximo, distancia entre ticks)
    #plt.yticks(np.arange(round(ymin), round(ymax), 50.0))  #Este ejemplo setea el mininimo, maximo y 50 de distancia entre ticks
    plt.yticks(np.arange(-100, round(ymax), 50.0))
    #
    # Agrega el ytick = 0 en la lista de yticks del eje y
    plt.yticks(list(plt.yticks()[0]) + [0])
    #
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
    vals = ax.get_yticks()
    ax.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    #ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{y:,.0f}'))
    #
    # Define que el formato de los numeros del eje y sean con coma para separar los miles  
    #ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #
    #
    import matplotlib.dates as mdates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d '))
    #
    # AGREGA FOOTNOTE
    #plt.text(0.5, 0.5, "Fuente: BCRA, GCB CAPITAL", fontsize=12, horizontalalignment='center', verticalalignment='center')
    plt.annotate('Fuente: Bolsar, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    #
    #
    # Save Figure
    #
    # Location jamas termina con una barra
    location = original_source + "19_COMPARACIONES"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = ""
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ticker1 +"_" + ticker2
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


#paint("AGRO", "BOLT")

#paint("ALUA", "TXAR")

#paint("GGAL", "TXAR")