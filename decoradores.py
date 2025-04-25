def mi_primer_decorador (function):
    
    def funcion_de_retorno():
        print('Cargando...')
        function()
        print('Proceso finalizado')
        
    return funcion_de_retorno

@mi_primer_decorador
def funcion_de_entrada():
    print('Hola Mundo')
    
if __name__ == "__main__":
    funcion_de_entrada()

