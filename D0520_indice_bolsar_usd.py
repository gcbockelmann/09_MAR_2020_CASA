



def update_index_usd(ticker10):
    # Esta funcion crea una matriz de index en USD
    # Y graba la matriz en un subdirectorio index
    global df, cur
    open_file_currency("USDARS_LIBRE")
    cur = cur.drop(['FUENTE'], axis=1)
    cur = cur.drop(['Especie'], axis=1)
    filename = "SERIE_CORRIENTE_" + ticker10
    open_index_file_spch(original_source + "\SPCH", filename, ".xlsx")
    #open_file_mkt_cap_ars("C:\GCB_CAPITAL\MARKET_CAP_ARS", ticker4, ".xlsx")
    merge=pd.merge(df, cur, how='inner', left_index=True, right_index=True) # Agrega una columna a la derecha de la Mkt Cap Ars que se llama USDARS_LIBRE
    #
    # ARMA LAS COLUMNAS EN USD
    #
    merge['Apertura_USD'] = merge['Apertura'] / merge['tc_nominal']  # Genera y asigna una columna calculada a merge
    merge['Minimo_USD'] = merge['Minimo'] / merge['tc_nominal']  # Genera y asigna una columna calculada a merge
    merge['Maximo_USD'] = merge['Maximo'] / merge['tc_nominal']  # Genera y asigna una columna calculada a merge
    merge['Cierre_del_dia_USD'] = merge['Cierre_del_dia'] / merge['tc_nominal']  # Genera y asigna una columna calculada a merge
    df = merge
    #df = df.drop(['Variacion_%'], axis=1)
    #save_file_mkt_cap_usd(ticker4)
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
    filename = "SERIE_CORRIENTE_" + ticker10
    save_file_generico(df, original_source + "\INDICES_USD", "SERIE_CORRIENTE_", "^MERV", "_USD.xlsx")
    return df

#update_index_usd("^MERV")
