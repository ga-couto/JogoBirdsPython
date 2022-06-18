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
    for i in range(2):
        fase.adicionar_passaro(PassaroVermelho(30,30))
    for i in range(400):
        fase.adicionar_passaro(PassaroAmarelo(25,25))

    #Adicionar Porcos VERTICAL
    for i in range(70, 430,40):
        fase.adicionar_obstaculo(Obstaculo(80,i))
        fase.adicionar_obstaculo(Obstaculo(220,i))
        fase.adicionar_obstaculo(Obstaculo(290,i))
        fase.adicionar_obstaculo(Obstaculo(363,i))
        fase.adicionar_obstaculo(Obstaculo(437,i))
        fase.adicionar_porco(Porco(535,i))
        fase.adicionar_obstaculo(Obstaculo(623,i))
        fase.adicionar_obstaculo(Obstaculo(697,i))
    # Adicionar Porcos HORIZONTAL
    for i in range(115,151,35):
        fase.adicionar_obstaculo(Obstaculo(i,57))
        fase.adicionar_obstaculo(Obstaculo(i, 399))
    for i in range(255,300,50):
        fase.adicionar_obstaculo(Obstaculo(i,55))
        fase.adicionar_obstaculo(Obstaculo(i, 399))
    for i in range(400,420,50):
        fase.adicionar_obstaculo(Obstaculo(i,55))
    for i in range(498,600,74):
        fase.adicionar_obstaculo(Obstaculo(i, 390))
    for i in range(660,700,50):
        fase.adicionar_obstaculo(Obstaculo(i,55))
        fase.adicionar_obstaculo(Obstaculo(i, 399))

    rodar_fase(fase)