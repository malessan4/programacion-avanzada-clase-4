# Ejemplo de creación de una función decoradora CON argumentos (Fuente ChatGPT-3)

def mi_decorador(funcion):
    def funcion_envoltorio(*args, **kwargs):
        print("Antes de llamar la función.")
        resultado = funcion(*args, **kwargs)
        print("Despues de llamar a la función.")
        return resultado
    return funcion_envoltorio

@mi_decorador
def mi_funcion():
    print("Dento de la función.")
    
mi_funcion()