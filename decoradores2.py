# Ejemplo de creación de una función decoradora sin argumentos

def my_primer_decorador(function):

    def funcion_de_retorno():
        print('Inicio...')
        function()
        print('Fin')

    return funcion_de_retorno


@my_primer_decorador
def funcion_de_entrada():
    print('Hola mundo')

@my_primer_decorador
def input_funcion():
    print('Hello world')


if __name__ == "__main__":
    funcion_de_entrada()
    print()
    input_funcion()
