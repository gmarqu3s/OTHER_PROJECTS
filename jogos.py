# import forca
from forca import play_forca
import adivinhacao

def select_games():
    print("""\n
    -==-==--==-==--==-==--==-==--==-
    -==-==- Escolha seu jogo -==-==-
    -==-==--==-==--==-==--==-==--==-
        |   (1) Forca       |
        |   (2) Adivinhação |   
    """)

    jogo = 0 # Inicializa com um valor inválido

    while jogo != 1 and jogo != 2:
        jogo = int(input("Qual jogo? "))
        if (jogo == 1):
            print("Jogando forca")
            play_forca()
        elif (jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.play_adivinhacao()
        else:
            print("\033[31mOpção inválida. Digite 1 para Forca ou 2 para Adivinhação.\033[m")

if (__name__ == "__main__"):
    select_games()
