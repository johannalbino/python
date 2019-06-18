#exercicio 3
#Faça um programa que resolva uma equação de segundo grau
# a2 + bx + c
#(-b +- sqtr(b2-4ac))/2

from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/(2*a)
x2 = (-b - raiz_delta)/(2*a)

print("x1 = %f" %x1)
print("x1 = %f" %x2)