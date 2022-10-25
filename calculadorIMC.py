nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

print("-" * 30)
print("Os dados coletados foram: ")
print("Seu nome: " , nome)
print("Sua idade: " , idade, "anos")
print("Sua altura: " , altura, "mts")
print("Seu peso: " , peso, "kgs") 

imc = peso / altura**2 

print("Seu IMC é:  %.4f" % imc)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 18.5:
    print("Magreza leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")

os.system("pause")
 