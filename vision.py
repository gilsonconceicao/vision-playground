import numpy as np
import cv2 as cv
import pyinputplus as pyip

status = ""

def open_camera():
    global status
    status = "Carregando..."
    print("Status:", status)

    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Câmera não abriu")
        exit()
    
    status = "Abriu!"

    print("Status:", status)
    
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Houve um erro ao tentar abrir câmera")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow('frame', gray)

        if cv.waitKey(1) == ord('q'):
            status = "Encerrado"
            break

    cap.release()
    cv.destroyAllWindows()

choice: str = pyip.inputChoice(
    ['SIM', 'NAO'], 
    prompt="DESEJA ABRIA A CÂMERA [SIM | NAO]: "
)

choiceFormated = choice.lower()

if( choiceFormated != 'SIM' and choiceFormated != "NAO"): 
    print("Essa opção não existe no sistema")

if (choiceFormated == 'SIM'):
    open_camera()
else:
    print("Você escolheu não, então, sem câmera!")