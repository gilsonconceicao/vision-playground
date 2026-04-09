import pyinputplus as pyip
import vision_playground.resolvers as OpenCameraResolve;


def main():
    choice: str = pyip.inputChoice(
        ['SIM', 'NAO'],
        prompt="DESEJA ABRIR A CÂMERA [SIM | NAO]: "
    ).upper()

    if choice == 'NAO':
        print("Você escolheu não, então, sem câmera!")
        return  # 🔥 importante: para aqui

    try:
        OpenCameraResolve()
    except Exception as error:
        print(f"Erro ao abrir a câmera: {error}")


if __name__ == "__main__":
    main()