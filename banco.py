
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

def nuevo_id_producto():
    counters["producto"] += 1
    return str(counters["producto"])

def pedir(mensaje, requerido=True):
    """Pide un dato por teclado."""
    valor = input(mensaje).strip()
    while requerido and not valor:
        valor = input("Dato requerido. " + mensaje).strip()
    return valor

def crear_cliente():
    print("=== Crear cliente ===")
    cc = pedir("CC: ")
    if cc in clientes:
        print("El cliente ya existe.")
        return cc

    nombre = pedir("Nombre: ")
    email = pedir("Email: ")
    edad = pedir("Edad: ")
    movil = pedir("Móvil: ")
    fijo = pedir("Fijo (opcional): ", requerido=False)
    pais = pedir("País: ")
    departamento = pedir("Departamento: ")
    ciudad = pedir("Ciudad: ")
    direccion = pedir("Dirección: ")

    clientes[cc] = {
        "cc": cc,
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {
            "pais": pais,
            "departamento": departamento,
            "ciudad": ciudad,
            "direccion": direccion
        },
        "productos_ids": {}
    }
    print("Cliente creado con éxito.")
    return cc

def abrir_producto(cc):
    print("=== Abrir producto ===")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    print("Portafolio disponible:")
    for clave in PORTAFOLIO:
        print(f" - {clave}: {PORTAFOLIO[clave]}")

    tipo = pedir("Tipo de producto (clave): ")
    if tipo not in PORTAFOLIO:
        print("Tipo no válido.")
        return

    producto_id = nuevo_id_producto()
    productos[producto_id] = {
        "id": producto_id,
        "cc": cc,
        "tipo": tipo,
        "fecha_inicio": "2025-08-13",
        "estado": ESTADOS["ACTIVO"],
        "saldo": 0.0
    }

    clientes[cc]["productos_ids"][producto_id] = True
    print(f"Producto '{PORTAFOLIO[tipo]}' creado con ID {producto_id}.")

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
            cc = crear_cliente()
            if cc:
                abrir_producto(cc)
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
