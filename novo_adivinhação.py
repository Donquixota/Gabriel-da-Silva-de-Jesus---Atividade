import random
numero_secreto = random.randint(1,10)
tentativas = 0
contagem_tentativas = 0
print ("==Bem-vindo ao jogo de Número Segreto==")
print ("Tente adivinhar o número secreto entre 1 e 10.")
while tentativas !=numero_secreto:
    numero = int (input("Digite o número: "))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print ("Parabéns, você acertou o numero secreto")
        print (f"Você precisou de {contagem_tentativas}")
        break
    elif numero < numero_secreto:
        print ("O número secreto é maior. ")
    else:
        print("O número secreto é menor. ")