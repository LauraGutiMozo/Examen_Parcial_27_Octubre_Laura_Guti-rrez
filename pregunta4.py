alumno1 = ("Carlos",3)
alumno2= ("Juan",5)
alumno3 =("Laura",10)

class alumno:
    def __init__(self,nombre,nota):
        self.nombre =nombre
        self.nota= nota
        print ("El alumno se ha creado con éxito")

    def __str__(self):
        return f"El alumno se llama {self.nombre}, y tiene una nota de {self.nota}"

class clasificar:
    def __init__(self,nombre,nota):
        alumno.__init__(self,nombre,nota)
    
    def clasificacion(alumno):   
        if nota >= 5:
            print (f"El alumno ha aprobado")
        if nota <= 5:
            print (f"El alumno ha suspendido")

    clasificacion(alumno1)
    clasificacion(alumno2)
    clasificacion(alumno2)  




