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
    
    status = "Abriu!"

    print("Status:", status)
    try:
        attempt = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                raise RuntimeError("Erro ao capturar frame da câmera")

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('frame', gray)

            attempt = attempt+1
            if (attempt is 1):
                print("# Pressione 'q' para sair")
                
            if cv.waitKey(1) & 0xFF == ord('q'):
                print("Encerrando câmera...")
                break

    finally:
        cap.release()
        cv.destroyAllWindows()
        print("Recursos liberados com sucesso")

    cap.release()
    cv.destroyAllWindows()