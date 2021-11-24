from math import sqrt
A = eval(input("Ingrese A: "))
b = eval(input("Ingrese b: "))
x0 = eval(input("Ingrese x0: "))
Tol = eval(input("Ingrese Tol: "))
w = eval(input("Ingrese w: "))
Nmax = eval(input("Ingrese Nmax: "))

print()
print("SOR(relajacion)")
print()
print("Resultados:")
print()


x1 = [0 for i in range(len(A))]
count = 0
disp = Tol + 1
deci = str(int(str(Tol)[4])+2)

def calcularNuevoSor(x0):
    for i in range(len(A)):
        sum1 = 0
        for j in range(len(A)):
            if j != i:
                sum1 += A[i][j]*x1[j]
        x1[i] = ((1-w)*x0[i])+(w*(b[i] - sum1)/A[i][i])
    return x1

def norma(x1,x0):
    result = 0
    for i, j in zip(x1,x0):
        result += (i-j)**2
    return sqrt(result)

while disp > Tol and count < Nmax:
    x1 = calcularNuevoSor(x0)
    result = [f"{i:.10e}" for i in x0]
    if count <= 9:
        ite = f"0{count}"
    else:
        ite = count
    print(f"{ite} {disp:.{deci}f} {result}")
    disp = (norma(x1,x0))
    x0 = [i for i in x1]    
    count += 1
    
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