from confluent_kafka import Producer
import time

def cargar_futbolistas(ruta_archivo):
    with open(ruta_archivo, encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo if linea.strip()]

def enviar_a_kafka(lista_nombres, productor, topico):
    for idx, nombre in enumerate(lista_nombres):
        productor.produce(topico, value=nombre.encode('utf-8'), key=str(idx))
        print(f"Enviado: {nombre}")
        productor.flush()
        time.sleep(1)

def main():
    config = {
        'bootstrap.servers': 'localhost:9092',
        'client.id': 'futbolistas-producer'
    }
    productor = Producer(config)
    topico = 'futbolistas'
    nombres = cargar_futbolistas('futbolistas.txt')
    enviar_a_kafka(nombres, productor, topico)
    print(f"Total enviados: {len(nombres)}")

if __name__ == "__main__":
    main() 