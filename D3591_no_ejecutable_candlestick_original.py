

#https://pythonprogramming.net/stock-data-manipulation-python-programming-for-finance/?completed=/handling-stock-data-graphing-python-programming-for-finance/

#https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/



import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')


open_file_spch("C:\GCB_CAPITAL\SPCH", "SERIE_CORRIENTE_AGRO", ".xlsx")

df['100ma'] = df['Cierre_del_dia'].rolling(window=100, min_periods=0).mean()
print(df.head())

# el primer tuple la x es la cantidad de rows desde abajo o achico el grafico de abajo hacia arriba a medida que lo aumento
# el primer tuple la y es la cantidad de columnas desde la derecha que voy a comprimir o achicar el grafico de derecha hacia la izquierda a medida que lo aumento

#grid size 6,1.. starting point... 0,0 the top corner.. rowspan how many rows 5...and how many columns... 1.

#ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

# Arma el eje del segundo chart de volumen, en formato barra.
# Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
# no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)


ax1.plot(df.index, df['Cierre_del_dia'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volumen_Nominal'])

plt.show()

########################### CANDLESTICK CHART
`
#resamplear la data diaria para que se vea

df_ohlc = df['Cierre_del_dia'].resample('10D').mean()
# si uno hace df.values obtendria todos los valores del dataframe pero sin los encabezados de las columnas ni el indice
#df.values

df_ohlc = df['Cierre_del_dia'].resample('10D').ohlc()
df_volume = df['Volumen_Nominal'].resample('10D').sum()
print (df_ohlc.head())

from mpl_finance import candlestick_ohlc
#from matplotlib.finance import candlestick_ohlc

import matplotlib.dates as mdates
#matplotlib no usa datetime dates por alguna razon.

#el ohlc no quiere ohlc sino que quiere fechas en formato mdates y luego ohlc.
df_ohlc.reset_index(inplace=True)
print(df_ohlc.head())
#Ahora necesitamos convertirlos a mdates.
#we are doing a fancy mapping of any function. We are not trying to pass any parameters,  
# date2num (our timedate number )
# to a silly number mdate
df_ohlc['Fecha'] = df_ohlc['Fecha'].map(mdates.date2num)
# veamos como quedo.. la columna fecha deberia quedar en numeros.
print(df_ohlc.head())

#Ahora vamos a plotear
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

# Arma el eje del segundo chart de volumen, en formato barra.
# Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
# no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
#xaxis_date() va a tomar los mdates numbers y los tranforma a bellas fechas.
ax1.xaxis_date()


########################### CANDLESTICK CHART #### PRUEBA

df_ohlc  = pd.DataFrame()
df_ohlc['open'] = df['Apertura']
df_ohlc['high'] = df['Maximo']
df_ohlc['low'] = df['Minimo']
df_ohlc['close'] = df['Cierre_del_dia']

df_volume = df['Volumen_Nominal']
print (df_ohlc.head())

from mpl_finance import candlestick_ohlc
#from matplotlib.finance import candlestick_ohlc

import matplotlib.dates as mdates
#matplotlib no usa datetime dates por alguna razon.

#el ohlc no quiere ohlc sino que quiere fechas en formato mdates y luego ohlc.
df_ohlc.reset_index(inplace=True)
print(df_ohlc.head())
#Ahora necesitamos convertirlos a mdates.
#we are doing a fancy mapping of any function. We are not trying to pass any parameters,  
# date2num (our timedate number )
# to a silly number mdate
df_ohlc['Fecha'] = df_ohlc['Fecha'].map(mdates.date2num)
# veamos como quedo.. la columna fecha deberia quedar en numeros.
print(df_ohlc.head())

#Ahora vamos a plotear
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)

# Arma el eje del segundo chart de volumen, en formato barra.
# Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
# no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
#xaxis_date() va a tomar los mdates numbers y los tranforma a bellas fechas.
ax1.xaxis_date()

#luego vamos a decirle que grafique candlestick, en que eje, y cual es la data. Width = 2 es que tan anchas las barras de las velas.
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup = 'g' )

#what and then between what, df.values and then zero . Esto va a completar. x es df.volume.index.map(mdates.date2num)  y es
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, color ='midnightblue')

plt.show()


#### FUNCION CHART CANDLESTICK

def chart_candlestick(ticker):
    """ Chartea en formato candlestick"""
    """ ... """
    ######## IMPORTA MODuLOS
    #
    from mpl_finance import candlestick_ohlc
    #from matplotlib.finance import candlestick_ohlc
    #
    #matplotlib no usa datetime dates por alguna razon.
    import matplotlib.dates as mdates
    #
    import matplotlib.ticker as mticker
    #
    ####### PREPARA DATAFRAMES DE LA INFORMACION A GRAFICAR
    #
    df_ohlc  = pd.DataFrame()
    df_ohlc['open'] = df['Apertura'] 
    df_ohlc['high'] = df['Maximo']
    df_ohlc['low'] = df['Minimo']
    df_ohlc['close'] = df['Cierre_del_dia']
    df_ohlc.reset_index(inplace=True)
    #
    #Ahora necesitamos convertirlos a mdates.
    #we are doing a fancy mapping of any function. We are not trying to pass any parameters,  
    # date2num (our timedate number )
    # to a silly number mdate
    df_ohlc['Fecha'] = df_ohlc['Fecha'].map(mdates.date2num)
    #
    # Prepara el dataframe de volumen
    df_volume = df['Volumen_Nominal']
    #print (df_ohlc.head())
    #
    ### PREPARA LOS CHARTS
    #
    #Le pone nombre a la figura 1 como fig1
    fig1 = plt.figure(1)
    #fig1.suptitle('El_titulo', y=1.05)
    fig1.suptitle('El_titulo')
    #
    ##### DEFINE LA CANTIDAD DE CHARTS QUE VA A TENER UNA FIGURA
    #
    # Esto diria que la figura 1, llama a todos los plots = axes_plots y va a tener 9 subplots, en 3 filas,  va a haber 3 por fila en 3 columnas.
    #fig1, axes_plots = plt.subplots(3,3) 
    #axes_plots[0,0].plot(df.index, df.values) 
    #
    ### PRIMER CHART DE CANDLESTICK 
    #
    # Agrego un subplot que se llama ax1
    #
    # En el primer parentesis el numero de rows luego el numero de columnas, y luego el numero de plot.
    # con esto ya le estoy diciendo a figura 1 que va a tener 2 charts en una sola columna, y este seria el primero.
    # Arma el primer cuadro que va a tener los precios
    ax1 = fig1.add_subplot(2, 1, 1)
    #
    ax1.set_title('one')
    ax1.set_ylabel('y-axis') 
    #
    #ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    #
    #xaxis_date() va a tomar los mdates numbers y los tranforma a bellas fechas.
    ax1.xaxis_date()
    #
    #luego vamos a decirle que grafique candlestick, en que eje, y cual es la data. Width = 2 es que tan anchas las barras de las velas.
    candlestick_ohlc(ax1, df_ohlc.values, width=0.4, colorup = 'g', colordown = 'r' )
    #
    #
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(0)
    #
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #
    # Se puede especificar la cantidad de labels que queremos ver
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #
    ax1.grid(True)
    #
    #### SEGUNDO CHART DE VOLUMEN
    #
    # Arma el segundo cuadro(Axes) de volumen, en formato barra.
    ax2 = fig1.add_subplot(2, 1, 2) 
    # Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
    # no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    #
    ax2.set_title('one')
    ax2.set_ylabel('y-axis') 
    ax2.set_xlabel('x-axis')     
    #
    # Rellene el eje de volumen pintando
    #what and then between what, df.values and then zero . Esto va a completar. x es df.volume.index.map(mdates.date2num)  y es
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, color ='midnightblue')
    #
    #
    # 
    #
    #
    fig1.tight_layout()
    #
    plt.show()
    
# muy buen video
https://www.youtube.com/watch?v=VLldcD-QR4Q





chart_candlestick("AGRO")


def chart_candlestick_spch(ticker):
    """ Chartea en formato candlestick"""
    """ ... """
    ######## IMPORTA MODuLOS
    #
    from mpl_finance import candlestick_ohlc
    #from matplotlib.finance import candlestick_ohlc
    #
    #matplotlib no usa datetime dates por alguna razon.
    import matplotlib.dates as mdates
    #
    import matplotlib.ticker as mticker
    #
    ############### CARGA EL DATAFRAME DEL TICKER
    #
    global df
    loc = "C:\GCB_CAPITAL\SPCH"
    file_name_part1 = "SERIE_CORRIENTE_"
    file_name = file_name_part1 + ticker
    ext = ".xlsx"    
    open_file_spch(loc, file_name, ext)
    #
    #
    #
    ####### PREPARA DATAFRAMES DE LA INFORMACION A GRAFICAR
    #
    df_ohlc  = pd.DataFrame()
    df_ohlc['open'] = df['Apertura'] 
    df_ohlc['high'] = df['Maximo']
    df_ohlc['low'] = df['Minimo']
    df_ohlc['close'] = df['Cierre_del_dia']
    df_ohlc.reset_index(inplace=True)
    #
    #Ahora necesitamos convertirlos a mdates.
    #we are doing a fancy mapping of any function. We are not trying to pass any parameters,  
    # date2num (our timedate number )
    # to a silly number mdate
    df_ohlc['Fecha'] = df_ohlc['Fecha'].map(mdates.date2num)
    #
    # Prepara el dataframe de volumen
    df_volume = df['Volumen_Nominal']
    #print (df_ohlc.head())
    #
    ### PREPARA LOS CHARTS
    #
    #Le pone nombre a la figura 1 como fig1
    fig1 = plt.figure(1)
    #fig1.suptitle('El_titulo', y=1.05)
    fig1.suptitle('Candlestick chart de la Serie de Precios Corrientes de ' + str(ticker))
    #
    # change figure size
    # figsize=(width=6, height=6)
    #fig1 = plt.figure(figsize=(6, 6))
    #
    ##### DEFINE LA CANTIDAD DE CHARTS QUE VA A TENER UNA FIGURA
    #
    # Esto diria que la figura 1, llama a todos los plots = axes_plots y va a tener 9 subplots, en 3 filas,  va a haber 3 por fila en 3 columnas.
    #fig1, axes_plots = plt.subplots(2,1) 
    #axes_plots[0,0].plot(df.index, df.values) 
    #
    #
    # Otra forma es especificarlo directamente creando los charts usando subplot2grid
    # (rows by columns), (row location, column location)
    # chart1= plt.subplot2grid((3,3), (0,0)) # Crea una grilla de 3x3 = 9 charts y luego asigna chart1 a la posicion 0,0 de la grilla.
    ## PRIMER CHART DE CANDLESTICK 
    #
    # Agrego un subplot que se llama ax1
    #
    # En el primer parentesis el numero de rows luego el numero de columnas, y luego el numero de plot.
    # con esto ya le estoy diciendo a figura 1 que va a tener 2 charts en una sola columna, y este seria el primero.
    # Arma el primer cuadro que va a tener los precios
    #ax1 = fig1.add_subplot(2, 1, 1)
    #
    ax1 = plt.subplot2grid((2,1), (0,0))
    #
    ax1.set_title('Evolucion del Precio por accion en ARS')
    ax1.set_ylabel('Precio por accion en ARS') 
    ax1.set_xlabel('Fecha')  
    #
    #ax1 = plt.subplot2grid((2,1), (0,0), rowspan=5, colspan=1)
    #
    #
    #xaxis_date() va a tomar los mdates numbers y los tranforma a bellas fechas.
    ax1.xaxis_date()
    #
    #luego vamos a decirle que grafique candlestick, en que eje, y cual es la data. Width = 2 es que tan anchas las barras de las velas.
    candlestick_ohlc(ax1, df_ohlc.values, width=0.4, colorup = 'g', colordown = 'r' )
    #
    #
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(0)
    #
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #
    # Se puede especificar la cantidad de labels que queremos ver
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #
    ax1.grid(True)
    #
    #### SEGUNDO CHART DE VOLUMEN
    #
    # Arma el segundo cuadro(Axes) de volumen, en formato barra.
    #ax2 = fig1.add_subplot(2, 1, 2) 
    # Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
    # no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
    #ax2 = plt.subplot2grid((2,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
    #
    ax2.set_title('Volumen Nominal en cantidad de acciones')
    ax2.set_ylabel('Cantidad de acciones') 
    ax2.set_xlabel('Fecha')     
    #
    # Define que el formato de los numeros del eje y sean con coma para separar los miles  
    ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #
    # Rellene el eje de volumen pintando
    #what and then between what, df.values and then zero . Esto va a completar. x es df.volume.index.map(mdates.date2num)  y es
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, color ='midnightblue')
    #
    #
    ###### DEFINE EL TAMANIO DE LOS GRAFICOS 
    #
    # Si se especifica tamanios a los labels ticks me parece que rompe con el tight layout.
    set_size(8,8)
    #
    #fig1.tight_layout()
    #
    #
    #
    #
    ###### MAXIMIZA LA VENTANA DE LA FIGURA
    #
    # Maximize the window of the chart
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    #
    #
    #
    plt.show()


chart_candlestick_spch("AGRO")
chart_candlestick_spch("ALUA")
chart_candlestick_spch("TXAR")



####################################
import matplotlib.pyplot as plt

def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

fig, ax=plt.subplots()

#ax.plot([1,3,2])

set_size(2,5)

plt.show()

#################################################################################
####
######
###

def chart_candlestick_mkt_cap_usd(ticker):
    """ Chartea en formato candlestick"""
    """ ... """
    ######## IMPORTA MODuLOS
    #
    from mpl_finance import candlestick_ohlc
    #from matplotlib.finance import candlestick_ohlc
    #
    #matplotlib no usa datetime dates por alguna razon.
    import matplotlib.dates as mdates
    #
    import matplotlib.ticker as mticker
    #
    ############### CARGA EL DATAFRAME DEL TICKER
    #
    global df
    #
    # Location jamas termina con una barra
    location = "C:\GCB_CAPITAL\MARKET_CAP_USD"
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
    #
    ####### PREPARA DATAFRAMES DE LA INFORMACION A GRAFICAR
    #
    df_ohlc  = pd.DataFrame()
    df_ohlc['open'] = df['Mkt_Cap_Open_USD'] 
    df_ohlc['high'] = df['Mkt_Cap_Max_USD']
    df_ohlc['low'] = df['Mkt_Cap_Min_USD']
    df_ohlc['close'] = df['Mkt_Cap_Close_USD']
    df_ohlc.reset_index(inplace=True)
    #
    #Ahora necesitamos convertirlos a mdates.
    #we are doing a fancy mapping of any function. We are not trying to pass any parameters,  
    # date2num (our timedate number )
    # to a silly number mdate
    df_ohlc['Fecha'] = df_ohlc['Fecha'].map(mdates.date2num)
    #
    # Prepara el dataframe de volumen
    df_volume = df['Volumen_%_Capital']
    #print (df_ohlc.head())
    #
    ### PREPARA LOS CHARTS
    #
    #Le pone nombre a la figura 1 como fig1
    fig1 = plt.figure(1)
    #fig1.suptitle('El_titulo', y=1.05)
    fig1.suptitle('Candlestick chart del Mkt Cap en USD de ' + str(ticker))
    #
    # change figure size
    # figsize=(width=6, height=6)
    #fig1 = plt.figure(figsize=(6, 6))
    #
    ##### DEFINE LA CANTIDAD DE CHARTS QUE VA A TENER UNA FIGURA
    #
    # Esto diria que la figura 1, llama a todos los plots = axes_plots y va a tener 9 subplots, en 3 filas,  va a haber 3 por fila en 3 columnas.
    #fig1, axes_plots = plt.subplots(2,1) 
    #axes_plots[0,0].plot(df.index, df.values) 
    #
    #
    # Otra forma es especificarlo directamente creando los charts usando subplot2grid
    # (rows by columns), (row location, column location)
    # chart1= plt.subplot2grid((3,3), (0,0)) # Crea una grilla de 3x3 = 9 charts y luego asigna chart1 a la posicion 0,0 de la grilla.
    #
    ## PRIMER CHART DE CANDLESTICK 
    #
    # Agrego un subplot que se llama ax1
    #
    # En el primer parentesis el numero de rows luego el numero de columnas, y luego el numero de plot.
    # con esto ya le estoy diciendo a figura 1 que va a tener 2 charts en una sola columna, y este seria el primero.
    # Arma el primer cuadro que va a tener los precios
    #ax1 = fig1.add_subplot(2, 1, 1)
    #
    ax1 = plt.subplot2grid((2,1), (0,0))
    #
    ax1.set_title('Evolucion del Mkt Cap en M USD')
    ax1.set_ylabel('Mkt Cap en M USD') 
    ax1.set_xlabel('Fecha')  
    #
    #ax1 = plt.subplot2grid((2,1), (0,0), rowspan=5, colspan=1)
    #
    #
    #xaxis_date() va a tomar los mdates numbers y los tranforma a bellas fechas.
    ax1.xaxis_date()
    #
    #luego vamos a decirle que grafique candlestick, en que eje, y cual es la data. Width = 2 es que tan anchas las barras de las velas.
    candlestick_ohlc(ax1, df_ohlc.values, width=0.4, colorup = 'g', colordown = 'r' )
    #
    #
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(0)
    #
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #
    # Se puede especificar la cantidad de labels que queremos ver
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #
    ax1.grid(True)
    #
    #### SEGUNDO CHART DE VOLUMEN
    #
    # Arma el segundo cuadro(Axes) de volumen, en formato barra.
    #ax2 = fig1.add_subplot(2, 1, 2) 
    # Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
    # no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
    #ax2 = plt.subplot2grid((2,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
    #
    ax2.set_title('Volumen como % del Capital')
    ax2.set_ylabel('Volumen como % del Capital') 
    ax2.set_xlabel('Fecha')     
    #
    # Define que el formato de los numeros del eje y sean con % 
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    #
    #
    # Define que el formato de los numeros del eje y sean con coma para separar los miles  
    #ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #
    # Rellene el eje de volumen pintando
    #what and then between what, df.values and then zero . Esto va a completar. x es df.volume.index.map(mdates.date2num)  y es
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, color ='midnightblue')
    #
    # Activa la grilla en el chart 2
    ax2.grid(True)
    #
    ###### DEFINE EL TAMANIO DE LOS GRAFICOS 
    #
    # Si se especifica tamanios a los labels ticks me parece que rompe con el tight layout.
    set_size(8,8)
    #
    #fig1.tight_layout()
    #
    #
    #
    #
    ###### MAXIMIZA LA VENTANA DE LA FIGURA
    #
    # Maximize the window of the chart
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    #
    #
    #
    plt.show()


chart_candlestick_mkt_cap_usd("AGRO")
chart_candlestick_mkt_cap_usd("ALUA")
chart_candlestick_mkt_cap_usd("TXAR")


#################################################################################
####
######
###

def chart_candlestick_mkt_cap_usd_ppp(ticker):
    """ Chartea en formato candlestick"""
    """ ... """
    ######## IMPORTA MODuLOS
    #
    from mpl_finance import candlestick_ohlc
    #from matplotlib.finance import candlestick_ohlc
    #
    #matplotlib no usa datetime dates por alguna razon.
    import matplotlib.dates as mdates
    #
    import matplotlib.ticker as mticker
    #
    ############### CARGA EL DATAFRAME DEL TICKER
    #
    global df
    # Location jamas termina con una barra
    location = "C:\GCB_CAPITAL\MARKET_CAP_USDPPP"
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
    #
    ####### PREPARA DATAFRAMES DE LA INFORMACION A GRAFICAR
    #
    df_ohlc  = pd.DataFrame()
    df_ohlc['open'] = df['Mkt_Cap_Open_USD_PPP'] 
    df_ohlc['high'] = df['Mkt_Cap_Max_USD_PPP']
    df_ohlc['low'] = df['Mkt_Cap_Min_USD_PPP']
    df_ohlc['close'] = df['Mkt_Cap_Close_USD_PPP']
    df_ohlc.reset_index(inplace=True)
    #
    #Ahora necesitamos convertirlos a mdates.
    #we are doing a fancy mapping of any function. We are not trying to pass any parameters,  
    # date2num (our timedate number )
    # to a silly number mdate
    df_ohlc['Fecha'] = df_ohlc['Fecha'].map(mdates.date2num)
    #
    # Prepara el dataframe de volumen
    df_volume = df['Volumen_%_Capital']
    #print (df_ohlc.head())
    #
    ### PREPARA LOS CHARTS
    #
    #Le pone nombre a la figura 1 como fig1
    fig1 = plt.figure(1)
    #fig1.suptitle('El_titulo', y=1.05)
    fig1.suptitle('Candlestick chart del Mkt Cap en USD_PPP de ' + str(ticker))
    #
    # change figure size
    # figsize=(width=6, height=6)
    #fig1 = plt.figure(figsize=(6, 6))
    #
    ##### DEFINE LA CANTIDAD DE CHARTS QUE VA A TENER UNA FIGURA
    #
    # Esto diria que la figura 1, llama a todos los plots = axes_plots y va a tener 9 subplots, en 3 filas,  va a haber 3 por fila en 3 columnas.
    #fig1, axes_plots = plt.subplots(2,1) 
    #axes_plots[0,0].plot(df.index, df.values) 
    #
    #
    # Otra forma es especificarlo directamente creando los charts usando subplot2grid
    # (rows by columns), (row location, column location)
    # chart1= plt.subplot2grid((3,3), (0,0)) # Crea una grilla de 3x3 = 9 charts y luego asigna chart1 a la posicion 0,0 de la grilla.
    #
    ## PRIMER CHART DE CANDLESTICK 
    #
    # Agrego un subplot que se llama ax1
    #
    # En el primer parentesis el numero de rows luego el numero de columnas, y luego el numero de plot.
    # con esto ya le estoy diciendo a figura 1 que va a tener 2 charts en una sola columna, y este seria el primero.
    # Arma el primer cuadro que va a tener los precios
    #ax1 = fig1.add_subplot(2, 1, 1)
    #
    ax1 = plt.subplot2grid((2,1), (0,0))
    #
    ax1.set_title('Evolucion del Mkt Cap en M USD_PPP')
    ax1.set_ylabel('Mkt Cap en M USD_PPP') 
    ax1.set_xlabel('Fecha')  
    #
    #ax1 = plt.subplot2grid((2,1), (0,0), rowspan=5, colspan=1)
    #
    #
    #xaxis_date() va a tomar los mdates numbers y los tranforma a bellas fechas.
    ax1.xaxis_date()
    #
    #luego vamos a decirle que grafique candlestick, en que eje, y cual es la data. Width = 2 es que tan anchas las barras de las velas.
    candlestick_ohlc(ax1, df_ohlc.values, width=0.4, colorup = 'g', colordown = 'r' )
    #
    #
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(0)
    #
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    #
    # Se puede especificar la cantidad de labels que queremos ver
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    #
    ax1.grid(True)
    #
    #### SEGUNDO CHART DE VOLUMEN
    #
    # Arma el segundo cuadro(Axes) de volumen, en formato barra.
    #ax2 = fig1.add_subplot(2, 1, 2) 
    # Para hacer que cuando hagamos zoom en el chart de precio, tambien el volumen haga zoom, se debe poner sharex =ax1
    # no significa que compartan el eje sino que comparten la informacion sobre el zoom como que estan alineados.
    #ax2 = plt.subplot2grid((2,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
    ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)
    #
    ax2.set_title('Volumen como % del Capital')
    ax2.set_ylabel('Volumen como % del Capital') 
    ax2.set_xlabel('Fecha')     
    #
    # Define que el formato de los numeros del eje y sean con % 
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['%1.2f%%' %i for i in vals]) 
    #
    #
    # Define que el formato de los numeros del eje y sean con coma para separar los miles  
    #ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
    #
    # Rellene el eje de volumen pintando
    #what and then between what, df.values and then zero . Esto va a completar. x es df.volume.index.map(mdates.date2num)  y es
    ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, color ='midnightblue')
    #
    # Activa la grilla en el chart 2
    ax2.grid(True)
    #
    ###### DEFINE EL TAMANIO DE LOS GRAFICOS 
    #
    # Si se especifica tamanios a los labels ticks me parece que rompe con el tight layout.
    set_size(8,8)
    #
    #fig1.tight_layout()
    #
    #
    #
    #
    ###### MAXIMIZA LA VENTANA DE LA FIGURA
    #
    # Maximize the window of the chart
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    #
    #
    #
    plt.show()


chart_candlestick_mkt_cap_usd_ppp("AGRO")
chart_candlestick_mkt_cap_usd_ppp("ALUA")
chart_candlestick_mkt_cap_usd_ppp("TXAR")