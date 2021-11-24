from math import sqrt
import numpy as np
A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))
x0 = eval(input("Ingrese x0: "))
Tol = input("Ingrese Tol: ")
deci = str(int(str(Tol)[3])+2)
Tol = eval(Tol)
Nmax = eval(input("Ingrese Nmax: "))

print()
print("Jacobi")
print()
print("Resultados:")

C = []
T = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A)):
    coef = 0
    C.append((1/A[i][i])*b[i])
    coef = -(1/A[i][i])
    for j in range(len(A)):
        if i != j:
            T[i][j] = A[i][j]*coef

print()
print("T:")
for i in T:
    result = ""
    for j in i:
        result += f"{j:.10e} "
    print(result)

print()
print("C:")
for i in C:
    print(i)

val, ne =  np.linalg.eig(T) # T es la matriz
sr = max(abs(val))
print()
print("Radio espectral: ")
print(sr)
print()
x1 = [0 for i in range(len(A))]
count = 0
disp = Tol + 1

def calcularNuevoJacobi(x0):
    for i in range(len(A)):
        sum1 = 0
        for j in range(len(A)):
            if j != i:
                sum1 += A[i][j]*x0[j]
        x1[i] = (b[i] - sum1)/A[i][i]
    return x1

def norma(x1,x0):
    result = 0
    for i, j in zip(x1,x0):
        result += (i-j)**2
    return sqrt(result)

while disp > Tol and count < Nmax:
    x1 = calcularNuevoJacobi(x0)
    result = [f"{i:.10e}" for i in x0]
    if count <= 9:
        ite = f"0{count}"
    else:
        ite = count
    print(f"{ite} {disp:.{deci}f} {result}")
    count += 1
    disp = norma(x1,x0)
    x0 = [i for i in x1]
if disp < Tol:
    if count <= 9:
        ite = f"0{count}"
    else:
        ite = count
    result = [f"{i:.10e}" for i in x0]
    print(f"{ite} {disp:.{deci}f} {result}")
    print()
    print("x:")
    for i in x0:
        print(i)
else:
    print(f"Fracaso en {Nmax} iteraciones")




