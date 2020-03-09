##################################################################################################################################3
##################### CREA UN DATAFRAME
##################################################################################################################################

#INDICE GENERAL
#INDICE GENERAL
# Crea la lista una lista vacia
indice_dataframe = []

#Agrega valores al indice del dataframe
for i in range(0, 2000, 1):
    indice_dataframe.append(i)

# Muestra el indice que se agregaria al dataframe
#indice_dataframe 

# Crea la lista de columnas para iniciar un dataframe solo con la columna Concepto
list_of_columns = ['Codigo', 'Concepto']

# Crea el dataframe
df_show = pd.DataFrame(index = indice_dataframe, columns=list_of_columns)

#Inicializa el diccionario de nombres de conceptos
nombres_conceptos={}


#### CREA FUNCION QUE LE DA FORMATO A LAS LISTAS PARA LOS TITULOS Y ESPACIOS EN BLANCO

def agrega_linea_a_dos_listas(lista_de_codigos_a_mostrar_show, lista_de_nombres_de_conceptos_a_mostrar_show, posicion, texto1, texto2):
    #
    lista_de_codigos_a_mostrar_show.insert(posicion , texto1)
    lista_de_nombres_de_conceptos_a_mostrar_show.insert(posicion, texto2)

def inicializa_un_nuevo_dataframe():
    #
    global df_show, nombres_conceptos
    #
    # Crea la lista una lista vacia
    indice_dataframe = []
    #
    #Agrega valores al indice del dataframe
    for i in range(0, 2000, 1):
        indice_dataframe.append(i)
    #
    # Crea la lista de columnas para iniciar un dataframe solo con la columna Concepto
    list_of_columns = ['Codigo', 'Concepto']
    #
    #
    # Crea el dataframe
    df_show = pd.DataFrame(index = indice_dataframe, columns=list_of_columns)
    #
    #Inicializa el diccionario de nombres de conceptos
    nombres_conceptos={}
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

#inicializa_un_nuevo_dataframe()
