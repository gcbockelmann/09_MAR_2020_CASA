#### EXPORTA A METASTOCK PRO Version 11.0 

#### FORMULA QUE CONVIERTE UN FORMATO DATETIME A STRING
def datetime_to_string(x):
    import datetime
    dateTimeObj = x
    timestampStr = dateTimeObj.strftime("%m/%d/%Y")
    return timestampStr

#EJEMPLO
#datetime_to_string(df["<date>"].loc[0])




def txt_spch_ARS(ticker):
    global df
    open_file_mkt_cap_usdppp(original_source + "\MARKET_CAP_USDPPP", ticker, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Apertura":"<open>"}, inplace=True)
    df.rename(columns = {"Maximo":"<high>"}, inplace=True)
    df.rename(columns = {"Minimo":"<low>"}, inplace=True)
    df.rename(columns = {"Cierre_del_dia":"<close>"}, inplace=True)
    df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<o/i>"]=0
    new_ticker=ticker+str("_ARS")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source+ "\TXT")                                 
    filename = str("spch_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)



#txt_spch_ARS("TXAR")
#txt_spch_ARS("CEPU")
#txt_spch_ARS("TGSU2")
#txt_spch_ARS("BOLT")


def txt_mkt_cap_ars(ticker):
    global df
    open_file_mkt_cap_ars(original_source + "\MARKET_CAP_ARS", ticker, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Open_ARS":"<open>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Max_ARS":"<high>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Min_ARS":"<low>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Close_ARS":"<close>"}, inplace=True)
    df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<o/i>"]=0
    new_ticker=ticker+str("_Cap_ARS")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source + "\TXT")                                 
    filename = str("mkt_cap_ars_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_mkt_cap_ars("CEPU")


def txt_mkt_cap_usd(ticker):
    global df
    open_file_mkt_cap_usd(original_source + "\MARKET_CAP_USD", ticker, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Open_USD":"<open>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Max_USD":"<high>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Min_USD":"<low>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Close_USD":"<close>"}, inplace=True)
    df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<o/i>"]=0
    new_ticker=ticker+str("_Cap_USD")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source + "\TXT")                                 
    filename = str("mkt_cap_usd_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_mkt_cap_usd("CEPU")
#txt_mkt_cap_usd("TGSU2")


#txt_mkt_cap_usd("TXAR")
#txt_mkt_cap_usd("SAMI")
#txt_mkt_cap_usd("BOLT")
#txt_mkt_cap_usd("CTIO")
#txt_mkt_cap_usd("ALUA")

#txt_mkt_cap_usd("TGSU2")
#txt_mkt_cap_usd("PAMP")



def txt_mkt_cap_usdppp(ticker):
    global df
    open_file_mkt_cap_usdppp(original_source + "\MARKET_CAP_USDPPP", ticker, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Open_USD_PPP":"<open>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Max_USD_PPP":"<high>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Min_USD_PPP":"<low>"}, inplace=True)
    df.rename(columns = {"Mkt_Cap_Close_USD_PPP":"<close>"}, inplace=True)
    df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<o/i>"]=0
    new_ticker=ticker+str("_Cap_USDPPP")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source + "\TXT")                                 
    filename = str("mkt_cap_usdppp_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_mkt_cap_usdppp("ALUA")
#txt_mkt_cap_usdppp("TXAR")
#txt_mkt_cap_usdppp("BOLT")
#txt_mkt_cap_usdppp("SAMI")
#txt_mkt_cap_usdppp("CTIO")

#txt_mkt_cap_usdppp("CEPU")
#txt_mkt_cap_usdppp("TGSU2")
#txt_mkt_cap_usdppp("PAMP")


###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

def txt_indice_ars(ticker):
    global df
    file_name = "SERIE_CORRIENTE_" + ticker
    open_index_file_spch(original_source + "\SPCH", file_name, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Apertura":"<open>"}, inplace=True)
    df.rename(columns = {"Maximo":"<high>"}, inplace=True)
    df.rename(columns = {"Minimo":"<low>"}, inplace=True)
    df.rename(columns = {"Cierre_del_dia":"<close>"}, inplace=True)
    #df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<vol>"]=0
    df["<o/i>"]=0
    new_ticker=ticker+str("_ars")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source + "\TXT")                                 
    filename = str("indice_ARS_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_indice_ars("^MERV")



def txt_indice_usd(ticker):
    global df
    file_name = "SERIE_CORRIENTE_" + ticker + "_USD"
    open_index_file_spch(original_source + "\INDICES_USD", file_name, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Apertura_USD":"<open>"}, inplace=True)
    df.rename(columns = {"Maximo_USD":"<high>"}, inplace=True)
    df.rename(columns = {"Minimo_USD":"<low>"}, inplace=True)
    df.rename(columns = {"Cierre_del_dia_USD":"<close>"}, inplace=True)
    #df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<vol>"]=0
    df["<o/i>"]=0
    new_ticker=ticker+str("_usd")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source + "\TXT")                                 
    filename = str("indice_USD_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_indice_usd("^MERV")

def txt_indice_usdppp(ticker):
    global df
    file_name = "SERIE_CORRIENTE_" + ticker + "_USDPPP"
    open_index_file_spch(original_source + "\INDICES_USDPPP", file_name, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Apertura_USDPPP":"<open>"}, inplace=True)
    df.rename(columns = {"Maximo_USDPPP":"<high>"}, inplace=True)
    df.rename(columns = {"Minimo_USDPPP":"<low>"}, inplace=True)
    df.rename(columns = {"Cierre_del_dia_USDPPP":"<close>"}, inplace=True)
    #df.rename(columns = {"Volumen_Nominal_Ajustado":"<vol>"}, inplace=True)
    df["<vol>"]=0
    df["<o/i>"]=0
    new_ticker=ticker+str("_usdppp")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source + "\TXT")                                 
    filename = str("indice_USDPPP_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_indice_usdppp("^MERV")


def txt_spch_ARS_para_cedears(ticker):
    global df
    open_file_spch(original_source + "SPCH", "SERIE_CORRIENTE_"+ticker, ".xlsx")
    df = df.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    df.rename(columns = {"Apertura":"<open>"}, inplace=True)
    df.rename(columns = {"Maximo":"<high>"}, inplace=True)
    df.rename(columns = {"Minimo":"<low>"}, inplace=True)
    df.rename(columns = {"Cierre_del_dia":"<close>"}, inplace=True)
    df.rename(columns = {"Volumen_Nominal":"<vol>"}, inplace=True)
    df["<o/i>"]=0
    new_ticker=ticker+str("_ARS")
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source+ "\TXT")                                 
    filename = str("spch_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)



#txt_spch_ARS_para_cedears("VALE")

###########################################################################################################################
###########################################################################################################################
###########################################################################################################################


def txt_currency(ticker):
    global df
    df = open_excel(original_source + "\CURRENCIES", ticker, ".xlsx")
    #df = cur.reset_index()
    df["<per>"]="D"
    df.rename(columns = {"Fecha":"<date>"}, inplace=True)
    #df.rename(columns = {"Apertura":"<open>"}, inplace=True)    
    #df.rename(columns = {"Maximo":"<high>"}, inplace=True)
    #df.rename(columns = {"Minimo":"<low>"}, inplace=True)
    if ticker == "USDARS" or ticker == "USDARS_CCL_GGAL" or ticker == "USDARS_LIBRE":
       df.rename(columns = {"tc_nominal":"<close>"}, inplace=True)
    elif ticker == "USDARS_PPP":
       df.rename(columns = {"tc_real":"<close>"}, inplace=True) 
    else:
       pass 
    #
    # Corrige las columnas faltantes
    df["<open>"]= df["<close>"]    
    df["<high>"]= df["<close>"] 
    df["<low>"]= df["<close>"]
    df["<vol>"]= 0  
    #df.rename(columns = {"Volumen_Nominal":"<vol>"}, inplace=True)
    df["<o/i>"]=0
    new_ticker=ticker
    df["<ticker>"]=new_ticker
    df2 = df[[ "<per>", "<date>", "<open>", "<high>", "<low>", "<close>", "<vol>", "<o/i>", "<ticker>"]] 
    df2['<date>'] = df['<date>'].apply(datetime_to_string)
    #
    #
    location = str(original_source+ "\TXT")                                 
    filename = str("currency_" + ticker)     
    extension = str(".txt")
    #En una variable string la doble blackslash \\ resulta en una sola \
    path = (location + "\\" + filename + extension)  
    #
    #
    df2.to_csv(path, index=False)


#txt_currency("USDARS")
#txt_currency("USDARS_CCL_GGAL")
#txt_currency("USDARS_LIBRE")
#txt_currency("USDARS_PPP")




#open_excel(original_source + "\CURRENCIES", ticker, ".xlsx")
#open_excel(original_source + "\CURRENCIES", "USDARS", ".xlsx")
