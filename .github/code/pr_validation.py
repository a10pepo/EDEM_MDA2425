import os

def validate_folder_structure(path):
    
    deliverables=os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/COMUN"))
    deliverables=deliverables+os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/MIA"))
    deliverables=deliverables+os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/MDA"))
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            for user_file in os.listdir(full_path):
                user_path = os.path.join(full_path, user_file)
                if os.path.isdir(user_path):
                    if user_file not in deliverables:
                        print("Esta Carpeta no es correcta, comprueba el nombre exacto de la carpeta: ", user_file)
                        exit(1)
                    else:
                        print("Carpeta correcta: ", user_file, " para el usuario ", file)
                else:
                    if "README.md" not in user_file:
                        print("Elimina el fichero fuera de la carpeta del usuario (solo README.md esta permitido): ", user_path)
     

if __name__ == "__main__":
    # iterate over all the files in the folder
    # check if the file is a directory
    validate_folder_structure(os.path.join(os.getcwd(), "ALUMNOS/MDAA"))
    validate_folder_structure(os.path.join(os.getcwd(), "ALUMNOS/MDAB"))
    validate_folder_structure(os.path.join(os.getcwd(), "ALUMNOS/MIA"))