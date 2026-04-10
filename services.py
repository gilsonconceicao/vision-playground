import numpy as np
import cv2 as cv
import pyinputplus as pyip

def open_camera_service():
    global status
    status = "Carregando..."
    print("Status:", status)
    
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Câmera não abriu")
        exit()

    face_cascade = cv.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
    
    status = "Abriu!"

    print("Status:", status)
    try:
        attempt = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                raise RuntimeError("Erro ao capturar frame da câmera")

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
            
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=5
            )

            for (x, y, w, h) in faces:
                cv.rectangle(
                    gray_bgr,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

            cv.imshow("Face Detection", gray_bgr)

            attempt = attempt+1
            if (attempt == 1):
                print("Pressione 'q' para sair")
                
            if cv.waitKey(1) & 0xFF == ord('q'):
                print("Tecla q pressionada. Encerrando câmera...")
                break

    finally:
        cap.release()
        cv.destroyAllWindows()
        print("Recursos liberados com sucesso")