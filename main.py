import pyinputplus as pyip
import resolvers;

choice: str = pyip.inputChoice(
    ['SIM', 'NAO'], 
    prompt="DESEJA ABRIA A CÂMERA [SIM | NAO]: "
)

choiceFormated = choice.upper()

if (choiceFormated == 'SIM'):
    resolvers.OpenCameraResolve()
else:
    print("Você escolheu não, então, sem câmera!")