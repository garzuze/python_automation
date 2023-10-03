import os
import shutil

path = r'C:\Users\adm\Desktop\Visitante'
files = os.listdir(path)

for file in files:
    # separa o arquivo da sua extensão
    filename,extension = os.path.splitext(file)
    extension = extension[1:] # tira o . da extensão

    # criamos uma pasta com a extensão, caso ela já não exista
    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

    