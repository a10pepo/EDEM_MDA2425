import os
import datetime



def check_class(folder_path):
    class_type=folder_path.split("/")[-1][0:3]
    deliverables=os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/"+class_type))
    deliverables=deliverables+os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/COMUN"))
    alumnos={}
    for alumno in os.listdir(folder_path):
        file_path = os.path.join(folder_path, alumno)
        if os.path.isdir(file_path):
            delivs={}
            alumnos[alumno]=delivs
            for element in deliverables:
                #print(file_path+"/"+element)
                if os.path.exists(file_path+"/"+element) & os.path.isdir(file_path+"/"+element):
                    print("Entregable "+element+" Existe para el alumno "+alumno)
                    alumnos[alumno][element]=True    
                else:
                    print("Entregable "+element+" NO Existe para el alumno "+alumno)
                    alumnos[alumno][element]=False
    return alumnos

def check_names(folder_path):
    for alumno in os.listdir(folder_path):
        file_path = os.path.join(folder_path, alumno)
        if os.path.isdir(file_path):
            # list all files in directory
            files = os.listdir(file_path)
            for element in files:
                print(element)


def generate_table(clase,alumnos):
    class_type=clase[0:3]
    deliverables=os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/"+class_type))
    deliverables=deliverables+os.listdir(os.path.join(os.getcwd(), "PROFESORES"+"/COMUN"))    
    print("Generating Table")
    try:
        table="<table>\n<tr><th>Alumno</th>"
        for element in deliverables:
            table+="\n<th>"+element+"</th>"
        table+="\n</tr>\n"
        table+="<tr>\n"  
        for alumno in sorted(alumnos):
            table+="<tr>\n<td><a href='https://github.com/a10pepo/EDEM_MDA2425/tree/main/ALUMNOS/"+clase+"/"+alumno+"'>"+str.upper(alumno)+"</a></td>"
            for element in deliverables:
                if alumnos[alumno][element]:
                    table+="\n<td>✅</td>"
                else:
                    table+="\n<td>❌</td>"
            table+="\n</tr>\n"
        table+="</table>\n"
        table+="\nLast Checked: "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n"
    except:
        print("error")
    return table

def modify_readme():
    print("Modifying README.md")
    with open(os.path.join(os.getcwd(),'README.md'), 'r') as file:
        data = file.read()
        parts = data.split('### Estado de las entregas')

    with open(os.path.join(os.getcwd(),'README.md'), 'w') as file:
        print("Writing README.md")
        try: 
            file.write(parts[0])
            file.write('### Estado de las entregas\n')
            file.write('Entregas Grupo MIA\n')
            file.write(generate_table("MIA",check_class(os.path.join(os.getcwd(), "ALUMNOS/MIA"))))
            file.write('\n')
            file.write('\n')
            file.write('Entregas Grupo MDA A\n')
            file.write(generate_table("MDAA",check_class(os.path.join(os.getcwd(), "ALUMNOS/MDAA"))))
            file.write('\n')
            file.write('Entregas Grupo MDA B\n')
            file.write(generate_table("MDAB",check_class(os.path.join(os.getcwd(), "ALUMNOS/MDAB"))))
            file.write('\n')            
        except Exception as e:
            print("Error writing file")
            print(e)
            file.close()
            with open(os.path.join(os.getcwd(),'README.md'), 'w') as file_recov:
                file_recov.write(data)
        



if __name__ == '__main__':  
    check_names(os.path.join(os.getcwd(), "ALUMNOS/MDAA"))
    check_names(os.path.join(os.getcwd(), "ALUMNOS/MDAB"))
    check_names(os.path.join(os.getcwd(), "ALUMNOS/MIA"))
    modify_readme()    
    print("README.md updated")

