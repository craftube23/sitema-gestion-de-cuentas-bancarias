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