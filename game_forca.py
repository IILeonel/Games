def jogar():
    print("***********************************************************************************")
    print("                            WELCOME TO THE FORCA !!                                ")
    print("***********************************************************************************")

    palavra_secreta = "bolo".upper()
    letras_certas = ["_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0
    print(letras_certas)

    while(not enforcou and not acertou):

        chute = input("Try a letter: ")
        chute = chute.strip().upper() #STRIP SERVE PARA ELIMINA OS ESPAÇOS CASO O USUARIO COLOQUE

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra): #UPPER SERVER PARA CONSIDERAR TODAS AS LETRAS EM MINUSCULOS 
                    letras_certas[posicao] = letra
                posicao += 1 # +=1 É A MESMA COISA QUE POSICAO = POSICAO +1
        else:
            erros += 1  # +=1 É A MESMA COISA QUE ERROS = ERROS +1

            enforcou = erros == 4
            print(letras_certas)




    print("THE END!!")










#CHAMA O PROGRAMA PRINCIPAL:
if(__name__=="__main__"):
    jogar()