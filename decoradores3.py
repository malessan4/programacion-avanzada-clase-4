# Ejemplo de creación de una función decoradora CON argumentos

def calcular_area_triangulo(function):
    
    def funcion_de_retorno(*args, **kwargs):
        res = function(*args, **kwargs)
        return res / 2
    
    return funcion_de_retorno

@calcular_area_triangulo
def calcular_area(base, altura):
    return base*altura

if __name__ == "__main__":
    print(calcular_area(4, 10))
    