import pyinputplus as pyip
import resolvers;

choice: str = pyip.inputChoice(
    ['SIM', 'NAO'], 
    prompt="DESEJA ABRIA A CÂMERA [SIM | NAO]: "
)

choiceFormated = choice.upper()

if choiceFormated == 'NAO':
    print("Você escolheu não, então, sem câmera!")

try:
    resolvers.OpenCameraResolve()
except Exception as error:
    print(f"Erro ao abrir a câmera: {error}")
    