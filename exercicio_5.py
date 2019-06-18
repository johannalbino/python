num1 = int(input("Digite um numero: "))
sinal = input("Digite o operador: ")
num2 = int(input("Digite um novo numero: "))

if sinal == "+":
	resultado = num1 + num2

elif sinal == "-":
	resultado = num1 - num2

elif sinal == "/":
	resultado = num1 / num2

elif sinal == "*":
	resultado = num1 * num2

elif sinal == "%":
	resultado = num1 % num2

elif sinal == "**":
	resultado = num1 ** num2

print (resultado)