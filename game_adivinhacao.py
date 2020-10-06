import random
def jogar():

    print("***********************************************************************************")
    print("                            WELCOME TO THE ADIVINHAÇÃO !!!                                 ")
    print("***********************************************************************************")

    #NUMERO SECRETO DO GAME 
    numero_secreto = round(random.randrange(101)) #GERANDO NUMERO PSEUDO ALEATORIO COM A BIBLIOTECA DO TOPO
    tentativas = 0
    pontos = 1000

    #INTRO PARA PERGUNTAR QUAL O NIVEIS O USUARIO DESEJA
    print("First thing... Chose your level: ")
    print("1)Easy \n2)Medium \n3)Hard")

    #PEDINDO O NIVEIS
    nivel = int(input("Say me a number for your level: "))

    #CONDIÇÕES DOS NIVEIS 
    if(nivel == 1):
        tentativas = 10
        print("Ok! Easy level, LET'S GO!!")
    elif(nivel == 2):
        tentativas = 5
        print("Hummm... Medium level, LET'S GO!!")
    elif(nivel == 3):
        tentativas = 3
        print("WooW!! Hard level? You're a monster. LET'S DO IT!!")

    #O LOOPING PARA QUE O JOGO NAO PARE
    for rodadas in range (1, tentativas +1):
        print("attemps {} of {}".format(rodadas, tentativas))
        chute_st= input("Say me a number betweem 1 and 100:  ")
        print("You said it: {} ".format(chute_st))
        chute = int(chute_st)

    #INSTRUÇÕES CASO O USUARIO ACERTE OU ERRE 
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

    #CONDIÇOES E OS PRINTS INFORMANDO COMO O USUARIO ESTA INDO NO GAME
        if(acertou):
            print("You're right and you got it {} points !!".format(pontos))
            break
        elif(maior):
            print("You're wrong!!! The kick was bigger then secret number")
        elif(menor):
            print("You're wrong!! The kick was low then secret number")
            pontos_perdidos = abs(numero_secreto - chute) #ABS = NUMERO ABSOLUTO 
            pontos = pontos - pontos_perdidos
    print("THE END!! \nThe secret numer is {}".format(numero_secreto))

    #CHAMA O PROGRAMA PRINCIPAL:
if(__name__=="__main__"):
     jogar()