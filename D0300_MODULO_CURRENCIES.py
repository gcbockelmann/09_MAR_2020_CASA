
#NUEVO MODULO CURRENCIES

#### DESCARGA MATRIZ DE MERCADO AMERICANO

def arma_df_con_mercado_americano(ticker, initial_date, end_date=0):
    import pandas_datareader as web
    import datetime
    import requests
    session= requests.Session()
    session.verify = False # SSL   verification will be turned OFF, requests will give you an InsecureR questWarning
    global df
    #
    # SET INITIAL DATE
    begin_year = int(initial_date[0:4])
    begin_month = int(initial_date[6:7])
    begin_day =  int(initial_date[8:10])
    #
    # CHECK INITIAL DATE
    #print(begin_year)
    #print(begin_month)
    #print(begin_day)
    #
    # SET START POINT OF THE REQUEST
    start = datetime.datetime(begin_year, begin_month, begin_day)
    #
    if end_date == 0:
       end = datetime.date.today()
    else:
       # SET END DATE
       end_year = int(end_date[0:4])
       end_month = int(end_date[6:7])
       end_day =  int(end_date[8:10])
       #
       # CHECK END DATE
       #print(end_year)
       #print(end_month)
       #print(end_day)
       #
       end = datetime.datetime(end_year, end_month, end_day-1)
    #
    #
    df = web.DataReader(ticker, 'yahoo', start, end, session=session)
    return df


#arma_df_con_mercado_americano("GGAL", "2019-04-09", "2020-01-15")

#arma_df_con_mercado_americano("GGAL", "2019-04-09", 0)


def graba_matriz_mercado_americano(ticker, start_date, end_date, dst_path, part1_name, extension):
    americano = arma_df_con_mercado_americano(ticker, start_date, end_date)
    # Resetea el indice para formatear la matriz
    americano = americano.reset_index()
    #
    # RENOMBRA LAS COLUMNAS
    americano.rename(columns = {'Date':'Fecha'}, inplace=True)
    americano.rename(columns = {'Adj Close':'Adj_Close'}, inplace=True)
    #
    americano = americano.set_index("Fecha")
    #
    save_file_generico(americano, dst_path, part1_name, ticker, ".xlsx")

#graba_matriz_mercado_americano("GGAL", "2020-01-01", "2020-01-24",  original_source +"\INPUT",  "AMERICANO_", ".xlsx")



def update_mercado_americano(ticker, source_path_serie_historica, nombre_archivo_serie_historica, ext_archivo_serie_historica, source_path_serie_adicional, nombre_archivo_serie_adicional, ext_archivo_serie_adicional, output_path, nombre_output_part1, ext_archivo_output):
    global americano, ggal_adr, df
    #
    # Abre la serie nueva input
    open_excel(source_path_serie_adicional, nombre_archivo_serie_adicional, ext_archivo_serie_adicional)  
    americano = df.set_index("Fecha")
    #
    #Abre la serie historica
    open_excel(source_path_serie_historica, nombre_archivo_serie_historica, ext_archivo_serie_historica)
    serie_de_tiempo(df)
    #print(df.columns)
    #print(americano.columns)
    #
    if list(df.columns) == list(americano.columns):
       df = pd.concat([df,americano]).drop_duplicates()
       # 1. Reseteo el indice para poder operar sobre las columnas    
       df = df.reset_index()
       # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
       df = df.drop_duplicates(subset='Fecha', keep='last')
       # 3. Vuelvo a establecer la columna fecha como indice
       df = df.set_index('Fecha', inplace=False)
       df=df.sort_index()
    #
    # Listo para grabar
    save_file_generico(df, output_path, nombre_output_part1 , ticker , ext_archivo_output)
    #
    return
    
#update_mercado_americano("GGAL", original_source + "\SPCH_AMERICANO", ("AMERICANO_" + "GGAL"), ".xlsx", original_source + "\INPUT", "AMERICANO_" + "GGAL", ".xlsx", original_source + "OUTPUT\SPCH_AMERICANO", "AMERICANO_", ".xlsx")






#FALTA FUNCION DE SOBRE-ESCRIBIR SPCH_AMERICANO

def sobre_escribe_spch_americano(ticker, fecha_del_ultimo_dato_para_actualizar):
    #
    #
    filename = "AMERICANO_"+ticker+".xlsx"
    #
    complete_path = original_source +"/OUTPUT/SPCH_AMERICANO/"+filename
    #
    import os
    import shutil
    #
    exists = os.path.isfile(complete_path)
    if exists:
       open_file_spch(original_source +"\OUTPUT\SPCH_AMERICANO", "AMERICANO_"+ticker, ".xlsx")
    #
    #
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    if fecha_del_ultimo_dato_para_actualizar == b:
       old_path = original_source +"OUTPUT\SPCH_AMERICANO\\"+filename
       nuevo_path = original_source +"SPCH_AMERICANO\\"+filename
       newPath = shutil.copy(old_path, nuevo_path)
    else:
       print("no escribe")
    #     
    return


#sobre_escribe_spch_americano("GGAL", "2020-01-16")




def arma_ccl_equities(ticker):
    # ARMA GGAL_CCL
    df = open_excel(original_source + "\SPCH_AMERICANO", "AMERICANO_"+ticker, ".xlsx")
    df = serie_de_tiempo(df)
    adr = df
    adr['factor_de_conversion']=10
    #
    df = open_file_spch(original_source + "\SPCH", "SERIE_CORRIENTE_"+ ticker, ".xlsx")
    #
    #
    merge=pd.merge(adr, df, how='inner', left_index=True, right_index=True)  
    merge['tc_nominal'] = merge['Cierre_del_dia']*merge['factor_de_conversion'] / merge['Close']  # Genera y asigna una columna calculada a merge 
    # Pone el correcto nombre a la especie
    merge['Especie']= ("USDARS_CCL_"+ticker)
    #Arma un dataframe solo con las columnas que me interesan
    merge=merge[['tc_nominal','Especie']]
    # Renombra la matriz a df para poder grabarla
    df=merge
    #
    # GRABA EL ARCHIVO
    #
    location = original_source + "\OUTPUT\CURRENCIES"                                 
    filename = str("USDARS_CCL_"+ticker)     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()

#arma_ccl_equities("GGAL")




## SOBREESCRIBE EL CCL

def sobre_escribe_ccl(ticker, fecha_del_ultimo_dato_para_actualizar):
    #
    #
    filename = "USDARS_CCL_"+ ticker + ".xlsx"
    #
    complete_path = original_source +"/OUTPUT/CURRENCIES/" + filename
    #
    import os
    import shutil
    #
    exists = os.path.isfile(complete_path)
    if exists:
       open_file_spch(original_source +"\OUTPUT\CURRENCIES", "USDARS_CCL_"+ticker, ".xlsx")
    #
    #
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    if fecha_del_ultimo_dato_para_actualizar == b:
       old_path = original_source + ("\OUTPUT\CURRENCIES\\" + filename)
       nuevo_path = original_source + "CURRENCIES\\" + filename
       newPath = shutil.copy(old_path, nuevo_path)
    else:
       print("no escribe")
    #     
    return

#sobre_escribe_ccl("GGAL", "2020-01-16")

def actualiza_dolar_libre(ticker):
    global df
    #
    # ABRE LA SERIE ORIGINAL
    #
    df = open_excel(original_source + "\CURRENCIES","USDARS_LIBRE",".xlsx")
    df=serie_de_tiempo(df)
    #
    # BUSCA EL ULTIMO PUNTO DE LA SERIE ORIGINAL
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    #print (b)
    #
    serie_original = df
    #
    #
    # ABRE LA SERIE NUEVA
    #
    df=open_excel(original_source + "\CURRENCIES","USDARS_CCL_"+ticker,".xlsx")
    df=serie_de_tiempo(df)
    df = df[df.index>b]
    puntos_nuevos = df
    #
    # Cambia el nombre a la columna para que la especie vaya a parar a la columna FUENTE
    #
    puntos_nuevos.rename(columns={"Especie":"FUENTE"}, inplace=True)
    #
    #ARMA LA NUEVA MATRIZ
    #
    # #Se usa para poner en el mismo data frame apliar datos.
    #df=pd.concat([serie_original, puntos_nuevos]).drop_duplicates(subset='Fecha', keep='first')
    df=pd.concat([serie_original, puntos_nuevos])
    #
    df = df.sort_index()
    #
    df["Especie"]="USDARS_LIBRE"
    #
    # ELIMINACION DE DUPLICADOS
    #
    # Eliminacion de duplicados del indice
    #
    # 1. Reseteo el indice para poder operar sobre las columnas    
    df = df.reset_index()
    # 2. Ordena la serie en ascendente
    df = df.sort_values(by='Fecha', ascending=True)
    # 3. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
    df = df.drop_duplicates(subset='Fecha', keep='last')
    # 4. Vuelvo a establecer la columna fecha como indice
    df = df.set_index('Fecha', inplace=False)
    #
    ## GRABA EL ARCHIVO
    #
    location = original_source + "\OUTPUT\CURRENCIES"                                 
    filename = str("USDARS_LIBRE")     
    extension = ".xlsx"
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    print (path)  
    path_writer = pd.ExcelWriter(path)
    df.to_excel(path_writer, 'DataFrame')
    path_writer.save()

#actualiza_dolar_libre("GGAL")



def sobre_escribe_dolar_libre(fecha_del_ultimo_dato_para_actualizar):
    #
    #
    filename = "USDARS_LIBRE.xlsx"
    #
    complete_path = original_source +"/OUTPUT/CURRENCIES/"+filename
    #
    import os
    import shutil
    #
    exists = os.path.isfile(complete_path)
    if exists:
       open_file_spch(original_source +"\OUTPUT\CURRENCIES", "USDARS_LIBRE", ".xlsx")
    #
    #
    #
    df.tail(1).index # para buscar la ultima fecha de la serie
    intermedio = str(df.tail(1).index) # Transformamos en una variable string
    b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
    if fecha_del_ultimo_dato_para_actualizar == b:
       old_path = original_source +"/OUTPUT/CURRENCIES/"+filename
       nuevo_path = original_source +"/CURRENCIES/"+filename
       newPath = shutil.copy(old_path, nuevo_path)
    else:
       print("no escribe")
    #     
    return

#sobre_escribe_dolar_libre("2020-02-07")     



def corre_modulo_usd_libre(ticker_for_ccl, date):
    graba_matriz_mercado_americano(ticker_for_ccl, "2020-01-01", date,  original_source +"\INPUT",  "AMERICANO_", ".xlsx")
    update_mercado_americano(ticker_for_ccl, original_source + "\SPCH_AMERICANO", ("AMERICANO_" + ticker_for_ccl), ".xlsx", original_source + "\INPUT", "AMERICANO_" + ticker_for_ccl, ".xlsx", original_source + "OUTPUT\SPCH_AMERICANO", "AMERICANO_", ".xlsx")
    sobre_escribe_spch_americano(ticker_for_ccl, date)
    arma_ccl_equities("GGAL")
    sobre_escribe_ccl(ticker_for_ccl, date)
    actualiza_dolar_libre(ticker_for_ccl)
    sobre_escribe_dolar_libre(date) 
    return

#corre_modulo_usd_libre("GGAL", "2020-01-23")
