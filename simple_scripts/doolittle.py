from gaussiana import formaMatrizAumentada, sustitucionRegresiva, sustitucionProgresiva
from directa import factorizacionDirecta
A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))
etapa = 0

print()
print("Doolittle")
print()
print("Resultados")
print()
print(f"Etapa {etapa}")
print()
for i in A:
    result = ""
    for j in i:
        result += f"{j:.10e} "
    print(result)
L, U = factorizacionDirecta(A,etapa, "do")
Lb = formaMatrizAumentada(L,b)
z = sustitucionProgresiva(Lb,len(L))
Uz = formaMatrizAumentada(U,z)
x = sustitucionRegresiva(Uz,len(U))
print()
print("Despues de aplicar sustitucion progresiva y regresiva")
print()
print("x:")
for i in x:
    print(i)




