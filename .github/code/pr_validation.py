import os

def validate_folder_structure(path):
    print("Current directory: ", os.getcwd())
    deliverable_names=os.listdir("PROFESORES")
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            for user_file in os.listdir(full_path):
                user_path = os.path.join(full_path, user_file)
                if os.path.isdir(user_path):
                    if user_file not in deliverable_names:
                        print("Esta Carpeta no es correcta, comprueba el nombre exacto de la carpeta: ", user_file)
                        exit(1)
                else:
                    print("Elimina el fichero fuera de la carpeta del usuario: ", user_path)
     

if __name__ == "__main__":
    # iterate over all the files in the folder
    # check if the file is a directory
    validate_folder_structure("ALUMNOS/ES")
    validate_folder_structure("ALUMNOS/FS")