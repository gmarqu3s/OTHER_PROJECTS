import random

def play_forca():
    print_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    letras_chutadas_lista = []

    while (not enforcou and not acertou):

        chute = pede_chute()
        letras_chutadas_lista.append(chute)

        if(chute in palavra_secreta):
            marca_chuta_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            letras_chutadas(letras_chutadas_lista)
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        print_msg_vencedor()
    else:
        print_msg_perdedor(palavra_secreta)

def print_msg_abertura():
        print("""\n
********************************
Bem vindo ao Jogo da Forca
********************************
""")
        
def carrega_palavra_secreta():
    arquivo = open(r"C:\Users\gabriel.santos\Desktop\Estudo\PYTHON_ALURA\game_python\palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute

def letras_chutadas(letras_chutadas):
    print(f"Letras chutadas:")
    for i in letras_chutadas:
        print(f"{i}, ", end='')

def marca_chuta_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def print_msg_vencedor():
    print(f"""
      Parabéns você ganhou!
          ___________  
         '._==_==_=_.' 
         .-\\:      /-.
        | (|:.     |) |
         '-|:.     |-' 
           \\::.    /  
            '::. .'    
              ) (      
            _.' '._    
           '-------'    
          """)

def print_msg_perdedor(palavra_secreta):
    print(f"""
    Puxa, você foi enforcado!
    A palavra secreta era {palavra_secreta}
          
        ███████████████████████████
        ███████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
        ███████▄░░░░░░░░░░░▄███████
        ██████████▄▄▄▄▄▄▄██████████
          """)

def desenha_forca(erros):
    print("\n  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")

if (__name__ == "__main__"):
    play_forca()
