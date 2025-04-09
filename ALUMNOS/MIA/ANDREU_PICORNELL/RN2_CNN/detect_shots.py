import cv2
from ultralytics import YOLO


def load_model(model_path="yolov8_custom.pt"):
    return YOLO(model_path)

def setup_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    return cap, out

def detect_objects(frame, model):
    results = model(frame)
    detections = {"Ball": None, "Hoop": None}  # Diccionario para guardar las mejores detecciones

    for result in results:
        for box in result.boxes.data:
            x1, y1, x2, y2, confidence, cls = map(float, box[:6])
            cls = int(cls)

            if cls == 0 and confidence > 0.2:  # Balón (Ball)
                if detections["Ball"] is None or confidence > detections["Ball"][4]:
                    detections["Ball"] = [x1, y1, x2, y2, confidence, "Ball"]
            
            elif cls in [1, 3] and confidence > 0.2:  # Aro (Hoop)
                if detections["Hoop"] is None or confidence > detections["Hoop"][4]:
                    detections["Hoop"] = [x1, y1, x2, y2, confidence, "Hoop"]

    # Filtramos las detecciones válidas (None si no se detectó)
    valid_detections = [det for det in detections.values() if det is not None]
    return valid_detections

def draw_annotations(frame, detections, basket_count):
    for obj in detections:
        x1, y1, x2, y2, confidence, label = obj

        if label == "Ball":
            color = (0, 255, 0)  # Verde para balón
        elif label == "Hoop":
            color = (0, 0, 255)  # Rojo para aro
        else:
            continue

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (int(x1), int(y1) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.putText(frame, f"Count: {basket_count}", (frame.shape[1] - 400, 80), 
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    return frame

def basket_counter(detections, counter, state):
    # Primero verificar si están ambos elementos
    hoop = next((obj for obj in detections if obj[5] == "Hoop"), None)
    ball = next((obj for obj in detections if obj[5] == "Ball"), None)
    
    if hoop and ball:
        hoop_x1, hoop_y1, hoop_x2, hoop_y2 = hoop[:4]
        ball_x1, ball_y1, ball_x2, ball_y2 = ball[:4]

        ball_top = ball_y1
        ball_center_x = (ball_x1 + ball_x2) / 2

        if (hoop_y1 <= ball_top <= hoop_y2) and (hoop_x1 <= ball_center_x <= hoop_x2):
            if state:
                counter = counter + 1
            state = False
        else:
            state = True

    return counter, state

def process_video(input_path, output_path, model):
    basket_count = 0
    new_count = True
    cap, out = setup_video(input_path, output_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        detections = detect_objects(frame, model)
        basket_count, new_count = basket_counter(detections, basket_count, new_count)
        frame = draw_annotations(frame, detections, basket_count)
        out.write(frame)

    cap.release()
    out.release()

def main():
    input_video = "baloncesto.mp4"
    output_video = "output.mp4"
    model = load_model("yolov8_custom.pt")  # Asegúrate de que tu modelo está entrenado para Ball (0) y Hoop (1 o 3)
    process_video(input_video, output_video, model)

if __name__ == "__main__":
    main()