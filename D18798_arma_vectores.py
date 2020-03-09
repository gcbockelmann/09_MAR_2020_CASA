# ARMA VECTORES
##############################################################################

# Asigna el vector generico inicializado a variables
for i in years_of_valuation:
    x = ("constantes"+str(i))
    b = x + str("=")+str(estructura_constantes)
    exec(b)




#################################################################################################
#Carga con los datos correctos cada vector de constantes

for i in years_of_valuation:
    x = ("constantes"+str(i))
    z = str(i)
    y = x + "['H1502ADD']="+ z
    exec(y)
    # Vamos a cargar la clase que se obtiene del vector datos_empresa en el vector constantes
    a = datos_empresa["CCLASS"]
    y = x + "['CCLASS']=a" 
    exec(y)




#################################################################################################

# Fusiona los diccionarios de cada anio
for i in years_of_valuation:
    #
    x = ("Columna"+str(i))
    y = ("constantes"+str(i))
    c = ("Vector"+str(i))
    #
    #
    #
    #
    d = c + str("=")+str("dict(") + str(x)+ str(",**")+str(y)+str(")")
    exec(d)
    # Agrega el anio a cada Vector
    g= "reporting_year"   
    k= "["
    l= "]"
    h= " = "
    j=str(i)
    m= "\""
    f =c+k+m+g+m+l+h+j
    exec(f)

    


##################################################################################################
# Corre la funcion calculate para todos los vectores
#for i in years_of_valuation:
#    a = i
#    x = "calculate(Vector"+str(i)+str(")")    
#    exec(x)
    
    
#################
#exec(open('C:\GCB_CAPITAL\\C0775_funcion_boton_calculate.py').read())
#calculate(Vector2002)
#calculate(Vector2015)


#
#global ticker
#
# Establece la serie en df_ticker para poder sacar los precios.
def get_price(ticker, ano, mes, dia):
    #
    global df_ticker
    #
    a = str(ano)+str(mes)+str(dia)
    #a = fecha
    #a = "2018-12-" + str(31-i)
    if a in df_ticker.index:
       return float(df_ticker["Cierre_del_dia"].loc[pd.to_datetime(a, format="%Y-%m-%d")])
    else: 
       for i in range(1,10):
           a = str(ano)+str(mes)+str(int(dia)-i)
           if a in df_ticker.index:
              return float(df_ticker["Cierre_del_dia"].loc[pd.to_datetime(a, format="%Y-%m-%d")]) 
              break
    return "NA"

#get_price("MIRG", "2018","12", "31")

def get_max_price(ticker, ano, mes, dia):
    #
    global df_ticker
    #
    a = str(ano)+str(mes)+str(dia)
    #a = fecha
    #a = "2018-12-" + str(31-i)
    #
    b1 = str(ano)+"-"+"1"+"-"+"1"
    b2 = str(ano)+"-"+"12"+"-"+"31" 
    # Filtra el dataframe hacia adelante y lo transforma en una serie
    a = (df_ticker["Cierre_del_dia"][df_ticker.index > b1]) 
    # Filtra la serie con un cap en la fecha maxima
    b= a[a.index <= b2]
    # Calcula el maximo
    c = max(b)
    return c

#get_max_price("MIRG", "2018","12", "31")

def get_min_price(ticker, ano, mes, dia):
    #
    global df_ticker
    #
    a = str(ano)+str(mes)+str(dia)
    #a = fecha
    #a = "2018-12-" + str(31-i)
    #
    b1 = str(ano)+"-"+"1"+"-"+"1"
    b2 = str(ano)+"-"+"12"+"-"+"31" 
    # Filtra el dataframe hacia adelante y lo transforma en una serie
    a = (df_ticker["Cierre_del_dia"][df_ticker.index > b1]) 
    # Filtra la serie con un cap en la fecha maxima
    b= a[a.index <= b2]
    # Calcula el maximo
    c = min(b)
    return c

#get_min_price("MIRG", "2018","12", "31")

#load_gdp_corriente("ARG")

if datos_empresa["Country"]=="Argentina":
   load_gdp_corriente("ARG")
   load_inflation("ARG")
else:
   print("No esta el GDP Corriente cargado")

load_msci()


# Corre la funcion calculate para todos los vectores
for i in years_of_valuation:
    print("Calculo del Vector"+str(i))
    a = i
    x = "calculate(Vector"+str(i)+str(")")    
    exec(x)
    # Crea una columna vacia para el año # HAY QUE CREA ESTA COLUMNA CADA VEZ QUE SE HACE UN ANIO NUEVO
    df_show[str(i)] = ""
    # Setea el indice como el Codigo para poder mapear en base al indice
    df = df_show.set_index('Codigo')
    # Asigna a la columna del anio 2018 , el diccionario (asigna a cada elemento del indice el valor mapeado por el diccionario)
    serie = "a=pd.Series(" + "Vector" + str(i) +")"    
    exec(serie)
    # checkea que sea una serie de pandas
    #print (isinstance(a, pd.Series))  
    df[str(i)] = a
    df[str(i)] = df[str(i)].replace(np.nan, '', regex=True)
    # Resetea el indice para volver al dataframe de exposicion
    df_show = df.reset_index()# Cambia de nombre el df para poder grabarlo

    
# Asigna el nombre df al df_show para poder grabarlo
df = df_show
# Graba el dataframe df en el path especificado
#save_file_generico(df, original_source + "\MODELO", "GENERICO_", ticker, ".xlsx")




lista_de_titulos = ["BI Universal Input Template",
"Current Assets",
"Current Assets",
"Property, Plant & Equipment",
"Supplemental Balance Sheet Data - Assets",
"Current Liabilities",
"Non-Current Liabilities",
"Supplemental Balance Sheet Data - Liabilities",
"Net Assets",
"Automated HOLT Fixes Switches",
"Supplemental Balance Sheet Items",
"Operating Income Before Depreciation",
"Operating Income After Depreciation",
"Pretax Income",
"Net Income After Minority Interest",
"Supplemental Income Statement Data",
"Supplemental Leases Variables",
"Assets",
"Liabilities",
"Income statement",
"Override Slots Forecast Adjustments",
"Other Company Data",
"Market Section",
"Cash EPS Adjustments",
"Merger & Acquisition",
"Statement of Cash Flows",
"Operating Activities",
"Investing Activities",
"Financing Activities",
"Global Non-Depreciating Assets",
"Non-Depreciating Assets Summary",
"Net Monetary Assets",
"Monetary Assets",
"Monetary Liabilities Excluding Debt",
"Investments & Advances",
"Inflation Adjusted Inventories",
"Inflation Adjusted Land",
"Other Assets",
"Gross Operating Intangibles (Indefinite Lived)",
"Lease Data Input - US GAAP (RI988U=1) - BI Variables",
"Balance Sheet",
"Worldscope (FUND_VENDOR_ID=4)",
"Lease Data Input - IFRS (RI988U=2) - BI Variables",
"Refer to Capitalization of R&D factsheet for more R&D Layers",
#
"Global Depreciating Assets",
"Depreciating Assets Summary",
"Inflation Adjusted Gross Plant",
"Capitalized Operating Leases",
"Inflation Adjusted Finite Intangible",

"CFROI Audit And Valuation",
"CFROI Used in Valuation",
"Valuation Factors",
"Fade - See Fade Factsheets",
"Audit of Company Specific Discount Rate",
"Valuation Output",
#
"Global Inflation Adjusted Cash Flow",
"Earnings Cash Flow",
"Non-Earnings Cash Flow",
"Adjusted Interest Expense",
"Monetary Holding Gain",
"LIFO Charge to FIFO Inventories",
"Net Pension Expense Cash Flow Adjustment",
"Change in Other Risk Provision",
#
"Gross Plant Life",
"Straight Line Life Data and Calculation",
"Weighted Average Life Data and Calculation",
#
"Project Life",
"Intangibles Fix Factsheet",
"Intangibles Summary",
"CAPITALIZED SOFTWARE DATA:",
"Software in Intangible Assets",
"Operating Intangibles:",
"Intangibles included in Non-Depreciating Assets:",
"3.Gross Indefinite Life Operating Intangibles",
"Other Indefinite Life Operating Intangibles - Manual Input",
"Gross Indefinite Life Operating Intangibles - Summary",
"Net Operating Intangibles",
"Intangibles included in Depreciating Assets",
"4.Gross Finite Life Operating Intangibles (in Life)",
"Other Finite Life Operating Intangibles (in Life) - Manual Input",
"Gross Finite Life Operating Intangibles (in Life) - Summary",
"5.Gross Finite Life Operating Intangibles (Not in Life)",
"Gross Finite Life Operating Intangibles (ex Life Calc) - Summary",
"Capitalized Software in Other Assets",
#
"Inflation Adjustments for Emerging Markets",
#
"Normalized Growth Rate",
"Normalized Growth Rate Summary",
"Simple Ploughback",
"Payments to Capital Owners",
"Retirements",
"Conditional Net Capital Events",
"BOY Inflation Adjusted Gross Investment",
"Other Information",
"Growth Rate Used in Valuation",
#
"Bounded Historic Growth Rate",
"Constant Currency Gross Plant",
"Gross Plant Historic Growth Rate Flows Into.",
"Constant Currency Depreciation Assets",
"Depreciating Assets Historic Growth Rate Flows Into.",
#
"Debt Audit",
"Merton Model Calculation Details",
"Market Value of Debt Calculation",
"Ratio Analysis",
#
"eCap Audit",
#
"Minority Interest Valuation",
#
"System Constants",
#
"Company Specific Discount Rate",
#
"Variables Adicionales",
]

# PARA HACER SEPARADOR DE PAGINAS

lista_de_titulos_de_paginas = ["BI Universal Input Template"]




lista_de_codigos_de_variables_a_imputar = ["BI0001", 
"BI0002",
"BI0003",
"BI0068",
"BI0004",
"BI0007",
"BI0196",
"BI0008",
"BI0158",
"BI0260",
"BI0073",
"BI0266",
"BI0069",
"BI0033",
"BI0031_I",
"BI0032_I",
"BI0006",
"RI204",
"RI505M",
#
"BI0070",
"BI0071",
"BI0072",
"BI0034",
"BI0005",
"BI0009",
"BI0075",
"BI0035",
"BI0038",
"BI0181",
"RI74",
"RI397",
"BI0216",
"BI0060",
"BI0130",
"RI36",
#
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
#
"RI572",
"RI573",
"RI574",
#
"RI575",
"RI576",
"RI578",
#
"RI286",
"RI287",
"RI290",
#
"RI294",
"RI296",
"RI300",
#
"RI331",
"RI332",
"RI295",
#
"RI330",
"RI563",
"RI564",
#
"RI561",
"RI292",
"RI562",
#
"RI240",
"RI59",
#
"RI562",
#
"H1601",
################
"BI0012",
"BI0012_6",
"BI0041",
"BI0189",
"BI0649",
"RI649",
"BI0013",
"BI0014",
"BI0178",
"BI0015",
"BI0015_8",
"BI0061",
"BI0017",
"BI0170",
"BI0016",
"BI0016_10",
"BI0049",
"BI0018",
"RI661",
"RI21",
"RI19",
"RI667",
"RI662",
"BI0014_8",
"RI65",
"RI998",
"RI25",
"S114V",
"BI004V",
"BI0046",
"RI398A",
"RI415",
"RI426",
"RI399A",
"RI128",
"RI874",
"RI190",
"RI62",
"RI147",
"BI0055",
"RI988F",
"LEASE_YR",
]




    
def graba_modelo(df, ticker):
    #
    global lista_de_titulos, lista_de_codigos_de_variables_a_imputar, datos_empresa, years_of_valuation
    #
    #GRABA EL ARCHIVO , SETEANDO FORMATOS DE COLUMNAS, AUTOFIT
    writer = pd.ExcelWriter(original_source + '\MODELO\OUTPUT\\' + 'MODELO_GENERICO_' + ticker + '.xlsx', engine='xlsxwriter')
    #
    df.to_excel(writer, sheet_name='MODELO')
    workbook  = writer.book
    worksheet = writer.sheets['MODELO']
    #format1 = workbook.add_format({'num_format': '#.##0,00'})
    #format1 = workbook.add_format({'num_format': '#,##0;(#,##0)'})})
    #format1 = workbook.add_format({'num_format': '#,##0;(#,##0)'})})
    format1 = workbook.add_format({'num_format': '0.00'})
    #get_col_widths(df)
    #
    # 
    #for i, width in enumerate(get_col_widths(df)):
    #    worksheet.set_column(i, i, width)
    #
    # Setea la columna B a ancho 18 (contiene fecha)
    worksheet.set_column('B:B', 15, format1)
    # Setea la columna C a ancho 18
    worksheet.set_column('C:C', 40, format1)
    #
    # Freeza los paneles
    worksheet.freeze_panes(1, 3)
    #
    # ####### PONE TITULOS NE NEGRITA
    #
    title_cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})
    #
    #
    #   
    #
    lista_de_posicion_vertical_a_poner_en_negrita = []
    lista_de_escritura_de_titulo = []
    #
    for i in lista_de_titulos:
        lista_nueva = list(df[df["Concepto"] == i].index)
        for x in lista_nueva:
            lista_de_posicion_vertical_a_poner_en_negrita.append(x)
            lista_de_escritura_de_titulo.append(i)
    #
    # Estas lineas eran para ver si las longitudes de las listas estaban bien o sea son iguales.
    #print (len(lista_de_posicion_vertical_a_poner_en_negrita))
    #print(len(lista_de_escritura_de_titulo))
    #
    # Escribe algo en una posicion fija
    #worksheet.write(0, 1,'Cell A1', title_cell_format)
    #
    # Itera para cada numero de posicion vertical de la lista de posiciones, saca el titulo de otra lista, y le aplica el formato.
    for i in range(0,len(lista_de_posicion_vertical_a_poner_en_negrita)):
        worksheet.write(lista_de_posicion_vertical_a_poner_en_negrita[i]+1, 2, str(lista_de_escritura_de_titulo[i]) ,title_cell_format)
    #
    ########################## PONE FORMATO A LA SEPARACION DE HOJAS     
    #
    lista_de_posicion_vertical_de_variables_a_imputar = []
    #
    for i in lista_de_codigos_de_variables_a_imputar:
        lista_nueva = list(df[df["Codigo"] == i].index)
        for x in lista_nueva:
            lista_de_posicion_vertical_de_variables_a_imputar.append(x)
    #
    #
    input_cell_format = workbook.add_format({'bold': False, 'font_color': 'black', 'bg_color':'#ffff99'})
    #    
    #worksheet.write(0, 0,'Cell A1', input_cell_format)
    #
    #
    #datos_empresa["Designated First Year (MFIRST)"]
    #Ahora es la columna 3 = columna 2002-2002+3
    for i in lista_de_posicion_vertical_de_variables_a_imputar:
        for x in range(1, 2+int(datos_empresa["Designated Last Reported Year (MLASTM)"])-int(datos_empresa["Designated First Year (MFIRST)"])):
            year = years_of_valuation[x-1]
            worksheet.write(i+1, x+2,df[str(year)].iloc[i], input_cell_format)
            #worksheet.write(i+1, x+2,'Cell A1', input_cell_format)
    #
    #
    # Graba el archivo
    writer.save()
    #
    ###### INICIALIZA LA MEMORIA
    #
    # Borra los vectores de la memoria
    for i in range(1990,2019):
        var_name = 'Columna' + str(i)
        if var_name in globals():
           #print (i)
           del globals()[var_name]
    #
    ###### INICIALIZA EL DATAFRAME Y LO DEJA LISTO PARA ARRANCAR
    #
    #del globals()["df"]
    #del globals()["df_show"]
    #
    #


graba_modelo(df, ticker)

### Borra las constantes

#for i in years_of_valuation:
#    x = ("constantes"+str(i))
#    b = "del "+ x
#    exec(b)

#for i in years_of_valuation:
#    x = ("Columna"+str(i))
#    b = "del "+ x
#    exec(b)



