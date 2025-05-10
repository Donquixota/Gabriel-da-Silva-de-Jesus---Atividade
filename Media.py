nota1 = float (input("Digite a primeira nota: "))
print(f"O resultado é: {nota1}")
nota2 = float (input("Digite a segunda nota:"))
print(f"O resultado é: {nota2}")

media = (nota1 + nota2) / 2
print (f"A média é: {media}")

if media >=7:
    print("Aprovado. ")
else:
    print ("Reprovado. ")