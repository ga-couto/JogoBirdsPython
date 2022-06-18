from os import path
import sys
project_dir = path.dirname(__file__)
project_dir = path.join('..')
sys.path.append(project_dir)
from atores import PassaroAmarelo, PassaroVermelho, Obstaculo, Porco
from fase import Fase
from placa_grafica_tkinter import rodar_fase
if __name__ == '__main__':
    fase= Fase(intervalo_de_colisao=30)


    #Adicionar alguns pássaros
    for i in range(10):
        fase.adicionar_passaro(PassaroVermelho(30,30))
    for i in range(300):
        fase.adicionar_passaro(PassaroAmarelo(25,25))

    #Adicionar Porcos VERTICAL
    for i in range(40, 401,40):
        fase.adicionar_porco(Porco(80,i))
        fase.adicionar_obstaculo(Obstaculo(215,i))
        fase.adicionar_obstaculo(Obstaculo(295,i))
        fase.adicionar_porco(Porco(350,i))
        fase.adicionar_porco(Porco(450,i))
        fase.adicionar_obstaculo(Obstaculo(535,i))
        fase.adicionar_porco(Porco(620,i))
        fase.adicionar_porco(Porco(700,i))
    for i in range(115,151,35):
        fase.adicionar_porco(Porco(i,40))
        fase.adicionar_porco(Porco(i, 401))
    for i in range(255,300,50):
        fase.adicionar_obstaculo(Obstaculo(i,40))
        fase.adicionar_obstaculo(Obstaculo(i, 401))
    for i in range(400,420,50):
        fase.adicionar_porco(Porco(i,40))
    for i in range(498,600,74):
        fase.adicionar_obstaculo(Obstaculo(i, 401))
    for i in range(660,700,50):
        fase.adicionar_porco(Porco(i,40))
        fase.adicionar_porco(Porco(i, 401))

    rodar_fase(fase)