



def make_a_directory(subdirectory_name):
    import os
    global original_source
    new_path = original_source + subdirectory_name
    #os.mkdir("C:\GCB_CAPITAL2\A")
    try:
        os.mkdir(new_path)
        return True
    except FileExistsError:
        # directory already exists
        print("directory already exists") 
        return False  


#make_a_directory("BACKUP_SPCH_2020_01_20")


def backup(subdirectory_name):
    global original_source
    import os
    directory_source = (original_source+"\SPCH")
    directory_destiny = (original_source + subdirectory_name)
    if make_a_directory(subdirectory_name):
       # COPIA LOS ARCHIVOS
       import shutil
       for filename in os.listdir(directory_source):
           if filename.endswith(".xlsx"):
              shutil.copy( directory_source + "\\" + filename, directory_destiny)
           print(filename)
    else:
       return ("Problema")


#backup("BACKUP_SPCH_2020_01_20")



