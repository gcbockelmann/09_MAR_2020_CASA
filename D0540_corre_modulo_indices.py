
### MODULO INDICES


##### MODULO INDICES

def corre_modulo_indice_merval(file_name):
    #
    #Prepara el input del merval
    print("Prepara el input del merval") 
    prepara_input_merval(original_source +"\BOLSAR", file_name, ".xlsx", original_source + "\INPUT", "Indices")
    print()
    #
    # Actualiza la serie de ^MERV
    print("Actualiza la serie de ^MERV") 
    update_indice("^MERV")
    print()
    #
    # Sobreescribe la serie de ^MERV
    b= file_name[0:10]
    #print(b)
    print("Sobre-escribe el indice")
    sobre_escribe_indice("^MERV", b)
    print()
    #
    # Actualiza la serie de ^MERV USD
    print("Actualiza la serie de MERV USD") 
    update_index_usd("^MERV")
    print()
    # Actualiza la serie de ^MERV USDPPP
    print("Actualiza la serie de MERV USDPPP")
    update_index_usdppp("^MERV")
    print()

#corre_modulo_indice_merval("2020-01-21_TODO")


