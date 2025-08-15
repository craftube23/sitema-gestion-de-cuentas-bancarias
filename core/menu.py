from core.operaciones import crear_cuenta

def mostrrar_menu():
    while True:
        print("\n-- Menu Principal ---")
        print("1. crear cuenta")
        print("0. salir")
        opcion = input("Seleccion una opcion: ")
        
        if opcion  == "1":
            crear_cuenta
        elif opcion == "0":
            print("saliendo.. ")
            break
        else:
            print("opcion invalida.")
        