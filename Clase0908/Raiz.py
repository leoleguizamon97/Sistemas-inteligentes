#Agente
def raiz(num):
    return num**(0.5)
#Actor
def presentar(num, res):
	print(f'La raiz cuadrada de {num} es: {res}')
def otro():
	while(True):
		accion =  input('Desea calcular la raiz de un numero?\n Si [S] - No [N]\n > ')
		if(accion.lower() == 's'):
			numero = float(input('Ingrese el numero del cual quiere calcular la raiz:\n > '))
			return numero
		elif(accion.lower() == 'n'):
			return "-"
#Sensor
while(True):
	numero = otro()
	if(numero == '-'):
		break
	else:
		#Llamada al agente
		resultado = raiz(numero)
		#Llamada al actor
		presentar(numero,resultado)