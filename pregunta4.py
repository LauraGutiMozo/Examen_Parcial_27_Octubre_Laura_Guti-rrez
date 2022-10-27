

class alumno:
    def __init__(self,nombre,nota):
        self.nombre =nombre
        self.nota= nota
        return "El alumno se ha creado con éxito"

    def __str__(self):
        return f"El alumno se llama {self.nombre}, y tiene una nota de {self.nota}"


class clasificar:  
    def __init__(self,nombre,nota):
        alumno.__init__(self,nombre,nota)  

    def __str__(self):
        return f"{self.clasificacion}"

    def clasificacion(self,nombre,nota):  
        alumno.__init__ (self,nombre,nota)
        if nota >= 5:
            print (f"El alumno ha aprobado")
        if nota <= 5:
            print (f"El alumno ha suspendido")


alumno1 = clasificar("Carlos",3)
print(alumno1)
clasificar()





