

################## ARMA LA SERIE DIFERENCIAL_USDARS_PPP


def diferencial(ticker1, ticker2):
    global diferencial_usdars_ppp, cur
    #
    #
    #
    if ticker1 == "USDARS_PPP":      
       # Tratamiento a la serie USDARS_PPP
       df = open_file_versatil(original_source + "\CURRENCIES", "USDARS_PPP", ".xlsx")
       df = serie_de_tiempo(df)
       df.rename(columns = {'tc_real':'USDARS_PPP'}, inplace=True)
       df.rename(columns = {"tc_real":"USDARS_PPP"})
       #df.columns = ['USDARS_PPP', 'W', 'X', 'Y', 'Z']
       #
       # Drop the column with label 'A'
       df.drop('Especie', axis=1, inplace=True)
       #df.drop('X', axis=1, inplace=True)
       #df.drop('Y', axis=1, inplace=True)
       #df.drop('Z', axis=1, inplace=True)
       #print (df)
       usdars_ppp = df
       #print (usdars_ppp)       
    else:
         pass
    # Prepara la segunda serie
    #
    open_file_currency("USDARS_LIBRE")
    usdars_libre = cur  
    #print(usdars_libre)
    #
    # MERGEA LAS DOS SERIES
    #
    merge=pd.merge(usdars_libre, usdars_ppp, how='inner', left_index=True, right_index=True) 
    merge['diferencial']=((merge['USDARS_PPP']/merge['tc_nominal'])-1)
    diferencial_usdars_ppp = merge
    diferencial_usdars_ppp['Especie'] = "USDARS_PPP/USDARS_LIBRE"
    #
    # GRABA EL DATAFRAME DIFERENCIAL
    #
    df = diferencial_usdars_ppp
    #
    writer = pd.ExcelWriter(original_source + '/CURRENCIES/' + 'DIFERENCIAL_' + ticker1 + "_" + ticker2 +  '.xlsx', engine='xlsxwriter')
    #
    # Write each dataframe to a different worksheet.
    df.to_excel(writer, sheet_name='Diferencial')
    #
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    #
    return diferencial_usdars_ppp


#diferencial("USDARS_PPP", "USDARS_LIBRE")

