import numpy as np 
#No he sido capaz de sacar este ejercicio de otra manera que no fuera con el paquete numpy

def Matriz():
    m =np.array([(1,4,-1),(-1,3,2),(2,2,0)])
    det = ((m[0][0]*m[1][1] * m[2][2]) + (m[0][1] * m[1][2] * m[2][0]) + (m[0][2] * m[1][0] * m[2][1])) - ((m[2][0] * m[1][1] * m[0][2]) + (m[2][1]  * m[1][2] * m[0][0]) + (m[2][2] * m[1][0] * m[0][1]))
    print (f"El determinante de la matriz será: {det}")

def dibujar_la_matriz(m):
    for i in range (len(m)):
        print("["),
        for j in range (len (m[i])):
            print("{:> 3s}".format (str(m[i][j]))),
            print("]")

if __name__=="__main__":
    print("Ejercicio 6")

    Matriz()
    dibujar_la_matriz ([(1,4,-1),(-1,3,2),(2,2,0)])
