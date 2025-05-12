def saludo1(nombre):
    print(f"Hola buenos dias {nombre} encantado")

def saludo2():
    print("buenas tardes capullo")


def saludo3():
    print("hola caracola")

def despedirse(nombre):
    print(f"que te jodan {nombre}")



opcion = input("introduces una opcion (1,2,3 o 4): ")

if opcion == "1":
    nombre = input("introduce tu nombre: ")
    saludo1(nombre)
    input("presione enter para continuar")
elif opcion == "3":
    saludo2()
    input("presione enter para continuar")
elif opcion == "3":
    saludo2()
    input("presione enter para continuar")
elif opcion == "4":
    nombre = input("introduce tu nombre: ")
    despedirse(nombre)
    input("presione enter para continuar")