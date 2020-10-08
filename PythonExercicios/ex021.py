''' Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3 '''

#NOT_WORKING ON VSCODE

from pygame import mixer
import os

mixer.init()
path = os.path.join(os.path.dirname(__file__), 'ex021.mp3')
mixer.music.load(path)
mixer.music.play
print(mixer.music.get_busy())
input()
