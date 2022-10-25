#Declarando variáveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/altura**2 #fórmula para calcular IMC

#Saída de dados
print("-" * 30)
print("Os dados coletados foram: ")
print("Seu nome: " ,nome)
print("Sua idade: " ,idade, "anos")
print("Sua altura: ", altura, "mts")
print("Seu peso: ", peso, "kgs")
print("Seu IMC: ", imc)
print("oi")

