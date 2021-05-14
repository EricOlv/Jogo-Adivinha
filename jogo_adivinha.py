import random

print('Adivinhe o número da sorte!')

numero_aleatorio = random.randrange(1, 11)

chute = 0
while chute < 5:
    numero = int(input('Digite seu chute da sorte: '))
    if chute >= 4 and numero != numero_aleatorio:
        print('Suas tentativas acabaram. Tente novamente.')
        break
    elif numero == numero_aleatorio:
        print(f'Parabéns você acertou! O número da sorte era o nº {numero_aleatorio}!')
        break
    elif numero < numero_aleatorio:
        print('Seu chute foi menor que o número da sorte.')
    elif numero > numero_aleatorio:
        print('Seu chute foi maior que o número da sorte.')

    chute += 1
    
    