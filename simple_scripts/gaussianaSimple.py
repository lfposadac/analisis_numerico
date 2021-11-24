from gaussiana import eliminacion, sustitucionRegresiva

A = eval(input("Ingrese la matriz A: "))
b = eval(input("Ingrese el arreglo b: "))

print("""
Eliminacion gaussiana simple
""")

Ab = eliminacion(A, b, len(A))
x = sustitucionRegresiva(Ab, len(A))

print()
print("Despues de aplicar sustitucion regresiva")
print()
print("x")
for i in x:
    print(i)




