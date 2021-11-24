from gaussiana import formaMatrizAumentada, sustitucionProgresiva, sustitucionRegresiva

A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))
etapa = 0

L = []
for i in range(len(A)):
    row = []
    for j in range(len(A)):
        if i != j:
            row.append(0.0)
        else:
            row.append(1.0)
    L.append(row)
U = [[0.0 for i in range(len(A))] for j in range(len(A))]
A = [[float(i) for i in j] for j in A]
U[0] = [i for i in A[0]]
def factorizacionLU(A, b, n, etapa):
    Ab = formaMatrizAumentada(A,b)                      
    for k in range(n-1):
        for i in range(k+1, n):
            L[i][k] = multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
        etapa += 1
        print()
        print(f"Etapa {etapa}")
        print()
        for i in Ab:
            result = ""
            for j in i[:len(Ab)]:
                result += f"{j:.10e} "
            print(result)
        print()
        print("L:")
        for i in L:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        print()
        print("U:")
        i = Ab[etapa]
        U[etapa] = i[:len(Ab)]
        for i in U:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        print()
    return Ab

print()
print("LU con gaussiana simple:")
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
Ab = factorizacionLU(A,b, len(A),etapa)

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