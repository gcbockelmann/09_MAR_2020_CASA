

##### CARGA DATOS DE LA EMPRESA

# Funcion que carga los datos de un ticker en la memoria y dentro del vector datos empresa
# Crea el diccionario datos empresa
datos_empresa = {}

def carga_datos_empresa(ticker_1):
    # Agrega al diccionario datos_empresa los datos de una empresa particular dependiendo del ticker
    global df_ticker, ticker
    open_file_mkt_cap_usdppp("C:\GCB_CAPITAL\MARKET_CAP_USDPPP", ticker_1, ".xlsx")   
    df_ticker=df     
    if ticker_1 == "MIRG":
       datos_empresa["Ticker"]="MIRG"
       datos_empresa["Name"]="Mirgor S.A."
       datos_empresa["Country"]="Argentina"
       datos_empresa["Exchange"]="Argentina"
       datos_empresa["ISIN"]="ARP6823S1295"
       datos_empresa["entity_number"]="1"
       datos_empresa["CCLASS"]="I"
       datos_empresa["GICS Global Industry Code Display"]="Household Appliances"
       datos_empresa["GICS for Industry Drivers"]=""
       datos_empresa["Firm Classification"]="Is"
       datos_empresa["Product Code"]="In Product"
       datos_empresa["Company Status"]="Active" #Active o Inactive
       datos_empresa["Publicly Traded Debt Company"]="Yes"  # Yes o no
       datos_empresa["IPO restricted"]="Yes or No"
       datos_empresa["Price"]=""
       datos_empresa["Warranted Price"]=""
       datos_empresa["Upside"]=""
       datos_empresa["Domicile Country"]="In Product"
       datos_empresa["Trade Country"]="In Product"
       datos_empresa["Cross Lister Type"]="In Product"
       datos_empresa["Designated First Year (MFIRST)"]=2002
       #datos_empresa["Last Fiscal Year"]=2018
       datos_empresa["Designated Last Reported Year (MLASTM)"]=2018
    elif ticker_1 == "TXAR":
       datos_empresa["Ticker"]="TXAR"
       datos_empresa["Name"]="Ternium Argentina S.A."
       datos_empresa["Country"]="Argentina"
       datos_empresa["Exchange"]="Argentina"
       datos_empresa["ISIN"]="ARP6823S1295"
       datos_empresa["entity_number"]="1"
       datos_empresa["CCLASS"]="I"
       datos_empresa["GICS Global Industry Code Display"]="Steel"
       datos_empresa["GICS for Industry Drivers"]=""
       datos_empresa["Firm Classification"]="Is"
       datos_empresa["Product Code"]="In Product"
       datos_empresa["Company Status"]="Active" #Active o Inactive
       datos_empresa["Publicly Traded Debt Company"]="Yes"  # Yes o no
       datos_empresa["IPO restricted"]="Yes or No"
       datos_empresa["Price"]=""
       datos_empresa["Warranted Price"]=""
       datos_empresa["Upside"]=""
       datos_empresa["Domicile Country"]="In Product"
       datos_empresa["Trade Country"]="In Product"
       datos_empresa["Cross Lister Type"]="In Product"
       datos_empresa["Designated First Year (MFIRST)"]=2003
       #datos_empresa["Last Fiscal Year"]=2018
       datos_empresa["Designated Last Reported Year (MLASTM)"]=2019
    #
    ticker = datos_empresa["Ticker"]
       
#ticker = datos_empresa["Ticker"]

#carga_datos_empresa("MIRG")