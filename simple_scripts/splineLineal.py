from gaussiana import eliminacionGaussianaConPivoteo, sustitucionProgresiva, sustitucionRegresiva, reordenar
from spline import makeMatrix, trazas
x = eval(input("Ingrese x: "))
y = eval(input("Ingrese y: "))
b = y
a, b = makeMatrix(x,b,1)
ab, marcas = eliminacionGaussianaConPivoteo(a, b, len(a),"")
x = sustitucionRegresiva(ab, len(ab))
x = reordenar(x,marcas)

print()
print("Trazadores lineales")
print()
print("Coeficientes:")
print()
result = ""
index = 0
for i in x:
    if index < 2:
        index += 1
        result += f"{i:.10e} "
    else:
        print(result)
        result = f"{i:.10e} "
        index = 1
print(result)
print()
trazas(x,1)