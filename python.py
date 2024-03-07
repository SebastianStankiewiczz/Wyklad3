import math
import random

#try:
#    a = int(input())
#    b = int(input())
#
#    result = a/b
#except Exception:
#    print("Error!")
#except ValueError:
#    print("Brak liczby")
#else:
#    print(result)
#
#l1 = [0,1,2,3,4,5,6,7,8,9]
#l2 = []
#
#for i in l1:
#    l2.append(i**2)
#print(l2)
#b = [3**y for y in range(6)]
#print(b)
##c = [x for x in a if x % 2 == 1]
##print(c)
#d = [(i, j) for i in l1 for j in l2]
#print(d)
#
#l3 = []
#for i in l1:
#    for j in l2:
#        l3.append((i, j))
#print(l3)
#
#s1 = {1:2, 2:3, 3:4}
#s2 = {v: k for k, v in s1.items()}
#print(s2)
#

#def rownania_kwadratowe(a, b, c):
#    delta = b**2 - 4*a*c
#    if delta < 0:
#        print("Brak rozwiazania")
#        return 0
#    elif delta == 0:
#        x = -b/(2*a)
#        print("Jeden pierwiastek")
#        return x
#    elif delta > 0:
#        x1 = (-b + math.sqrt(delta)) / (2*a)
#        x2 = (-b - math.sqrt(delta)) / (2*a)
#        print("Dwa pierwiastki")
#        return x1, x2
#
#print(rownania_kwadratowe(6, 1, 3))
#print(rownania_kwadratowe(1, 2, 1))
#print(rownania_kwadratowe(1, 4, 1))
#
#def dlugosc_odcinka(x1 = 1, x2 = 2, y1 = 3, y2 = 4):
#    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
#print(dlugosc_odcinka())
#print(dlugosc_odcinka(2, 4, 5, 7))
#print(dlugosc_odcinka(x2=1, y2=5, x1=6, y1=7))
#

#plik = open("tekst.txt", 'r', encoding="utf-8")
#znaki = plik.read(10)
#linia = plik.readline()
#linie = plik.readlines()
#plik.close()
#
#print(znaki)
#print(linia)
#print(linia)
#print(linie)

#plik = open("tekst.txt", 'a+', encoding="utf-8")
#plik.seek(0)
#znaki = plik.read(10)
#plik.write('aaaaaasdfasdf')
#plik.close()
#print(znaki)

#with open("tekst.txt", 'r') as plik:
#    znaki = plik.readlines()
#
#print(znaki)

#################
from random import *

#A = []
#for x in range(10):
#    A.append(1-x)
#print(A)

#B = []
#for x in range(8):
#    B.append(4**x)
#print(B)
#
#C = [x for x in B if x % 2 == 0]
#print(C)

#slownik = {"jajka":"szt", "mleko":"szt", "ziemniaki":"kg", "mieso":"kg", "woda":"szt"}
#szt = {slownik.values()}

#print(szt)

#def trojkat_prostokatny(a,b,c):
#    if(a*a)+(b*b) > (c*c):
#        print("Trojkat jest prostokatny")
#    else:
#        print("Trojkąt nie jest prostokątny")
#
#print(trojkat_prostokatny(1,1,2))

#def pole_trapezu(a = 3, b = 7, h = 4):
#    pole = ((a+b)*h)/2
#    return pole

#print(pole_trapezu())

#def pierwiastek(a):
#        if a > 0:
#            print(math.sqrt(a))
#        elif a < 0:
#            print("Liczba jest ujemna!")
#print(pierwiastek(4))

#def iloczyn(a = 1, b = 4, ile = 10):
#
#    for i in range(ile - 1):
#        a *= b
#    return a
#print(iloczyn())


#lista = [randint(1,100) for i in range(10)]
#lista_parzyste = [x for x in lista if x % 2 == 0]
#print(lista_parzyste)














































