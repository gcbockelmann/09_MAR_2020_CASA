

# CREA UNA COLUMNA GENERICA PARA SER COMPLETADA 

# Crea un diccionario que es mi vector de mapeo   #ACA VAN LOS INPUTS
Columna={ 'Year':2018, 
'BI0001':436.76, 
'BI0002':4869.76,
'BI0003':8743.99,
'BI0068':288.59,
'BI0004':14339.11,
# Short-Term Investment - Agregar al VECTOR del indice
'RI193':145.98,
'BI0007':3980.16,
'BI0196':2694.94,
'BI0008':1285.22,
'BI0158':32.33,
'BI0260':32.33,
'BI0073':197.91,
'BI0266':197.91,
# Other Long-Term Assets
'BI0069':7.09,
'BI0033':60.63,
'BI0031_I':477.31,
'BI0032_I':898.67,
# Total Assets
'BI0006':17068.03,
# Goodwill -- Net
'RI204':0.51,
# Capitalized Software - Accumulated Depreciation
'RI537':106.73,
# Capitalized Software (in Intangibles) - Net
'RI536B':60.13,
# Amortization of Capitalized Software
'RI532':36.96,
#
# Current Liabilities
#
#
"BI0070":12608.63,
"BI0071":0,
"BI0072":18.44,
"BI0034":2.09,
"BI0005":12629.16,
#
"BI0009":0,
"BI0075":0.1,
"BI0035":12.28,
"BI0038":1.86,
"BI0181":12643.39,
# Deferred Taxes
"RI74": 12.28,
# Deferred Revenue - Long-Term
"RI397":0,
# Net Assets
"BI0216":4424.63,
"BI0060":4424.63,
"BI0130":0,
"BI0216":4424.63,
"RI36":4272.12,
"S101":0,
"S102":0,
"S103":0,
"S104":0,
"S105":0,
"S106":0,
"S107":0,
"S108":1,
"S109":0,
"S110":1,
"LIC_METHOD":0,
"SOFT_METHO":0,
"RI572":0,
"RI573":0,
"RI574":0,
#
"RI575":0,
"RI576":0,
"RI578":0,
#
"RI286":0,
"RI287":0,
"RI290":0,
#
"RI294":0,
"RI296":0,
"RI300":0,
#
"RI331":0,
"RI332":0,
"RI295":0,
#
"RI330":0,
"RI563":0,
"RI564":0,
#
"RI561":0,
"RI292":0,
"RI562":0,
#
"RI240":0,
"H1621":50,
"RI59":4,
"H1601":30,
## PARTE DEL VECTOR - ESTADO DE RESULTADOS
#Turnover
"BI0012":33713.71,
#Cost of Goods Sold
"BI0041":26044.03,
# Selling, General & Administrative Expenses
"BI0189":2573.52,
"BI0649":0,
"BI0013":5096.16,
"BI0014":342.55,
"BI0178":4753.61,
"BI0015":59.62,
"BI0061":-4387.68,
"BI0017":-146.85,
"BI0170":159.46,
"BI0016":239.5,
"BI0049":-0.08,
"BI0018":-79.96,
#
# Supplemental Income Statement
#
# Common Dividends (Including Total Special Dividends)
"RI21":-79.96,
# Preferred Dividends
"RI19":-79.96,
"RI667":-79.96,
"RI662":-79.96,
#Amortization of Intangibles
"RI65":36.96,
"BI0047":166.77,
"BI0046":0,
"RI62":94.74,
"BI0055":-278.16,
## PARTE DEL VECTOR - CASH FLOW STATEMENT
"RI123":0,
"RI125":0,
"RI124":0,
"RI126":0,
"RI106":0,
"RI213":0,
"RI217":0,
"RI302":0,
"RI303":0,
"RI304":0,
"RI305":0,
"RI307":0,
"RI308":0,
# 
"RI113":0,
"RI109":0,
"RI309":0,
"RI128":0,
"RI107":0,
"RI129":0,
"RI310":0,
"RI311":0,
#
"RI108":0,
"Ri115":0,
"RI127":0,
"RI111":0,
"RI114":0,
"RI301":0,
"RI414":0,
"RI312":0,
"RI313":0,
#
"RI314":0,
#
"RI274":0,
##
# Acciones en circulacion
"RI25":18,
"RI27":6,
## PARTE DEL VECTOR - GROSS PLANT LIFE
#Building Used
"H1021":649.05,
#Revaluation of Fixed Assets
"RI540":0,
#Machinery and Tools
"H1023":2133.62,
#Other Fixed Assets
"H1024":946.12,
#Vehicles
"RI542":21.14,
#Vessels & Aircrafts
"RI543":0,
#Long Leasehold Life
"RI544":0,
#Short Leasehold Life
"RI545":0,
"AVG":0,
## 
## INTANGIBLES FIX FACTSHEET
##
#
"RI537":106.72,
"RI536B":60.13,
"RI532":36.96,
#
"HT1330":0,
#
#OPERATING LEASES
#
"H1013":0,
#
# INFLATION ADJUSTED CASH FLOW
#
"SYSC14":35,
"H1433":30,
"SYSC3":5225.33,
# MINORITY INTERST VALUATION
"H2132_OR":1,
# SYSTEM CONSTANTS
#Plant Inflation Adjustment Trigger Override
"H1394":0,
#Plant Inflation Adjustment Trigger Override
"H1295":0, 
#Monetary Holding Gain/Loss Switch 
"H1296":0, 
#FIFO Profits Switch
"H1289":0,
#Fiscal Month 
"RI998":0, 
}


# Toma el vector generico y lo inicializa
estructura_vector = Columna
for r in estructura_vector.keys():
    estructura_vector[r] = 0
