#Actor
def actor(accion):
	print('Se realizo la accion: ' + accion)
	return
#Agente
def hacer(accion):
	if(accion == 'limpiar'):
		#Limpiar
		actor('limpiar')
	elif(accion == 'izq'):
		#MovIzq
		actor('Izquierda')
	elif(accion == 'der'):
		#MovDer
		actor('Derecha')
	elif(accion == 'nada'):
		#Nada
		actor('Nada')
	else:
		return
#Sensor
while(True):
	entrada = input("Que accion realizara ahora?")
	if(entrada == 'apagar'):
		break
	hacer(entrada)
