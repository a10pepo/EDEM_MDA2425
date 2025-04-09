## 🏀 Detección de Canastas en Video con YOLOv8

Este proyecto procesa un video de baloncesto y detecta automáticamente cuando se realiza una canasta. Utiliza un modelo personalizado de YOLOv8 entrenado para reconocer el balón y el aro.

### ¿Cómo funciona?

1. Se carga un video de entrada (`baloncesto.mp4`).
2. El modelo detecta el balón y el aro en cada frame.
3. Si el balón pasa por el aro (según la lógica implementada), se cuenta como una canasta.
4. El resultado se guarda como un nuevo video con anotaciones visuales y el contador de canastas.

### 📦 Resultado

El archivo `output.mp4` es generado al finalizar el análisis. Este archivo muestra el video original con cuadros alrededor del balón y el aro, junto con un contador en pantalla indicando la cantidad de canastas detectadas.

📹 [Descargar ejemplo](./output.mp4)

---

> Modelo usado: `yolov8_custom.pt`  
> Script principal: [`detect_shots.py`](./detect_shots.py)
