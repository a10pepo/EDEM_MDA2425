import subprocess
import pywhatkit as kit

wifiobjetivo = 'Marina_de_Empresas'
mensaje = 'Hola, llegué a Edem'
contacto_1 = '+593998206519'
contacto_2 = '+593986037613'

#Ojo! debes tener whatsapp web abierto

def obtener_wifi_actual():
    try:
        # Ejecuta el comando para obtener detalles de la red Wi-Fi
        result = subprocess.check_output("netsh wlan show interfaces", shell=True).decode("utf-8", errors="ignore")
        for line in result.splitlines():
            if "SSID" in line:
                ssid = line.split(":")[1].strip()
                return ssid
    except Exception as e:
        print("Error al obtener el nombre de la red Wi-Fi:", e)
    return None

def verificar_conexion_wifi(wifi_name):
    # Verifica si el SSID actual coincide con la red objetivo
    ssid = obtener_wifi_actual()
    return ssid == wifi_name if ssid else False

# Ejemplo de uso
if verificar_conexion_wifi(wifiobjetivo):
    print("Conectado a la red Wi-Fi objetivo:", wifiobjetivo)
    kit.sendwhatmsg_instantly(contacto_1, mensaje)
    kit.sendwhatmsg_instantly(contacto_2, mensaje)
else:
    print("No estás conectado a la red Wi-Fi objetivo.")