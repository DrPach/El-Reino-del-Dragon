import time
import random

print("\n ****************************************BIENVENIDOS AL REINO DEL DRAGÓN*************************************************************** \n")

def introduccion(jugador):
	print("\n \nEn este juego, el jugador se encuentra en una tierra llena de dragones. Los dragones viven en sus cuevas y en ellas guardan sus tesoros.")
	print("Algunos dragones son buenos y compartirán su tesoro, otros dragones son codiciosos y hambrientos y se comerán a cualquiera que pise su cueva.")
	print("El jugador se encuentra frente a las dos cuevas, una con un dragón amable y otra con un dragón hambriento.") 
	print("El jugador tiene que elegir a cual cueva entrar, sin saber de ante mano donde esta uno u el otro. \n \n")
	jugador=input("	Introduce tu nombre de jugador: ")
	print("\nMuy bien {}. Bienvenido a la tierra de dragones. \nAnte ti se encuentran dos cuevas de aspecto semejante.\nTú OBJETIVO es sobrevivir al menos 3 veces seguidas y acumular todo el dinero posible por el camino.\n\nSi lo logras, ganarás.\nDe lo contrario serás devorado por el dragón Abraham!!!\n".format(jugador))
	return jugador



def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print ("A que cueva quieres entrar? 1 o 2?")
        cueva =input() 
        
    return cueva


def cheqcueva(CambiarCueva,vivo,dinero):
    print ("\n\nTe acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y huele mal...")
    time.sleep(2)
    print ("Un gran dragon aparece frente a ti...")
    print("Abre su boca y...")
    time.sleep(2)
    print ("")
    
    eleccionesvitales = random.randint (1, 2)
    
    if CambiarCueva == str(eleccionesvitales):
        print ("\nTe entrega el tesoro...")
        
        time.sleep(2)
        
        ganancia=random.randint (500, 2000)
        dinero=dinero+ganancia
        print("El dragón comparte su tesoro contigo.... \nTienes {} $ ahora mismo\n".format(dinero))
        time.sleep(2)
        print("Has sobrevivido a esta ronda.\n\nContinuemos.\n")
        time.sleep(2)
        vivo+=1
        
        return vivo,dinero


    
    else:
        print ("\nEl dragón te arranca la cabeza de un mordisco....")
        vivo=5
        print("Vaya,estabas cerca....\n")
        print("\nFIN DEL JUEGO. Pringado!!!\n")
        return vivo,dinero
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
    
nom= ""
vivo=0
result=0
dinero=0
diner=0
introduccion(nom)

while result < 3:

	NumCaverna = CambiarCueva()
	result,diner=cheqcueva(NumCaverna,vivo,dinero)
	vivo=result
	dinero=diner

    
if result ==3:
	print("\n\nHAS GANADO EL JUEGO!!!!\nY HAS ACUMULADO {} $\n ".format(dinero))  
