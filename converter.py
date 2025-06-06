import pillow_avif
from PIL import Image
import os

lista_arquivos = os.listdir("imagens")
print(lista_arquivos)

for arquivo in lista_arquivos:
    imagem = Image.open(f"imagens/{arquivo}")

    imagem.save(f'convertidos/{arquivo.replace("avif", "jpg")}')