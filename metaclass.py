def dice (self):
    print('Guauuu')
    
    
Animal = type('Perro', (), {'nombre': 'a definir'})
Perro = type('Perro', (Animal, ),dict(cantidad_patas=4, dice=dice))

p1 = Perro()
print(p1.nombre)
print(p1.cantidad_patas)
p1.dice()



new_class = type('myClass',(object, ),{'a' : True})

a = new_class()
print(a.a)