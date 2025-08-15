from core.persistencia import  cargar_datos, guardar_datos

def crear_cuenta():
    datos = cargar_datos()
    
    numero_cuenta = input('Ingrese el numero de cuenta: ')
    if numero_cuenta in datos:
        print('esa cuenta ya existe')
        return
    
    nombre_cliente = input('ingrese el nombre del cliente: ')
    saldo_inicial = float(input('ingrese el saldo inicial: '))
    
    datos[numero_cuenta] = {
        "nombre": nombre_cliente,
        "saldo": saldo_inicial
    }
    
    guardar_datos(datos)
    print(f"cuenta {numero_cuenta} creada con exito.")
    
def depositar_dinero():
    """Permite depositar dinero a una cuenta existente."""
    datos = cargar_datos()

    numero_cuenta = input("Ingrese el número de cuenta: ")
    if numero_cuenta not in datos:
        print(" Esa cuenta no existe.")
        return

    monto = float(input("Ingrese el monto a depositar: "))
    if monto <= 0:
        print(" El monto debe ser mayor a 0.")
        return

    datos[numero_cuenta]["saldo"] += monto
    guardar_datos(datos)
    print(f" Depósito realizado. Nuevo saldo: {datos[numero_cuenta]['saldo']:.2f}")