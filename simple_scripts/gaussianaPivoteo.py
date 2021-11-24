from gaussiana import eliminacionGaussianaConPivoteo, sustitucionRegresiva

A = eval(input("Ingrese la matriz A: "))
b = eval(input("Ingrese el arreglo b: "))

print("""
Eliminacion con pivoteo parcial
""")

Ab = eliminacionGaussianaConPivoteo(A, b, len(A))
x = sustitucionRegresiva(Ab, len(A))

print()
print("Despues de aplicar sustitucion regresiva")
print()
print("x")
for i in x:
    print(i)



