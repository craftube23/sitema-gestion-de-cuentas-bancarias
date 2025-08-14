
# Diccionarios en memoria
clientes = {}     
productos = {}    
historial = {}    
counters = {      
    "producto": 1000,
    "mov": 1
}

# Portafolio de productos
PORTAFOLIO = {
    "cta_ahorros": "Cuenta de Ahorros",
    "cta_corriente": "Cuenta Corriente",
    "cdt": "CDT",
    "credito_libre_inv": "Crédito Libre Inversión",
    "credito_vivienda": "Crédito Vivienda",
    "credito_compra_auto": "Crédito Compra Automóvil"
}

# Estados posibles
ESTADOS = {
    "ACTIVO": "Activo",
    "INACTIVO": "Inactivo",
    "CANCELADO": "Cancelado",
    "PAGADO": "Pagado"
}

def menu():
    salir = False
    while not salir:
        print("""
======== MENÚ ========
1. Crear cuenta (cliente y/o producto)
2. Depositar dinero
3. Solicitar crédito
4. Retirar dinero
5. Pago cuota crédito
6. Cancelar cuenta
7. Salir
======================
""")
        opcion = input("Seleccione opción: ").strip().upper()
        
        if opcion == "1":
            print("Opción 1: Crear cuenta (pendiente de implementar)")
        elif opcion == "2":
            print("Opción 2: Depositar dinero (pendiente)")
        elif opcion == "3":
            print("Opción 3: Solicitar crédito (pendiente)")
        elif opcion == "4":
            print("Opción 4: Retirar dinero (pendiente)")
        elif opcion == "5":
            print("Opción 5: Pago cuota crédito (pendiente)")
        elif opcion == "6":
            print("Opción 6: Cancelar cuenta (pendiente)")
        elif opcion == "7":
            salir = True
        elif opcion == "H":
            print("Ver historial (pendiente)")
        else:
            print("Opción no válida.")
    print("¡Hasta luego!")

if __name__ == "__main__":
    menu()
