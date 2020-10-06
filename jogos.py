import game_adivinhacao
import game_forca

def escolha():
    print("***********************************************************************************")
    print("                                 CHOSE THE GAME:                                   ")
    print("***********************************************************************************")

    print("1)Advinhação \n2)Forca")
    escolha = int(input("What game? "))
    if (escolha == 1):
        print("Adivinhação? I LOVE IT! LET'S GO!!")
        game_adivinhacao.jogar()
    elif(escolha == 2):
        print("Forca? I LOVE IT! LET'S DO IT!!")
        game_forca.jogar()

#CHAMA O PROGRAMA PRINCIPAL:
if(__name__=="__main__"):
    escolha()