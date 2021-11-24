import sys
import math
def factorizacionDirecta(A,etapa,me="cr"):
    L, U =  inicializaLU(len(A),1.0)
    for k in range(len(A)):
        sum1 = 0
        for p in range(k):
            sum1 += L[k][p]*U[p][k]
        if me == "do":
            U[k][k] = A[k][k] - sum1
        elif me == "cr":
            L[k][k] = A[k][k] - sum1
        else:
            try:
                L[k][k] = math.sqrt(A[k][k] - sum1)
                U[k][k] = math.sqrt(A[k][k] - sum1)
            except:
                print("El lenguaje no soporta numeros imaginarios y el metodo lo requiere para este ejercicio")
                sys.exit()
        for i in range(k+1,len(A)):
            sum2 = 0
            for p in range(k):
                sum2 += L[i][p]*U[p][k]
            if me == "do":
                L[i][k] = (A[i][k] - sum2)/U[k][k]
            if me == "cr":
                L[i][k] = A[i][k] - sum2
            else:
                L[i][k] = (A[i][k] - sum2)/U[k][k]
        for j in range(k+1,len(A)):
            sum3 = 0
            for p in range(k):
                sum3 += L[k][p]*U[p][j]
            if me == "do":
                U[k][j] = A[k][j] - sum3
            if me == "cr":
                U[k][j] = (A[k][j] - sum3)/L[k][k]
            else:
                U[k][j] = (A[k][j] - sum3)/L[k][k]
        etapa += 1
        print()
        print(f"Etapa {etapa}")
        print()
        print("L:")
        for i in L:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        print()
        print("U:")
        for i in U:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        print()
    return L, U

def inicializaLU(n,val):
    L = [[0 for i in range(n)] for j in range(n)]
    U = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        L[i][i]  = val
        U[i][i]  = val
    return L, U




