
clientes = {}
productos = {}
historial = {}
counters = {
    "producto": 1000,
    "mov": 1
}

PORTAFOLIO = {
    "cta_ahorros": "Cuenta de Ahorros",
    "cta_corriente": "Cuenta Corriente",
    "cdt": "CDT",
    "credito_libre_inv": "Crédito Libre Inversión",
    "credito_vivienda": "Crédito Vivienda",
    "credito_compra_auto": "Crédito Compra Automóvil"
}

ESTADOS = {
    "ACTIVO": "Activo",
    "INACTIVO": "Inactivo",
    "CANCELADO": "Cancelado",
    "PAGADO": "Pagado"
}

TIPOS_MOV = {
    "DEPOSITO": "Depósito",
    "RETIRO": "Retiro",
    "CREDITO": "Crédito otorgado",
    "PAGO_CREDITO": "Pago cuota crédito"
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
        valor = input(mensaje).strip()
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
    cc = pedir("CC: ")
    if cc in clientes:
        return cc
    nombre = pedir("Nombre: ")
    email = pedir("Email: ")
    edad = pedir("Edad: ")
    movil = pedir("Móvil: ")
    fijo = pedir("Fijo: ", requerido=False)
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
    return cc

def abrir_producto(cc, tipo):
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
    return producto_id

def seleccionar_producto(cc, tipos_permitidos):
    for pid in clientes[cc]["productos_ids"]:
        info = productos[pid]
        if info["tipo"] in tipos_permitidos:
            print(f"{pid} - {PORTAFOLIO[info['tipo']]} | Saldo: {info['saldo']} | Estado: {info['estado']}")
    return pedir("ID del producto: ")

def depositar():
    cc = pedir("CC: ")
    if cc not in clientes:
        return
    pid = seleccionar_producto(cc, ["cta_ahorros", "cta_corriente"])
    if pid not in productos:
        return
    valor = float(pedir("Valor: "))
