def main():
    capacidad = 10
    elementos = [0] * capacidad
    cima = -1

    print("Tecla elemento de la pila (termina con -1)")

    x = 0
    CLAVE = -1

    while x != CLAVE:
        entrada = input()
        try:
            x = int(entrada)
            if cima < capacidad - 1:
                cima += 1
                elementos[cima] = x
            else:
                print("Pila Llena")
                break
        except ValueError:
            print("Entrada no válida")

    if cima >= 0:
        print("Elementos de la pila:")
        while cima >= 0:
            x = elementos[cima]
            cima -= 1
            print(x, end=" ")
    else:
        print("Pila Vacía")

if __name__ == "__main__":
    main()
