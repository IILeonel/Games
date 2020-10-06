import random

def abertura():
    print("***********************************************************************************")
    print("                            WELCOME TO THE FORCA !!                                ")
    print("***********************************************************************************")

def p_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_certas(palavra):
    lista = ["_" for letra in palavra]
    return lista

def pedindo_chute():

    chute = str(input("Try a letter: "))
    chute = chute.strip().upper() #STRIP SERVE PARA ELIMINA OS ESPAÇOS CASO O USUARIO COLOQUE
    return chute

def chute_correto(chute, letras_certas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra): #UPPER SERVER PARA CONSIDERAR TODAS AS LETRAS EM MINUSCULOS 
            letras_certas[posicao] = letra
        posicao += 1 # +=1 É A MESMA COISA QUE POSICAO = POSICAO +1
                
def mensagem_vencedor():
    print("YEAHHH!! YOU´RE THE CHAMPION!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("OH MY SORRY, BUT YOU DIE")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print(("THE WORD IS: {}".format(palavra_secreta)))

def desenha_forca(tentativas):

    if(tentativas == 1):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print("OK! I LIKED YOU, SO YOU HAVE 3 MORE CHANCE")
def jogar():

    abertura() #FUNÇÃO

    palavra_secreta = p_secreta() #FUNÇÃO
    
    letras_certas = inicializa_letras_certas(palavra_secreta)
    print(letras_certas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute = pedindo_chute() #FUNÇÃO

        if (chute in palavra_secreta):
           chute_correto(chute, letras_certas, palavra_secreta)
        else:
            tentativas += 1  # +=1 É A MESMA COISA QUE ERROS = ERROS +1
            desenha_forca(tentativas)

        enforcou = tentativas == 10
        acertou ="_" not in letras_certas

        print(letras_certas)
    
    if(acertou):
        mensagem_vencedor() #FUNÇÃO
    else:
        mensagem_perdedor(palavra_secreta) #FUNÇÃO

    


#CHAMA O PROGRAMA PRINCIPAL:
if(__name__=="__main__"):
    jogar()