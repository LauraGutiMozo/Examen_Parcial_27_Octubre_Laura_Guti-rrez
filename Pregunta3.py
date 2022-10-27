class alumno:
    def __init__(self,nombre,nota):
        self.nombre =nombre
        self.nota= nota
        return "El alumno se ha creado con éxito"

    def clasificacion(self):
        
        if self.nota >= 5:
            print (f"El alumno ha aprobado")
        if self.nota <= 5:
            print (f"El alumno ha suspendido")

if __name__=="__main__":

    alumno1 = clasificar("Carlos",3)
    print (alumno1)
    alumno2c= clasificar("Juan",5)
    print (alumno1)
    alumno3 = clasificar("Laura",10)
    print (alumno1)