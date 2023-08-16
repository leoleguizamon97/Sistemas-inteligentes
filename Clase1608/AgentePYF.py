import random

#FUNCIONES
def picas(n,m):
	p = 0
	for i in range(4):
		for j in range(4):
			if( i!= j and n[i]==m[j] ):
				p += 1
	return p
def fijas(n,m):
	f = 0
	for i in range(4):
		if( n[i]==m[i] ):
			f += 1
	return f

#AGENTE
class Agente:
	def programa(self,perception):
		if(perception=='S'):
			#Iniciar agente
			self.minumero = random.sample([0,1,2,3,4,5,6,7,8,9],4)
			#Tomamos todas las posibles opciones para el programa y se guardan en opciones
			#La idea es reducir de esta lista las opciones segun el ingreso del sensor
			self.opciones = []
			for a in range(10):
				for b in range(10):
					for c in range(10):
						for d in range(10):
							if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
								self.opciones.append([a,b,c,d])
			return 'R'
		
		elif(perception=='#'):
			#Preguntar numero
			#Aca mandamos un numero aleatorio de las opciones disponibles
			#Es como preguntar de las opciones
			self.m = self.opciones[random.randint(0,len(self.opciones)-1)]
			return str(self.m[0]) + str(self.m[1]) + str(self.m[2]) + str(self.m[3])
		
		elif(perception.index(',')>=0):
			#Leer picas y fijas
			valores = perception.split(',')
			P = int(valores[0])
			F = int(valores[0])
			k = 0
			while(k<len(self.opciones)):
				p = picas(self.opciones[k],self.m)
				f = fijas(self.opciones[k],self.m)
				if(p==P and f==F):
					k+=1
				else:
					self.opciones.pop(k)
				k+=1
		else:
			#Leer numero
			n = [int(perception[i]) for i in range(4)]
			p = picas(n,self.minumero)
			f = picas(n,self.minumero)
		return k
print('**********************************************')
#Iniciacion
a = Agente()
a.programa('S')
#Ciclo principal
while(True):
	n = a.programa('#')
	print(f'Nuero agente: {n}')
	p = input('PICAS: ')
	f = input('FIJAS: ')
	a.programa(p + ',' + f)