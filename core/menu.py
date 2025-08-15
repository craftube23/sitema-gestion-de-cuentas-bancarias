from core.operaciones import crear_cuenta, depositar_dinero

def mostrar_menu():
    while True:
        print("\n-- Menu Principal ---")
        print("1. crear cuenta")
        print("2. Depositar dinero")
        print("0. salir")
        opcion = input("Seleccion una opcion: ")
        
        if opcion  == "1":
            crear_cuenta()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "0":
            print("saliendo.. ")
            break
        else:
            print("opcion invalida.")
        