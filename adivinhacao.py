from random import randrange

def play_adivinhacao():
    print("""\n
********************************
Bem vindo ao Jogo da Adivinhação
********************************""")

    secret_num = randrange(1,101)
    # print(f"\nNúmero secreto: {secret_num}\n")
    attemps = 0
    points = 100
    lost_points = 0

    print(f"""
Qual nível de dificuldade?
    (1) Fácil - 8 tentativas 
    (2) Médio - 6 tentativas
    (3) Difícil - 4 tentativas
    """)

    level = int(input("Digite 1, 2 ou 3 para escolher: "))

    if level == 1:
        attemps = 8
    elif level == 2:
        attemps = 6
    else:
        attemps = 4

    for round in range (1, attemps +1):
        print(f"\nTentativa {round} de {attemps}.")
        kick_int = int(input("Escolha um número de 1 a 100: "))
        # print(f"Você digitou {kick_int}, vamos ver se está certo?!\n")
        kick = kick_int

        if kick < 1 or kick > 101:
            print("\n\033[31mVocê deve digitar um número entre 1 e 100\033[m")
            continue

        right = kick == secret_num
        larger = kick > secret_num
        smaller = kick < secret_num

        if(right):
            print(f"\n\033[34mParabéns! Você acertou e fez {points:.0f} pontos!\033[m")
            break
        else:
            if(larger):
                print(f"\033[31mVocê errou! Seu chute({kick_int}) foi maior que o número secreto. :(\033[m")
            elif(smaller):
                print(f"\033[31mVocê errou! Seu chute({kick_int}) foi menor que o número secreto. :(\033[m")
            lost_points = abs(secret_num - kick) / 3 # abs(valor absoluto) - mantém o número positivo # pontos perdidos da rodada
            points = points - lost_points            # subtraindo os pontos perdidos da pontuação total 

    print(f"\nFim de jogo.\nNúmero secreto foi: {secret_num}\n")


if (__name__ == "__main__"):
    play_adivinhacao ()
