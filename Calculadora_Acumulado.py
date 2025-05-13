soma = 0
numero = 1
while numero !=0:
    numero = int(input("Digite um número(0 para sair):2"))
    soma = soma + numero
    if numero !=0:
        print (f"A soma até o momento é {soma}")
print (f"A soma dos número digitado é {soma}")