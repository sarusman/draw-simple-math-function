import matplotlib.pyplot as plt
import sys
from math import *

print("Fonction avec variable 'x'\n - Exponentielle exp(x) x∈[-710, 710] ")
function=input()
print("Intervalle fermé de 2 réel separé d'un espace : ")
interval=input().split()
interval=[int(i) for i in interval]



def solve_f(function, intervalle):
	x_range=[]
	y_range=[]
	for x in range(intervalle[0], intervalle[1]):
		x_range.append(x)
		y_range.append(eval(function))
	return x_range, y_range


def main(function, interval):
	solved_x, solved_y=solve_f(function, interval)
	plt.plot(solved_x, solved_y)
	plt.grid(True)
	plt.show()

try:
	x=interval[0]
	eval(function)
	main(function, interval)
except SyntaxError:
	print("Forme de la fonction invalide")

except NameError:
	print("Une variable n'est pas defini : "+sys.exc_info()[1])

except ZeroDivisionError:
	print('Intervalle invalide : division par 0')

except:
	print("Erreur inconnu \n" +str(sys.exc_info()))

