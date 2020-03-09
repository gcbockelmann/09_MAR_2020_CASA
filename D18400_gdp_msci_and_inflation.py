
#### CARGA GDP CORRIENTE

#  ACARGAR EN ARMA VECTORES


def load_gdp_corriente(country):
    global df, gdp_corriente
    open_file_versatil(original_source + "INPUT_MANUAL\\", "GDP_ARG", ".xlsx")
    serie_de_tiempo(df)
    gdp_corriente = df

#load_gdp_corriente("ARG")

def get_gdp_corriente(ano, mes, dia):
    #
    #
    #
    global gdp_corriente
    #
    a = str(ano)+str(mes)+str(dia)
    #
    if a in gdp_corriente.index:
       return float(gdp_corriente["gdp_corriente"].loc[pd.to_datetime(a, format="%Y-%m-%d")])
    else: 
       return "NA"

#get_gdp_corriente("2018","12","31")

def load_msci():
    global df, msci
    open_file_versatil(original_source + "INPUT_MANUAL\\", "MSCI_WORLD_INDEX", ".xlsx")
    serie_de_tiempo(df)
    msci = df

#load_msci()

def get_msci(ano, mes, dia):
    #
    #
    #
    global msci
    #
    a = str(ano)+str(mes)+str(dia)
    #
    if a in msci.index:
       return float(msci["msci_world_index"].loc[pd.to_datetime(a, format="%Y-%m-%d")])
    else: 
       return "NA"

#get_msci("2018","12","31")


def load_inflation(country):
    global df, inflation
    open_file_versatil(original_source + "\INPUT_MANUAL", "CPI_ARG_MANUAL", ".xlsx")
    serie_de_tiempo(df)
    inflation = df

#load_inflation("ARG")

def get_inflation(ano, mes, dia):
    #
    #
    global inflation
    #
    a = str(ano)+str(mes)+str(dia)
    #
    if a in inflation.index:
       return float(inflation["VARIACION_A-A"].loc[pd.to_datetime(a, format="%Y-%m-%d")])
    else: 
       return "NA"

#get_inflation("2018","12","31")



def f_dcf(year, month, life, historic_growth_rate_of_gp, gp):
    if historic_growth_rate_of_gp == 0:
       return 0 
    a= 1/float(life)
    #historic_growth_rate_of_gp=1.9
    capex_1= (gp*(historic_growth_rate_of_gp/100))/(((1+(historic_growth_rate_of_gp/100))**life)-1)
    #inflation_rate = 2
    #inflation_rate = 100*get_inflation("2018","12","31")
    #print(inflation_rate)
    #
    total_inflation_adjustment=0
    #total_inflation_adjustment = []
    #
    # 
    beginning_year=year-life
    #   
    for i in range(0, life-1):
        capex = capex_1*((1+(historic_growth_rate_of_gp/100))**i)
        #print(capex)
        if get_inflation(str(beginning_year+1+i),"12","31")=="NA":
           inflation_rate=0
           #inflation_rate=2  
        else:
           #inflation_rate = 100*get_inflation(str(beginning_year+1+i),"12","31")
           inflation_rate=2  
        #print(inflation_rate)
        adjusted_capex = capex*(1+(inflation_rate/100))**(life-1-i)
        inflation_adjustment = adjusted_capex - capex
        total_inflation_adjustment +=inflation_adjustment
        #total_inflation_adjustment.append(inflation_adjustment)
    return total_inflation_adjustment


#f_dcf(2017,12, 5, 22.4, 2500)

#f_dcf(2017,12, 9, 7.39, 935.42)

def land_inflation_factor(year, month, life, historic_growth_rate_of_gp, land):
    #
    if historic_growth_rate_of_gp == 0:
       return 0 
    a= 1/float(life)
    #historic_growth_rate_of_gp=1.9
    capex_1= (gp*(historic_growth_rate_of_gp/100))/(((1+(historic_growth_rate_of_gp/100))**life)-1)
    #inflation_rate = 2
    #inflation_rate = 100*get_inflation("2018","12","31")
    #print(inflation_rate)
    #
    total_inflation_adjustment=0
    #total_inflation_adjustment = []
    #
    # 
    beginning_year=year-life
    #   
    for i in range(0, life-1):
        capex = capex_1*((1+(historic_growth_rate_of_gp/100))**i)
        #print(capex)
        if get_inflation(str(beginning_year+1+i),"12","31")=="NA":
           inflation_rate=0
        else:
           inflation_rate = 100*get_inflation(str(beginning_year+1+i),"12","31")
        #print(inflation_rate)
        adjusted_capex = capex*(1+(inflation_rate/100))**(life-1-i)
        inflation_adjustment = adjusted_capex - capex
        total_inflation_adjustment +=inflation_adjustment
        #total_inflation_adjustment.append(inflation_adjustment)
    return total_inflation_adjustment


#################################REHACIENDO LA FORMULA POR PARTES ###########################

def initial_capex(actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth):
    #
    #
    capex= actual_gross_amount/((((1+(nominal_average_rate_of_growth/100))**total_years_of_delayering)-1)/((nominal_average_rate_of_growth/100)))
    #
    #
    return capex

#initial_capex(2500, 5, 22.4)


def asset_layers(asset_layer_number, actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth):
    #
    initial = initial_capex(actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth)
    #
    if asset_layer_number <= total_years_of_delayering:
       capex_layer = initial*(1+(nominal_average_rate_of_growth/100))**(asset_layer_number-1)
    else: 
       print ("Error: capex_layer_number mayor al numero de years de delayering")
       capex_layer = 0
    #
    return capex_layer
    
#asset_layers(2, 2500, 5, 22.4)

def inflation_adjustment(average_rate_of_inflation, amount_of_capex_layer, years_of_compounding):
    #
    inflation_adjustment = amount_of_capex_layer * (1+(average_rate_of_inflation/100))**(years_of_compounding)
    #
    return inflation_adjustment


#inflation_adjustment(2, 320, 4)
#inflation_adjustment(2, 480, 2)
#inflation_adjustment(2, 719, 0)



def arma_lista_de_capex_layers(actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth):
    #
    #
    capex_layer_a = initial_capex(actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth)
    #
    lista_de_capex_layers = []
    #
    lista_de_capex_layers.append(capex_layer_a)
    #  
    for i in range(1,(total_years_of_delayering)):
        layer = asset_layers(i+1, actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth)
        lista_de_capex_layers.append(layer)
    #
    if len(lista_de_capex_layers)==total_years_of_delayering:
       return lista_de_capex_layers
    else:
       print ("Error: en la formual de delayering, cantidad de capex_layers diferentes a la cantidad de anios de compounding")
    #
    
#arma_lista_de_capex_layers(2500, 5, 22.4)
#layers = arma_lista_de_capex_layers(2500, 5, 22.4)

def arma_lista_de_inflation_adjusted_values(lista_de_capex_layers,average_rate_of_inflation):
    #
    #
    #capex_layer_a = initial_capex(lista_de_capex_layers, actual_gross_amount, nominal_average_rate_of_growth)
    #
    total_years_of_delayering = len(lista_de_capex_layers)
    #
    lista_de_inflation_adjusted_values = []
    #
    #  
    for i in range(1,(total_years_of_delayering+1)):
        # 
        inflation_adjustment_point = inflation_adjustment(average_rate_of_inflation, lista_de_capex_layers[-1+i] , total_years_of_delayering-i)
        lista_de_inflation_adjusted_values.append(inflation_adjustment_point)
    #
    return lista_de_inflation_adjusted_values
    #if len(lista_de_inflation_adjusted_values)==total_years_of_delayering:
    #   return lista_de_inflation_adjusted_values
    #else:
    #   print ("Error: en la formual de delayering, cantidad de inflation_adjustments diferentes a la cantidad de anios de compounding")
    

def devuelve_total_ajustado(actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth, average_rate_of_inflation):
    #
    layers = arma_lista_de_capex_layers(actual_gross_amount, total_years_of_delayering, nominal_average_rate_of_growth)
    #
    ajustados = arma_lista_de_inflation_adjusted_values(layers, average_rate_of_inflation)
    #
    total_ajustados = sum(ajustados)
    #
    return total_ajustados

#devuelve_total_ajustado(2500, 5, 22.4, 2)

# Se usa un metodo de list comprehension
#ajustes = [a - b for a, b in zip(ajustados, layers)]
#total_adjustement = sum(ajustes)


#### PRUEBA REAL

#layers = arma_lista_de_capex_layers(1.368461960, 11, 1.89999997)
#ajustados = arma_lista_de_inflation_adjusted_values(layers, 2)


#PRUEBA 2018
#layers = arma_lista_de_capex_layers(32.3250007629395, 2, 4.07192707061768)
#ajustados = arma_lista_de_inflation_adjusted_values(layers, 40.6999931335449)

### FUNCION MEJORADA

#PPI index
#inflation_list = [6.28288984298706, 15.0721435546875, 13.7508029937744, 12.1904850006104, 16.3191566467285, 26.0062103271484, 12.1993427276611, 38.178466796875, 16.2636528015137]


def arma_lista_de_inflation_adjusted_values_mejorada(lista_de_capex_layers,lista_de_inflation):
    #
    if len(lista_de_inflation) == len(lista_de_capex_layers):
       #
       total_years_of_delayering = len(lista_de_capex_layers)
       #
       lista_de_inflation_adjusted_values = []
       #
       for i in range(1,(total_years_of_delayering+1)):        
           inflation_adjustment_point = inflation_adjustment(average_rate_of_inflation, lista_de_capex_layers[-1+i] , total_years_of_delayering-i)
           lista_de_inflation_adjusted_values.append(inflation_adjustment_point)
       #
    else:
       print("Problema: Ambas listas no tienen la misma cantidad de elementos")
    #
    #
    #
    #
    #
    #  
    #
    #
    #return lista_de_inflation_adjusted_values
    #if len(lista_de_inflation_adjusted_values)==total_years_of_delayering:
    #   return lista_de_inflation_adjusted_values
    #else:
    #   print ("Error: en la formual de delayering, cantidad de inflation_adjustments diferentes a la cantidad de anios de compounding")



################################### FUNCION AJUSTE POR INFLACION CON COMPOUNDING
def inflation_adjustment_with_compounding(list_of_inflation, amount_of_capex_layer, years_of_compounding):
    #
    inflation_adjustment = amount_of_capex_layer
    #   
    if years_of_compounding<=len(list_of_inflation):
       for i in range(0,len(list_of_inflation)):
           inflation_adjustment *= (1+(list_of_inflation[i]/100))
       return inflation_adjustment
    else:
       print ("problema:")
    
#for i in range(0,len(inflation_list)):
#    inflation_adjustment *= (1+(inflation_list[i]/100))

#inflation_adjustment_with_compounding(inflation_list, 0.79406755, 9)
#inflation_adjustment_with_compounding(inflation_list, 0.85182089, 8)

################################### FUNCION AJUSTE POR INFLACION CON COMPOUNDING_VERSION2
def inflation_adjustment_with_compounding(list_of_inflation, amount_of_capex_layer):
    #Recibe un vector de inflaciones y compone el monto por la x cantidad de elementos de la lista
    inflation_adjustment = amount_of_capex_layer
    #   
    for i in range(0,len(list_of_inflation)):
        inflation_adjustment *= (1+(list_of_inflation[i]/100))
    return inflation_adjustment
    
#inflation_adjustment_with_compounding(inflation_list, 0.79406755)

#inflation_list.pop(0)

#inflation_adjustment_with_compounding(inflation_list, 0.85182089)

#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################

#PPI index
#inflation_list = [6.28288984298706, 15.0721435546875, 13.7508029937744, 12.1904850006104, 16.3191566467285, 26.0062103271484, 12.1993427276611, 38.178466796875, 16.2636528015137]

def adjusted_values(list_of_inflation,lista_de_capex_layers):
    #
    total_inflated_values = []
    #
    #
    if len(list_of_inflation) == len(lista_de_capex_layers):
       for i in range(0, (len(lista_de_capex_layers))):
           if i == 0: 
              #print(i)
              inflated_value = inflation_adjustment_with_compounding(list_of_inflation, lista_de_capex_layers[i])
              #print (list_of_inflation)
              #print (inflated_value)
              total_inflated_values.append(inflated_value)
           elif i == (len(lista_de_capex_layers)-1): 
              #print ("8")  
              inflated_value = lista_de_capex_layers[i]
              #print (inflated_value)   
              total_inflated_values.append(inflated_value)       
              #print ("HOLAAAA")                    
           elif i < (len(lista_de_capex_layers)-1):
              #print(i)
              copia_inflation = list_of_inflation.copy()
              for counter in range(0,i):  
                  copia_inflation.pop(0)
                  #print ("i es=", i)
                  #print (copia_inflation)
              inflated_value = inflation_adjustment_with_compounding(copia_inflation, lista_de_capex_layers[i])
              #print (lista_de_capex_layers[i])
              #print (inflated_value)
              total_inflated_values.append(inflated_value)
           else:
              #print(i)  
              #if i == len(lista_de_capex_layers)
              #inflated_value = lista_de_capex_layers[i+1]
              #print (inflated_value)          
              print ("Aca hay un problema")
       #
       return total_inflated_values
    #
    else:
       print("Problema: diferentes cantidad de elementos en las listas")

#adjusted_values(inflation_list, layers)

#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################

def devuelve_total_ajustado_con_inflacion_compuesta(lista_de_inflacion, lista_de_capex_layers):
    #
    total_de_valores_ajustados = adjusted_values(lista_de_inflacion, lista_de_capex_layers)
    #
    total_de_valores_ajustados = sum(total_de_valores_ajustados)
    #
    return total_de_valores_ajustados

#devuelve_total_ajustado_con_inflacion_compuesta(inflation_list, layers)



def load_ppi_inflation(country):
    global df, ppi
    open_file_versatil(original_source + "\INPUT_MANUAL", "PPI_ARG_MANUAL", ".xlsx")
    serie_de_tiempo(df)
    ppi = df

# Carga 
load_ppi_inflation("ARG")



def get_ppi_inflation(ano, mes, dia):
    #
    #
    global ppi
    #
    a = str(ano)+str(mes)+str(dia)
    #
    if a in ppi.index:
       return float(ppi["VARIACION_A-A"].loc[pd.to_datetime(a, format="%Y-%m-%d")])
    else: 
       return np.nan

#get_ppi_inflation("2018","12","31")



#datos_empresa["GICS Global Industry Code Display"]="Household Appliances"

def load_historic_industry_growth():
    global df, historic_industry_growth
    open_file_versatil(original_source + "\INPUT_MANUAL", "INDUSTRY_GROWTH", ".xlsx")
    serie_de_tiempo(df)
    historic_industry_growth = df

# Carga 
load_historic_industry_growth()



def get_historic_industry_growth(ano, mes, dia):
    #
    global historic_industry_growth
    #
    a = str(ano)+str(mes)+str(dia)
    #
    if a in historic_industry_growth.index:
       return float(historic_industry_growth[datos_empresa["GICS Global Industry Code Display"]].loc[pd.to_datetime(a, format="%Y-%m-%d")])
    else: 
       return np.nan

#get_historic_industry_growth("2018","12","31")
