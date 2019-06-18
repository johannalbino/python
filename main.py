#arquivo responsavel por chamar os demais arquivos
# -*- coding: utf-8 -*-
#autor : Johann Herbert
#curso de Python - Udemy

import aleatorio as a
import media as m


lista = a.geralistaInteiro(4)
lista.sort()

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print ("Minha Lista")
print (lista)
print ("A média da minha lista é "+ str(media))
print ("A mediana da minha lista é " + str (mediana))
print ("A mediana da minha lista é " + str (moda))