from gaussiana import eliminacionGaussianaConPivoteo, sustitucionRegresiva, reordenar

A = eval(input("Ingrese la matriz A: "))
b = eval(input("Ingrese el arreglo b: "))

print("""
Eliminacion con pivoteo total
""")

Ab, marcas = eliminacionGaussianaConPivoteo(A, b, len(A),"")
x = sustitucionRegresiva(Ab, len(A))
x = reordenar(x, marcas)

print()
print("Despues de aplicar sustitucion regresiva")
print()
print("x")
for i in x:
    print(i)