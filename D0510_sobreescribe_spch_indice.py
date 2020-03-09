

def sobre_escribe_indice(ticker, fecha_del_ultimo_dato_para_actualizar):
    #
    #
    filename = "SERIE_CORRIENTE_" + str(ticker)
    #
    import os
    import shutil
    #
    exists = os.path.isfile(original_source + "/OUTPUT/INDICES/SERIE_CORRIENTE_" +str(ticker)+".xlsx")
    #
    if exists:
         df = open_file_spch(original_source + "\OUTPUT\INDICES", filename , ".xlsx")
         df.tail(1).index # para buscar la ultima fecha de la serie
         intermedio = str(df.tail(1).index) # Transformamos en una variable string
         b = intermedio[16:26] # Extraemos el dato de la fecha del ultimo dia de la serie en formato STRING
         if fecha_del_ultimo_dato_para_actualizar == b:
            old_path = original_source +"/OUTPUT/INDICES/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
            nuevo_path = original_source +"/SPCH/SERIE_CORRIENTE_"+str(ticker)+".xlsx"
            newPath = shutil.copy(old_path, nuevo_path)
            return
         else:
            print("Date not match")
            return
    else:
       print("no escribe dado que no existe el path a copiar")
       return



#sobre_escribe_indice("^MERV", '2020-01-21')