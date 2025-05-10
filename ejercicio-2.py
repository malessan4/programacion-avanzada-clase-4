def holaChau(func):
    def envoltorio():
        print("Hola")
        func()
        print("Chau")
    return envoltorio

    

@holaChau
def mensaje():
    print("Esto es programacion Avanzada")
    
mensaje()

def divideCero(func):
    def envoltorio(a,b):
        if b == 0:
            print("Error, no se puede dividir por cero.")
            return None
        return func(a,b)
    return envoltorio

@divideCero
def division(a,b):
    return a/b


print(division(4,2))

