class alumno:
    def __init__(self,nombre,nota):
        self.nombre =nombre
        self.nota= nota
        

    def __str__(self):
        return "El alumno se ha creado con éxito"



class alumno1(alumno):  
    def __init__(self,nombre,nota):
        alumno.__init__(self,nombre,nota)  

    def __str__(self):
        return f"El alumno se llama {self.nombre}, y tiene una nota de {self.nota}"

def  probando ():
    A = alumno1("Carlos",3)
    print (A)
    return alumno1


def clasificacion(self,nombre,nota):  
    alumno.__init__ (self,nombre,nota)
    if nota >= 5:
        return f"El alumno ha aprobado"
    if nota <= 5:
        return f"El alumno ha suspendido"



A = alumno1("Carlos",3)
clasificacion(A)
probando(A)