from pytube import *
import moviepy.editor as mp
import re
import os
from time import sleep

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite uma opçao valida. \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[Usuario preferiu não digitar.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('\033[31m Instalador Youtube \033[m')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


while True:
    resposta = menu(['Instalar Video(MP4)', 'Instalar Música(MP3)', 'Sair'])
    if resposta == 1:
        try:

           link = input('Digite O Link do Video Que Deseja Instalar: ')
           path = input('Digite o Diretorio que deseja salvar o video: ')
           yt = YouTube(link)
           print()
           print('Titulo:', yt.title)
           print("Numero de Viewrs: ", yt.views)
           print('Tamanho do video: ', yt.length, "Segundos")
           sleep(1)
           ys = yt.streams.get_highest_resolution()
           print("Instalando...")
           sleep(1)
           ys.download(path)
           sleep(1)
           print("\033[32mDownload Completo \033[m")

        except Exception as e:
             print('\033[31mOps! Algo deu Errado Tente Novamente\033[m')
             sleep(2)




    elif resposta == 2:

        link = input('Digite o link da Música que deseja Instalar:  ')
        path = input('Digite o Diretorio que deseja salvar a Música:  ')
        yt = YouTube(link)
        sleep(1)


        print('Baixando ... ')
        ys = yt.streams.filter(only_audio=True).first().download(path)
        print("\033[32mDowloand Completo\033[m")

        print('Convertendo Arquivo')
        for file in os.listdir(path):

            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
                sleep(1)
                print('\033[32mArquivo Convertido com Sucesso\033[m')


    elif resposta == 3:
        print('Saindo...')
        break
    else:
        print('\033[31mERROR Digite Uma Opção Valida!\033[m')
        sleep(2)


