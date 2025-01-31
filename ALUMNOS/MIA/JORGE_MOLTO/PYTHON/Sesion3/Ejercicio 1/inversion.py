
import funciones_inversion 

'''
Opciones en la aplicación: 
[1]. Calcular inversión
[X]. Cerrar el programa

'''

def main(): 
    usuario_control = ''
    while(usuario_control != 'X'):
        while(True):
            funciones_inversion.dialogo_usuario()
            usuario_control = str(input('Inserte elección: ').upper())
            if usuario_control in ('1'): 
                llamar_funcionalidad(usuario_control)
            if usuario_control in ('X'):
                break
            else:
                print('Introduce un valor aceptado por el asistente del chat')
    funciones_inversion.cerrar_programa()

def llamar_funcionalidad(funcinalidad: str):
    if (funcinalidad == '1'): 
        funciones_inversion.calcular_inversion()    

main()

