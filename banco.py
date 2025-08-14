
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

# Tipos de movimientos
TIPOS_MOV = {
    "DEPOSITO": "Depósito",
    "RETIRO": "Retiro"
}

def nuevo_id_producto():
    counters["producto"] += 1
    return str(counters["producto"])

def nuevo_id_mov():
    counters["mov"] += 1
    return str(counters["mov"])

def pedir(mensaje, requerido=True):
    valor = input(mensaje).strip()
    while requerido and not valor:
        valor = input("Dato requerido. " + mensaje).strip()
    return valor

def registrar_historial(producto_id, tipo_mov, valor):
    if producto_id not in historial:
        historial[producto_id] = {}
    mov_id = nuevo_id_mov()
    historial[producto_id][mov_id] = {
        "id": mov_id,
        "fecha": "2025-08-13",
        "tipo_mov": tipo_mov,
        "valor": valor
    }

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

def seleccionar_cuenta(cc):
    """Devuelve el ID de una cuenta de ahorro/corriente."""
    for pid in clientes[cc]["productos_ids"]:
        info = productos[pid]
        if info["tipo"] in ("cta_ahorros", "cta_corriente"):
            print(f" * {pid} - {PORTAFOLIO[info['tipo']]} | Saldo: {info['saldo']}")
    return pedir("Ingrese el ID de la cuenta: ")

def depositar():
    print("=== Depositar dinero ===")
    cc = pedir("CC del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    pid = seleccionar_cuenta(cc)
    if pid not in productos:
        print("Producto no encontrado.")
        return
    valor = float(pedir("Valor a depositar: "))
    productos[pid]["saldo"] += valor
    registrar_historial(pid, TIPOS_MOV["DEPOSITO"], valor)
    print(f"Depósito realizado. Nuevo saldo: {productos[pid]['saldo']}")

def retirar():
    print("=== Retirar dinero ===")
    cc = pedir("CC del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    pid = seleccionar_cuenta(cc)
    if pid not in productos:
        print("Producto no encontrado.")
        return
    valor = float(pedir("Valor a retirar: "))
    if valor > productos[pid]["saldo"]:
        print("Fondos insuficientes.")
        return
    productos[pid]["saldo"] -= valor
    registrar_historial(pid, TIPOS_MOV["RETIRO"], -valor)
    print(f"Retiro realizado. Nuevo saldo: {productos[pid]['saldo']}")

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
            depositar()
        elif opcion == "3":
            print("Opción 3: Solicitar crédito (pendiente)")
        elif opcion == "4":
            retirar()
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
