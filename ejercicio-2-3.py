from datetime import datetime
def decorador_fecha_hora(func):
    def envoltorio( *args, **kwargs):
        print(f'Fecha y hora {datetime.now()}')
        resultado = func(*args, **kwargs)
        print(f'Fin. Fecha y hora: {datetime.now()}')
        return resultado
    return envoltorio

def formato_fecha_hora(func):
    def envoltorio(*args, **kwargs):
        print()
        print("===================")
        resultado = func(*args, **kwargs)
        print("===================")
        print()
    return envoltorio

@formato_fecha_hora
@decorador_fecha_hora
def imprimeMensaje():
    print("Hola, esto es un mensaje")
    
imprimeMensaje()