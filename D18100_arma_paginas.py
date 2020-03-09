##################################################################################################################################3
##################### BALANCE SHEET
##################################################################################################################################
#ARMA UNA LISTA CON LOS CONCEPTOS ESTANDARIZADOS QUE SERIAN LOS CODIGOS DE LAS VARIABLES
conceptos_estandarizados_balance_sheet = ("BI0001",
"BI0001_1",
"BI0001_FS",
"RI1",
"XS1",
"BI0002",
"BI0002_FS",
"RI2", 
"BI0003",
"BI0003_FS",
"RI3",
"BI0068",
"BI0068_1",
"BI0068_2",
"BI0068_3",
"BI0068_FS",
"RI68",
"BI0004",
"RI4",
"RI193",
"BI0007",
"BI0007_5",
"BI0007_9",
"BI0007_8",
"BI0007_T",
"HA1481",
"BI0007_FS",
"RI7",
"BI0196",
"BI0196_5",
"BI0196_9",
"BI0196_8",
"BI0196_T",
"HA1482",
"BI0196_FS",
"RI196",
"BI0008",
"BI0008_5",
"BI0008_9",
"BI0008_8",
"BI0008_T",
"HA1483",
"BI0008_FS",
"RI8",
"BI0158",
"BI0158_FS",
"RI158",
"BI0260",
"BI0260_FS",
"RI260",
"BI0073",
"BI0073_FS",
"RI73",
"BI0266",
"BI0266_FS",
"RI266",
"RI4",
"RI8",
"BI0069",
"BI0069_1",
"BI0069_2",
"BI0069_3",
"BI0069_4",
"RI69",
"BI0033",
"BI0033_FS",
"RI33",
"BI0031_I",
"BI0031_FS",
"RI31i",
"BI0032_I",
"BI0032_4",
"BI0032_FS",
"RI32i",
"BI0006",
"RI6",
"RI204",
"RI601A",
"RI505M",
"SOFT_METHO",
"RI537",
"RI536B",
"RI532",
"BI0070",
"BI0070_FS",
"RI70",
"BI0071",
"BI0071_FS",
"RI71",
"BI0072",
"BI0072_1",
"BI0072_2",
"BI0072_3",
"BI0072_4",
"RI72",
"BI0034",
"BI0034_8",
"BI0034_FS",
"RI34",
"BI0005",
"RI5",
"BI0009",
"BI0009_8",
"BI0009_9",
"BI0009_FS",
"RI9",
"BI0075",
"BI0075_1",
"BI0075_2",
"BI0075_3",
"BI0075_4",
"BI0075_FS",
"RI75",
"BI0035",
"BI0035_FS",
"RI35",
"BI0038",
"BI0038_FS",
"RI38",
"BI0181",
"RI181",
"RI74",
"RI397",
"RI6",
"RI181",
"BI0216",
"RI216",
"BI0060",
"R160",
"BI0130",
"BI0130_FS",
"RI130",
"BI0216",
"RI216",
"RI36",
"H1467",
"S101",
"S102",
"S103",
"S104",
"S105",
"S106",
"S107",
"S108",
"S109",
"S110",
"LIC_METHOD",
"SOFT_METHO",
"RI572",
"RI573",
"RI574",
"RI575",
"RI576",
"RI578",
"RI286",
"RI287",
"RI290",
"RI294",
"RI296",
"RI300",
"RI331",
"RI332",
"RI295",
"RI330",
"RI563",
"RI564",
"RI561",
"RI292",
"RI562",
"RI240",
"H1621",
"RI59",
"H1601")


#ARMO UN DICCIONARIO PARA LOS CODIGOS DE LAS VARIABLES CON SUS RESPECTIVOS NOMBRES
nombres_conceptos_estandarizados_balance_sheet = {"BI0001" : "Cash & Short-Term Investments",
"BI0001_1":"    Counterparty Deposits in Cash", 
"BI0001_FS":"    Fin Sub - Cash & Short-Term Investments",
"RI1":"Cash & Short-Term Investments",
"XS1":"Excess Cash (Non'operating) - BS plug",
"BI0002":"Debtors (Receivables)",
"BI0002_FS":"    Fin Sub - Debtors (Receivables)",
"RI2":"Debtors (Receivables)", 
"BI0003":"Stocks (Inventories)",
"BI0003_FS":"    Fin Sub - Stocks (Inventories)",
"RI3":"Stocks (Inventories)",
"BI0068":"Other Current Assets",
"BI0068_1":"    Derivative Assets in Other Current Assets",
"BI0068_2":"    Assets Held for Sale - Current",
"BI0068_3":"    Regulatory Assets in Other Current Assets",
"BI0068_FS":"    Fin Sub - Other Current Assets",
"RI68":"Other Current Assets",
"BI0004":"Total Current Assets",
"RI4":"Total Current Assets",
"RI193":"Short-Term Investments",
"BI0007":"Gross Plant",
"BI0007_5":"    Rental Assets - Gross",
"BI0007_9":"        RoU Lease Assets - Gross (Override Only If RI988U = 1, US GAAP)",
"BI0007_8":"        RoU Lease Assets - Gross (Override Only If RI988U = 2, IFRS)",
"BI0007_T":"        RoU Lease Assets, Total - Gross (Override Only If Incorrect Value Captured)",
"HA1481":"    Right-of-Use Lease Assets - Gross (Don't Override This)",
"BI0007_FS":"    Fin Sub - Gross Plant",
"RI7":"Gross Plant",
"BI0196":"Accumulated Depreciation",
"BI0196_5":"    Rental Assets - Accumulated Depreciation",
"BI0196_9":"        RoU Lease Assets - Accum. Dep. (Override Only If RI988U = 1, US GAAP)",
"BI0196_8":"        RoU Lease Assets - Accum. Dep. (Override Only If RI988U = 2, IFRS)",
"BI0196_T":"        RoU Lease Assets, Total - Accum. Dep. (Override Only If Incorrect Value Captured)",
"HA1482":"    Right-of-Use Lease Assets - Accum. Dep. (Don't Override This)",
"BI0196_FS":"    Fin Sub - Accumulated Depreciation",
"RI196":"Accumulated Depreciation",
"BI0008":"Net Plant",
"BI0008_5":"    Rental Assets - Net",
"BI0008_9":"        RoU Lease Assets - Net (Override Only If RI988U = 1, US GAAP)",
"BI0008_8":"        RoU Lease Assets - Net (Override Only If RI988U = 2, IFRS)",
"BI0008_T":"        RoU Lease Assets, Total - Net",
"HA1483":"    Right-of-Use Lease Assets (Don't Override This)",
"BI0008_FS":"    Fin Sub - Net Plant",
"RI8":"Net Plant",
"BI0158":"Land and Improvements -- Net",
"BI0158_FS":"    Fin Sub - Land and Improvements -- Net",
"RI158":"Land and Improvements -- Net",
"BI0260":"Land and Improvements at Cost",
"BI0260_FS":"    Fin Sub - Land and Improvements at Cost",
"RI260":"Land and Improvements at Cost",
"BI0073":"Construction in Progress -- Net",
"BI0073_FS":"    Fin Sub - Construction in Progress -- Net",
"RI73":"Construction in Progress -- Net",
"BI0266":"Construction in Progress at Cost",
"BI0266_FS":"    Fin Sub - Construction in Progress at Cost",
"RI266":"Construction in Progress at Cost",
"RI4":"Total Current Assets",
"RI8":"Net Plant",
"BI0069":"Other Long-Term Assets",
"BI0069_1":"    Derivative Assets in Other Long-Term Assets",
"BI0069_2":"    Assets Held for Sale",
"BI0069_3":"    Regulatory Assets in Long-Term Assets",
"BI0069_4":"    Fin Sub - Long-Term Assets",
"RI69":"Other Long-Term Assets",
"BI0033":"Intangible Assets -- Net",
"BI0033_FS":"Fin Sub - Intangible Assets -- Net",
"RI33":"Intangible Assets -- Net",
"BI0031_I":"Investment & Advances (Equity)",
"BI0031_FS":"    Fin Sub - Investment & Advances (Equity)",
"RI31i":"Investment & Advances (Equity)",
"BI0032_I":"Investment & Advances (Other)",
"BI0032_4":"    Nuclear Plant decommisioning trusts",
"BI0032_FS":"    Fin Sub - Investment & Advances (Other)",
"RI32i":"Investment & Advances (Other)",
"BI0006":"Total Assets",
"RI6":"Total Assets",
"RI204":"Goodwill -- Net",
"RI601A":"Other Net Operating Intangibles",
"RI505M":"Discontinued Operations and Other",
"SOFT_METHO":"Software Method (0 = Off / 3 = Indef. Life / 4 = Finite In-Life / 5 = Finite ex-Life)",
"RI537":"Capitalized Software - Accumulated Depreciation",
"RI536B":"Capitalized Software (in intangibles) - Net",
"RI532":"Amortization of Capitalized Software",
"BI0070":"Creditors (Accounts Payable)",
"BI0070_FS":"Fin Sub - Creditors (Accounts Payable)",
"RI70":"Creditors (Accounts Payable)",
"BI0071":"Income Taxes Payable",
"BI0071_FS":"Fin Sub - Income Taxes Payable",
"RI71":"Income Taxes Payable",
"BI0072":"Other Current Liabilities",
"BI0072_1":"Derivative Liabilities in Other Current Liabilities",
"BI0072_2":"Liabilities Held for Sale - Current",
"BI0072_3":"Regulatory Liabilities in Other Current Liabilities",
"BI0072_4":"Fin Sub - Other Current Liabilities",
"RI72":"Other Current Liabilities",
"BI0034":"Debt in Current Liabilities",
"BI0034_8":"    Capital Lease Liabilities, Current",
"BI0034_FS":"    Fin Sub - Debt in Current Liabilities",
"RI34":"Debt in Current Liabilities",
"BI0005":"Total Current Liabilities",
"RI5":"Total Current Liabilities",
"BI0009":"Long-Term Debt -- Total",
"BI0009_8":"    Non-Current Lease Liabilities (Override Only If RI988U = 2, IFRS)",
"BI0009_9":"    Non-Current Lease Liabilities (Override Only If RI988U = 1, US GAAP AND FUND_VENDOR_ID=1, Compustat)",
"BI0009_FS":"    Fin Sub - Long-Term Debt -- Total",
"RI9":"Long-Term Debt -- Total",
"BI0075":"Other Long-Term Liabilities",
"BI0075_1":"    Derivative Liabilities in Other Long-Term Liabilities",
"BI0075_2":"    Liabilities Held for Sale",
"BI0075_3":"    Regulatory Liabilities in Other Long-Term Liabilities",
"BI0075_4":"    Assets Retirement Obligations",
"BI0075_FS":"    Fin Sub - Other Long-Term Liabilities",
"RI75":"Other  Long-Term Liabilities",
"BI0035":"Deferred Taxes & Investment Tax Credit",
"BI0035_FS":"    Fin Sub - Deferred Taxes & Investment Tax Credit",
"RI35":"Deferred Taxes & Investment Tax Credit",
"BI0038":"Minority Interest",
"BI0038_FS":"    Fin Sub - Minority Interest",
"RI38":"Minority Interest",
"BI0181":"Total Liabilities",
"RI181":"Total Liabilities",
"RI74":"Deferred Taxes",
"RI397":"Deferred Revenue - Long-Term",
"RI6":"Total Assets",
"RI181":"Total Liabilities",
"BI0216":"Net Assets",
"RI216":"Net Assets",
"BI0060":"Common Equity",
"R160":"Common Equity",
"BI0130":"Preferred Stock",
"BI0130_FS":"Fin Sub - Preferred Stock",
"RI130":"Preferred Stock",
"BI0216":"Total Stockholder's Equity",
"RI216":"Total Stockholder's Equity",
"RI36":"Retained Earnings",
"H1467":"Unidentified Assets or Liabilities",
"S101":"Hedged Asset Adjustment Switch",
"S102":"Discontinued Ops Switch",
"S103":"Regulatory Assets Switch",
"S104":"Nuclear Decommisionning Switch",
"S105":"Rental Assets Switch",
"S106":"Pass Through Expense Switch",
"S107":"Investment Fix Switch",
"S108":"Estimate Rent using MLP Switch",
"S109":"Financial Subsidiary Switch",
"S110":"Exceptional Taxation Switch",
"LIC_METHOD":"Licenses Cap. Method (0=Off / 3=Indef Life / 4=Finite In-Life / 5=Finite Ex-Life)",
"SOFT_METHO":"Software Cap. Method (0=Off / 3=Indef Life / 4=Finite In-Life / 5=Finite Ex-Life)",
"RI572":"Long-Term Pension Asset (FAS158)",
"RI573":"Current Pension Liability (FAS158)",
"RI574":"Long-Term Pension Liability (FAS158)",
"RI575":"Long-Term Postretirement Asset (FAS158)",
"RI576":"Current Postretirement Liability (FAS158)",
"RI578":"Long-Term Postretirement Liability (FAS158)",
"RI286":"Projected Benefit Obligation -- Overfunded (Liability in +ve)",
"RI287":"Pension Plan Assets -- Overfunded (Assets in +ve)",
"RI290":"Pension Prepaid/Accrued Cost -- Overfunded (Liability in -ve)",
"RI294":"Projected Benefit Obligation -- Underfunded (Liability in +ve)",
"RI296":"Pension Plan Assets -- Underfunded (Assets in +ve)",
"RI300":"Pension Prepaid/Accrued Cost -- Underfunded (Liability in -ve)",
"RI331":"Pension Plans - Service Cost",
"RI332":"Pension Plans - Interest Cost",
"RI295":"Periodic Pension Cost -- Net",
"RI330":"Postretirement Benefit Asset (Liab) (Net) (Liability in -ve)",
"RI563":"OPEB Projected Benefit Obligation (PBO) (Liability in +ve)",
"RI564":"OPEB Plan Assets (Assets in +ve)",
"RI561":"Postretirement Service Cost",
"RI292":"Periodic Postretirement Benefit Cost (Net)",
"RI562":"Postretirement Pension Cost",
"RI240":"LIFO reserve",
"H1621":"%of Inventory on FIFO -- Enter as a whole number",
"RI59":"Inventory Valuation Method (1), (2), (3)",
"H1601":"Total Effective Tax Rate -- Enter as a whole Number",
}


############################################################# ARMA LA SERIE PARA MOSTRAR

# ARMA UNA LISTA SHOW (PARA MOSTRAR) QUE ES EN PRINCIPIO SIMILAR A LA DE LOS CODIGOS PARA PODER SER MODIFICADA, CON TITULOS, ESPACIOS ,ETC
show_conceptos_estandarizados_balance_sheet  = []
for k in range(0,len(conceptos_estandarizados_balance_sheet )):
    show_conceptos_estandarizados_balance_sheet.append(conceptos_estandarizados_balance_sheet[k])

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

########################################################################### ACTUALIZA EL DICCIONARIO CON LOS NOMBRES DE TODOS LOS CONCEPTOS AGREGADOS

# ARMA UNA LISTA SHOW (PARA MOSTRAR) EL NOMBRE CORRESPONDIENTE A CADA VARIABLE O CODIGO - SE ARMAR PARA MODER MIDIFICAR Y QUE SE PUEDA METER TITULOS, ESPACIOS ,ETC
#Arma una lista para poner en orden la lista de nombres de conceptos estandarizados
show_nombres_conceptos_estandarizados_balance_sheet  = []

#Corre un loop desde 0 hasta la longitud de la lista de conceptos
#Agrega a la lista de SHOW DE NOMBRES los conceptos 
for k in range(0,len(show_conceptos_estandarizados_balance_sheet)):
    show_nombres_conceptos_estandarizados_balance_sheet.append(conceptos_estandarizados_balance_sheet[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_balance_sheet)

#####################################################################################################################################################


# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_balance_sheet = []

# Agrega a la lista nombbres de los conceptos todos los nombres de los conceptos que estan en el diccionario nombres_de_los_conceptos 
for k in conceptos_estandarizados_balance_sheet:
    show_nombres_conceptos_estandarizados_balance_sheet.append(nombres_conceptos[k])


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

##############################################################################################################################################
#### LE DOY FORMATO A LAS LISTAS PARA LOS TITULOS Y ESPACIOS EN BLANCO

def agrega_linea_a_dos_listas(lista_de_codigos_a_mostrar_show, lista_de_nombres_de_conceptos_a_mostrar_show, posicion, texto1, texto2):
    #
    lista_de_codigos_a_mostrar_show.insert(posicion , texto1)
    lista_de_nombres_de_conceptos_a_mostrar_show.insert(posicion, texto2)

    
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 0, "****" , "****")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 1, "" , "BI Universal Input Template")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 2, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 3, "" , "Current Assets")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 23, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 25, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 26, "" , "Property, Plant & Equipment")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 35, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 44, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 53, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 60, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 67, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 68, "" , "Other Long-Term Assets & Investments")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 69, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 90, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 91, "" , "Supplemental Balance Sheet Data - Assets")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 92, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 96, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 101, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 102, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 103, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 104, "" , "Current Liabilities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 105, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 124, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 125, "" , "Non-Current Liabilities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 126, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 147, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 148, "" , "Supplemental Balance Sheet Data - Liabilities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 149, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 152, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 153, "" , "Net Assets")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 154, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 159, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 167, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 169, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 171, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 172, "" , "Automated HOLT Fixes Switches")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 173, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 186, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 187, "" , "Supplemental Balance Sheet Items")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 188, "" , "")

agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 192, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 196, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 200, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 204, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 208, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 212, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 216, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_balance_sheet, show_nombres_conceptos_estandarizados_balance_sheet, 220, "" , "")



###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_balance_sheet)
#len(show_nombres_conceptos_estandarizados_balance_sheet)

#len(show_conceptos_estandarizados_balance_sheet)==len(show_nombres_conceptos_estandarizados_balance_sheet)


################################################
############################################# estado de resultados
#############################################

conceptos_estandarizados_estado_de_resultado = ("RI630",
"BI0012",
"BI0012_6",
"BI0012_FS",
"RI12",
"BI0041",
"BI0041_FS",
"RI41",
"BI0189",
"BI0189_FS",
"RI189",
"BI0649",
"BI0649_FS",
"RI649",
"BI0014_8",
"BI0015_8",
"RI47I",
"BI0013",
"RI13",
"BI0014",
"BI0014_5",
"BI0014_8",
"BI0065_8",
"BI0014_FS",
"RI14",
"BI0178",
"RI178",
# Pretax Income
"RI178",
"BI0015",
"BI0015_8",
"BI0015_FS",
"RI15",
"BI0061",
"BI0061_FS",
"RI61",
"BI0017",
"BI0017_FS",
"RI17",
"BI0170",
"RI170",
# Net Income After Minority Interest
"RI170",
"BI0016",
"BI0016_10",
"BI0016_FS",
"RI16",
"BI0049",
"BI0049_FS",
"RI49",
"BI0018",
"RI18",
"H1610",
"IBES_NI",
"RI661",
# Supplemental Income Statement Data
"RI21",
"RI19",
"RI667",
"RI662",
#
"H1202",
"RI65",
"BI0047",
"RI96",
"BI0014_8",
"BI0015_8",
"RI47I",
"S114V",
"BI004V",
"RI47",
"BI0046",
"RI46",
"RI388",
#
"RI398A",
"RI415",
"RI426",
"RI399A",
#
"RI874",
"RI883",
#
"RI190",
"RI62",
"RI147",
#
"BI0055",
"RI55",
#
"RI128",
#
"RI661",
#
"H1602",
#
# Supplemental Leases Variables
#
"RI988U",
"RI988F",
"DIP18",
"LEASE_YR",
"S114",
#
# Lease Data- Balance Sheet
#
#
"HA1481",
"HA1482",
"HA1483",
"HA1233",
"HA1234",
"HA1231",
"HA1232",
"RI47",
"RI47I",
#
"BI0007_9",
"BI0196_9",
"BI0008_9",
#
# Liabilities
#
"FUND_VENDOR_ID",
# Compustat
"BI0034_9",
"BI0009_9",
#
# Worldscope
#
"BI0072_9",
"BI0075_9",
#
# Income Statement
#
"S114V",
"BI0047",
"BI0047V",
#
# Lease Data Input - IFRS
#
# Assets
#
"BI0007_8",
"BI0196_8",
"BI0008_8",
#
#Liabilities
#
"BI0034_8",
"BI0009_8",
#
# Income Statement
#
"S114V",
"BI0047",
"BI0047V",
"BI0014_8",
"BI0015_8",
#
#
#
# Override Slots For Forecast Adjustments
"RI46_OR",
"BI0046",
#
"H1032_OR",
"H1032",
#
"RI49_OR",
"BI0049",
#
"H2132_OR",
"H2132",
#
"H1657_OR",
"H1657_PCT",
"H1657",
#
"RI55_OR",
"RI55",
#
"RI503_OR",
"RI503",
#
"RI19_OVR",
"RI19",
#
"RI998",
"RI29",
#
"RI22",
"RI23",
"RI24",
#
"RI700",
"RI701",
"RI702",
#
"RI25",
"RI745",
"RI171",
"RI27",
"RI202",
"H1111",
#
"RI750",
"RI751",
"RI752",
"RI753",
"RI760",
#
"H1656",
"H1657_OR",
"H1657_PCT",
"H1657",
"H1658",
#
"RI605",
#
"RI602",
"RI603",
#
"H1273",
"H1649",
"H1648",
#
"H1831B",
"H1919_FC",
"H1965",
#
"H1032",
#
# Refer to "Capitalization of R&D" factsheet for more R&D Layers
#
"RI664",
"H1292",
"H1292_QTR",
"H1293",
#
"RI665",
"H1290",
"H1290_QTR",
"H1291",
#
"RI664B",
"H1292B",
"H1292B_QTR",
"H1293B",
#
"RI665B",
"H1290B",
"H1290B_QTR",
"H1291B")

#len(nombres_conceptos_estandarizados_estado_de_resultado)
#len(conceptos_estandarizados_estado_de_resultado)


nombres_conceptos_estandarizados_estado_de_resultado = {"RI630":"Pro-Forma Sales",
"BI0012":"Turnover (Net Sales)",
"BI0012_6":"Pass Through Expense",
"BI0012_FS":"Fin Sub - Turnover (Net Sales)",
"RI12":"Turnover (Net Sales)",
"BI0041":"Cost of Goods Sold",
"BI0041_FS":"Fin Sub - Cost of Goods Sold",
"RI41":"Cost of Goods Sold",
"BI0189":"Selling, General & Administrative Expenses",
"BI0189_FS":"Fin Sub - Selling, General & Administrative Expenses",
"RI189":"Selling, General & Administrative Expenses",
"BI0649":"Total Other Income (Expense)",
"BI0649_FS":"Fin Sub - Total Other Income (Expense)",
"RI649":"Total Other Income (Expense)",
"BI0014_8":"    Depreciation Of Right-of-Use Assets",
"BI0015_8":"    Interest Expense on Lease Liabilities",
"RI47I":"Rental Expense Imputed",
"BI0013":"Operating Income Before Depreciation",
"RI13":"Operating Income Before Depreciation",
#
# Operating income After Depreciation
#
"BI0014":"Depreciation and Amortization (con signo positivo)",
"BI0014_5":"    Rental Assets - Depreciation Expense",
"BI0014_8":"    Depreciation of Right-of-Use Assets",
"BI0065_8":"    Amortization of Right-of-Use Intangible Assets (Not used by model yet)",
"BI0014_FS":"    Fin Sub - Depreciation and Amortization",
"RI14":"Depreciation and Amortization",
"BI0178":"Operating Income After Depreciation",
"RI178":"Operating Income After Depreciation",
#
# Pretax Income
#
"RI178":"Operating Income After Depreciation",
"BI0015":"Interest Expense -- Gross",
"BI0015_8":"    Interest Expense on Lease Liabilities",
"BI0015_FS":"    Fin Sub - Interest Expense",
"RI15":"Interest Expense -- Gross",
"BI0061":"Non-Operating Income (Expense)",
"BI0061_FS":"    Fin Sub - Non-Operating Income (Expense)",
"RI61":"Non-Operating Income (Expense)",
"BI0017":"Special Items",
"BI0017_FS":"Fin Sub - Special Items",
"":"    Tax Special Items",
"RI17":"Special Items",
"BI0170":"Pretax Income",
"RI170":"Pretax Income",
#
# Net Income After Minority Interest
#
"RI170":"Pretax Income",
"BI0016":"Income Taxes",
"BI0016_10":"Nonrecurring Exception Taxation",
"BI0016_FS":"Fin Sub - Income Taxes",
"RI16":"Income Taxes",
"BI0049":"Minority Interest",
"BI0049_FS":"Fin Sub - Minority Interest",
"RI49":"Minority Interest",
"BI0018":"Net Income After Minority Interest",
"RI18":"Net Income After Minority Interest",
"H1610":"Net Income Forecast (Diluted) - Do Not Override",
"IBES_NI":"IBCS Net Income (For Reference Only)",
"RI661":"FASB 121 Write Down",
#
# Supplemental Income Statement Data
#
"RI21":"Common Dividends (Including Total Special Dividends)",
"RI19":"Preferred Dividends",
"RI667":"Special Dividends per share",
"RI662":"Spin-OFF per share",
#
"H1202":"Depreciation of Gross Plant",
"RI65":"Amortization of Intangibles",
"BI0047":"Rental Expense",
"RI96":"Minimum Rent in First Year",
"BI0014_8":"    Dep. Of Right-of-Use Assets",
"BI0015_8":"    Interest Expense on Leases Liabilities",
"RI47I":"Rental Expense Imputed",
"S114V":"Variable Rent Switch (1=Remove)",
"BI004V":"Rental Expense (Variable Portion)",
"RI47":"Rental Expense",
"BI0046":"R&D Expense",
"RI46":"Research & Development Expense",
"RI388":"In-Process R&D Charges",
#
"RI398A":"Actual Stock Option Expense (included in Net Income)",
"RI415":"Actual Stock Option Expense after Tax",
"RI426":"Stock Option Expense included in R&D Expense",
"RI399A":"Implied Stock Option Expense (Not included in Net Income)",
#
"RI874":"Options Exercisable",
"RI883":"Options Exercisable - Weighted Average Price",
#
"RI190":"Nonop Inc Excl Inter Inc",
"RI62":"Interest Income",
"RI147":"Interest Capitalized",
#
"BI0055":"Unconsolidated Subs - Equity/Earnings",
"RI55":"Unconsolidated Subs - Equity/Earnings",
#
"RI128":"Capital Expenditures (SCFP)",
#
"H1602":"Tax on Special Items",
#
# Supplemental Leases Variables
#
"RI988U":"Accounting Standard - Universal (1=US GAAP, 2=IFRS)",
"RI988F":"Accounting Standard - For Override (1=US GAAP, 2=IFRS)",
"DIP18":"Leases Adj. Flag (1=disable)",
"LEASE_YR":"Lease Adoption Year",
"S114":"HOLT Leases Adjustment Switch",
#
"HA1481":"Right-of-Use Assets, gross",
"HA1482":"Right-of-Use Assets, accum dep",
"HA1483":"Right-of-Use Assets, net",
"HA1233":"Lease Liabiltiy, current",
"HA1234":"Lease Liabiltiy, non-current",
"HA1231":"Total Lease Liabilities",
"HA1232":"Net Lease Assets / Liabilities",
"RI47":"Rental expense HOLT uses to cpitalize operating leases",
"RI47I":"Rental expense - Imputed (Only for RI988U=2, IFRS)",
#
"BI0007_9":"Right-of-Use Assets, Operating Lease - Gross",
"BI0196_9":"Right-of-Use Assets, Operating Lease - Accum. Dep.",
"BI0008_9":"Right-of-Use Assets, Operating Lease - Net",
#
#
# Liabilities
#
"FUND_VENDOR_ID":"Data Vendor",
# Compustat
"BI0034_9":"Operating Lease Liabilities in Current Debt",
"BI0009_9":"Operating Lease Liabilities in Long-Term Debt",
#
# Worldscope
#
"BI0072_9":"Operating Lease in Other Current Liabilities",
"BI0075_9":"Operating Lease in Other Long-Term Liabilities",
#
# Income Statement
#
"S114V":"Variable Rent Switch (1=Remove)",
"BI0047":"Rental Expense - Ingest",
"BI0047V":"Rental Expense - Variable",
#
# Lease Data Input - IFRS
#
# Assets
#
"BI0007_8":"Right-of-Use Assets, Capital Lease - Gross",
"BI0196_8":"Right-of-Use Assets, Capital Lease - Accum. Dep.",
"BI0008_8":"Right-of-Use Assets, Capital Lease - Net",
#
#Liabilities
#
"BI0034_8":"Cap Lease liability, short-term",
"BI0009_8":"Cap Lease liability, long-term",
#
# Income Statement
#
"S114V":"Variable Rent Switch (1=Remove)",
"BI0047":"Rental Expense - Ingest",
"BI0047V":"Rental Expense - Variable",
"BI0014_8":"Depreciation of Right-of-Use Assets",
"BI0015_8":"Interest on Lease Liabilities",
#
#
# Override Slots For Forecast Adjustments
#
"RI46_OR":"R&D  Exp. - FY1 Override",
"BI0046":"R&D Expense",
#
"H1032_OR":"Life - Capitalized R&D - Override",
"H1032":"Life - Capitalized R&D",
#
"RI49_OR":"MI (Income Acct) - FY1 Override",
"BI0049":"Minority Interest",
#
"H2132_OR":"MI Ratio - FY1 Override",
"H2132":"Minority Interest Ratio",
#
"H1657_OR":"Cash EPS Adjustment FY1 override",
"H1657_PCT":"Cash EPS % Adjustment",
"H1657":"Cash EPS Adjustment to Non-Earnings Cash Flow",
#
"RI55_OR":"Unconsolidated Subs - Eq. /Earnings (FY1 override)",
"RI55":"Unconsolidated Subs - Equity/Earnings",
#
"RI503_OR":"Unreal. Gains (losses) - FY1 Override",
"RI503":"FCST: Unrealized Gains (Losses) in Securities",
#
"RI19_OVR":"Preferred Dividends - Custom Override",
"RI19":"Preferred Dividends",
#
# Other Company Data
#
"RI998":"Fiscal Year Month",
"RI29":"Number of Employees",
# Market Section
"RI22":"High Stock Price",
"RI23":"Low Stock Price",
"RI24":"Closing Stock Price",
#
# Market Section
#
"RI700":"High Stock Price - Fiscal Centered (Adjusted)",
"RI701":"Low Stock Price - Fiscal Centered (Adjusted)",
"RI702":"Closing Stock Price - Fiscal Centered (Adjusted)",
#
"RI25":"Common Shares Outstanding",
"RI745":"Current Shares Outstanding",
"RI171":"Fully Dillluted Shares Outstanding - Used for Net Income Forecast",
"RI27":"Adjustment Factor -- Cumulative",
"RI202":"Adjustment Factor -- Cumulative by Payable Date",
"H1111":"Common Shares Outstanding (Split-Adjusted) - Do Not Override",
#
"RI750":"Low Earnings Estimate",
"RI751":"Consensus Earnings Estimate",
"RI752":"High Earnings Estimate",
"RI753":"Number of Analyst Estimates",
"RI760":"EPS Footnote",
#
# Cash EPS Adjustments
#
"H1656":"Cash EPS Trigger (DS)",
"H1657_OR":"Cash EPS Adjustment FY1 override",
"H1657_PCT":"Cash EPS % Adjustment",
"H1657":"Cash EPS Adjustment to Non-earnings cash flow",
"H1658":"Cash EPS Trigger Override",
#
# Merger & Acquisition Data
#
"RI605":"Pooling Goodwill",
#
"RI602":"Cummulative Goodwill Written-Off -- Enter as Negative",
"RI603":"Current Year Goodwill Written-Off -- Enter as Negative",
#
"H1273":"Gross Plant Recaptured",
"H1649":"Cash Flows Recaptured",
"H1648":"Rental Expense Adjustment for Corporate Actions",
#
"H1831B":"Other Sources of Capital (For NGR)",
"H1919_FC":"Foreign Currency Translation to Goodwill (For NGR)",
"H1965":"Other Acquisition Capital (For NGR)",
#
"H1032":"Bounded Capitalized R&D Life",
#
# Refer to "Capitalization of R&D" factsheet for more R&D Layers
#
"RI664":"Acquired (Spin-off) R&D Relayering - 1",
"H1292":"Acquired (Spin-off) R&D Switch (Life) - 1",
"H1292_QTR":"Acquired (Spin-off) R&D Switch (Life) Effective Quarter - 1",
"H1293":"Acquired (Spin-off) R&D Switch (Layer) - 1",
#
"RI665":"Acquired (Spin-off) R&D Relayering - 2",
"H1290":"Acquired (Spin-off) R&D Switch (Life) - 2",
"H1290_QTR":"Acquired (Spin-off) R&D Switch (Life) Effective Quarter - 2",
"H1291":"Acquired (Spin-off) R&D Switch (Layer) - 2",
#
"RI664B":"Acquired (Spin-off) R&D Relayering - 3",
"H1292B":"Acquired (Spin-off) R&D Switch (Life) - 3",
"H1292B_QTR":"Acquired (Spin-off) R&D Switch (Life) Effective Quarter - 3",
"H1293B":"Acquired (Spin-off) R&D Switch (Layer) - 3",
#
"RI665B":"Acquired (Spin-off) R&D Relayering - 4",
"H1290B":"Acquired (Spin-off) R&D Switch (Life) - 4",
"H1290B_QTR":"Acquired (Spin-off) R&D Switch (Life) Effective Quarter - 4",
"H1291B":"Acquired (Spin-off) R&D Switch (Layer) - 4"}



############################################################# ARMA LA SERIE PARA MOSTRAR

# ARMA UNA LISTA SHOW (PARA MOSTRAR) QUE ES EN PRINCIPIO SIMILAR A LA DE LOS CODIGOS PARA PODER SER MODIFICADA, CON TITULOS, ESPACIOS ,ETC
show_conceptos_estandarizados_estado_de_resultado  = []
for k in range(0,len(conceptos_estandarizados_estado_de_resultado )):
    show_conceptos_estandarizados_estado_de_resultado.append(conceptos_estandarizados_estado_de_resultado[k])

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

########################################################################### ACTUALIZA EL DICCIONARIO CON LOS NOMBRES DE TODOS LOS CONCEPTOS AGREGADOS

# ARMA UNA LISTA SHOW (PARA MOSTRAR) EL NOMBRE CORRESPONDIENTE A CADA VARIABLE O CODIGO - SE ARMAR PARA MODER MIDIFICAR Y QUE SE PUEDA METER TITULOS, ESPACIOS ,ETC
#Arma una lista para poner en orden la lista de nombres de conceptos estandarizados
show_nombres_conceptos_estandarizados_estado_de_resultado  = []

#Corre un loop desde 0 hasta la longitud de la lista de conceptos
#Agrega a la lista de SHOW DE NOMBRES los conceptos 
for k in range(0,len(show_conceptos_estandarizados_estado_de_resultado)):
    show_nombres_conceptos_estandarizados_estado_de_resultado.append(conceptos_estandarizados_estado_de_resultado[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_estado_de_resultado)

#####################################################################################################################################################


# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_estado_de_resultado = []

# Agrega a la lista nombbres de los conceptos todos los nombres de los conceptos que estan en el diccionario nombres_de_los_conceptos 
for k in conceptos_estandarizados_estado_de_resultado:
    show_nombres_conceptos_estandarizados_estado_de_resultado.append(nombres_conceptos[k])


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

##############################################################################################################################################
    
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 0, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 1, "" , "Operating Income Before Depreciation")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 2, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 22, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 23, "" , "Operating Income After Depreciation")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 24, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 33, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 34, "" , "Pretax Income")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 35, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 49, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 50, "" , "Net Income After Minority Interest")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 51, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 64, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 66, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 67, "" , "Supplemental Income Statement Data")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 68, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 73, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 87, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 92, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 95, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 99, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 102, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 104, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 106, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 108, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 109, "" , "Supplemental Leases Variables")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 110, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 116, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 117, "" , "Lease Data - Balance Sheet (Do not override these variables. Override BI below in lease data input.)")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 125, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 126, "" , "Lease Data - Income Statement (Do not override these variables. Override BI Below in lease data input.)")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 129, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 130, "" , "Lease Data Input - US GAAP (RI988U=1) - BI Variables")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 131, "" , "Balance Sheet")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 132, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 133, "" , "Assets")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 137, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 138, "" , "Liabilities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 140, "" , "Compustat (FUND_VENDOR_ID=1)")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 143, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 144, "" , "Worldscope (FUND_VENDOR_ID=4)")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 147, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 148, "" , "Income statement")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 149, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 153, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 154, "" , "Lease Data Input - IFRS (RI988U=2) - BI Variables")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 155, "" , "Balance Sheet")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 156, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 157, "" , "Assets")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 161, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 162, "" , "Liabilities")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 165, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 166, "" , "Income statement")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 172, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 173, "" , "Override Slots Forecast Adjustments")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 174, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 177, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 180, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 183, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 186, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 190, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 193, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 196, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 199, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 200, "" , "Other Company Data")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 201, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 204, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 205, "" , "Market Section")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 206, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 210, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 214, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 221, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 222, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 228, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 229, "" , "Cash EPS Adjustments")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 230, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 236, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 237, "" , "Merger & Acquisition")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 238, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 240, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 243, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 247, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 251, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 253, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 254, "" , "Refer to Capitalization of R&D factsheet for more R&D Layers")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 255, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 260, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 265, "" , "")
#
agrega_linea_a_dos_listas(show_conceptos_estandarizados_estado_de_resultado, show_nombres_conceptos_estandarizados_estado_de_resultado, 270, "" , "")




###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_estado_de_resultado)
#len(show_nombres_conceptos_estandarizados_estado_de_resultado)

#len(show_conceptos_estandarizados_estado_de_resultado)==len(show_nombres_conceptos_estandarizados_estado_de_resultado)


#####################################################
################################################ CASH FLOW
##################################################

conceptos_estandarizados_cash_flow = ("RI123",
"RI125",
"RI124",
"RI126",
"RI106",
"RI213",
"RI217",
"RI302",
"RI303",
"RI304",
"RI305",
"RI307",
"RI308",
"RI113",
"RI109",
"RI309",
"RI128",
"RI107",
"RI129",
"RI310",
"RI311",
"RI108",
"Ri115",
"RI127",
"RI111",
"RI114",
"RI301",
"RI414",
"RI312",
"RI313",
"RI314",
"RI274")


nombres_conceptos_estandarizados_cash_flow = {"RI123":"Income Before Extra & Discontinued Operations",
"RI125":"Depreciation and Amortization",
"RI124":"Extra & Discontinued Operations",
"RI126":"Deferred Taxes",
"RI106":"Equity Earnings  Unc Subs",
"RI213":"Sale of PP&E Invest Loss/Gain",
"RI217":"Other Funds From operations",
"RI302":"Accounts Receivable - Decrease (Increase) (S of CF)",
"RI303":"Inventory - Decrease (Increase) (S of CF)",
"RI304":"Accounts Payable & Accrued Liability - Increase",
"RI305":"Income Taxes - Accrued - Increase (Decrease) (S of CF)",
"RI307":"Assets & Liability - Other (Net Change) (S of CF)",
"RI308":"Operating Activities - Net Cash Flow (S of CF)",
"RI113":"Increase in investments",
"RI109":"Sales of investments",
"RI309":"Short-Term investment change",
"RI128":"Capital Expenditure (con signo positivo)",
"RI107":"Sale of PP&E",
"RI129":"Acquisitions (con signo positivo)",
"RI310":"Investment Activities - Oth",
"RI311":"Investment Activities - Net Cash Flow (formula especial)",
"RI108":"Sale of Common & Preferred",
"Ri115":"Purchase of Common & Preferred",
"RI127":"Cash Dividends",
"RI111":"Issuance of Long'Term Debt",
"RI114":"Reduction of Long Term Debt",
"RI301":"Changes in Current Debt",
"RI414":"Stock Benefit of Stock Options",
"RI312":"Financing Activities - Other",
"RI313":"Financing Activities - Net Cash Flow",
"RI314":"Exchange Rate Effect",
"RI274":"Cash & Equivalents Increase'Decrease"}



############################################################# ARMA LA SERIE PARA MOSTRAR

# ARMA UNA LISTA SHOW (PARA MOSTRAR) QUE ES EN PRINCIPIO SIMILAR A LA DE LOS CODIGOS PARA PODER SER MODIFICADA, CON TITULOS, ESPACIOS ,ETC
show_conceptos_estandarizados_cash_flow  = []
for k in range(0,len(conceptos_estandarizados_cash_flow)):
    show_conceptos_estandarizados_cash_flow.append(conceptos_estandarizados_cash_flow[k])

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

########################################################################### ACTUALIZA EL DICCIONARIO CON LOS NOMBRES DE TODOS LOS CONCEPTOS AGREGADOS

# ARMA UNA LISTA SHOW (PARA MOSTRAR) EL NOMBRE CORRESPONDIENTE A CADA VARIABLE O CODIGO - SE ARMAR PARA MODER MIDIFICAR Y QUE SE PUEDA METER TITULOS, ESPACIOS ,ETC
#Arma una lista para poner en orden la lista de nombres de conceptos estandarizados
show_nombres_conceptos_estandarizados_cash_flow  = []

#Corre un loop desde 0 hasta la longitud de la lista de conceptos
#Agrega a la lista de SHOW DE NOMBRES los conceptos 
for k in range(0,len(show_conceptos_estandarizados_cash_flow)):
    show_nombres_conceptos_estandarizados_cash_flow.append(conceptos_estandarizados_cash_flow[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_cash_flow)

#####################################################################################################################################################


# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_cash_flow = []

# Agrega a la lista nombbres de los conceptos todos los nombres de los conceptos que estan en el diccionario nombres_de_los_conceptos 
for k in conceptos_estandarizados_cash_flow:
    show_nombres_conceptos_estandarizados_cash_flow.append(nombres_conceptos[k])


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

##############################################################################################################################################
    
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 0, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 1, "" , "Statement of Cash Flows")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 2, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 3, "" , "Operating Activities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 17, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 18, "" , "Investing Activities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 19, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 28, "" , "")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 29, "" , "Financing Activities")
agrega_linea_a_dos_listas(show_conceptos_estandarizados_cash_flow, show_nombres_conceptos_estandarizados_cash_flow, 30, "" , "")




###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_cash_flow)
#len(show_nombres_conceptos_estandarizados_cash_flow)

#len(show_conceptos_estandarizados_cash_flow)==len(show_nombres_conceptos_estandarizados_cash_flow)



####################### GLOBAL NON-DEPRECIATING ASSETS

conceptos_estandarizados_global_non_depreciating_assets = ("H1441",
"H1422",
"H1445",
"H1449",
"H1417",
"RI601A",
"HT1320",
"H1450",
"H1497",
#NET MONETARY ASSETS
"H1430",
"H1418",
"H1441",
#MONETARY ASSETS
"RI1",
"RI2",
"H1408",
"H1409",
"H1412",
#"H1441",
"H1429",
"H1427",
"RI6",
"RI4",
"RI8",
"H1414",
"H1415",
"H1430",
# mONETARY lIABILITIES eXCLUDING dEBT
"RI70",
"RI71",
"RI72",
"HT1371",
"RI523",
"H1418",
# iNVESTMENTS & ADVANCES
"RI32i",
"RI506",
"H1422",
# INFLATION ADJUSTED INVENTORIES
"RI3",
"RI240",
"H1445",
# INFLATION ADJUSTED LAND
"H1439",
"H1101",
"H1425",
"H1449",
# OTHER ASSETS
"H1419",
"RI290",
"RI300",
"H1448",
"RI152",
"H1413",
"RI524",
"H1424",
"H1417",
# GROSS OPERATING INTANGIBLES (INDEFINITE LIFE)
"HT1319",
"HT1321",
"HT1343",
"HT1320")


nombres_conceptos_estandarizados_global_non_depreciating_assets = {"H1441":"Net Monetary Assets",
"H1422":"Investments & Advances",
"H1445":"Inflation Adjusted Inventories",
"H1449":"Inflation Adjusted Land",
"H1417":"Other-Long Term Assets",
"RI601A":"Other Net Operating Intangibles",
"HT1320":"Gross Operating Intangibles (Indefinite Lived)",
"H1450":"Miscellaneous Non-Depreciating Assets",
"H1497":"Non-Depreciating Assets",
#
"H1430":"Monetary Assets",
"RI397":"Deferred Revenue - Long Term",
"HT1370":"Deferred Revenue Switch (1-exclude from Debt)",
"HT1371":"Deferred Revenue excluded from Debt",
"H1418":"(-) Monetary Liabilities Excluding Debt",
"H1441":"Net Monetary Assets",
#
"RI1":"Cash & Short-Term Investments",
"RI2":"Accounts Receivable",
"H1408":"Estimated Financial Subsidiary Debt",
"H1409":"Industrial Receivables",
"H1412":"Other Current Assets",
"H1429":"Long-Term Monetary Assets",
"H1427":"(-) Pension Assets",
"RI6":"Total Assets",
"RI4":"(-) Total Current Assets",
"RI8":"(-) Net Plant",
"H1414":"(-) Investment & Other Assets",
"H1415":"Undefinied Assets",
"H1430":"Monetary Assets",
# Monetary Liabilities Excluding Debt
"RI70":"Accounts Payable",
"RI71":"Income Taxes Payable",
"RI72":"Other Current Liabilities",
"HT1371":"Deferred Revenue Excluded from Debt",
"RI523":"Long-Term Notes & Payables",
"H1418":"(-) Monetary Liabilities Excluding Debt",
#
# Investments & Advances
#
"RI32i":"Investments & Advances (Other)",
"RI506":"Historical Cost of Investments Marked to Market",
"H1422":"Investments & Advances",
#
# Inflation Adjusted Inventories
#
"RI3":"Inventories",
"RI240":"LIFO Reserve",
"H1445":"Inflation Adjusted Inventories",
#
# Inflation Adjusted Land
#
"H1439":"Land and Improvements",
"H1101":"Land Inflation Factor",
"H1425":"Land Inflation Adjustment",
"H1449":"Inflation Adjusted Land",
#
# Other Assets
#
"H1419":"Other Assets less Deferred Charges",
"RI290":"(-) Pension - Prepaid/Accrued Cost (Overfunded) (subtract if > 0)",
"RI300":"(-) Pension - Prepaid/Accrued Cost (Underfunded) (subtract if > 0)",
"H1448":"(-) Deferred Taxes - Bounded",
"RI152":"Deferred Charges",
"H1413":"Other Assets Less Prepaid Pensions and Deferred Taxes",
"RI524":"(-) Leasing and Guarantee Deposits",
"H1424":"Residual Leasehold Deposits",
"H1417":"Other Assets - Long-Term",
"HT1319":"Net Value of Indefinite Lived Operating Intangibles",
"HT1321":"Accumulated Amortization of Indefinite Lived Operating Intangibles",
"HT1343":"Cumulative Impairment of Indefinite Lived Operating Intangibles",
"HT1320":"Gross Operating Intangibles  (Indefinite Lived)"}

### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df2 = pd.DataFrame(index = conceptos_estandarizados_global_non_depreciating_assets, columns=list_of_columns)
#df2['Concepto'] = pd.Series(nombres_conceptos_estandarizados_global_non_depreciating_assets)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_global_non_depreciating_assets  = []
for k in range(0,len(conceptos_estandarizados_global_non_depreciating_assets)):
    show_conceptos_estandarizados_global_non_depreciating_assets.append(conceptos_estandarizados_global_non_depreciating_assets[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_non_depreciating_assets )

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_global_non_depreciating_assets.insert(0 ,"****")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(1 ,"****")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(2 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(3 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(13 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(14 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(15 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(19 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(20 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(21 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(35 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(36 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(37 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(44 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(45 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(46 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(50 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(51 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(52 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(56 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(57 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(58 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(63 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(64 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(65 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(75 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(76 ,"")
show_conceptos_estandarizados_global_non_depreciating_assets.insert(77 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_global_non_depreciating_assets  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_global_non_depreciating_assets )):
    show_nombres_conceptos_estandarizados_global_non_depreciating_assets.append(conceptos_estandarizados_global_non_depreciating_assets[k])


# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_global_non_depreciating_assets)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_global_non_depreciating_assets  = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_global_non_depreciating_assets:
    show_nombres_conceptos_estandarizados_global_non_depreciating_assets.append(nombres_conceptos[k])


show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(0 ,"****")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(1 ,"Global Non-Depreciating Assets")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(2 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(3 ,"Non-Depreciating Assets Summary")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(13 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(14 ,"Net Monetary Assets")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(15 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(19 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(20 ,"Monetary Assets")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(21 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(35 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(36 ,"Monetary Liabilities Excluding Debt")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(37 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(44 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(45 ,"Investments & Advances")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(46 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(50 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(51 ,"Inflation Adjusted Inventories")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(52 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(56 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(57 ,"Inflation Adjusted Land")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(58 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(63 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(64 ,"Other Assets")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(65 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(75 ,"")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(76 ,"Gross Operating Intangibles (Indefinite Lived)")
show_nombres_conceptos_estandarizados_global_non_depreciating_assets.insert(77 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_global_non_depreciating_assets)
#len(show_nombres_conceptos_estandarizados_global_non_depreciating_assets)

#len(show_conceptos_estandarizados_global_non_depreciating_assets)==len(show_nombres_conceptos_estandarizados_global_non_depreciating_assets)

#################################################################################################



############# GLOBAL DEPRECIATING ASSETS

conceptos_estandarizados_global_depreciating_assets = ("H1207",
"H1231",
"H1278",
"H1279",
"H1243",
"H1252",
"H1213",
"HT1307",
"HI1250",
"H1297",
# Inflation Adjusted Gross Plant
"RI7",
"RI540",
"H1228",
"RI541",
"H1200",
"H1200",
"H1439",
"H1231",
"H1269",
"H1201",
"H1201",
"H1102",
"H1206",
"H1201",
"H1206",
"H1207",
# Capitalized Operating Leases
"RI47",
"H1218",
"H1013",
"H2110_S",
"H1221",
"H1221",
"H1809",
"H1013",
"H2102",
#
"RI524",
"H2102",
"H1241",
#
"H1221",
"H1241",
"H1242",
#
"H1241",
"H1242",
"H1243",
# Capitalized REsearch & Development
"H1246",
"H1032",
"RI388",
"H1502",
#
"H1292",
"H1293",
"RI664",
#
"H1290",
"H1291",
"RI665",
#
"H1292B",
"H1293B",
"RI664B",
#
"H1290B",
"H1291B",
"RI665B",
#
"H1252",
# Inflation Adjusted Finite Intangibles
"HT1329",
"HT1328",
"HT1323",
#
"HT1329",
"HT1328",
"HT1327",
#
"HT1323",
"HT1327",
"HT1348",
#
"HT1348",
"HT1102",
"HT1306",
#
"HT1348",
"HT1306",
"HT1307",
#NON IN PAGE BUT AUXILIAR CALCULATIONS
"H1011",
"H1201",
"H1206",
#
"H1207",
"H1102",
"H1809GP")

nombres_conceptos_estandarizados_global_depreciating_assets = {"H1207":"Inflation Adjusted Gross Plant",
"H1231":"Construction in Progress",
"H1278":"Cummulative Gross Plant Recaptured",
"H1279":"Net Gross Plant Recaptured Inflation Adjustment",
"H1243":"Capitalized Operating Lease",
"H1252":"Capitalized Research & Development",
"H1213":"Adjusted Intangibles",
"HT1307":"Inflation Adjusted Finite Intangibles",
"HI1250":"Miscellaneous Depreciating Assets",
"H1297":"Depreciating Assets",
# Inflation Adjusted GRoss Plant
"RI7":"Gross Plant",
"RI540":"Revaluations",
"H1228":"Remaining FASB121 writedown",
"RI541":"(-) Revaluation of Land",
"H1200":"Gross Plant at Historical Cost",
#
"H1200":"Gross Plant at Historical Cost",
"H1439":"(-) Land and Improvements",
"H1231":"(-) Construction in progress",
"H1269":"Gross FAS 86 Software",
"H1201":"Adjusted Gross Plant",
#
"H1201":"Adjusted Gross Plant",
"H1102":"Gross Plant Inflation Adjustment Factor",
"H1206":"Gross Plant Inflation Adjustment",
#
"H1201":"Adjusted Gross Plant",
"H1206":"Gross Plant Inflation Adjustment",
"H1207":"Inflation Adjusted Gross Plant",
#
# Capitalized Operating Leases
#
"RI47":"Rental expense",
"H1218":"Credit Related Debt Rate Differential",
"H1013":"Asset Life (Leased Assets)",
"H2110_S":"Corp A Bond Yield - Average",
"H1221":"Capitalized Leased Property",
#
"H1221":"Capitalized Leased Property",
"H1809":"Historic Growth Rate",
"H1013":"Asset Life (Leased Assets)",
"H2102":"Debt - Operating Leases",
#
"RI524":"Leasing & Guarantee Deposits",
"H2102":"Debt - Operating Leases",
"H1241":"Inflation Adjusted Leased Property On Balance Sheet",
#
"H1221":"Capitalized Leased Property",
"H1241":"(-) Inflation Adjusted Leased Property On Balance Sheet",
"H1242":"Inflation Adjusted Leased Property Off Balance Sheet",
#
"H1241":"Inflation Adjusted Leased Property On Balance Sheet",
"H1242":"Inflation Adjusted Leased Property Off Balance Sheet",
"H1243":"Capitalized Operating Leases",
#
# Capitalized Research & Development
#
"H1246":"R&D Used (Includes Exploration Expense)",
"H1032":"Life - Capitalized R&D",
"RI388":"In-Process R&D",
"H1502":"Constant Currency Adjustment Factor",
#
"H1292":"Acquired (Spin-off) R&D Swith (Life) - 1",
"H1293":"Acquired (Spin-off) R&D Swith (Layer) - 1",
"RI664":"Acquired (Spin-off) R&D Relayering - 1",
#
"H1290":"Acquired (Spin-off) R&D Swith (Life) - 2",
"H1291":"Acquired (Spin-off) R&D Swith (Layer) - 2",
"RI665":"Acquired (Spin-off) R&D Relayering - 2",
#
"H1292B":"Acquired (Spin-off) R&D Swith (Life) - 3",
"H1293B":"Acquired (Spin-off) R&D Swith (Layer) - 3",
"RI664B":"Acquired (Spin-off) R&D Relayering - 3",
#
"H1290B":"Acquired (Spin-off) R&D Swith (Life) - 4",
"H1291B":"Acquired (Spin-off) R&D Swith (Layer) - 4",
"RI665B":"Acquired (Spin-off) R&D Relayering - 4",
#
"H1252":"Capitalized Research & Development",
#
# Inflation Adjusted Finite Intangibles
#
"HT1329":"Net Value of Finite Operating Intangibles (in Life Calc)",
"HT1328":"Accumulated Amortization of Finite Operating Intangibles (in Life Calc)",
"HT1323":"Gross Value of Finite Operating Intangibles (in Life Calc)",
#
"HT1329":"Net Value of Finite Operating Intangibles (ex Life Calc)",
"HT1328":"Accumulated Amortization of Finite Operating Intangibles (ex Life Calc)",
"HT1327":"Gross Value of Finite Operating Intangibles (ex Life Calc)",
#
"HT1323":"Gross Value of Finite Operating Intangibles (in Life Calc)",
"HT1327":"Gross Value of Finite Operating Intangibles (ex Life Calc)",
"HT1348":"Gross Operating Intangibles (Finite Lived)",
#
"HT1348":"Gross Operating Intangibles (Finite Lived)",
"HT1102":"Finite Intangibles Inflation Adjustment Factor",
"HT1306":"Finite Intangibles Inflation Adjustment",
#
"HT1348":"Gross Operating Intangibles (Finite Lived)",
"HT1306":"Finite Intangibles Inflation Adjustment",
"HT1307":"Inflation Adjusted Finite Intangibles",
#
# NON IN PAGE BUT AUXILIAR CALCULATIONS
#
"H1011":"Life - Gross Plant (integer) -- Asset Life",
#
"H1201":"Adjusted Gross Plant (Historic Cost)",
"H1206":"Gross Plant Inflation Adjustment",
"H1207":"Adjusted Gross Plant (Historic Cost)",
#
#
"H1102":"Inflation adjustment Factor From model",
"H1809GP":"Historic Growth Rate of Gross Plant - Or Historic Nominal average rate of assets increase during asset life"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df3 = pd.DataFrame(index = conceptos_estandarizados_global_depreciating_assets, columns=list_of_columns)
#df3['Concepto'] = pd.Series(nombres_conceptos_estandarizados_global_depreciating_assets)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_global_depreciating_assets  = []
for k in range(0,len(conceptos_estandarizados_global_depreciating_assets)):
    show_conceptos_estandarizados_global_depreciating_assets.append(conceptos_estandarizados_global_depreciating_assets[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_depreciating_assets )

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_global_depreciating_assets.insert(0 ,"****")
show_conceptos_estandarizados_global_depreciating_assets.insert(1 ,"****")
show_conceptos_estandarizados_global_depreciating_assets.insert(2 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(3 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(4 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(15 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(16 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(17 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(23 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(29 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(33 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(37 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(38 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(39 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(45 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(50 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(54 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(58 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(62 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(67 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(71 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(75 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(79 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(83 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(85 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(86 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(87 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(91 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(95 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(99 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(103 ,"")
show_conceptos_estandarizados_global_depreciating_assets.insert(107 ,"")



# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_global_depreciating_assets  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_global_depreciating_assets )):
    show_nombres_conceptos_estandarizados_global_depreciating_assets.append(conceptos_estandarizados_global_depreciating_assets[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_global_depreciating_assets)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_global_depreciating_assets  = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_global_depreciating_assets:
    show_nombres_conceptos_estandarizados_global_depreciating_assets.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(0 ,"****")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(1 ,"Global Depreciating Assets")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(2 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(3 ,"Depreciating Assets Summary")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(4 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(15 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(16 ,"Inflation Adjusted Gross Plant")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(17 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(23 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(29 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(33 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(37 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(38 ,"Capitalized Operating Leases")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(39 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(45 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(50 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(54 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(58 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(62 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(67 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(71 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(75 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(79 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(83 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(85 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(86 ,"Inflation Adjusted Finite Intangible")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(87 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(91 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(95 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(99 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(103 ,"")
show_nombres_conceptos_estandarizados_global_depreciating_assets.insert(107 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_global_depreciating_assets)
#len(show_nombres_conceptos_estandarizados_global_depreciating_assets)

#len(show_conceptos_estandarizados_global_depreciating_assets)==len(show_nombres_conceptos_estandarizados_global_depreciating_assets)





############# CFROI AUDIT

conceptos_estandarizados_cfroi_audit_and_valuation = ("H1499",
"H1500",
"H1699",
"H1056",
"H2312",
#
"H2313",
"H2316",
"H2415",
"H2416",
#
"H1800",
"H1829",
"H1829GP",
"H1809",
"H1913",
"H1860",
"H2417",
"H2418",
#
"H4195",
"H2425",
"H2425G",
"H2413",
#
"H2409",
"H2410",
"H2411",
#
"H2412",
"H2411",
"H2413",
#Valuation Output
"H2441",
"H2442",
"H2440",
"H2443",
"H2421",
"H2444",
"H2446",
"H2447",
"H1111",
"H2445",
#
"H1121",
"H1123",
"H1124",
# NOT IN PAGE , ADDITIONAL CALCULATIONS
"H2460",
#
"H2460",
"H2423",
"H2425",
"H2424",
"H2437",
"H2427",
"H2425G",
"H2416",
"H2415",
"H2413",
"H2450",
"H2430",
"H4405",
"H2488",
"FOVRH2437",
"HS2450",
"H1055",
"H2417",
"H2418",
"H2428",
"H4431",
"H2429",
#
"H2460",
"H2468",
"HS2450",
#
#
"HS2450",
"H2468",
"H2469",
"H2442")

nombres_conceptos_estandarizados_cfroi_audit_and_valuation = {"H1499":"Non-Depreciating Assets",
"H1500":"Inflation Adjusted Gross Investment",
"H1699":"Inflation Adjusted Cash Flow",
"H1056":"Asset Project Life (CFROI)",
"H2312":"CFROI",
# CFROI Used in Valuation
# ----------------------
"H2313":"CFROI Passed to Val (Exist Asts w/Intangibles)",
"H2316":"CFROI Passed to Val (Future Investments)",
"H2415":"CFROI Existing - Passed Valuation",
"H2416":"CFROI Future - Passed Valuation - VAL: ROI Future",
# Valuation Factors
"H1800":"Industry Historic Growth Rate",
"H1829":"Adjusted, Historical Growth Rate of Deprec Assets, %",
"H1829GP":"Adjusted, Historical Growth Rate of Gross Plant, %",
"H1809":"Historic Growth Rate",
"H1913":"Normalized Growth Rate, Spot",
"H1860":"Normalized Growth Rate (BOY)",
"H2417":"Growth Existing - Passed to Valuation",
"H2418":"Growth Future - Passed to Valuation",
# Fade - See Fade Factsheets
"H4195":"eCAP Score",
"H2425":"CFROI Fade Window",
"H2425G":"Growth Fade Window",
"H2413":"Company-Specific Discount Rate",
# Audit of Company Specific Discount Rate
"H2409":"Size DR Differential",
"H2410":"Leverage DR Differential",
"H2411":"Discount Rate Differential",
#
"H2412":"Country Discount Rate",
"H2411":"Discount Rate Differential",
"H2413":"Company-Specific Discount Rate",
#
# Valuation Output
#
"H2441":"Value of Existing Assets",
"H2442":"Value of Future Assets",
"H2440":"Market Value of Investments",
"H2443":"Total Economic Value",
"H2421":"Market Value of Debt & Equivalents (-)",
"H2444":"Economic Equity Value",
"H2446":"Value of Minority Interest (-)",
"H2447":"Economic Common Equity Value",
"H1111":"Adjusted Shares Outstanding (/)",
"H2445":"HOLT Value Per Share",
#
"H1121":"Adjusted High Price",
"H1123":"Adjusted Low Price",
"H1124":"Adjusted Closing Price",
#
# NOT IN PAGE, AUXILIAR CALCULATIONS
#
"H2460":"PV of Existing Assets (Valuation Call)",
#
"H2460":"PV of Existing Assets (Valuation Call) - CALCULATED",
"H2423":"VAL: Inf Adjusted Gross Investment",
#"H2425":"VAL: ROI hold period",
"H2424":"VAL: Non Depreciating Assets",
"H2437":"CFROI Fade Factor",
"H2427":"VAL: ROI FADE-TO",
#"H2425G":"VAL: Growth Hold Period",
"H2416":"CFROI Future - Passed Valuation - VAL: ROI Future",
"H2415":"CFROI used in Valuation",
"H2413":"Discount rate - company specific",
"H2450":"Replacement CFROI used in Valuation",
"H2430":"VAL: ROI Fade exponential fade rate",
"H4405":"DR as 1-year rate",
"H2488":"Sustainable Growth Rate FY5",
"FOVRH2437":"Sensitivity: Fade Rate",
"HS2450":"Replacement CFROI Override pseudo-scalar",
"H1055":"Asset Project Life",
"H2417":"VAL: Growth Existing",
"H2418":"Normalized Growth Rate used in Valuation",
"H2428":"VAL: Growth Fade-To",
"H4431":"Exponential Fade Window Years",
"H2429":"VAL: Disc Rate Fade-To",
#
"H2460":"PV of Existing Assets (Valuation Call)",
"H2468":"NPV of Replacement Investment (Valuation Call)",
"HS2450":"Replacement CFROI Override pseudo-scalar",
#
"HS2450":"Replacement CFROI Override pseudo-scalar",
"H2468":"NPV of Replacement Investment (Valuation Call)",
"H2469":"NPV of Growth Investment (Valuation Call)",
"H2442":"Value of Future Assets - NPV of Future Investments"}

### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
list_of_columns = ['Concepto']
# Crea el dataframe
df4 = pd.DataFrame(index = conceptos_estandarizados_cfroi_audit_and_valuation , columns=list_of_columns)
df4['Concepto'] = pd.Series(nombres_conceptos_estandarizados_cfroi_audit_and_valuation )


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_cfroi_audit_and_valuation  = []
for k in range(0,len(conceptos_estandarizados_cfroi_audit_and_valuation)):
    show_conceptos_estandarizados_cfroi_audit_and_valuation.append(conceptos_estandarizados_cfroi_audit_and_valuation[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_cfroi_audit_and_valuation)

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(0 ,"****")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(1 ,"****")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(2 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(3 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(9 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(10 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(11 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(16 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(17 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(18 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(27 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(28 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(29 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(34 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(35 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(36 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(40 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(44 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(45 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(46 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(57 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(61 ,"")
show_conceptos_estandarizados_cfroi_audit_and_valuation.insert(63 ,"")



# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation )):
    show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.append(conceptos_estandarizados_cfroi_audit_and_valuation[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_cfroi_audit_and_valuation)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation  = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_cfroi_audit_and_valuation:
    show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(0 ,"****")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(1 ,"CFROI Audit And Valuation")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(2 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(3 ,"CFROI Calculation")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(9 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(10 ,"CFROI Used in Valuation")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(11 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(16 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(17 ,"Valuation Factors")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(18 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(27 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(28 ,"Fade - See Fade Factsheets")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(29 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(34 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(35 ,"Audit of Company Specific Discount Rate")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(36 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(40 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(44 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(45 ,"Valuation Output")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(46 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(57 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(61 ,"")
show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation.insert(63 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_cfroi_audit_and_valuation)
#len(show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation)

#len(show_conceptos_estandarizados_cfroi_audit_and_valuation)==len(show_nombres_conceptos_estandarizados_cfroi_audit_and_valuation)



###############################################
############################################## GLOBAL INFLATION ADJUSTMENT

conceptos_estandarizados_global_inflation_adjusted_cash_flow = ("H1609",
"H1659",
"H1697",
#
# Earnings Cash Flow
#
"H1608",
"RI17",
"RI388",
"H1605",
"H1605",
"H1601",
"H1602",
"H1248",
"H1653",
"H1630",
"H1609",
#
# Non-Earnings Cash Flow
#
"RI14",
"HT1345",
"RI47",
"H1657",
"HT1322",
"RI49",
"H1612",
"H1619",
"H1629",
"H1639",
"H1640",
"H1650",
"H1649",
"H1249",
"H1659",
#
# Adjusted Interest Expense
#
"RI15",
"H1611",
"RI47",
"H1612",
#
# Monetary Holding Gain
#
"H1442",
"H1616",
"H1617",
#
"H1609",
"RI14",
"H1612",
"HT1345",
"H1615",
#
"H1617",
"H1615",
"H1619",
#
# LIFO Charge to FIFO Inventories
#
"RI3",
"H1621",
"H1622",
#
"H1628",
"H1620",
"SYSC3",
"H1623",
#
"H1623",
"H1626",
"H1629",
#
"H1624",
#
# Net Pension Expense Cash Flow Adjustment 
#
"H1635",
"RI286",
"RI294",
"RI332",
"H1631",
"RI330",
"RI561",
"RI292",
"H1633",
"H469T",
"H1638",
"H1636",
"H1639",
#
# Change in Other Risk Provision
#
"SYSC14",
"H1433",
"H1640")


nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow = {"H1609":"Earnings Cash Flow",
"H1659":"Non-Earnings Cash Flow",
"H1697":"Inflation Adjusted Cash Flow",
#
# Earnings Cash Flow
# 
"H1608":"Net Income",
"RI17":"Special Items",
"RI388":"In-Process R&D",
"H1605":"Special Items After In-Process R&D",
"H1605":"Special Items After In-Process R&D",
"H1601":"Total Effective Tax Rate",
"H1602":"Tax on Special Items",
"H1248":"R&D Adjustement to Net Income",
"H1653":"Investment Cash Flow",
"H1630":"Stock Option Expense Cash Flow Adjustment",
"H1609":"Earnings Cash Flow",
#
# Non-Earnings Cash Flow
#
"RI14":"Depreciation and Amortization",
"HT1345":"Amortization of FAS 86 Software",
"RI47":"Rental Expense",
"H1657":"Cash EPS Adjustment to Non-Earnings Cash Flow",
"HT1322":"Operating Amortization (excluded from Cash Flow)",
"RI49":"Minority Interest (Income Statement)",
"H1612":"Adjusted Interest Expense",
"H1619":"Monetary Holding Gain",
"H1629":"LIFO Charge to FIFO Inventory",
"H1639":"Net Pension Expense Cash Flow Adjustment",
"H1640":"(+)/(-) Curr Yr Change in Other Risk Provisions",
"H1650":"Miscellaneous Cash Flow",
"H1649":"Partial Year Cash Flow Adj. (Purchase Accounting)",
"H1249":"Capitalized R&D Amortization",
"H1659":"Non-Earnings Cash Flow",
#
# Adjusted Interest Expense
#
"RI15":"Interest Expense (Gross)",
"H1611":"(-) Financial Sub Interest Expense",
"RI47":"(-) Interest Capitalized",
"H1612":"Adjusted Interest Expense",
#
# Monetary Holding Gain
#
"H1442":"Net Monetary Assets for BOY Valuation",
"H1616":"(x) Percent Change in GNP Deflator",
"H1617":"Monetary Holding Gain Estimate",
#
"H1609":"Earnings Cash Flow",
"RI14":"Depreciation & Amortization",
"H1612":"Adjusted Interest Expense",
"HT1345":"Amortization of FAS 86 Software",
"H1615":"Size Limit Test for Monetary Holding Gain",
#
"H1617":"Monetary Holding Gain Estimate",
"H1615":"Size Limit Test for Monetary Holding Gain",
"H1619":"Monetary Holding Gain (Bounded by Size Limit)",
#
# LIFO Charge to FIFO Inventories
#
"RI3":"Inventories",
"H1621":"(x) % of Inventories on FIFO ",
"H1622":"Inventories on FIFO",
#
"H1628":"Inventories on FIFO for BOY Valuation",
"H1620":"(x) % Change in PPI",
"SYSC3":"Producer Price Index",
"H1623":"Estimated LIFO Charge to FIFO Inventories",
#
"H1623":"Estimated LIFO Charge to FIFO Inventories",
"H1626":"Size Limit Test for LIFO Charge",
"H1629":"LIFO Charge to FIFO Inventories",
#
"H1624":"Industry Switch to Disable LIFO Charge",
#
# Net Pension Expense Cash Flow Adjustment
# 
"H1635":"Pension Cash Flow Adjustment",
"RI286":"Pension-PBO (Overfunded)",
"RI294":"Pension-PBO (Underfunded)",
"RI332":"Pension Plans Interest Cost",
"H1631":"Estimated FASB 106 Interest Rate",
"RI330":"Postretirement Benefit Asset (Liab)(Net)",
"RI561":"Postretirement Service Cost",
"RI292":"Periodic Postretirement Benefit Cost (Net)",
"H1633":"Estimated Postretirement Interest Cost",
"H469T":"Pension Liability",
"H1638":"Statutory Pension Discount Rate",
"H1636":"Pension Interest Expense",
"H1639":"Net Pension Expense Cash Flow Adjustment",
#
# Change in Other Risk Provision
#
"SYSC14":"Corp. Income Tax Rt.",
"H1433":"Statutory Federal Income Tax Rate",
"H1640":"Curr Yr Change in Other Risk Provisions"}

### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
list_of_columns = ['Concepto']
# Crea el dataframe
df5 = pd.DataFrame(index = conceptos_estandarizados_global_inflation_adjusted_cash_flow, columns=list_of_columns)
df5['Concepto'] = pd.Series(nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_global_inflation_adjusted_cash_flow = []
for k in range(0,len(conceptos_estandarizados_global_inflation_adjusted_cash_flow)):
    show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.append(conceptos_estandarizados_global_inflation_adjusted_cash_flow[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(0 ,"****")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(1 ,"****")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(2 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(3 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(7 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(8 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(9 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(21 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(22 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(23 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(39 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(40 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(41 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(46 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(47 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(48 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(52 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(58 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(62 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(63 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(64 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(68 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(73 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(77 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(79 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(80 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(81 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(82 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(83 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(97 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(98 ,"")
show_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(99 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow )):
    show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.append(conceptos_estandarizados_global_inflation_adjusted_cash_flow[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_global_inflation_adjusted_cash_flow:
    show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(0 ,"****")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(1 ,"Global Inflation Adjusted Cash Flow")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(2 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(3 ,"Inflation Adjusted Gross Cash Flow Summary")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(7 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(8 ,"Earnings Cash Flow")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(9 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(21 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(22 ,"Non-Earnings Cash Flow")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(23 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(39 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(40 ,"Adjusted Interest Expense")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(41 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(46 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(47 ,"Monetary Holding Gain")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(48 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(52 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(58 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(62 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(63 ,"LIFO Charge to FIFO Inventories")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(64 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(68 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(73 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(77 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(79 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(80 ,"Net Pension Expense Cash Flow Adjustment")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(81 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(82 ,"Periodic Pension Cost (Net)")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(83 ,"Pension Plans - Service Cost")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(97 ,"")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(98 ,"Change in Other Risk Provision")
show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow.insert(99 ,"")





# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)
#len(show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

#len(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)==len(show_nombres_conceptos_estandarizados_global_inflation_adjusted_cash_flow)



###############################################
############################################## GROSS PLANT LIFE

conceptos_estandarizados_gross_plant_life = ("H1005",
"H1015",
"H1006T",
#
"H1006",
#
"H1001",
"H1002",
"H1003",
#
"H1007",
"H1011",
#
# Straight Line Life Data and Calculation
#
"RI7",
"H1439",
"H1231",
"H1201",
# 
"RI14",
"RI65",
"H1202",
#
"H1201",
"H1202",
"H1005",
#
"H1021",
"RI540",
"H1022",
"H1023",
"H1024",
"RI542",
"RI543",
"RI544",
"RI545",
"H1014",
"H1081",
"H1082",
"H1083",
"H1084",
"H1085",
"H1086",
"H1087",
"H1222",
"AVG",
"H1002",
"H1015")

nombres_conceptos_estandarizados_gross_plant_life = {"H1005":"Gross Plant Life - Straight Line",
"H1015":"Gross Plant Life - Weighted Average",
"H1006T":"Life Calculation Method (1005 = Straight Line)",
#
"H1006":"Gross Plant Life - 3-Year Median",
#
"H1001":"Industry Plant Life - Lower Bound",
"H1002":"Industry Plant Life - Average Bound",
"H1003":"Industry Plant Life - Upper Bound",
#
"H1007":"Gross Plant Life 3-Year Median Bounded by Gross Investment",
"H1011":"Gross Plant Life 3-Year Median Bounded by Gross Investment (Merger)",
#
# Straight Line Life Data and Calculation
#
"RI7":"Gross Plant",
"H1439":"Land and Improvements",
"H1231":"Construction in Progress",
"H1201":"Adjusted Gross Plant",
#
"RI14":"Depreciation and Amortization",
"RI65":"Amortization of Intangibles",
"H1202":"Depreciation of Gross Plant",
#
"H1201":"Adjusted Gross Plant",
"H1202":"Depreciation of Gross Plant",
"H1005":"Gross Plant Life - Straight Line",
#
# Weighted Average Life and Calculation
#
"H1021":"Buildings Used",
"RI540":"Revaluation of Fixed Assets",
"H1022":"Buildings",
"H1023":"Machinery and Tools",
"H1024":"Other Fixed Assets",
"RI542":"Vehicles",
"RI543":"Vessels & Aircrafts",
"RI544":"Long Leasehold Property ",
"RI545":"Short Leasehold Property ",
"H1014":"Depreciable Asset Sum",
"H1081":"Building Life",
"H1082":"Machinery Life",
"H1083":"Other Fixed Assets Life",
"H1084":"Vehicles Life",
"H1085":"Vessels & Aircraft Life",
"H1086":"Long Leasehold Life ",
"H1087":"Short Leasehold Life ",
"H1222":"Weighted Average Life Calculated Depreciation",
"AVG":"Gig Average Flag",
"H1002":"Gig Average Project Life",
"H1015":"Gross Plant Life - Weighted Average"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df6 = pd.DataFrame(index = conceptos_estandarizados_gross_plant_life, columns=list_of_columns)
#df6['Concepto'] = pd.Series(nombres_conceptos_estandarizados_gross_plant_life)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_gross_plant_life = []
for k in range(0,len(conceptos_estandarizados_gross_plant_life)):
    show_conceptos_estandarizados_gross_plant_life.append(conceptos_estandarizados_gross_plant_life[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_gross_plant_life.insert(0 ,"****")
show_conceptos_estandarizados_gross_plant_life.insert(1 ,"****")
show_conceptos_estandarizados_gross_plant_life.insert(2 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(6 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(8 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(12 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(15 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(16 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(17 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(22 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(26 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(30 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(31 ,"")
show_conceptos_estandarizados_gross_plant_life.insert(32 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_gross_plant_life  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_gross_plant_life )):
    show_nombres_conceptos_estandarizados_gross_plant_life.append(conceptos_estandarizados_gross_plant_life[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_gross_plant_life)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_gross_plant_life = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_gross_plant_life:
    show_nombres_conceptos_estandarizados_gross_plant_life.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_gross_plant_life.insert(0 ,"****")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(1 ,"Gross Plant Life")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(2 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(6 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(8 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(12 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(15 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(16 ,"Straight Line Life Data and Calculation")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(17 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(22 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(26 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(30 ,"")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(31 ,"Weighted Average Life Data and Calculation")
show_nombres_conceptos_estandarizados_gross_plant_life.insert(32 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_gross_plant_life)
#len(show_nombres_conceptos_estandarizados_gross_plant_life)

#len(show_conceptos_estandarizados_gross_plant_life)==len(show_nombres_conceptos_estandarizados_gross_plant_life)




###############################################
##############################################PROJECT LIFE

conceptos_estandarizados_project_life = ("H1055",
"H1056",
#
"H1207",
"H1007",
"H1041",
#
"H1221",
"H1013",
"H1042",
#
"H1252",
"H1032",
"H1043",
#
"H1041",
"H1042",
"H1043",
"HT1335",
"H1045",
#
"H1207",
"H1221",
"H1252",
"H1046",
#
"H1046",
"H1045",
"H1051",
#
"H1051",
"H1053",
"H1055",
"H1056")


nombres_conceptos_estandarizados_project_life = {"H1055":"Asset Project Life Used in Valuation",
"H1056":"Asset Project Life Used in CFROI Calculation",
#
"H1207":"Inflation Adjusted Gross Plant",
"H1007":"Gross Plant Life 3-Year Median Bounded",
"H1041":"Implied Depreciation of Gross Plant for Asset Life",
#
"H1221":"Inflation Adjusted Gross Leased Property",
"H1013":"Lease Life",
"H1042":"Implied Depreciation of Leased Assets for Project Life",
#
"H1252":"Current $ Gross Capitalized R&D",
"H1032":"Capitalized R&D Life",
"H1043":"Implied Amortization of Capitalized R&D for Project Life",
#
"H1041":"Implied Depreciation of Gross Plant for Project Life",
"H1042":"Implied Depreciation of Leased Assets for Project Life",
"H1043":"Implied Amortization of Capitalized R&D for Project Life",
"HT1335":"Implied Depreciation of Finite Intangibles for Asset Life",
"H1045":"Implied Depreciation & Amortization for Project Life",
#
"H1207":"Inflation Adjusted Gross Plant",
"H1221":"Inflation Adjusted Gross Leased Property",
"H1252":"Current $ Gross Capitalized R&D",
"H1046":"Depreciable Asset Sum for Project Life",
#
"H1046":"Depreciable Asset Sum for Project Life",
"H1045":"Implied Depreciation & Amortization for Project Life",
"H1051":"Asset Project Life",
#
"H1051":"Asset Project Life",
"H1053":"Asset Project Life - Integer",
"H1055":"Asset Project Life Used in Valuation",
"H1056":"Asset Project Life Used in CFROI Calculation"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df7 = pd.DataFrame(index = conceptos_estandarizados_project_life, columns=list_of_columns)
#df7['Concepto'] = pd.Series(nombres_conceptos_estandarizados_project_life)

#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_project_life = []
for k in range(0,len(conceptos_estandarizados_project_life)):
    show_conceptos_estandarizados_project_life.append(conceptos_estandarizados_project_life[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_project_life.insert(0 ,"****")
show_conceptos_estandarizados_project_life.insert(1 ,"****")
show_conceptos_estandarizados_project_life.insert(2 ,"")
show_conceptos_estandarizados_project_life.insert(5 ,"")
show_conceptos_estandarizados_project_life.insert(9 ,"")
show_conceptos_estandarizados_project_life.insert(13 ,"")
show_conceptos_estandarizados_project_life.insert(17 ,"")
show_conceptos_estandarizados_project_life.insert(23 ,"")
show_conceptos_estandarizados_project_life.insert(28 ,"")
show_conceptos_estandarizados_project_life.insert(32 ,"")






# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_project_life  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_project_life )):
    show_nombres_conceptos_estandarizados_project_life.append(conceptos_estandarizados_project_life[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_project_life)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_project_life = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_project_life:
    show_nombres_conceptos_estandarizados_project_life.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_project_life.insert(0 ,"****")
show_nombres_conceptos_estandarizados_project_life.insert(1 ,"Project Life")
show_nombres_conceptos_estandarizados_project_life.insert(2 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(5 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(9 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(13 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(17 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(23 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(28 ,"")
show_nombres_conceptos_estandarizados_project_life.insert(32 ,"")



# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_project_life)
#len(show_nombres_conceptos_estandarizados_project_life)

#len(show_conceptos_estandarizados_project_life)==len(show_nombres_conceptos_estandarizados_project_life)


###############################################
############################################## INTANGIBLES FIX

conceptos_estandarizados_intangibles_fix_factsheet = ("RI33",
"RI204",
#
# LICENSES DATA
#
"LIC_METHOD",
#
"RI616",
"RI617",
"RI618",
"RI621",
#
# CAPITALIZED SOFTWARE DATA: 
#
"RI69",
"H1269",
"RI537",
"RI536",
"HT1345",
#
# Software in Intangible Assets:
#
"RI537",
"RI536B",
"RI532",
#
# Operating Intangibles
#
"HT1349",
"HT1307",
#
# Intangibles included in Non-Depreciating Assets:
#
"HT1320",
"RI601A",
"HT1349",
#
# 3. Gross Indefinite Life Operating Intangibles
#
#
# Gross Indefinite Life Operating Intangibles - Manual Input  
#
"HT1321M",
"HT1319M",
#
# Gross Indefinite Life Operating Intangibles - Summary
#
"HT1320",
"HT1321",
"HT1319",
#
"HT1342",
"HT1343",
#
# Net Operating Intangibles
#
"RI601A",
"HT1322",
#
# Intangibles included in Depreciating Assets
#
"HT1323",
"HT1327",
"HT1348",
#
"HT1348",
"HT1306",
"HT1307",
#
# 4. Gross Finite Life Operating Intangibles (in Life)
#
# Other Finite Life Operating Intangibles (in Life) - Manual Input
#
"HT1324M",
"HT1325M",
"HT1326M",
#
# Other Finite Life Operating Intangibles (in Life) - Summary
#
"HT1323",
"HT1324",
"HT1325",
#
"HT1323",
"HT1326",
"HT1330",
#
"HT1331",
#
"HT1333",
"HT1332",
"HT1334",
#
#
# 5. Gross Finite Life Operating Intangibles (Not in Life)
#
# Other Gross Finite Life Operating Intangibles (Not in Life) - Manual Input
#
"HT1328M",
"HT1329M",
#
# Gross Finite Life Operating Intangibles (ex- Life calc) - Summary
#
"HT1327",
"HT1328",
"HT1329",
#
# Unidentified Net Intangibles
#
"RI33",
"RI204",
"RI601A",
"HT1319",
"HT1325",
"HT1329",
"HT1483",
#
# Capitalized Software in Other Assets
#
"RI69",
"H1269",
"RI537",
"RI536",
#
"HT1345",
"HT1347",
"HT1346")


nombres_conceptos_estandarizados_intangibles_fix_factsheet = {"RI33":"Intangibles (net)",
"RI204":"Goodwill",
#
# LICENSES DATA:
#
"LIC_METHOD":"License Method (0=Off / 3=Indef.Life / 4=Finite In-Life / 5=Finite Ex-Life)",
#
"RI616":"Licenses - Gross",
"RI617":"Licenses - Accumulated Depreciation",
"RI618":"Licenses - Net",
"RI621":"Licenses Amortization",
#
# CAPITALIZED SOFTWARE DATA:
#
#
"SOFT_METHO":"Software Method (0=Off / 3=Indef.Life / 4=Finite In-Life / 5=Finite Ex-Life)",
# 
# Software in Other Assets (old US clasification):
#
"RI69":"Assets (Other)",
"H1269":"Gross FAS 86 Software",
"RI537":"FAS 86 Accumulated Depreciation",
"RI536":"FAS 86 Software - Net",
"HT1345":"Amortization of Fas 86 Software",
#
# Software in Intangible Assets:
#
"RI537":"FAS 86 Accumulated Depreciation",
"RI536B":"Cap. Software (in Intangible) - Net",
"RI532":"Amortization of Capitalized Software",
#
# Operating Intangibles:
#
"HT1349":"Intangibles Included in Non-Depreciating Assets",
"HT1307":"Intangibles Included in Depreciating Assets",
#
# Intangibles included in Non-Depreciating Assets:
#
"HT1320":"Gross Operating Intangibles (Indefinite Life)",
"RI601A":"Other Net Operating Intangibles",
"HT1349":"Non-Depreciating Intangible Assets",
#
# 3. Gross Indefinite Life Operating Intangibles
#
# Gross Indefinite Life Operating Intangibles - Manual Input  
#
"HT1321M":"Accumulated Amortization -- Gross Op Intangibles (Indefinite) - Manual Input ",
"HT1319M":"Net Value of Gross Op Intangibles (Indefinite) - Manual Input",
#
# Gross Indefinite Life Operating Intangibles - Summary
#
"HT1320":"Gross Operating Intangibles (Indefinite Life)",
"HT1321":"Accumulated Amortization of Gross Operating Intangibles (Indefinite Life) ",
"HT1319":"Net Value of Gross Operating Intangibles (Indefinite Life)",
#
"HT1342":"Current Impairment of Intangibles x Life Calc",
"HT1343":"Cumulative Impairment of indefinite-Lived Intangibles",
#
# Net Operating Intangibles
#
"RI601A":"Other Net operating Intangibles",
"HT1322":"Operating Amortization (excluded from Gross Cash Flow)",
#
# Intangibles Included in Depreciating Assets
#
"HT1323":"Gross Finite Operating Intangibles (in Life Calc)",
"HT1327":"Gross Finite Operating Intangibles (ex Life Calc)",
"HT1348":"Gross Finite Life Operating Intangibles",
#
"HT1348":"Gross Finite Life Operating Intangibles",
"HT1306":"Finite Life Intangibles Inflation Adjustment",
"HT1307":"Inflation Adjusted Finite Life Intagibles",
#
# 4. Gross Finite Life Operating Intangibles (in Life)
#
# Other Finite Life Operating Intangibles (in Life) - Manual Input
#
"HT1324M":"Accumulated Amortization - Finite Operating Intangibles (in Life Calc) - Manual Input",
"HT1325M":"Net Value of Gross Finite Op Intangibles (in Life Calc) - Manual Input",
"HT1326M":"Amortization Expense - Finite Gross intangibles in life calc - Manual Input",
#
# Gross Finite Life Operating Intangibles (in Life) - Summary
#
"HT1323":"Gross Finite Life Intangibles (in Life Calc)",
"HT1324":"Accumulated Amortization of Finite Life Operating Intangibles (in Life Calc)",
"HT1325":"Net Value of Gross Finite Life Operating Intangibles (in Life Calc)",
#
"HT1323":"Gross Finite Life Operating Intangibles (in Life Calc)",
"HT1326":"Amortization Expense - Finite Life Operating Intangibles in Life calc)",
"HT1330":"Finite Life Operating Intangibles - Calculate Life",
#
"HT1331":"Finite Life Operating Intangibles Life - 3year Median",
#
"HT1333":"Finite Life Operating Intangibles - High Project Life",
"HT1332":"Finite Life Operating Intangibles - Low Project Life",
"HT1334":"Finite Life Operating Intangibles - Project Life 3-Year Bounded Median",
#
# 5. Gross Finite Life Operating Intangibles (Not in Life)
#
# Other Gross Finite Life Operating Intangibles (Not in Life) - Manual Input
#
"HT1328M":"Accumulated Amortization - Finite Operating Intangibles (ex Life Calc) - Manual Input",
"HT1329M":"Net Value of Gross Finite Op Intangibles (ex Life Calc) - Manual Input",
#
# Gross Finite Life Operating Intangibles (ex Life Calc) - Summary",
# 
"HT1327":"Gross Finite Life Operating Intangibles (ex Life Calc)",
"HT1328":"Accumulated Amortization of Finite Life Operating Intangibles (ex Life Calc)",
"HT1329":"Net Value of Finite Life Operating Intangibles (ex Life Calc)",
#
# Unidentified Net Intangibles
#
"RI33":"Intangibles (net)",
"RI204":"Goodwill (net)",
"RI601A":"Other Net Operating Intangibles",
"HT1319":"Net Value of Indefinite Life Operating Intangibles",
"HT1325":"Net Value of Finite Operating Intangibles (in Life Calc)",
"HT1329":"Net Value of Finite Operating Intangibles (ex Life Calc)",
"HT1483":"Unidentified Net Intangibles",
#
# Capitalized Software in Other Assets
#
"RI69":"Assets (Other)",
"H1269":"Gross Capitalized Software",
"RI537":"Accumulated Depreciation of Capitalized Software",
"RI536":"Net Capitalized Software",
#
"HT1345":"Amortization of Capitalized Software",
"HT1347":"Capitalized Software Cash EPS Trigger (Dip Switch)",
"HT1346":"Capitalized Software Cash EPS Trigger Override"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
list_of_columns = ['Concepto']
# Crea el dataframe
df8 = pd.DataFrame(index = conceptos_estandarizados_intangibles_fix_factsheet, columns=list_of_columns)
df8['Concepto'] = pd.Series(nombres_conceptos_estandarizados_intangibles_fix_factsheet)

#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_intangibles_fix_factsheet = []
for k in range(0,len(conceptos_estandarizados_intangibles_fix_factsheet)):
    show_conceptos_estandarizados_intangibles_fix_factsheet.append(conceptos_estandarizados_intangibles_fix_factsheet[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_intangibles_fix_factsheet.insert(0 ,"****")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(1 ,"****")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(2 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(3 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(4 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(7 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(8 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(9 ,"")
#show_conceptos_estandarizados_intangibles_fix_factsheet.insert(10 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(11 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(16 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(17 ,"")
#show_conceptos_estandarizados_intangibles_fix_factsheet.insert(18 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(19 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(20 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(25 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(26 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(27 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(31 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(32 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(33 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(36 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(37 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(38 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(42 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(43 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(44 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(45 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(46 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(49 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(50 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(51 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(55 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(58 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(59 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(60 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(63 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(64 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(65 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(69 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(70 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(74 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(75 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(76 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(77 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(78 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(82 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(83 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(84 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(88 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(92 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(94 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(98 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(99 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(100 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(101 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(102 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(105 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(106 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(107 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(111 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(112 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(113 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(121 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(122 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(123 ,"")
show_conceptos_estandarizados_intangibles_fix_factsheet.insert(128 ,"")







# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_intangibles_fix_factsheet  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_intangibles_fix_factsheet )):
    show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.append(conceptos_estandarizados_intangibles_fix_factsheet[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_intangibles_fix_factsheet)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_intangibles_fix_factsheet:
    show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(0 ,"****")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(1 ,"Intangibles Fix Factsheet")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(2 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(3 ,"Intangibles Summary")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(4 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(7 ,"LICENSES DATA:")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(8 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(9 ,"")
#show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(10 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(11 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(16 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(17 ,"CAPITALIZED SOFTWARE DATA:")
#show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(18 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(19 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(20 ,"Software in Other Assets (old US Classification):")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(25 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(26 ,"Software in Intangible Assets")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(27 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(31 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(32 ,"Operating Intangibles:")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(33 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(36 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(37 ,"Intangibles included in Non-Depreciating Assets:")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(38 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(42 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(43 ,"3.Gross Indefinite Life Operating Intangibles")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(44 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(45 ,"Other Indefinite Life Operating Intangibles - Manual Input")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(46 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(49 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(50 ,"Gross Indefinite Life Operating Intangibles - Summary")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(51 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(55 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(58 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(59 ,"Net Operating Intangibles")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(60 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(63 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(64 ,"Intangibles included in Depreciating Assets")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(65 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(69 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(70 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(74 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(75 ,"4.Gross Finite Life Operating Intangibles (in Life)")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(76 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(77 ,"Other Finite Life Operating Intangibles (in Life) - Manual Input")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(78 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(82 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(83 ,"Gross Finite Life Operating Intangibles (in Life) - Summary")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(84 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(88 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(92 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(94 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(98 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(99 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(100 ,"5.Gross Finite Life Operating Intangibles (Not in Life)")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(101 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(102 ,"Other Gross Finite Life Operating Intangibles (Not in Life) - Manual Input")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(105 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(106 ,"Gross Finite Life Operating Intangibles (ex Life Calc) - Summary")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(107 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(111 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(112 ,"Unidentified Net Intangibles")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(113 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(121 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(122 ,"Capitalized Software in Other Assets")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(123 ,"")
show_nombres_conceptos_estandarizados_intangibles_fix_factsheet.insert(128 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_intangibles_fix_factsheet)
#len(show_nombres_conceptos_estandarizados_intangibles_fix_factsheet)

#len(show_conceptos_estandarizados_intangibles_fix_factsheet)==len(show_nombres_conceptos_estandarizados_intangibles_fix_factsheet)



###############################################
############################################## INFLATION ADJUSTMENT FOR EMERGING MARKETS 

conceptos_estandarizados_inflation_adjustments_for_emerging_markets = ("H1294",
"H1394",
"H1206",
#
"H1295",
"H1395",
"H1425",
#
"H1296",
"H1396",
"H1619",
"H1641",
#
"H1289",
"H1389",
"H1629",
#
"H1101",
"H1102",
"H1616")


nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets = {"H1294":"Plant Inflation Adjustment Switch (0: Off, 1: On)",
"H1394":"Plant Inflation Adjustment Trigger Override",
"H1206":"Gross Plant Inflation Adjustment",
#
"H1295":"Land Inflation Adjustment Switch (0: Off, 1: On)",
"H1395":"Land Inflation Adjustment Trigger Override",
"H1425":"Land Inflation Adjustment",
#
"H1296":"Monetary Holding Gain-Loss Switch (0: Off, 1: On)",
"H1396":"Monetary Holding Gain-Loss Trigger Override",
"H1619":"Monetary Holding Gain-Loss (Bounded by Size Limit)",
"H1641":"Monetary Holding Loss for Financials",
#
"H1289":"FIFO Profits Switch (0: Off, 1: On)",
"H1389":"FIFO Profits Trigger Override",
"H1629":"LIFO Charge to FIFO Inventory",
#
"H1101":"Land Inflation Factor",
"H1102":"GROSS PLANT INFLATION ADJUSTMENT FACTOR",
"H1616":"LIFO Charge to FIFO Inventory"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df9 = pd.DataFrame(index = conceptos_estandarizados_inflation_adjustments_for_emerging_markets, columns=list_of_columns)
#df9['Concepto'] = pd.Series(nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets = []
for k in range(0,len(conceptos_estandarizados_inflation_adjustments_for_emerging_markets)):
    show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.append(conceptos_estandarizados_inflation_adjustments_for_emerging_markets[k])

# Arma la serie con los conceptos/codigos 
#prueba = pd.Series(show_conceptos_estandarizados_global_inflation_adjusted_cash_flow)

# A MODO DE EJEMPLO COMO INSERTAR BLANCOS Y SEPARADORES EN LOS CODIGOS

show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(0 ,"****")
show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(1 ,"****")
show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(2 ,"")
show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(6 ,"")
show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(10 ,"")
show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(15 ,"")
show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(19 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets )):
    show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.append(conceptos_estandarizados_inflation_adjustments_for_emerging_markets[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_inflation_adjustments_for_emerging_markets:
    show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.append(nombres_conceptos[k])


show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(0 ,"****")
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(1 ,"Inflation Adjustments for Emerging Markets")
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(2 ,"")
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(6 ,"")
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(10 ,"")
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(15 ,"")
show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets.insert(19 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)
#len(show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)

#len(show_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)==len(show_nombres_conceptos_estandarizados_inflation_adjustments_for_emerging_markets)




###############################################
############################################## NORMALIZED GROWTH RATE

conceptos_estandarizados_normalized_growth_rate = ("H1961",
"H1811",
"H1931",
#
"H1503_USED",
"H1859A",
#
"H1930",
"H1836C",
#
"H1913",
"H1860",
#
# Simple Ploughback
#
"H1699",
"H1812",
"H1630X",
"H1813",
#
# Payments to Capital Owners
#
"RI15",
"H1611",
"RI47",
"H2107",
"H1639",
"RI641",
"H1812",
#
# Retirements
# 
"H1207",
"H1011",
"H1809GP",
"H1810",
"H1276",
"H1285",
"H1253",
"H1253_ENP",
"HT1323",
"HT1327",
"HT1334",
"H1809GP",
"HT1810",
"H1850",
"H1811",
#
# Conditional Net Capital Events
#
"H1963",
"H1964",
"H1831B",
"H1918",
#
"H1919_FC",
"H1919_O",
"H1906",
"H1919",
#
"H1962",
"H1964M",
"H1964I",
"H1967",
#
"H1965",
#
"H1909",
#
"H1909",
#
"H1968",
"H%1909",
"H1928",
"H1929",
#
"H1930",
#
# BOY Inflation Adjusted Gross Investment
#
#"H1503",
"H1500",
"H1836C",
"H1921",
"H1503_USED",
#
# Other Information
# 
"H3028",
"H1829",
"H1829GP",
"H1800",
#
# Growth Rate Used In Valuation
#
"H1913",
"H2401",
"H2418")


nombres_conceptos_estandarizados_normalized_growth_rate = {"H1961":"Simple Ploughback",
"H1811":"Less: Retirements",
"H1931":"Sustainable Cash Flow",
#
"H1503_USED":"BOY Inflation Adjusted Gross Investment",
"H1859A":"Sustainable Growth Rate, %",
#
"H1930":"Plus: Conditional Net Capital Events",
"H1836C":"Cash Available for Reinvestment",
#
"H1913":"Normalized Growth Rate Spot, %",
"H1860":"Normalized Growth Rate Spot (3-Year Median), %",
#
# Simple Ploughback
#
"H1699":"Inflation Adjusted Gross Cash Flow",
"H1812":"Less: Payments to Capital Owners",
"H1630X":"Plus: Stock Option Expense ex R&D",
"H1813":"Simple Ploughback",
#
# Payments to Capital Owners
#
"RI15":"Interest Expense (Gross)",
"H1611":"Financial Sub Interest Expense",
"RI47":"Rental Expense",
"H2107":"Common & Preferred Dividends",
"H1639":"Net Pension Cash Flow Adjustment",
"RI641":"Minority Interest Dividends",
"H1812":"Payments to Capital Owners",
#
# Retirements
#
"H1207":"Inflation Adjusted Gross Cash Flow",
"H1011":"Life - Gros Plant (Integer)",
"H1809GP":"Historic Growth Rate of Gross Plant",
"H1810":"Infl Adjusted Gross Plant Retirements",
"H1276":"Gross Plant Recaptured Layer",
"H1285":"HGHGPAA Layer Inflation Adjustment",
"H1253":"Capitalized R&D Retirements",
"H1253_ENP":"Capitalized E&P Retirements",
"HT1323":"Gross Finite Operating Intangibles (in Life Calc)",
"HT1327":"Gross Finite Operating Intangibles (ex Life Calc)",
"HT1334":"Finite Operating Intangibles Project Life 3 yr Median Bound",
"H1809GP":"Historic Growth Rate",
"HT1810":"Inflation Adjusted Intangibles Retirements",
"H1850":"Misc Retirements",
"H1811":"Retirements",
#
# Conditional Net Capital Events
#
"H1963":"Equity Issuances (Cash Flow Statement)",
"H1964":"Debt Increases",
"H1831B":"Other Sources of Capital",
"H1918":"Cash Flow from Capital Events Financing",
#
"H1919_FC":"Foreign Currency Translation to Goodwill",
"H1919_O":"Change in Gross Goodwill",
"H1906":"Acquired R&D",
"H1919":"Change in Gross Goodwill",
#
"H1962":"Equity Repurchases (Cash Flow Statement)",
"H1964M":"Debt Decreases",
"H1964I":"Other distributions of capital (HOLT)",
"H1967":"Total Equity and Debt Returned (HOLT)",
#
"H1965":"Other Acquisition Capital (HOLT)",
#
"H1221B":"Change in Leased Assets",
#
"H1909":"Net Capital Events (Spot)",
#
"H1968":"NCE Materiality Threshold",
"H%1909":"NCE, % of Gross Investment",
"H1928":"Material Net Capital Events (1=Yes; 0=No)",
"H1929":"Material Net Capital Events 2-out-of-3 Years (1=Yes; 0=No)",
#
"H1930":"Conditional Net Capital Events",
#
# BOY Inflation Adjusted Gross Investment
#
#"H1503":"BOY Inflation Adjusted Gross Investment",
"H1500":"Inflation Adjusted Gross Investment (EOY)",
"H1836C":"Less: Dynamic Cash Flow",
"H1921":"Plus: Investment & Advances (Equity) Change",
"H1503_USED":"BOY Inflation Adjusted Gross Investment",
#
# Other Information
#
"H3028":"Real Asset Growth, %",
"H1829":"Historical Growth Rate of Depreciating Assets, Adjusted , %",
"H1829GP":"Historical Growth Rate of Gross Plant, Adjusted %",
"H1800":"Industry Historic Growth Rate, %",
#
# Growth Rate Used In Valuation
#
"H1913":"Normalized Growth Rate (Spot)",
"H2401":"Forecast Valuation Weighting, %",
"H2418":"Normalized Growth Rate Used In Valuation"}

### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df10 = pd.DataFrame(index = conceptos_estandarizados_normalized_growth_rate, columns=list_of_columns)
#df10['Concepto'] = pd.Series(nombres_conceptos_estandarizados_normalized_growth_rate)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_normalized_growth_rate = []
for k in range(0,len(conceptos_estandarizados_normalized_growth_rate)):
    show_conceptos_estandarizados_normalized_growth_rate.append(conceptos_estandarizados_normalized_growth_rate[k])

show_conceptos_estandarizados_normalized_growth_rate.insert(0 ,"****")
show_conceptos_estandarizados_normalized_growth_rate.insert(1 ,"****")
show_conceptos_estandarizados_normalized_growth_rate.insert(2 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(3 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(4 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(8 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(11 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(14 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(17 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(18 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(19 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(24 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(25 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(26 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(34 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(35 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(36 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(52 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(53 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(54 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(59 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(64 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(69 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(71 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(73 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(75 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(81 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(82 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(83 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(88 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(89 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(90 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(95 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(96 ,"")
show_conceptos_estandarizados_normalized_growth_rate.insert(97 ,"")





# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_normalized_growth_rate  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_normalized_growth_rate )):
    show_nombres_conceptos_estandarizados_normalized_growth_rate.append(conceptos_estandarizados_normalized_growth_rate[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_normalized_growth_rate)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_normalized_growth_rate = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_normalized_growth_rate:
    show_nombres_conceptos_estandarizados_normalized_growth_rate.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(0 ,"****")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(1 ,"Normalized Growth Rate")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(2 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(3 ,"Normalized Growth Rate Summary")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(4 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(8 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(11 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(14 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(17 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(18 ,"Simple Ploughback")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(19 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(24 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(25 ,"Payments to Capital Owners")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(26 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(34 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(35 ,"Retirements")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(36 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(52 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(53 ,"Conditional Net Capital Events")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(54 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(59 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(64 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(69 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(71 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(73 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(75 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(81 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(82 ,"BOY Inflation Adjusted Gross Investment")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(83 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(88 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(89 ,"Other Information")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(90 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(95 ,"")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(96 ,"Growth Rate Used in Valuation")
show_nombres_conceptos_estandarizados_normalized_growth_rate.insert(97 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_normalized_growth_rate)
#len(show_nombres_conceptos_estandarizados_normalized_growth_rate)

#len(show_conceptos_estandarizados_normalized_growth_rate)==len(show_nombres_conceptos_estandarizados_normalized_growth_rate)




###############################################
############################################## BOUNDED HISTORIC GROWTH RATE

conceptos_estandarizados_bounded_historic_growth_rate = ("H1207",
"H1278",
"H1279",
"H1501GP",
#
"H1502",
"H1505GP",
"H1504",
"H1506GPB",
"CCLASS",
#
"H1506GPB",
"H1111",
"H1506GP",
#
"H1506GP",
"H1821GPA",
#
"H1506GPB",
"H1821GPB",
#
"H1821GPA",
"H1821GPB",
"H1821GP",
#
"H1804",
"H1803",
"H1823GP",
"H1825GP",
"H1827GP",
"H1829GP",
#
"H1829GP",
"H1800",
"H1802GP",
#
"H1804",
"H1803",
"H1809GP",
#
# Gross Plant Historic Growth Rate Flows Into...
#
"H1102",
"H1103",
"H1104",
"H1101",
"H1810",
"H1822",
#
# Constant Currency Depreciating Assets
#
"H1501GP",
"H1252",
"H1243",
"H1501",
#
"H1502",
"H1505",
"H1504",
"H1506B",
#
"H1506B",
"RI25",
"RI675",
"H1107",
"RI27",
"H1109",
"H1111",
"H1506",
#
"H1506",
"H1821A",
#
"H1506B",
"H1821B",
#
"H1821A",
"H1821B",
"H1821",
#
"H1804",
"H1803",
"H1823",
"H1825",
"H1827",
"H1829",
#
"H1829",
"H1800",
"H1802",
#
"H1804",
"H1803",
"H1809",
#
# Depreciating Assets Historic Growth Rate Flows Into...
#
"H2417",
"H3136",
"HT1810",
"H1105",
"H1108")


nombres_conceptos_estandarizados_bounded_historic_growth_rate = {"H1207":"Inflation Adjusted Gross Plant",
"H1278":"Cumulative Gross Plant Recaptured",
"H1279":"Net Gross Plant Recaptured Inflation Adjustment",
"H1501GP":"Inflation Adjusted Gross Plant (Including GPR)",
#
"H1502":"Constant Currency Adjustment Factor",
"H1505GP":"Constant Dollar Gross Plant (for Industrial HGR)",
"H1504":"Constant Dollar Gross Plant (for Financial HGR)",
"H1506GPB":"Constant Dollar Gross Plant (Used)",
"CCLASS":">>> I = INDUSTRIAL >> F = FINANCIAL",
#
"H1506GPB":"Constant Dollar Gross Plant (Used)",
"H1111":"Shares - Common shares Outstanding (Split - Adjusted)",
"H1506GP":"Constant Dollar Gross Plant Per share",
#
"H1506GP":"Constant Dollar Gross Plant Per share",
"H1821GPA":"Growth in Constant Dollar Gross Plant Per share",
#
"H1506GPB":"Constant Dollar Gross Plant (Used)",
"H1821GPB":"Growth in Constant Dollar Gross Plant (not Per Share)",
#
"H1821GPA":"Growth in Constant Dollar Gross Plant Per share",
"H1821GPB":"Growth in Constant Dollar Gross Plant (not Per Share)",
"H1821GP":"Growth in Constant Dollar Gross Plant (Used)",
#
"H1804":"Historic Growth Rate Upper Limit",
"H1803":"Historic Growth Rate Lower Limit",
"H1823GP":"Bounded Constant $ Gross Plant Per",
"H1825GP":"NLOG of Bounded Constant $ Gross Plant",
"H1827GP":"7-Year Average of NLOG Constant Dollar Gross Plant",
"H1829GP":"Adjusted Historic Growth Rate, % of Gross Plant",
#
"H1829GP":"Adjusted Historic Growth Rate, % of Gross Plant",
"H1800":"Industry Historic Growth Rate",
"H1802GP":"Actual Historic Growth Rate of Gross Plant",
#
"H1804":"Historic Growth Rate Upper Limit",
"H1803":"Historic Growth Rate Lower Limit",
"H1809GP":"Historic Growth Rate of Gross Plant",
#
# Gross Plant Historic Growth Rate Flows Into...
#
"H1102":"Gross Plant Inflation Adjusted Factor",
"H1103":"Accumulated Depreciation (of Plant) Inflation Adjustment Factor",
"H1104":"Net Plant Inflation Adjustment Factor",
"H1101":"Land Inflation Adjustment Factor",
"H1810":"Inflation Adjusted Gross Plant Retirements",
"H1822":"Gross Plant Retirements (Forecaster)",
#
# Constant Currency Depreciating Assets
#
"H1501GP":"Inflation Adjusted Gross Plant (including GPR)",
"H1252":"Capitalized R&D (Inflation Adjusted)",
"H1243":"Capitalized Operating Leases - HOLT Asset",
"H1501":"Depreciating Assset (for HGR)",
#
"H1502":"Constant Currency Adjustment Factor",
"H1505":"Constant Dollar Depreciating Assets (for Industrials HGR)",
"H1504":"Constant Dollar Gross Investment (for Financial HGR)",
"H1506B":"Constant Dollar Gross Investment (Used)",
#
"H1506B":"Constant Dollar Gross Investment (Used)",
"RI25":"Common Shares Outstanding",
"RI675":"Untraded Shares Outstanding",
"H1107":"Shares Outstanding including untraded",
"RI27":"Adjustment Factor (Cumulative)",
"H1109":"Adjustment Factor Pay-Date",
"H1111":"Shares - Common shares Outstanding (Split - Adjusted)",
"H1506":"Constant Dollar Gross Investment Per Share",
#
"H1506":"Constant Dollar Gross Investment Per Share",
"H1821A":"Growth in Constant Dollar Gross Investment Per Share",
#
"H1506B":"Constant Dollar Gross Investment (Used)",
"H1821B":"Growth in Constant Dollar Gross Investment (Not Per Share)",
#
"H1821A":"Growth in Constant Dollar Gross Investment Per Share",
"H1821B":"Growth in Constant Dollar Gross Investment (Not Per Share)",
"H1821":"Growth in Constant Dollar Gross Investment (Used)",
#
"H1804":"Historic Growth Rate Upper Limit",
"H1803":"Historic Growth Rate Lower Limit",
"H1823":"Bounded Constant $ Gross Investment",
"H1825":"NLOG Bounded Constant $ Gross Investment",
"H1827":"7-Year Average of NLOG Constant Dollar Gross Investment",
"H1829":"Adjusted Historic Growth Rate, % of Depreciating Assets",
#
"H1829":"Adjusted Historic Growth Rate, % of Depreciating Assets",
"H1800":"Industry Historic Growth Rate",
"H1802":"Actual Historic Growth Rate of Depreciating Assets",
#
"H1804":"Historic Growth Rate Upper Limit",
"H1803":"Historic Growth Rate Lower Limit",
"H1809":"Historic Growth Rate of Depreciating Assets",
#
# Depreciating Assets Historic Growth Rate Flows Into...
#
"H2417":"Growth Rate Existing Assets",
"H3136":"Capitalized Operating Lease Retirements",
"HT1810":"Inflation Adjusted Intangibles Retirements",
"H1105":"Inflation Adjusted Depreciation Change to Infla adjusted Gross Plan  Retirements (Real RONA)",
"H1108":"Inflation Adjusted Accumulated Depreciation to Inflation Adjusted Gross Plant (Real RONA)"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df12 = pd.DataFrame(index = conceptos_estandarizados_bounded_historic_growth_rate, columns=list_of_columns)
#df12['Concepto'] = pd.Series(nombres_conceptos_estandarizados_bounded_historic_growth_rate)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_bounded_historic_growth_rate = []
for k in range(0,len(conceptos_estandarizados_bounded_historic_growth_rate)):
    show_conceptos_estandarizados_bounded_historic_growth_rate.append(conceptos_estandarizados_bounded_historic_growth_rate[k])

show_conceptos_estandarizados_bounded_historic_growth_rate.insert(0 ,"****")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(1 ,"****")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(2 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(3 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(4 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(9 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(15 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(19 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(22 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(25 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(29 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(36 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(40 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(44 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(45 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(46 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(53 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(54 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(55 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(60 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(65 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(74 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(77 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(80 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(84 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(91 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(95 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(99 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(100 ,"")
show_conceptos_estandarizados_bounded_historic_growth_rate.insert(101 ,"")



# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_bounded_historic_growth_rate  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_bounded_historic_growth_rate )):
    show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.append(conceptos_estandarizados_bounded_historic_growth_rate[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_bounded_historic_growth_rate)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_bounded_historic_growth_rate:
    show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(0 ,"****")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(1 ,"Bounded Historic Growth Rate")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(2 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(3 ,"Constant Currency Gross Plant")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(4 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(9 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(15 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(19 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(22 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(25 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(29 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(36 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(40 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(44 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(45 ,"Gross Plant Historic Growth Rate Flows Into.")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(46 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(53 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(54 ,"Constant Currency Depreciation Assets")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(55 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(60 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(65 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(74 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(77 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(80 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(84 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(91 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(95 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(99 ,"")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(100 ,"Depreciating Assets Historic Growth Rate Flows Into.")
show_nombres_conceptos_estandarizados_bounded_historic_growth_rate.insert(101 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_bounded_historic_growth_rate)
#len(show_nombres_conceptos_estandarizados_bounded_historic_growth_rate)

#len(show_conceptos_estandarizados_bounded_historic_growth_rate)==len(show_nombres_conceptos_estandarizados_bounded_historic_growth_rate)


###############################################
############################################## DEBT AUDIT

conceptos_estandarizados_debt_audit = ("RI34",
"RI9",
"H1407",
"H1408",
"H2101",
#
"H1013",
"RI47",
"H1648",
"H1809GP",
"H1221",
"H1013",
"H1809GP",
"H2102",
"H1241",
"H2103",
"RI75",
"H2125",
"H2120",
"RI523",
"HT1371",
"RI953",
"H2126",
"H2111",
#
"H2105",
"H2155",
#
"H2122",
"H2119",
"H2157",
#
"H2400",
"H1864",
"H2420",
#
"H5425",
#
# Market Value of Debt
# Merton Model Inputs
#
"H2438",
"H2446M",
"H2157",
"H5423",
"H3021H",
"H5416",
#
# Merton Model Calculation Details
#
"H2490",
"H5411",
"H5413",
"H5415",
#
# Market Value of Debt Calculation
# Probability-Weighted Value of Debt if Survive
#
"H5425",
"H54005",
#
"H5426",
#
# Probability-Weighted Value of Debt if Default
#
"H5427",
"H2492",
"H5428",
#
"H5425",
#
"H5433",
"H5415",
"H5429",
"H2421",
#
"H5432",
"H5430",
#
# Ratio Analysis
# 
"RI15",
"H1882",
#
"HCD512",
"HCD5117",
#
"HCD568",
"HCD510",
#
"HCD52",
"HCD55",
#
"H5422",
"H5417",
#
"HCD5120")

nombres_conceptos_estandarizados_debt_audit = {"RI34":"Total Book Debt - Current",
"RI9":"Total Book Debt - Long Term",
"H1407":"Total Book Debt",
"H1408":"Less: Financial Subsidiary Debt",
"H2101":"Adjusted Book Debt (ex Fin Sub)",
#
"H1013":"Asset Life (Leased Assets)",
"RI47":"Rental Expense",
"H1648":"Rental Expense Adjustment from Corporate Actions",
"H1809GP":"Historic Growth Rate",
"H1221":"Inflation Adjusted Gross Leased Property",
"H1013":"Asset Life (Leased Assets)",
"H1809GP":"Historic Growth Rate",
"H2102":"Debt Value of Operating Leases Before Balance Sheet Leases",
"H1241":"Inflation Adjusted Leased Property On Balance Sheet (Japan Only)",
"H2103":"Debt Value of Operating Leases",
"RI75":"Other Long-Term Liabilities",
"H2125":"Plus: Pension Liabilities",
"H2120":"Plus: Postretirement Liabilities",
"RI523":"Less: Long-Term Notes and Accounts",
"HT1371":"Less: Long-Term Deferred Revenue",
"RI953":"Less: Capital Grants and Subsidies",
"H2126":"Other Liabilities",
"H2111":"Market Value of Preferred Stock",
#
"H2105":"HOLT Debt Normalized Growth",
"H2155":"Total Debt and Equivalents Excl, Pension Debt & Stock Option Claim",
#
"H2122":"Pension Debt",
"H2119":"Stock Option Claim (Value of Shares Excercisable)",
"H2157":"Total Debt and Equivalents",
#
"H2400":"Number of Months since last fiscal year",
"H1864":"Nominal Normalized Growth Rate (LFY)",
"H2420":"Year-To-Date Adjustment",
#
"H5425":"Total Debt and Equivalents Used in Valuation",
#
#
#
"H2438":"Market Cap",
"H2446M":"Minority Interests",
"H2157":"Total Debt and Equivalents",
"H5423":"Enterprise Value",
"H3021H":"Economic Leverage (%)",
"H5416":"Equity Volatility (90-day)",
#
#
#
"H2490":"Asset Value - Merton Model",
"H5411":"Asset Volatility - Merton Model",
"H5413":"Distance to Default - Merton Model",
"H5415":"Probability of Default Estimate",
#
#
#
"H5425":"Total Debt and Equivalents",
"H54005":"Probability of Survival",
#
"H5426":"Probability-Weighted Value of Debt - Survive",
#
#
"H5427":"Recovery Rate Estimate (%)",
"H2492":"Inflation Adjusted Net Assets",
"H5428":"Net Asset Recovery Value Estimate",
#
"H5425":"Total Debt & Equivalents (time-adjusted)",
#
"H5433":"Lesser of Total Debt & Equivalents or Net Asset Recovery",
"H5415":"Probability of Default",
"H5429":"Probability-Weighted Value of Debt - Default",
"H2421":"Market Value of Debt & Equivalents Used in Valuation",
#
"H5432":"Market Value of Debt Adjustment",
"H5430":"Market Value of Debt Adjustment (% of Total HOLT Debt)",
#
# Ratio Analysis
#
"RI15":"Interest Expense -- Gross",
"H1882":"Implicit Interest Rate",
#
"HCD512":"Net Book Debt / EBITDA",
"HCD5117":"Net HOLT Debt / EBITDAR",
#
"HCD568":"Total Book Debt / Total Capital",
"HCD510":"HOLT DEBT / Total HOLT Capital",
#
"HCD52":"EBITDA/Gross Interest",
"HCD55":"EBITDAR/(Gross Interest+Rentals)",
#
#
"H5422":"Drift Term for Merton Model",
"H5417":"Market Cap for Merton (1)",
#
"HCD5120":"HOLT Fixed Charge Ratio (with Capex)"}


### CONTROLA QUE ESTEN TODOS LOS CONCEPTOS
#list_of_columns = ['Concepto']
# Crea el dataframe
#df13 = pd.DataFrame(index = conceptos_estandarizados_debt_audit, columns=list_of_columns)
#df13['Concepto'] = pd.Series(nombres_conceptos_estandarizados_debt_audit)

#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_debt_audit = []
for k in range(0,len(conceptos_estandarizados_debt_audit)):
    show_conceptos_estandarizados_debt_audit.append(conceptos_estandarizados_debt_audit[k])


show_conceptos_estandarizados_debt_audit.insert(0 ,"****")
show_conceptos_estandarizados_debt_audit.insert(1 ,"****")
show_conceptos_estandarizados_debt_audit.insert(2 ,"")
show_conceptos_estandarizados_debt_audit.insert(8 ,"")
show_conceptos_estandarizados_debt_audit.insert(27 ,"")
show_conceptos_estandarizados_debt_audit.insert(30 ,"")
show_conceptos_estandarizados_debt_audit.insert(34 ,"")
show_conceptos_estandarizados_debt_audit.insert(38 ,"")
show_conceptos_estandarizados_debt_audit.insert(40 ,"")
show_conceptos_estandarizados_debt_audit.insert(41 ,"")
show_conceptos_estandarizados_debt_audit.insert(42 ,"")
show_conceptos_estandarizados_debt_audit.insert(49 ,"")
show_conceptos_estandarizados_debt_audit.insert(50 ,"")
show_conceptos_estandarizados_debt_audit.insert(51 ,"")
show_conceptos_estandarizados_debt_audit.insert(56 ,"")
show_conceptos_estandarizados_debt_audit.insert(57 ,"")
show_conceptos_estandarizados_debt_audit.insert(58 ,"")
show_conceptos_estandarizados_debt_audit.insert(61 ,"")
show_conceptos_estandarizados_debt_audit.insert(63 ,"")
show_conceptos_estandarizados_debt_audit.insert(64 ,"")
show_conceptos_estandarizados_debt_audit.insert(68 ,"")
show_conceptos_estandarizados_debt_audit.insert(70 ,"")
show_conceptos_estandarizados_debt_audit.insert(75 ,"")
show_conceptos_estandarizados_debt_audit.insert(78 ,"")
show_conceptos_estandarizados_debt_audit.insert(79 ,"")
show_conceptos_estandarizados_debt_audit.insert(80 ,"")
show_conceptos_estandarizados_debt_audit.insert(83 ,"")
show_conceptos_estandarizados_debt_audit.insert(86 ,"")
show_conceptos_estandarizados_debt_audit.insert(89 ,"")
show_conceptos_estandarizados_debt_audit.insert(92 ,"")
show_conceptos_estandarizados_debt_audit.insert(95 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_debt_audit  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_debt_audit )):
    show_nombres_conceptos_estandarizados_debt_audit.append(conceptos_estandarizados_debt_audit[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_debt_audit)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_debt_audit = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_debt_audit:
    show_nombres_conceptos_estandarizados_debt_audit.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_debt_audit.insert(0 ,"****")
show_nombres_conceptos_estandarizados_debt_audit.insert(1 ,"Debt Audit")
show_nombres_conceptos_estandarizados_debt_audit.insert(2 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(8 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(27 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(30 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(34 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(38 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(40 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(41 ,"Market Value of Debt")
show_nombres_conceptos_estandarizados_debt_audit.insert(42 ,"Merton Model Inputs")
show_nombres_conceptos_estandarizados_debt_audit.insert(49 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(50 ,"Merton Model Calculation Details")
show_nombres_conceptos_estandarizados_debt_audit.insert(51 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(56 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(57 ,"Market Value of Debt Calculation")
show_nombres_conceptos_estandarizados_debt_audit.insert(58 ,"Probability-Weighted Value of Debt if Survive")
show_nombres_conceptos_estandarizados_debt_audit.insert(61 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(63 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(64 ,"Probability-Weighted Value of Debt if Default")
show_nombres_conceptos_estandarizados_debt_audit.insert(68 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(70 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(75 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(78 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(79 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(80 ,"Ratio Analysis")
show_nombres_conceptos_estandarizados_debt_audit.insert(83 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(86 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(89 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(92 ,"")
show_nombres_conceptos_estandarizados_debt_audit.insert(95 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_debt_audit)
#len(show_nombres_conceptos_estandarizados_debt_audit)

#len(show_conceptos_estandarizados_debt_audit)==len(show_nombres_conceptos_estandarizados_debt_audit)





####ECAP AUDIT
#############################################################################################

conceptos_estandarizados_eCap_audit = ("H4188",
"H4205",
"H4187A",
"H4187C",
"H4187D",
"H4188_S",
"H4189A",
"H4189C",
"H4189D",
"H4189",
"H1488_P",
"H4187F",
"H4187B",
"H4187E",
"H4182F",
"H4187G",
"H4188_F",
"H4188T")

nombres_conceptos_estandarizados_eCap_audit = {"H1207":"Inflation Adjusted Gross Plant",
"H4188":"eCap Award",
"H4205":"eCap Window",
"H4187A":"CFROI Level Test for eCAP(1=Fail)",
"H4187C":"CFROI Stability Test for eCAP(1=Fail)",
"H4187D":"CFROI Trend Test for eCAP(1=Fail)",
"H4188_S":"eCap Default Profitability Test (>0=Fail)",
"H4189A":"CFROI Level Test: 4 yr exception",
"H4189C":"CFROI Stability Test: 4 yr exception",
"H4189D":"CFROI Trend Test: 4 yr exception",
"H4189":"eCap 4/5 Year CFROI Check (<0 = Excpetion Test Fail)",
"H1488_P":"eCap Profitability Test (1=Pass)",
"H4187F":"5 Yr Med Growth Test for eCAP",
"H4187B":"VCR Filter for eCAP",
"H4187E":"Sector Filter for eCAP",
"H4182F":"Forecast CFROI >=8 check",
"H4187G":"Forecast CFROI chg check",
"H4188_F":"eCap Filter Test (0=Pass)",
"H4188T":"eCap Combined Test Result (1=Pass)"}

show_conceptos_estandarizados_eCap_audit = []
for k in range(0,len(conceptos_estandarizados_eCap_audit)):
    show_conceptos_estandarizados_eCap_audit.append(nombres_conceptos_estandarizados_eCap_audit[conceptos_estandarizados_eCap_audit[k]])



prueba = pd.Series(show_conceptos_estandarizados_eCap_audit)


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_estandarizados_eCap_audit = []
for k in range(0,len(conceptos_estandarizados_eCap_audit)):
    show_conceptos_estandarizados_eCap_audit.append(conceptos_estandarizados_eCap_audit[k])

show_conceptos_estandarizados_eCap_audit.insert(0 ,"****")
show_conceptos_estandarizados_eCap_audit.insert(1 ,"****")
show_conceptos_estandarizados_eCap_audit.insert(2 ,"")
show_conceptos_estandarizados_eCap_audit.insert(5 ,"")
show_conceptos_estandarizados_eCap_audit.insert(6 ,"")
show_conceptos_estandarizados_eCap_audit.insert(11 ,"")
show_conceptos_estandarizados_eCap_audit.insert(12 ,"")
show_conceptos_estandarizados_eCap_audit.insert(17 ,"")
show_conceptos_estandarizados_eCap_audit.insert(19 ,"")
show_conceptos_estandarizados_eCap_audit.insert(20 ,"")
show_conceptos_estandarizados_eCap_audit.insert(26 ,"")
show_conceptos_estandarizados_eCap_audit.insert(28 ,"")


# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_estandarizados_eCap_audit  = []
for k in range(0,len(show_nombres_conceptos_estandarizados_eCap_audit )):
    show_nombres_conceptos_estandarizados_eCap_audit.append(conceptos_estandarizados_eCap_audit[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_estandarizados_eCap_audit)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_estandarizados_eCap_audit = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_estandarizados_eCap_audit:
    show_nombres_conceptos_estandarizados_eCap_audit.append(nombres_conceptos[k])

show_nombres_conceptos_estandarizados_eCap_audit.insert(0 ,"****")
show_nombres_conceptos_estandarizados_eCap_audit.insert(1 ,"eCap Audit")
show_nombres_conceptos_estandarizados_eCap_audit.insert(2 ,"")
show_nombres_conceptos_estandarizados_eCap_audit.insert(5 ,"")
show_nombres_conceptos_estandarizados_eCap_audit.insert(6 ,"Profitability Tests (Default)")
show_nombres_conceptos_estandarizados_eCap_audit.insert(11 ,"")
show_nombres_conceptos_estandarizados_eCap_audit.insert(12 ,"Profitability Tests (Exeption) - When CFROI < 8% in 1-out-of...")
show_nombres_conceptos_estandarizados_eCap_audit.insert(17 ,"")
show_nombres_conceptos_estandarizados_eCap_audit.insert(19 ,"")
show_nombres_conceptos_estandarizados_eCap_audit.insert(20 ,"Filters")
show_nombres_conceptos_estandarizados_eCap_audit.insert(26 ,"")
show_nombres_conceptos_estandarizados_eCap_audit.insert(28 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_estandarizados_eCap_audit)
#len(show_nombres_conceptos_estandarizados_eCap_audit)

#len(show_conceptos_estandarizados_eCap_audit)==len(show_nombres_conceptos_estandarizados_eCap_audit)


#############################################################################################
##################################### ARMA MINORITY INTEREST
###################################################################################

conceptos_minority_interest_valuation = ("RI38",
"RI60",
"RI604",
"H2132_OR",
"H2132_OR",
"H2444",
"H2446")


nombres_conceptos_minority_interest_valuation = {"RI38":"Minority Interest (B/S)",
"RI60":"Common Equity (as reported)",
"RI604":"Goodwill Reserve",
"H2132_OR":"MI Ratio - FY1 Override",
"H2132_OR":"Minority Interest Ratio",
"H2444":"VAL: Total Economic Equity Value",
"H2446":"VAL: Value of Minority Interest"}


#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_minority_interest_valuation = []
for k in range(0,len(conceptos_minority_interest_valuation)):
    show_conceptos_minority_interest_valuation.append(conceptos_minority_interest_valuation[k])

show_conceptos_minority_interest_valuation.insert(0 ,"****")
show_conceptos_minority_interest_valuation.insert(1 ,"****")
show_conceptos_minority_interest_valuation.insert(2 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_minority_interest_valuation  = []
for k in range(0,len(show_nombres_conceptos_minority_interest_valuation )):
    show_nombres_conceptos_minority_interest_valuation.append(conceptos_minority_interest_valuation[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_minority_interest_valuation)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_minority_interest_valuation = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_minority_interest_valuation:
    show_nombres_conceptos_minority_interest_valuation.append(nombres_conceptos[k])

show_nombres_conceptos_minority_interest_valuation.insert(0 ,"****")
show_nombres_conceptos_minority_interest_valuation.insert(1 ,"Minority Interest Valuation")
show_nombres_conceptos_minority_interest_valuation.insert(2 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_minority_interest_valuation)
#len(show_nombres_conceptos_minority_interest_valuation)

#len(show_conceptos_minority_interest_valuation)==len(show_nombres_conceptos_minority_interest_valuation)



#############################################################################################
############################### OPERATING LEASES
############################################################################3333

conceptos_operating_leases = ("H1243",
"H2102",
"H1221",
"H1809GP",
"H1013",
"RI47",
"H2110_S",
"H1809",
"H1239",
"H1194",
"H1230",
"RI95",
"H1190",
"RI389",
"H1191",
"RI96",
"RI164",
"RI165",
"RI166",
"RI167",
"RI95",
"H1192",
"H1193")

nombres_conceptos_operating_leases  = {"H1243":"Capitalized Operating Leases - HOLT Asset",
"H2102":"Capitalized Operating Leases - HOLT Debt",
"H1221":"????",
"H1809GP":"????",
"H1013":"Asset Life (Leased Assets)",
"RI47":"Rental Expenses",
"H2110_S":"Corp A Bond Yield - Average",
"H1809":"Historic Growth Rate",
"H1239":"Capitalized Operating Lease Debt Life (HOLT)",
"H1194":"Capitalized Operating Lease Debt - Contract Value (Traditional PV)",
"H1230":"Operating Leases - Implied Contract Life",
"RI95":"Minimum Rent in Five Years (Total)",
"H1190":"Average 5-year Operating Lease Payment",
"RI389":"Thereafter Portion of Leases",
"H1191":"Operating Leases - Implied .Thereafter. Contract Life",
"RI96":"Minimum Rent in First Year",
"RI164":"Minimum Rent in Second Year",
"RI165":"Minimum Rent in Thrid Year",
"RI166":"Minimum Rent in Fourth Year",
"RI167":"Minimum Rent in Fifth Year",
"RI95":"Minimum Rent in Five Years (Total)",
"H1192":"NPV of Lease Payments (Years 1-5)",
"H1193":"PV of Lease Payments .Thereafter."}


show_conceptos_operating_leases  = []
for k in range(0,len(conceptos_operating_leases)):
    show_conceptos_operating_leases.append(nombres_conceptos_operating_leases[conceptos_operating_leases[k]])




prueba = pd.Series(show_conceptos_operating_leases)

#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_operating_leases = []
for k in range(0,len(conceptos_operating_leases)):
    show_conceptos_operating_leases.append(conceptos_operating_leases[k])

show_conceptos_operating_leases.insert(0 ,"****")
show_conceptos_operating_leases.insert(1 ,"****")
show_conceptos_operating_leases.insert(2 ,"")
show_conceptos_operating_leases.insert(3 ,"HOLT Cap Operating Lease Data")
show_conceptos_operating_leases.insert(11 ,"")
show_conceptos_operating_leases.insert(12 ,"")
show_conceptos_operating_leases.insert(14 ,"")
show_conceptos_operating_leases.insert(16 ,"")
show_conceptos_operating_leases.insert(17 ,"Traditional Capitalized Operating Lease Data")
show_conceptos_operating_leases.insert(32 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO





###########################################################################


show_nombres_conceptos_operating_leases  = []
for k in range(0,len(show_nombres_conceptos_operating_leases )):
    show_nombres_conceptos_operating_leases.append(conceptos_operating_leases[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_operating_leases)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_operating_leases = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_operating_leases:
    show_nombres_conceptos_operating_leases.append(nombres_conceptos[k])

show_nombres_conceptos_operating_leases.insert(0 ,"****")
show_nombres_conceptos_operating_leases.insert(1 ,"****")
show_nombres_conceptos_operating_leases.insert(2 ,"")
show_nombres_conceptos_operating_leases.insert(3 ,"HOLT Cap Operating Lease Data")
show_nombres_conceptos_operating_leases.insert(11 ,"")
show_nombres_conceptos_operating_leases.insert(12 ,"")
show_nombres_conceptos_operating_leases.insert(14 ,"")
show_nombres_conceptos_operating_leases.insert(16 ,"")
show_nombres_conceptos_operating_leases.insert(17 ,"Traditional Capitalized Operating Lease Data")
show_nombres_conceptos_operating_leases.insert(32 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_operating_leases)
#len(show_nombres_conceptos_operating_leases)

#len(show_conceptos_operating_leases)==len(show_nombres_conceptos_operating_leases)


#############################################################################################
###########ARMA SYSTEM CONSTANTS
###################################################################################33

conceptos_system_constants = ("H1616",
"H1502GDP",
"H1502",
"H1220",
"H2110",
"H1620",
"H1621",
"H1601",
"H1433",
"H2412",
"H2413",
"H2712",
"H1117",
"H1118",
"H1431")

nombres_conceptos_system_constants = {"H1616":"Percent Change in GDP Deflator",
"H1502GDP":"Raw GDP Value",
"H1502":"Constant Currency Adjustment Factor",
"H1220":"Real Debt Rate",
"H2110":"Preferred or Utility .A. Bond Yield",
"H1620":"% change in PPI",
"H1621":"% of Inventories on FIFO",
"H1601":"Total Effective Tax Rate, %",
"H1433":"Statutory Federal Income tax rate",
"H2412":"Country Discount Rate",
"H2413":"Company-Specific Discount Rate",
"H2712":"Financial Discount Rate",
"H1117":"Local Market Index",
"H1118":"Dividends for Local Market Index",
"H1431":"Industrial Receivables days Outstanding"}




#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_system_constants = []
for k in range(0,len(conceptos_system_constants)):
    show_conceptos_system_constants.append(conceptos_system_constants[k])

show_conceptos_system_constants.insert(0 ,"****")
show_conceptos_system_constants.insert(1 ,"****")
show_conceptos_system_constants.insert(2 ,"")
show_conceptos_system_constants.insert(6 ,"")
show_conceptos_system_constants.insert(9 ,"")
show_conceptos_system_constants.insert(12 ,"")
show_conceptos_system_constants.insert(15 ,"")
show_conceptos_system_constants.insert(19 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_system_constants  = []
for k in range(0,len(show_nombres_conceptos_system_constants )):
    show_nombres_conceptos_system_constants.append(conceptos_system_constants[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_system_constants)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_system_constants = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_system_constants:
    show_nombres_conceptos_system_constants.append(nombres_conceptos[k])

show_nombres_conceptos_system_constants.insert(0 ,"****")
show_nombres_conceptos_system_constants.insert(1 ,"System Constants")
show_nombres_conceptos_system_constants.insert(2 ,"")
show_nombres_conceptos_system_constants.insert(6 ,"")
show_nombres_conceptos_system_constants.insert(9 ,"")
show_nombres_conceptos_system_constants.insert(12 ,"")
show_nombres_conceptos_system_constants.insert(15 ,"")
show_nombres_conceptos_system_constants.insert(19 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_system_constants)
#len(show_nombres_conceptos_system_constants)

#len(show_conceptos_system_constants)==len(show_nombres_conceptos_system_constants)




#############################################################################################
##### DISCOUNT RATE
##################################################################################33

conceptos_discount_rate = ("H2412",
"H2409",
"H2410",
"H2413",
"H2403",
"H2498",
"H2407",
"H2497",
)

nombres_conceptos_discount_rate = {"H2412":"Country Discount Rate",
"H2409":"Size Differential",
"H2410":"Leverage Differential",
"H2413":"Company-Specific Discount Rate",
"H2403":"Company Market Capitalization - 12-Month Avg",
"H2498":"Base Firm Market Capitalization",
"H2407":"Company Leverage",
"H2497":"Base Firm Leverage",
}




#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_discount_rate = []
for k in range(0,len(conceptos_discount_rate)):
    show_conceptos_discount_rate.append(conceptos_discount_rate[k])

show_conceptos_discount_rate.insert(0 ,"****")
show_conceptos_discount_rate.insert(1 ,"****")
show_conceptos_discount_rate.insert(2 ,"")
show_conceptos_discount_rate.insert(7 ,"")
show_conceptos_discount_rate.insert(10 ,"")
#show_conceptos_discount_rate.insert(12 ,"")
#show_conceptos_discount_rate.insert(15 ,"")
#show_conceptos_discount_rate.insert(19 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_discount_rate = []
for k in range(0,len(show_nombres_conceptos_discount_rate )):
    show_nombres_conceptos_discount_rate.append(conceptos_discount_rate[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_discount_rate)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_discount_rate = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_discount_rate:
    show_nombres_conceptos_discount_rate.append(nombres_conceptos[k])

show_nombres_conceptos_discount_rate.insert(0 ,"****")
show_nombres_conceptos_discount_rate.insert(1 ,"Company Specific Discount Rate")
show_nombres_conceptos_discount_rate.insert(2 ,"")
show_nombres_conceptos_discount_rate.insert(7 ,"")
show_nombres_conceptos_discount_rate.insert(10 ,"")
#show_nombres_conceptos_discount_rate.insert(12 ,"")
#show_nombres_conceptos_discount_rate.insert(15 ,"")
#show_nombres_conceptos_discount_rate.insert(19 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_discount_rate)
#len(show_nombres_conceptos_discount_rate)

#len(show_conceptos_discount_rate)==len(show_nombres_conceptos_discount_rate)



#########ARMA CONCEPTOS ADICIONALES
#################################

conceptos_adicionales = ("H1423",
"H1017",
"RI953_SWITCH",
"reporting_year",
"CCLASS",
"H1136",
"H0009",
"gdp_precios_corrientes",
"H2489",
"FIN_MKT_COE",
"DR_FLAG",
"H2412G",
"FRMCLASS",
"FIN_MKT_COEG",
"H2494",
"H4186",
"H4182A",
"H4184A",
"H4185A",
"H4186A",
"H2312ADJ",
"H2468",
"H2159",
"DIP205",
"DIP78",
"DR_GROUP",
"H2498_N",
"H2498_WI",
"H2498_WI_BASE",
"FX09",
"RI994",
"FX_PER",
"13991",
"H5400_USED",
"H2405",
"H2408",
"H2415T3",
"H2415T2",
"ROIUIVFLR",
)

nombres_conceptos_adicionales = {"H1423":"Algo ",
"H1017":"Grants and Subsidies - Gross Equivalent",
"RI953_SWITCH":"Grants and Subsidies - Gross Equivalent",
"reporting_year":"Reporting Year",
"CCLASS":"Company Class",
"H1136":"Common Dividends (Ex Special Dividends)",
"H0009":"Preferred Dividends",
"gdp_precios_corrientes":"GDP a precios corrientes",
"H2489":"Base Discount Rate",
"FIN_MKT_COE":"Financial Market COE",
"DR_FLAG":"Switch for Global Discount Rate - 1=On",
"H2412G":"Global Market Implied Discount Rate",
"FRMCLASS":"Firm Classification - 0-Ind./1-Fin./2-Util.",
"FIN_MKT_COEG":"",
"H2494":"V/C Value / Cost - Market",
"H4186":"CFROI Coefficient of Variation",
"H4182A":"PErsistence of CROI >=8",
"H4184A":"5 Yr Adj Average CFROI",
"H4185A":"5 Year Adj. CFROI Standard Deviation",
"H4186A":"Adjusted CFROI Coefficient of Variation",
"H2312ADJ":"Adjusted H2312 for use in the CFROE Fade ---",
"H2468":"NPV of Replacement Investment -Valuation Call",
"H2159":"Desconocida",
"DIP205":"Standardized Leverage - R/E",
"DIP78":"Standardized Leverage",
"DR_GROUP":"DR Group",
"H2498_N":"Global Standard Firm Market Capitalization - new",
"H2498_WI":"MSCI World Index - in US$",
"H2498_WI_BASE":"MSCI World Index Base - in US$",
"FX09":"US Dollar to Fundamental Currency Conversion",
"RI994":"Fundamental Currency",
"FX_PER":"FX period",
"13991":"Unkown variable used in calculation of FX09",
"H5400_USED":"Probability of Default - Used",
"H2405":"Economic Leverage Implied from Credit Rating",
"H2408":"Industrial Economic Leverage for Discount Rate",
"H2415T3":"Aux Var: H2415 history",
"H2415T2":"Aux Var: H2415 FY0",
"ROIUIVFLR":"floorr",
}




#############################################################ARMA LA SERIE PARA MOSTRAR

show_conceptos_adicionales = []
for k in range(0,len(conceptos_adicionales)):
    show_conceptos_adicionales.append(conceptos_adicionales[k])

show_conceptos_adicionales.insert(0 ,"****")
show_conceptos_adicionales.insert(1 ,"****")
show_conceptos_adicionales.insert(2 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CODIGO

###########################################################################


show_nombres_conceptos_adicionales  = []
for k in range(0,len(show_nombres_conceptos_adicionales)):
    show_nombres_conceptos_adicionales.append(conceptos_adicionales[k])

# Une los diccionarios para luego poder pasarle el diccionario al vector
nombres_conceptos = dict(nombres_conceptos , **nombres_conceptos_adicionales)

# Inicializa el vector a mostrar de nombres de los conceptos
show_nombres_conceptos_adicionales = []

# Agrega al vector a mostrar de nombres de los conceptos todos los nombres de los conceptos que estan en el vector codigos 
for k in conceptos_adicionales:
    show_nombres_conceptos_adicionales.append(nombres_conceptos[k])

show_nombres_conceptos_adicionales.insert(0 ,"****")
show_nombres_conceptos_adicionales.insert(1 ,"Variables Adicionales")
show_nombres_conceptos_adicionales.insert(2 ,"")

# HASTA ACA TENGO LA SERIE QUE IRIA EN LA COLUMNA CONCEPTO

###################################################################
# VERIFICO QUE ESTE OKEY PARA CARGAR EN EL DATAFRAME

#len(show_conceptos_adicionales)
#len(show_nombres_conceptos_adicionales)

#len(show_conceptos_adicionales)==len(show_nombres_conceptos_adicionales)













