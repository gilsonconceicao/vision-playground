import pyinputplus as pyip
from services import open_camera_service

def main():
    choice: str = pyip.inputChoice(
        ['SIM', 'NAO'],
        prompt="DESEJA ABRIR A CÂMERA [SIM | NAO]: "
    ).upper()

    if choice == 'NAO':
        print("Você escolheu não, então, sem câmera!")
        return

    try:
        open_camera_service()
    except Exception as error:
        print(f"Erro ao abrir a câmera: {error}")


if __name__ == "__main__":
    main()