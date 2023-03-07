from random import random

print("*********************************")
print("Bem-vindo ao jogo de adivinhação!")
print("*********************************")

#Variável de parametro
numero_secreto = round(random.randrange(1,51))
total_de_tentativas = 0
chute = 0

print("Qual nivel de dificuldade você quer?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if( nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    #Valor de entrada do usuário
    chute = input("Digite um número entre 1 e 50: ")
    print("Você digitou", chute)
    #Conversor do valor de entrada para inteiro
    chute = int(chute)

    if(chute < 1 or chute > 50):
        print("Você digitou um número incompatível, digia um número entre 1 e 50!!")
        continue

    #Variáveis para facilitar a leitura do código
    acertou = chute == numero_secreto
    maior_chute = chute > numero_secreto
    menor_chute = chute < numero_secreto

    #Condição para o jogo
    if (acertou):
        print("você acertou!!")
        break
    else:
        if(maior_chute):
            print("Você errou!! o seu chute foi maior que o número secreto")
        elif(menor_chute):
            print("Você errou!! o seu chute foi menor que o número secreto")


print(chute)
print("\n*********************************")
print("Fim  de jogo!!!")
