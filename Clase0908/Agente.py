numero = 50
nmayor = 100
nmenor = 0
print("Se adivinara el numero (Entero) en el cual está pensando, responda \n Mayor [+] \n Menor [-] \n Igual [=] \n Según corresponda")

#Agente
def mayor(num):
	global numero
	global nmayor
	global nmenor

	nmenor = numero
	numero = int( (nmayor - num)/2 + numero)

def menor(num):
	global numero
	global nmayor
	global nmenor

	nmayor = numero
	numero = int( (nmenor - num)/2 + numero)


#Actor
def presentar():
	print(f"Su numero es el: {numero}?")

while(True):
	presentar()
	#Sensor
	while(True):
		temp = input("El numero presentado es mayor o menor? [+] [-]\t")
		if(temp == '+'):
			mayor(numero)
			break
		elif(temp == '-'):
			menor(numero)
			break
		else:
			print('XXXX Entrada no valida XXXX')
	