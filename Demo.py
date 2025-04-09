class cuadrado:
    def __init__(self,lado):

        self.lado = lado  
    def area (self):
        return self.lado * self.lado 
lado = int (input("Ingresa el lado"))
        
mi_ejemplo = cuadrado(lado)
r = mi_ejemplo.area()
print (f"El area es {r}")