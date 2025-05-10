from decorador import decorador_fecha_hora, formato_fecha_hora

@formato_fecha_hora
@decorador_fecha_hora

def suma(a,b):
    print(f'Resultado: {a+b}')
    
suma(4,6)