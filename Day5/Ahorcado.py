import random

listaPalabras = ["gabinete","casa","burro","camiseta"]
letrasCorrectas = []
letrasIncorrectas = []
vidas = 6
aciertos = 0
juego_terminado = False


def elegirPalabra(listaPalabras):
    palabra = random.choice(listaPalabras)
    letrasUnicas = len(set(palabra))
    return palabra, letrasUnicas

def mostrarGuiones(palabra):
    listaGuiones = []
    for letra in palabra:
        if letra in letrasCorrectas:
            listaGuiones.append(letra) #Se agregan las letras y se le muestran al usuario
        else:
            listaGuiones.append('_')    #Si no adivina, solamente se agrega un guión bajo
    print(" ".join(listaGuiones))

def pedirLetra():
    esValido = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while not esValido:
        letra = input("Ingresa una letra: ").lower()
        if letra in abecedario and len(letra) == 1:
            esValido = True
        else:
            print("Ingresa una letra válida")
    return letra


def chequearLetra(letraValidada, palabraOculta, vidas, coincidencias): #Revisar si la letra se encuentra en la palabra a adivinar
    finDeJuego = False

    if letraValidada in palabraOculta:
        letrasCorrectas.append(letraValidada)
        coincidencias += 1
    else:
        letrasIncorrectas.append(letraValidada)
        vidas -= 1

    if vidas == 0:
        finDeJuego = perder()
    elif coincidencias == cantidadLetras:
        finDeJuego = ganar(palabraOculta)

    return vidas, finDeJuego, coincidencias

def perder():
    print("Tus vidas se han agotado :(")
    print("La palabra oculta era: " + palabra)
    return True

def ganar(palabraDescubierta):
    mostrarGuiones(palabraDescubierta)
    print("Encontraste la palabra!!! :)")
    return True


palabra,cantidadLetras = elegirPalabra(listaPalabras)
while not juego_terminado:
    print("\n" + '*' * 20 + '\n')
    mostrarGuiones(palabra)

    print("\n")
    print("Letras incorrectas: " + " ".join(letrasIncorrectas))
    print(f"Vidas: {vidas}")

    print("\n" + '*' * 20 + '\n')
    letraValidada = pedirLetra()
    vidas, finDeJuego, aciertos = chequearLetra(letraValidada,palabra,vidas,aciertos)
    juego_terminado = finDeJuego