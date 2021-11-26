from gaussiana import formaMatrizAumentada, sustitucionProgresiva, sustitucionRegresiva, pivoteoParcial, intercambioMarcas, reordenar

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
    marcas = [i for i in range(n)]                   
    for k in range(n-1):
        L[k][k] = 1
        Ab, mayor = pivoteoParcial(Ab, n, k, True)
        if mayor != k:
            marcas = intercambioMarcas(marcas, mayor, k)
        mults_aux = {}
        for i in range(k+1, n):
            mults_aux[(i,k)] = multiplicador = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicador * Ab[k][j])
        for i, j in mults_aux:
            Ab[i][j] = mults_aux[(i,j)]
        for i, j in mults_aux:
            L[i][j] = Ab[i][j]
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
        print("P:(marcas)")
        result = ""
        for i in marcas:
            l = float(i)
            result += "{0:.10e}".format(l)+" "
        print(result)
        print()
    return Ab, marcas

print()
print("LU con pivoteo parcial:")
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
Ab, marcas = factorizacionLU(A,b, len(A), etapa)

b = reordenar(b, marcas)
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



