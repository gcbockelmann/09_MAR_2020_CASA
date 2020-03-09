def actualizacion_modulo_spch(date):
    borrar_archivos_de_un_subdirectorio(original_source + "/INPUT")
    #
    #
    #
    secciona_tab_de_equities_de_bolsar(original_source + "\BOLSAR",  date+"_TODO", ".xlsx", 0, original_source + "\INPUT")
    ####  LIMPIAR SUBDIRECTORIO OUTPUT                                         
    borrar_archivos_de_un_subdirectorio(original_source+"/OUTPUT/BONOS")
    borrar_archivos_de_un_subdirectorio(original_source+"/OUTPUT/CEDEARS")
    borrar_archivos_de_un_subdirectorio(original_source+"/OUTPUT/CURRENCIES")
    borrar_archivos_de_un_subdirectorio(original_source+"/OUTPUT/EQUITIES")
    borrar_archivos_de_un_subdirectorio(original_source+"/OUTPUT/INDICES")
    exec(open(original_source+"D0091_z_lista_de_securities.py").read())
    #
    #BACKUP
    #exec(open(original_source+"D0150_backup.py").read())
    backup("BACKUP_SPCH_"+ date)
    #COPIA ARCHIVOS SPCH
    #exec(open(original_source+"D0095_sobrescribe_archivos_de_excel.py").read())
    copia_spch(date)
    return


#actualizacion_modulo_spch("2020-01-23")