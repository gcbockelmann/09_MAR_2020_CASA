


#open_index_file_spch("C:\GCB_CAPITAL\INDICES_USD", "SERIE_CORRIENTE_^MERV", "_USD.xlsx")

def update_index_usdppp(ticker):
    global df, cur   
    # Carga la matriz de USDARS_PPP
    #
    cur = open_excel(original_source + "\CURRENCIES", "USDARS_PPP", ".xlsx")
    cur = df
    cur = serie_de_tiempo(cur)
    #
    # Crea una matriz solo con la columna tc_real
    cur = cur[["tc_real"]]
    #
    # OBSOLETO DESDE QUE CREE LA MATRIZ SOLO CON LA COLUMNA tc_real
    #cur.columns = ['tc_real', 'W', 'X', 'Y', 'Especie']
    # Drop the column with label 'A'
    #if 'W' in cur:
    #   cur.drop('W', axis=1, inplace=True)
    #if 'X' in cur:
    #   cur.drop('X', axis=1, inplace=True)
    #if 'Y' in cur:
    #   cur.drop('Y', axis=1, inplace=True)
    #if 'Especie' in cur:
    #   cur.drop('Especie', axis=1, inplace=True)
    #cur.head()
    #
    # Abre la matriz de indices
    open_index_file_spch(original_source + "\INDICES_USD", "SERIE_CORRIENTE_^MERV", "_USD.xlsx")
    #
    # Proceso
    #
    merge=pd.merge(df, cur, how='inner', left_index=True, right_index=True) 
    #
    #
    ######## PASA EL RESTO DE LAS COLUMNAS A USD_PPP
    #
    merge['Apertura_USDPPP'] = merge['Apertura'] / merge['tc_real']  # Genera y asigna una columna calculada a merge
    merge['Minimo_USDPPP'] = merge['Minimo'] / merge['tc_real']  # Genera y asigna una columna calculada a merge
    merge['Maximo_USDPPP'] = merge['Maximo'] / merge['tc_real']  # Genera y asigna una columna calculada a merge
    merge['Cierre_del_dia_USDPPP'] = merge['Cierre_del_dia'] / merge['tc_real']  # Genera y asigna una columna calculada a merge
    #
    df = merge
    #df=df.drop(['Variacion_%'], axis=1)
    #save_file_mkt_cap_usd(ticker1)
    #
    # Eliminacion de duplicados del indice
    #
    # 1. Reseteo el indice para poder operar sobre las columnas    
    df = df.reset_index()
    # 2. Elimino los duplicados que antes eran parte del indice y ahora estan en la columna Fecha
    df = df.drop_duplicates(subset='Fecha', keep='last')
    # 3. Vuelvo a establecer la columna fecha como indice
    df = df.set_index('Fecha', inplace=False)
    #
    filename = "SERIE_CORRIENTE_" + ticker
    save_file_generico(df, original_source + "\INDICES_USDPPP", "SERIE_CORRIENTE_", "^MERV", "_USDPPP.xlsx")
    return df

#update_index_usdppp("^MERV")

#RECUPERA LA SERIE DE TIEMPO
#open_file_versatil("C:\GCB_CAPITAL\INDICES_USDPPP", "SERIE_CORRIENTE_^MERV_USDPPP", ".xlsx")
#df = df.set_index('Fecha')
#chart_series_de_dataframe(df , "Cierre_del_dia_USDPPP", "2004-01-04", "2019-09-20")



