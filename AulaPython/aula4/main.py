import os
import shutil

def organizar_pastas(diretorio):
    for filename in os.listdir(diretorio):
        if not os.path.isdir(os.path.join(diretorio, filename)):
            ext = filename.split('.')[-1]
            pasta = os.path.join(diretorio, exit)
            
            if not os.path.exists(pasta):
                os.makedirs(pasta)

            shutil.move(os.path.join(diretorio, filename), os.path.join(pasta, filename))

if __name__ == "__main__":
    diretorio = "c:\\Users/Usuario\Desktop\AulaPython"
    organizar_pastas(diretorio)
    print("Organização concluida")
    