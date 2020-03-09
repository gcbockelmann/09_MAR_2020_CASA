#CHART SERIES DE DATAFRAME
def chart_series_de_dataframe(df, s, comienzo="", fin=""):
    #
    #
    ##### IMPORTA MODULOS
    #
    import datetime
    #
    #   
    ###### PREPARA EL DF ESPECIFICADO ################################################
    # toma el dataframe df
    # 
    #global df
    #
    #indice = df.index.values
    #indice = None
    #
    #if indice == 0:
    #   indice = None
    #else:
    #   indice = df.index.values
    #
    #
    #
    # Hace algo con el estilo del chart... que no estoy seguro 	que
    #plt.style.use('classic')
    #
    ######### IDENTIFICA LA SERIE A GRAFICAR
    #
    # Por medio de strings le indica cual es la serie a graficar
    str_serie_a_graficar = s
    #
    #
    # Establece la serie a graficar como una de las columnas del df
    #serie_a_graficar = df[str_serie_a_graficar]
    serie_a_graficar = s
    #
    ##############################################################################################
    ##### PREPARA LA FIGURA    ###################################################################
    ##############################################################################################
    #
    # ASIGNA UN NOMBRE A LA FIGURA 1
    # Le pone nombre a la figura 1 como fig1
    fig1 = plt.figure(1)
    #
    ######################################################################################
    #############################  TITULO DEL CHART     ##################################
    #####################################################################################
    #
    if 'Especie' in df:
       # Extrae el nombre del ticker del dataframe
       ticker = df['Especie'][-1]
    else: 
       # Asigna a ticker:
       ticker = "desconocido"
    #
    if serie_a_graficar == "Cierre_del_dia":
       titulo_de_figura = "Titulo de la Figura"
    elif serie_a_graficar == "Mkt_Cap_Close_ARS":
       titulo_de_figura = "Titulo de la Figura"
    elif serie_a_graficar == "Mkt_Cap_Close_USD":
       titulo_de_figura = "Titulo de la Figura"
    elif serie_a_graficar == "Mkt_Cap_Close_USD_PPP":
       titulo_de_figura = "Titulo de la Figura"
    elif serie_a_graficar == "diferencial":
       titulo_de_figura = "Diferencial"
    elif serie_a_graficar == "tc_nominal":
       titulo_de_figura = "Tipo de cambio nominal"
    elif serie_a_graficar == "tc_real":
       titulo_de_figura = "Tipo de cambio real"
    elif serie_a_graficar == "EV/EBITDA":
       titulo_de_figura = "Evolucion del EV/EBITDA"
    elif serie_a_graficar == "PE_ratio":
       titulo_de_figura = "Evolucion del PE_ratio"
    elif serie_a_graficar == "Rentabilidad_Acumulada_ARS":
       titulo_de_figura = "Titulo de la Figura"
    elif serie_a_graficar == "Rentabilidad_Acumulada_USD":
       titulo_de_figura = "Titulo de la Figura"
    elif serie_a_graficar == "Rentabilidad_Acumulada_USDPPP":
       titulo_de_figura = "Titulo de la Figura"
    else:
       titulo_de_figura = "Titulo de la Figura"
    #
    #fig1.suptitle('El_titulo', y=1.05)
    #fig1.suptitle('El_titulo de la figura')
    fig1.suptitle(titulo_de_figura)
    #
    if serie_a_graficar == "Cierre_del_dia":
       title = "Chart del precio de Cierre del dia de la accion de " + str(ticker)
    elif serie_a_graficar == "Mkt_Cap_Close_ARS":
       title = "Chart del Mkt Cap en M ARS de " + str(ticker)
    elif serie_a_graficar == "Mkt_Cap_Close_USD":
       title = "Chart del Mkt Cap en M USD de " + str(ticker)
    elif serie_a_graficar == "Mkt_Cap_Close_USD_PPP":
       title = "Chart del Mkt Cap en M USD_PPP de " + str(ticker)
    elif serie_a_graficar == "diferencial":
       title = "Chart del diferencial de " + str(ticker)
    elif serie_a_graficar == "tc_nominal":
       title = "Chart del Tipo de cambio nominal de " + str(ticker)
    elif serie_a_graficar == "tc_real":
       title = "Chart del Tipo de cambio real bilateral de " + str(ticker)
    elif serie_a_graficar == "EV/EBITDA":
       title = "Chart de Evolucion del EV/EBITDA de " + str(ticker)
    elif serie_a_graficar == "PE_ratio":
       title = "Chart de Evolucion del PE_ratio de " + str(ticker)
    elif serie_a_graficar == "PS_ratio":
       title = "Chart de Evolucion del PS_ratio de " + str(ticker)
    elif serie_a_graficar == "P/BVPS_ratio":
       title = "Chart de Evolucion del P/BVPS_ratio de " + str(ticker)
    elif serie_a_graficar == "Rentabilidad_Acumulada_ARS":
       title = "Chart de " + str(s) + " de " + str(ticker) 
    elif serie_a_graficar == "Rentabilidad_Acumulada_USD":
       title = "Chart de " + str(s) + " de " + str(ticker) 
    elif serie_a_graficar == "Rentabilidad_Acumulada_USDPPP":
       title = "Chart de " + str(s) + " de " + str(ticker) 
    else:
       title = "Chart desconocido "
    #
    # Define el titulo como una variable string
    #title = "Nivel de Atraso Cambiario USDARS vs USDARS_PPP"
    plt.title(title)
    #
    ############################################################################################
    ############################### OTRAS CUESTIONES ###########################################
    ############################################################################################
    # 
    # Cambia el tamanio de la figura
    # figsize=(width=6, hegith=6)
    #figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    from matplotlib.pyplot import figure 
    figure(num=1, figsize=(100, 200), dpi=80, facecolor='w', edgecolor='k') 
    #
    # ASIGNA UN NOMBRE A LOS SUBPLOTS DE LA FIGURA 1 EN ESTE CASO AX = CHART1
    # Asigna el nombre ax (axes) a la primer figura
    ax = fig1.add_subplot(1,1,1)
    #ax2 = fig1.add_subplot(2,1,2)
    #ax3 = fig1.add_subplot(3,1,3)
    # 
    ##############################################################################################
    ##### DEFINE LA CANTIDAD DE CHARTS QUE VA A TENER UNA FIGURA##################################
    ##############################################################################################
    #
    #
    # Esto diria que la figura 1, llama a todos los plots = axes_plots y va a tener 9 subplots, en 3 filas,  va a haber 3 por fila en 3 columnas.
    #fig1, axes_plots = plt.subplots(1,1) 
    #axes_plots[0,0].plot(df.index, df.values) 
    #
    #
    #
    ##############################################################################################
    ##### DEFINE EL RANGO DEL CHART                             ##################################
    ##############################################################################################
    #
    #El formato aceptado por el DataFrame es df['2018-01-04':'2018-01-06']
    #  
    # Asigna a la variable start la fecha de comienzo
    start = comienzo 
    # Transforma la fecha de start a formato datetime
    start_dt = pd.to_datetime(comienzo, format="%Y-%m-%d")
    #
    # Asigna a la variable end a la fecha de finalizacion
    end = fin
    # Transforma la fecha de finalizacion a formato datetime
    end_dt = pd.to_datetime(fin, format="%Y-%m-%d")
    #
    #
    ################################################################################
    ###                        MANDA A GRAFICAR LAS SERIES                       ###
    ################################################################################
    #
    ################################################################################
    ###              PONE NOMBRE DE LA SERIE PRINCIPAL EN LA LEYENDA      
    ################################################################################
    if serie_a_graficar == "Cierre_del_dia":
       label_s = "Cierre_del_dia de " + str(ticker)
    elif serie_a_graficar == "Mkt_Cap_Close_ARS":
       label_s = "Mkt_Cap_Close_ARS de " + str(ticker)
    elif serie_a_graficar == "Mkt_Cap_Close_USD":
       label_s = "Mkt_Cap_Close_USD de " + str(ticker)
    elif serie_a_graficar == "Mkt_Cap_Close_USD_PPP":
       label_s = "Mkt_Cap_Close_USD_PPP de " + str(ticker)
    elif serie_a_graficar == "diferencial":
       label_s = "Diferencial " + str(ticker)
    elif serie_a_graficar == "tc_nominal":
       label_s = "tc_nominal " + str(ticker)
    elif serie_a_graficar == "tc_real":
       label_s = "tc_real_bilateral " + str(ticker)
    elif serie_a_graficar == "EV/EBITDA":
       label_s = "Multiplo de EV/EBITDA de " + str(ticker)
    elif serie_a_graficar == "PE_ratio":
       label_s = "Multiplo de PE_ratio de " + str(ticker)
    elif serie_a_graficar == "PS_ratio":
       label_s = "Multiplo de PS_ratio de " + str(ticker)
    elif serie_a_graficar == "P/BVPS_ratio":
       label_s = "Multiplo de P/BVPS_ratio de " + str(ticker)
    elif serie_a_graficar == "Rentabilidad_Acumulada_ARS":
       label_s = "Rentabilidad Acumulada en % ARS de " + str(ticker)
    elif serie_a_graficar == "Rentabilidad_Acumulada_USD":
       label_s = "Rentabilidad Acumulada en % USD de " + str(ticker)
    elif serie_a_graficar == "Rentabilidad_Acumulada_USDPPP":
       label_s = "Rentabilidad Acumulada en % USD_PPP de " + str(ticker)
    else: 
       label_s = "label 1 - No indentificado"
    #
    if comienzo == "":
       if fin == "":
          # Caso similar a sin argumentos 
          # Ploteo ella serie principal con los datos de x e y
          if serie_a_graficar == "Rentabilidad_Acumulada_ARS":
             ax.plot(df.index, (df[serie_a_graficar]/100), label=label_s , color='midnightblue', linestyle= '-', linewidth=1)
          else:
             ax.plot(df.index, df[serie_a_graficar], label=label_s , color='midnightblue', linestyle= '-', linewidth=1)
          #
    else:
       # Para graficar solo un rango de fechas y que pueda ser de rango variable debo armar un dataframe
       # primero armo un dataframe para lo que quiero en el eje j
       data_y_serie_principal = df[serie_a_graficar][start_dt:end_dt]
       # y luego armo un dataframe para lo que quiero en el eje x
       data_x_serie_principal = df[serie_a_graficar][start_dt:end_dt].index
       # Ploteo la serie principal con los datos de x e y
       ax.plot(data_x_serie_principal, data_y_serie_principal, label=label_s, color='midnightblue', linestyle= '-', linewidth=1)
    #
    #
    #
    # Calcula las Moving Average y los suma a la df
    #
    if serie_a_graficar == "Rentabilidad_Acumulada_ARS":
       nuevo_df = pd.DataFrame(df[serie_a_graficar]) #esta linea estaba haciendo quilombo >>si funciona borrar esta linea
       nuevo_df["MA200"] = (df[serie_a_graficar]/100).rolling(200).mean()
       nuevo_df["MA100"] = (df[serie_a_graficar]/100).rolling(100).mean()
       nuevo_df["MA50"] = (df[serie_a_graficar]/100).rolling(50).mean()
       nuevo_df["MA25"] = (df[serie_a_graficar]/100).rolling(25).mean()
    else:
       nuevo_df = pd.DataFrame(df[serie_a_graficar]) #esta linea estaba haciendo quilombo >>si funciona borrar esta linea
       nuevo_df["MA200"] = df[serie_a_graficar].rolling(200).mean()
       nuevo_df["MA100"] = df[serie_a_graficar].rolling(100).mean()
       nuevo_df["MA50"] = df[serie_a_graficar].rolling(50).mean()
       nuevo_df["MA25"] = df[serie_a_graficar].rolling(25).mean()
    #
    # Activa las medias moviles o las desactiva
    #
    if comienzo == "":
       if fin == "":
          nuevo_df['MA200'].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
          nuevo_df['MA100'].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
          nuevo_df['MA50'].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
          nuevo_df['MA25'].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    else:
       nuevo_df['MA200'][start_dt:end_dt].plot(ax=ax, label ='MA200', color ='g', linestyle = '-', linewidth = 1, ) #18,12 es grande
       nuevo_df['MA100'][start_dt:end_dt].plot(ax=ax, label ='MA100', color ='r', linestyle = '-', linewidth = 1 ) #18,12 es grande
       nuevo_df['MA50'][start_dt:end_dt].plot(ax=ax, label ='MA50', color ='y', linestyle = '-', linewidth = 1 ) #18,12 es grande
       nuevo_df['MA25'][start_dt:end_dt].plot(ax=ax, label ='MA25', color ='m', linestyle = '-', linewidth = 1 ) #18,12 es grande
    #
    #
    #
    #
    #
    ################################################################################
    ##########################     LA LEYENDA       ################################
    ################################################################################
    #
    # Posicion de la leyenda
    # loc='best'
    # loc='upper left'
    # loc='upper center'
    # loc='upper right'
    # loc='lower left'
    # loc='lower center'
    # loc='lower right'
    # loc='right'
    # loc='center'
    # loc='left'
    # loc='center left'
    # loc='center right'
    #
    # Marco de la leyenda
    # frameon=True    # frameon=False elimina el marco de la leyenda
    # 
    # Leyenda Transparente
    # fancybox=True; fancybox=False
    # 
    # Leyenda Grado de Transparencia
    # framealpha=1 es totalmente opaca y 0 debe ser totalmente traslucida.
    #
    # Leyenda en 3D
    # shadow=True
    #
    # Leyenda con borde
    # borderpad=1
    # 
    # Numero de columnas que utiliza la leyenda
    # ncol=2    #exhibe los datos de la leyenda en 2 columnas
    # 
    # Tamanio del rectangulo de la leyenda y posicion >> #bbox_to_anchor(x, y, width, height)
    # bbox_to_anchor=(0.5, 1.00)     # x=(un numero entre 0 y 1) ; y=(un numero entre 0 y 1, siendo 0.9 muy arriba), la altura y luego el ancho
    # bbox_to_anchor=(0.5, 0.0, 0.5, 0.5)     
    #
    #Ejemplo:
    #ax.legend(loc='bottom left', frameon=True, fancybox=False, framealpha=1, shadow=True, borderpad=1, bbox_to_anchor=(0.5, 0.5, 0.5, 0.5), ncol=2) 
    #
    ax.legend(loc='upper left', frameon=True, fancybox=False, framealpha=1, shadow=True, borderpad=1, ncol=1) 
    #
    #
    #####################################################################3
    #
    #   PONE LINDOS LOS EJES
    # 
    # Define el margen de cuan pegados estan los labels entre si del eje x. cuanto mas pequeno empieza a ser neceseario mostrar mas detalle en los labels.
    plt.margins(0.1)
    #
    #Distancia desde el fondo del chart (corre la altura del eje x en el dibujo. Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.25)
    #
    #
    ####################################################################################################################
    # 
    #  ARREGLA LA GRILLA
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
    ###################################################################################################################
    #
    # FORMATO DE LOS NUMEROS DEL EJE Y - VERTICAL
    #
    # Minimo y maximo que puede alcanzar el eje
    plt.ylim=((-0.2, 1.2))
    #
    # Define que el formato de los numeros del eje y sean en porcentaje
    #vals = ax.get_yticks()
    #ax.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    #
    #
    # Calcula el maximo y el minimo de la serie
    #
    ymax = df[str_serie_a_graficar].max()
    #
    ymin = df[str_serie_a_graficar].min()
    #
    # Establece el minimo, maximo, y distancia entre ticks del eje y
    #el np.arange se lo usa para definir una lista de (minimo, maximo, distancia entre ticks)
    #plt.yticks(np.arange(round(ymin), round(ymax), 0.1))  #Este ejemplo setea el mininimo, maximo y 50 de distancia entre ticks
    #plt.yticks(np.arange(-0.2, round(ymax), step=0.1))
    #
    #
    ###############################################################################################################
    ########################################### TITULO DEL EJE Y  #################################################
    #############################################################################################################
    #
    if serie_a_graficar == "Cierre_del_dia":
       # Define el label del eje y
       y_label = "en ARS por accion"
       # Define que el formato de los numeros del eje y sean con coma para separar los miles  
       ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    elif serie_a_graficar == "Mkt_Cap_Close_ARS":
          # Define el label del eje y
          y_label = "Mkt Cap en M ARS"
          # Define que el formato de los numeros del eje y sean con coma para separar los miles  
          ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    elif serie_a_graficar == "Mkt_Cap_Close_USD":
       # Define el label del eje y
       y_label = "Mkt Cap en M USD"
       # Define que el formato de los numeros del eje y sean con coma para separar los miles  
       ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    elif serie_a_graficar == "Mkt_Cap_Close_USD_PPP":
       # Define el label del eje y
       y_label = "Mkt Cap en M USD_PPP"
       # Define que el formato de los numeros del eje y sean con coma para separar los miles  
       ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    elif serie_a_graficar == "diferencial":
        # Define el label del eje y
        y_label = "Diferencial en porcentaje de " + str(ticker)
        # Define que el formato de los numeros del eje y sean en porcentaje
        vals = ax.get_yticks()
        ax.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    elif serie_a_graficar == "tc_nominal":
        # Define el label del eje y
        y_label = "Tipo de cambio nominal " + str(ticker)
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    elif serie_a_graficar == "tc_real":
        # Define el label del eje y
        y_label = "Tipo de cambio real bilateral " + str(ticker)
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    elif serie_a_graficar == "EV/EBITDA":
        # Define el label del eje y
        y_label = "Multiplo de EV/EBITDA de " + str(ticker)
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.2f}'))
    elif serie_a_graficar == "PE_ratio":
        # Define el label del eje y
        y_label = "Multiplo de PE_ratio de " + str(ticker)
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.2f}'))
    elif serie_a_graficar == "PS_ratio":
        # Define el label del eje y
        y_label = "Multiplo de PS_ratio de " + str(ticker)
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.2f}'))
    elif serie_a_graficar == "P/BVPS_ratio":
        # Define el label del eje y
        y_label = "Multiplo de P/BVPS_ratio de " + str(ticker)
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.2f}'))
    elif serie_a_graficar == "Rentabilidad_Acumulada_ARS":
        # Define el label del eje y
        y_label = "Rentabilidad Acumulada en % ARS de " + str(ticker)
        # Define que el formato de los numeros del eje y sean en porcentaje
        vals = ax.get_yticks()
        ax.set_yticklabels(['%.2f%%' %i for i in vals]) 
    elif serie_a_graficar == "Rentabilidad_Acumulada_USD":
        # Define el label del eje y
        y_label = "Rentabilidad Acumulada en % USD de " + str(ticker)
        # Define que el formato de los numeros del eje y sean en porcentaje
        vals = ax.get_yticks()
        ax.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    elif serie_a_graficar == "Rentabilidad_Acumulada_USDPPP":
        # Define el label del eje y
        y_label = "Rentabilidad Acumulada en % USDPPP de " + str(ticker)
        # Define que el formato de los numeros del eje y sean en porcentaje
        vals = ax.get_yticks()
        ax.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    else: 
        # Define el label del eje y
        y_label = "ticker desconocido"
        # Define que el formato de los numeros del eje y sean con coma para separar los miles  
        ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #
    #Define el label del eje y como una variable string
    #y_label = "en ARS por USD"
    #
    #Define el ylabel, y=1 estaria en el limite superior, y=0.50 estaria casi en el medio
    plt.ylabel(y_label, fontsize=9, x=0.10, y=0.50)
    #
    ##################################################################################################################
    #
    #  FORMATO DEL EJE X - HORIZONTAL
    # 
    import matplotlib.dates as mdates
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #
    # Pone los labels del eje x de forma vertical
    plt.xticks(rotation='vertical')
    #
    #Define el label del eje x como una variable string
    x_label = "Fecha"
    #
    #Define el xlabel, x=1 estaria en el limite inferior derecho, x=0.50 estaria casi en el medio
    plt.xlabel(x_label, fontsize=9, x=0.50, y=0.10)
    #
    #
    ################################################################################################################
    #
    #   AGREGA FOOTNOTE
    #
    #plt.text(0.5, 0.5, "Fuente: BCRA, GCB CAPITAL", fontsize=12, horizontalalignment='center', verticalalignment='center')
    #
    #
    if serie_a_graficar == "Cierre_del_dia":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "Mkt_Cap_Close_ARS":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "Mkt_Cap_Close_USD":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "Mkt_Cap_Close_USD_PPP":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, Indec, US Bureau of Labor Statistics, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "diferencial":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, BCRA, Indec, US Bureau of Labor Statistics, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "tc_nominal":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: BCRA, Bolsar, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "tc_real":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: BCRA, Bolsar, Indec, US Bureau of Labor Statistics, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "EV/EBITDA":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "PE_ratio":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "PS_ratio":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    elif serie_a_graficar == "P/BVPS_ratio":
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, Presentaciones de la compania, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    else: 
       # Define la anotacion de la fuente (como nota al pie)
       plt.annotate('Fuente: Bolsar, GCB CAPITAL', (0,0), (-70, -100), xycoords='axes fraction', textcoords='offset points', va='top')
    #
    ########################################################################################################################
    #
    # Manda a dibujar
    plt.show()


#rentabilidad_total("AGRO", "2001-01-01")
#chart_series_de_dataframe(df , "Rentabilidad_Acumulada_ARS")
#chart_series_de_dataframe(df , "Rentabilidad_Acumulada_USD")
#chart_series_de_dataframe(df , "Rentabilidad_Acumulada_USDPPP")

#chart_series_de_dataframe(diferencial_usdars_ppp , "diferencial", "2012-01-04", "2019-09-13")
#chart_series_de_dataframe(diferencial_usdars_ppp , "diferencial")
#chart_series_de_dataframe(diferencial_usdars_ppp , "diferencial", "2004-01-04", "2019-09-13")
#chart_series_de_dataframe(diferencial_usdars_ppp , "diferencial", "2012-01-04", "2019-09-20")
#chart_series_de_dataframe(diferencial_usdars_ppp , "diferencial", "2004-01-04", "2019-09-20")
#df["2012-01-04":"2019-09-20"]
#df['USDARS_PPP']["2012-01-04":"2019-09-20"].plot()
#chart_series_de_dataframe(df , "PE_ratio", "2012-01-04", "2019-09-13")

#chart_series_de_dataframe(df, "USDARS_PPP", "2018-09-11", "2019-09-13")
#df.index["2012-01-04":"2019-09-20"]


def chart_accion(ticker, comienzo="", final=""):
    loc = original_source + "\ONLINE\SPCH"
    file_name_part1 = "SERIE_CORRIENTE_"
    file_name = file_name_part1 + ticker
    ext = ".xlsx"    
    open_file_spch(loc, file_name, ext)
    global df
    chart_series_de_dataframe(df , "Cierre_del_dia", comienzo, final)
    return

#chart_accion("AGRO", "2004-01-04", "2019-09-20")
#chart_accion("AGRO")

def chart_mkt_cap_ars(ticker, comienzo="", final=""):
    ### Esta funcion abre un archivo el archivo de excel mkt_cap_ars correspondiente a ese ticker y lo carga en la matriz df
    global df
    # Location jamas termina con una barra
    location = original_source + "ONLINE\MKT_CAP_ARS"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "MKT_CAP_ARS_"
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
    open_file_mkt_cap_ars(location, ticker, extension)
    #    
    # Dibuja
    #
    chart_series_de_dataframe(df , "Mkt_Cap_Close_ARS", comienzo, final)
    #
    return 

#chart_mkt_cap_ars("AGRO", "2004-01-04", "2019-09-20")
#chart_mkt_cap_ars("AGRO")

def chart_mkt_cap_usd(ticker, comienzo="", final=""):
    ### Esta funcion abre un archivo el archivo de excel mkt_cap_usd correspondiente a ese ticker y lo carga en la matriz df
    global df
    # Location jamas termina con una barra
    location = original_source + "ONLINE\MKT_CAP_USD"
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
    open_file_mkt_cap_usd(location, ticker, extension)
    #    
    # Dibuja
    #
    chart_series_de_dataframe(df , "Mkt_Cap_Close_USD", comienzo, final)
    #
    return

#chart_mkt_cap_usd("AGRO", "2004-01-04", "2019-09-20")
#chart_mkt_cap_usd("AGRO")


def chart_mkt_cap_usd_ppp(ticker, comienzo="", final=""):
    ### Esta funcion abre un archivo el archivo de excel mkt_cap_usd correspondiente a ese ticker y lo carga en la matriz df
    global df
    # Location jamas termina con una barra
    location = original_source + "ONLINE\MKT_CAP_USDPPP"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "MKT_CAP_USDPPP_"
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
    open_file_mkt_cap_usdppp(location, ticker, extension)
    #    
    # Dibuja
    #
    chart_series_de_dataframe(df , "Mkt_Cap_Close_USD_PPP", comienzo, final)
    #
    return

#chart_mkt_cap_usd_ppp("AGRO", "2004-01-04", "2019-09-20")
#chart_mkt_cap_usd_ppp("AGRO")
#chart_mkt_cap_usd_ppp("TXAR")



def chart_currency(ticker, comienzo="", final=""):
    ### Esta funcion ....
    global df, cur
    #
    # ABRE EL DATAFRAME DE CURRENCIES
    #
    # La funcion open_file_currency graba en la global cur la matriz de tipo de cambio
    #open_file_currency(ticker)
    #
    cur = open_excel(original_source + "\ONLINE", ticker, ".xlsx")
    cur = serie_de_tiempo(cur)
    #
    # Se copia la matriz cur a la matriz df para poer graficarla
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
    elif ticker == "USDARS_MEP":
       serie = "tc_nominal"
       tipo_de_cambio = "nominal"
    else:
       serie = "tc_nominal"
       tipo_de_cambio = "nominal"
    #
    # Dibuja
    #
    chart_series_de_dataframe(df, serie, comienzo, final)
    #
    return




#chart_currency("USDARS_LIBRE", "2004-01-04", "2020-02-11")
#chart_currency("USDARS_MEP", "2004-01-04", "2019-09-20")
#chart_currency("USDARS_BCRA", "2004-01-04", "2019-09-20")
#chart_currency("USDARS_PPP", "2004-01-04", "2020-02-10")

def chart_atraso_cambiario(ticker1, ticker2, comienzo="", final=""):
    ### Esta funcion abre un archivo de diferencial
    global df
    # Location jamas termina con una barra
    location = original_source + "CURRENCIES"
    #
    # Slash es la barra
    slash = str("//")
    #
    # Filename parte 1 es un nombre que le agrega el programa a los archivos
    file_name_parte1 = "DIFERENCIAL_" + ticker1 + "_" + ticker2
    #
    # Filename parte 2 es el ticker
    file_name_parte2 = ""
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
    open_excel(location, file_name_parte1, extension)
    df=df.set_index("Fecha")
    # Dibuja
    #
    chart_series_de_dataframe(df , "diferencial", comienzo, final)
    #
    return

#chart_atraso_cambiario("USDARS_PPP", "USDARS_LIBRE", "2002-01-01", "2020-02-10")
#chart_atraso_cambiario("USDARS_PPP", "USDARS_LIBRE", "2018-01-01", "2020-02-10")
#chart_atraso_cambiario("USDARS_PPP", "USDARS_LIBRE", "2019-01-01", "2020-02-10")