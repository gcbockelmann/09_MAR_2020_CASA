### CARGA NADS GENERICO DESDE UN EXCEL

# Asigna el vector generico inicializado a variables
#  Crea en memoria espacio para las variables Columna
#for i in range (datos_empresa["Designated First Year (MFIRST)"],datos_empresa["Designated Last Reported Year (MLASTM)"]+1):
#    x = ("Columna"+str(i))
#    b = x + str("=")+str(estructura_vector)
#    exec(b)
  

#for i in range (2017,2018):
#    # Crea vectores
#    x = ("Columna"+str(i))
#    b = x + str("=")+str(estructura_vector)
#    exec(b)



def open_equity(ticker):
    #
    # Importa modulos con los que va a verificar la existencia de archivos (mas adelante)
    import os
    import shutil
    # Trabaja con variables globales
    global df, a, b, c, Columna2018, diccionario_surgido_del_pdf, datos_empresa, years_of_valuation
    #
    # Inicializa el diccionario empresa
    datos_empresa = {}
    carga_datos_empresa(ticker) 
    #
    ############################################################ BORRA LOS VECTORES ANTERIORES QUE PUEDE HABER EN MEMORIA
    #if len(years_of_valuation)>0:
    #   for i in years_of_valuation:
    #       x = ("constantes"+str(i))
    #       b = "del "+ x
    #       exec(b)
    #
    # Toma un rango grande y borra todas las variables que puede haber generado el sistema
    for i in range(1990,2019):
        var_name = 'Columna' + str(i)
        if var_name in globals():
           #print (i)
           del globals()[var_name]
    #
    #del globals()["df"]
    #del globals()["df_show"]
    inicializa_un_nuevo_dataframe()
    #
    #
    ### NUEVO ARMADOR DE MODELOS
    exec(open(original_source+"D18000_inicia_dataframe.py").read())
    exec(open(original_source+"D18100_arma_paginas.py").read())
    exec(open(original_source+"D18200_agrega_partes_al_dataframe.py").read())
    exec(open(original_source+"D18400_gdp_msci_and_inflation.py").read())
    exec(open(original_source+"D18500_funcion_boton_calculate.py").read())
    exec(open(original_source+'D18793_crea_columna_generica.py').read())
    exec(open(original_source+'D18794_crea_estructura_constantes.py').read())
    # Define el ticker
    exec(open(original_source+'D18795_carga_datos_empresa.py').read())
    # Prepara para leer el archivo de excel
    exec(open(original_source+'D18797_carga_nads_generico.py').read())
    #
    #    if exists("Columna"+str(i)):
    #       del globals()["Columna"+str(i)]
    #    x = ("Columna"+str(i))
    #    y = ("global "+"Columna"+str(i))
    #    exec(y)
    #    if exists("Columna"+str(i)):
    #       print("Columna"+str(i))
    #       #print (x)
    #    exists(x)
    #
    #    #print(x)
    #    var_name = '"' + 'Columna' + str(i) + '"'
    #    print(var_name)
    #    #
    #    if not exists(var_name):
    #       pass
    #    else:
    #       y = ("global "+"Columna"+str(i))
    #       exec(y)
    #       b = "del "+ x
    #       exec(b) 
    #
    ##########################################################################################################################
    #
    # DEFINE RANGOS ESTANDAR EN CASO DE NO ESTAR DEFINIDO UN RANGO
    if len(datos_empresa)==0:
       datos_empresa["Designated First Year (MFIRST)"]=0
       datos_empresa["Designated Last Reported Year (MLASTM)"]=0
    #
    ######################## CORRE UN LOOP INICIALIZANDO LAS VARIABLES
    for i in range (datos_empresa["Designated First Year (MFIRST)"],datos_empresa["Designated Last Reported Year (MLASTM)"]+1):
        x = ("Columna"+str(i))
        b = x + str("=")+str(estructura_vector)
        exec(b, globals())      
    #######################################################################
    #
    #Muestra las caracteristicas del equity y carga el ultimo escenario
    #exists = os.path.isfile("C:/GCB_CAPITAL/ESCENARIOS/"+str(ticker)+".xlsx")
    exists = os.path.isfile(original_source + "MODELO/ESCENARIOS/"+str(ticker)+".xlsx") 
    if exists:
       open_file_versatil(original_source + "MODELO\ESCENARIOS", ticker, ".xlsx")
    else: 
       print("File not found")
    #
    # Establece el indice como la columna TICKER
    df = df.set_index("TICKER")
    # No se exactamente que hace
    df.columns = df.iloc[0]
    # convierte a strings todos los headings
    df.columns = df.columns.map(str)
    #
    #
    #
    #
    #
    #
    # Inicializa un vector para poder contar que anios estan en el df
    years_of_valuation = []
    #
    #
    #
    for i in range(datos_empresa["Designated First Year (MFIRST)"],datos_empresa["Designated Last Reported Year (MLASTM)"]+1):
        if str(i) in df and int(str(i)) in range(datos_empresa["Designated First Year (MFIRST)"],datos_empresa["Designated Last Reported Year (MLASTM)"]+1):
           years_of_valuation.append(i)
           b = df[str(i)]
           b=b.reset_index()
           b = b.dropna()
           #c = b.set_index("TICKER")
           diccionario_surgido_del_pdf = b.set_index('TICKER')[str(i)].to_dict()
           if i <= 2001:
              print("No definido para rangos inferiores al 2001")
           elif i == 2001:
              # Prepara la estructura de una columna generica 2001
              # Toma la estructura de la columna en este caso 2001 y la vacia
              #
              x = globals()["Columna"+str(i)]
              for r in x.keys():
                  x[r] = 0
              for llave in list(x.keys()):
                  #print(i)
                  #i in diccionario_surgido_del_pdf
                  if llave in diccionario_surgido_del_pdf:
                     x["Year"]=str(i)
                     x[llave] = diccionario_surgido_del_pdf[llave]
           elif 2001 <= i <= (datos_empresa["Designated Last Reported Year (MLASTM)"]+1):
              # Prepara la estructura de una columna generica ano
              # Toma la estructura de la columna en este caso ano y la vacia
              #
              x = globals()["Columna"+str(i)]
              for r in x.keys():
                  x[r] = 0
              for llave in list(x.keys()):
                  #print(i)
                  #i in diccionario_surgido_del_pdf
                  if llave in diccionario_surgido_del_pdf:
                     x["Year"]=str(i)
                     x[llave] = diccionario_surgido_del_pdf[llave]
        else:
              #lista_de_columnas = list(df.columns)
              #lista_de_columnas.remove("Codigo")    
              #lista_de_columnas.remove("Concepto")
              #for i in lista_de_columnas:
              #    if i not in range(datos_empresa["Designated First Year (MFIRST)"],datos_empresa["Designated Last Reported Year (MLASTM)"]):
              #       df.drop(i, axis=1)
              pass
    # 
    #
    # Arma las listas de columnas del df y le quita la columna concepto y codigo
    #lista_de_columnas = list(df.columns)
    #if "Codigo" in lista_de_columnas:
    #   lista_de_columnas.remove("Codigo")    
    #if "Concepto" in lista_de_columnas:
    #   lista_de_columnas.remove("Concepto")
    #
    #print(lista_de_columnas)
    #
    # Crea una lista de anios posibles
    # 
    #lista_de_anios_posibles = []
    #
    #for i in range (1990, 2018+1):
    #    lista_de_anios_posibles.append(i)
    #
    #print (lista_de_anios_posibles)
    #
    # Crea una lista de columnas a borrar del dataframe
    #
    #lista_de_columnas_a_borrar = []
    #
    #for i in lista_de_anios_posibles:
    #    #
    #    if str(i) in df.columns or i in df.columns:
    #       if int(i) in range(int(datos_empresa["Designated First Year (MFIRST)"]), int(datos_empresa["Designated Last Reported Year (MLASTM)"]+1)):
    #          print("dentro del rango"+ str(i))
    #          # No hace nada si el ano posible esta en el df y esta en dentro del rango
    #          pass
    #       else:
    #          # No hace nada si el ano posible esta en el df y esta en dentro del rango 
    #          print("No en el rango"+ str(i))
    #          lista_de_columnas_a_borrar.append(i)
    ##          pass
    #    else:         
    #       print("No en el df.columns "+ str(i))
    #       pass
    #
    #print(lista_de_columnas_a_borrar)
    #
    #for i in lista_de_columnas_a_borrar:
    #    df = df.drop(str(i), axis=1)
    #
    #
    # Crea una lista de anios de vlauacion pero en string
    #years_for_strings = years_of_valuation.copy()
    #years_strings=list(map(str,years_for_strings))
    # 
   
     
   

#open_equity("MIRG")



def exists(var):
     var_exists = var in locals() or var in globals()
     # will return true or false
     return var_exists

#exists("variable_name")

#exists("Columna1990")

######################################### PRUEBA NUEVA FUNCION



