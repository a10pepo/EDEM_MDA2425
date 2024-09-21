import os



deliverables=["DOCKER","PYTHON","LINUX","AHORCADO","SQL","FLASK","KAFKA","SPARK","DATAFLOW","CLOUD"]
allowed=["DOCKER","PYTHON","LINUX","AHORCADO","SQL","README.MD","CHUCK","FLASK", "SPARK", "KAFKA", "VALENBISI","CLOUD"]

alias_dict = {
    "DOCKER":["DOCKER"],
    "PYTHON":["PYTHON"],
    "LINUX":["LINUX"],
    "NOTEBOOKS":["NOTEBOOKS"],
    "AHORCADO":["AHORCADO"],
    "SQL":["SQL"],
    "MACHINELEARNING":["MACHINE_LEARNING"],
    "MACHINE LEARNING":["MACHINE_LEARNING"],
    "MACHINE_LEARNING":["MACHINE_LEARNING"],
    "ML": ["MACHINE_LEARNING"],
    "DEEP LEARNING":["DEEP_LEARNING"],
    "DEEPLEARNING":["DEEP_LEARNING"],
    "DEEPLEARNING_FULLYCONNECTED":["DEEP_LEARNING"],
    "REDES_NEURONALES":["DEEP_LEARNING"],
}



def check_class(folder_path):
    alumnos={}
    for alumno in os.listdir(folder_path):
        file_path = os.path.join(folder_path, alumno)
        if os.path.isdir(file_path):
            delivs={}
            alumnos[alumno]=delivs
            for element in deliverables:
                #print(file_path+"/"+element)
                if (os.path.exists(file_path+"/"+element) & os.path.isdir(file_path+"/"+element)) or (os.path.exists(file_path+"/"+element.capitalize()) & os.path.isdir(file_path+"/"+element.capitalize())):
                    if "Pending" in os.listdir(file_path+"/"+element) or "pending" in os.listdir(file_path+"/"+element):
                        alumnos[alumno][element]=False
                    alumnos[alumno][element]=True    
                else:
                    alumnos[alumno][element]=False
    return alumnos

def check_names(folder_path):
    for alumno in os.listdir(folder_path):
        file_path = os.path.join(folder_path, alumno)
        if os.path.isdir(file_path):
            # list all files in directory
            files = os.listdir(file_path)
            for element in files:
                if element.upper() not in allowed:
                    #print("File not allowed "+file_path+" Elment: "+element)
                    if element.upper() in alias_dict:
                         #print("Alias found: "+element+" -> "+str(alias_dict[element.upper()]))
                         if os.path.exists(file_path+"/"+alias_dict[element.upper()][0]):
                            print("File already exists "+file_path+"/"+alias_dict[element.upper()][0])
                         else:   
                            os.rename(file_path+"/"+element,file_path+"/"+alias_dict[element.upper()][0])
                         

                    # else:
                    #     print("File not allowed "+file_path+" Elment: "+element.upper())             


def getcolor(element):
    if element in ["DOCKER","PYTHON","LINUX","NOTEBOOKS","AHORCADO"]:
        return "#dee2d0"
    
    if element in ["SQL","FLASK" ]:
        return "#a5cbaa"
    if element in [ "SPARK", "KAFKA"]:
        return "#9bc99e"
    if element in ["DATAFLOW","CLOUD","DEVSECOPS"]:
        return "#779777"
    if element in ["ESTADISTICA"]:
        return "#5f7b6e"
    if element in ["DEEP_LEARNING","MACHINE_LEARNING", "DEPLOYMENT"]:
        return "#4d5e5b"
    else:
        return "#ffc1b1"

def generate_table(clase,alumnos):
    
    try:
        table="<table>\n<tr><th>Alumno</th>"
        for element in deliverables:
            table+="\n<th>"+element+"</th>"
        table+="\n</tr>\n"
        table+="<tr>\n"
        table+="<td> Modulos </td>\n"
        table+="<td color='#dee2d0' style='text-align: center;font-weight: bold' colspan='5'> M0 - Fundamentos </td>\n"
        table+="<td color='#a5cbaa' style='text-align: center;font-weight: bold' colspan='2'> M1.1 - Tratamiento Tradicional </td>\n"
        table+="<td color='#9bc99e' style='text-align: center;font-weight: bold' colspan='2'> M1.2 - Streaming On Prem </td>\n"
        table+="<td color='#779777' style='text-align: center;font-weight: bold' colspan='3'> M1.3 - Cloud Approach </td>\n"
        table+="<td color='#5f7b6e' style='text-align: center;font-weight: bold' colspan='1'> M2.1 - Estadística </td>\n"
        table+="<td color='#5f7b6e' style='text-align: center;font-weight: bold' colspan='2'> M2.2 - ML / DL </td>\n"
        table+="</tr>\n"
        table+="<tr>\n"  
        for alumno in sorted(alumnos):
            table+="<tr>\n<td><a href='https://github.com/a10pepo/EDEM_MDA2324/tree/main/Alumnos/"+clase+"/"+alumno+"'>"+str.capitalize(alumno)+"</a></td>"
            for element in deliverables:
                color=getcolor(element)
                if alumnos[alumno][element]:
                    table+="\n<td bgcolor='"+color+"'>✅</td>"
                else:
                    table+="\n<td bgcolor='"+color+"'>❌</td>"
            table+="\n</tr>\n"
        table+="</table>\n"
    except:
        print("error")
    return table

def modify_readme():
    with open('README.md', 'r') as file:
        data = file.read()
        parts = data.split('### Estado de las entregas')

    with open('README.md', 'w') as file:
        try: 
            file.write(parts[0])
            file.write('### Estado de las entregas\n')
            file.write('Entregas Fin de Semana\n')
            file.write(generate_table("FS",check_class('Alumnos/FS')))
            file.write('\n')
            file.write('\n')
            file.write('Entregas Entre Semana\n')
            file.write(generate_table("ES",check_class('Alumnos/ES')))
            file.write('\n')
        except:
            file.close()
            with open('README.md', 'w') as file_recov:
                file_recov.write(data)
        



if __name__ == '__main__':  
    check_names('ALUMNOS/ES')
    check_names('ALUMNOS/FS')
    modify_readme()    
    print("README.md updated")

