elementos=int(input('Cuál es el numero de elementos de la lista?\n'))
lista=[ ]
for i in range(elementos):
	lista.append( input(f'Cual es el elemento {i} \n'))


def aritmetica(list):
	for eles in list:
		fin=eles.find(' ')
		otro=fin+1
		print(f'       {eles[:otro]}')
		print(f'{eles[fin]}    {eles[otro:]} ')
		print('____________')
aritmetica(lista)
