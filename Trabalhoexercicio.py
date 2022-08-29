from ast import While
from random import randint, random
from random import randrange
import random

tiros = 0
cerebros = 0
passos = 0


dadoverde = "CPCTPC"
dadoamarelo = "TPCTPC"
dadovermelho = "TRTCPT"

copo = []
pontos = []
jogadores = []

for i in range (0,6):
    copo.append(dadoverde)
for i in range (0,4):
    copo.append(dadoamarelo)
for i in range (0,3):
    copo.append(dadovermelho)
    
print ("Mostrar dados")
for elementos in copo:
    print(elementos)
print ("ZOMBIE DICE GAME")
print ("Seja bem-vindo ao jogo")
 
print("\n")
numberPlayers = int(input("Entre com a quantidade de jogadores"))
if numberPlayers:
    print("Iniciar Jogo")
    for ind in range (0, numberPlayers):
        print ("\n")
        nome = input("Entre com o nome do jogador {}:".format(ind+i))
        cerebro = 0
        tiros = 0
        
        player = [ind, nome, cerebro, tiros]
        jogadores.append (player)
        print ("Olá {}".format(jogadores[ind] [1]))
        while (True):

            for i in range (0,3):
                numSorteado = randint (0, 12)
                print ("Dado Sorteado {}: {}".format((i+1), numSorteado))
                dadoSorteado = copo [numSorteado]
                faceDado = randint (0,5)
                if dadoSorteado[faceDado] == "C":
                    print("Cerebro !! ")
                    print("Voce comeu meu Cerebro !!\n ")
                    cerebros = cerebros + 1
                elif dadoSorteado[faceDado] == "I":
                    print ("Tiro !! ")
                    print ("Voce levou um Tiro !!\n ")
                    tiros = tiros + 1
                else:
                    print ("Passos !!")
                    print ("A vitima Escapou !!\n")
                    passos = passos + 1
                    
            print ("\n")
            playerGame = input ("Deseja continuar (s / n")
            if playerGame == "n":
                print ("Continuar no Jogo\n")
            else:
                print ("saindo do jogo")
                
                tiros = 0
                cerebro = 0
                passos = 0
                break
                    