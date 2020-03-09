
def borrar_archivos_de_un_subdirectorio(path):
    # Elimina todos los archivos contenidos en un subdirectorio
    import os
    import glob
    complete_path = path + '/*' 
    files = glob.glob(complete_path)
    for f in files:
        os.remove(f)


#borrar_archivos_de_un_subdirectorio("C:/GCB_CAPITAL/INPUT")

