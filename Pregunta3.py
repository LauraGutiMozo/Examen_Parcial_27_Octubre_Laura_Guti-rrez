class alumno:
    def __init__(self,nombre,nota):
        self.nombre =nombre
        self.nota= nota
        print ("El alumno se ha creado con éxito")

    def clasificacion(self):
        
        if self.nota >= 5:
            print (f"El alumno ha aprobado")
        if self.nota <= 5:
            print (f"El alumno ha suspendido")

