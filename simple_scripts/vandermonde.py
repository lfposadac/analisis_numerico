import numpy as np
from gaussiana import eliminacionGaussianaConPivoteo, sustitucionRegresiva, reordenar

xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))

print()
print("Vandermonde")
print()
print("Resultados:")
print()

A = []
b = ys

print("Matriz de Vandermonde:")
print()

for i in xs:
    data = [(i)**k for k in range(len(xs))]
    data = data[::-1]
    result = ""
    for i in data:
        result += f"{float(i):.5} "
    print(result)
    A.append(data)

    
Ab, marcas = eliminacionGaussianaConPivoteo(A, b, len(A),"")
x = sustitucionRegresiva(Ab, len(A))
x = reordenar(x, marcas)

print()
print("Coeficientes del polinomio:")
print()
result = ""
for i in x:
    result += f"{float(i):.5} "
print(result)

result = ""
coef = len(x)
for i in x:
    coef -= 1
    if coef != 0:
        if i >= 0.0:
            result += "+"+str(i)+"*"+"x**"+str(coef)
        else:
            result += str(i)+"*"+"x**"+str(coef)
    else:
        if i >= 0.0:
            result += "+"+str(i)
        else:
            result += str(i)

print("Polinomio:")
print()
print(result)  

