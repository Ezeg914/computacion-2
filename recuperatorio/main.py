import os
from PIL import Image
from utils import extractRGB, rotateAndMergeImage
 
if __name__ == '__main__':
    
    file = input('Nombre de la Imagen (extension incluida): ')
    image = Image.open(file)
    print('''
          1. Extract RGB
          2. Rotate Image
          3. Exit
          ''')
    while True:
        op = input('> ')
        if op == '1':
            extractRGB(image)
        elif op == '2':
            rotateAndMergeImage()
        elif op == '3':
            break
        else:
            print('Opcion Invalida')
    print('Gracias, nos vemos!')