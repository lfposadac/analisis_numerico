import math
from math import *

f = eval("lambda x: "+input("Ingrese la funcion: "))
df = eval("lambda x: "+input("Ingrese la derivada de la funcion: "))
df2 = eval("lambda x: "+input("Ingrese la segunda derivada de la funcion: "))
tol = float(input("Ingrese la tolerancia: "))
x0 = float(input("Ingrese x0: "))
niter = float(input("Ingrese el maximo de iteraciones: "))

fx = f(x0)
dfx = df(x0)
dfx2 = df2(x0)
cont = 0
err = 0
err = tol + 1
print("""
Raices Multiples
Tabla de resultados: 
|i|        xi       |      f(xi)     |        E       |
""")


while (err > tol) and (fx != 0) and (dfx != 0) and (dfx2 != 0) and (cont < niter):
    if err == tol + 1:
        print(f" {cont}  {x0:.10e} {fx:.10e}")
    else:
        if cont < 10:
            print(f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}")
        else:
            print(f" {cont} {x0:.10e} {fx:.10e} {err:.10e}")
    x1 = x0 - ((fx*dfx)/((dfx)**2-(fx*dfx2)))
    fx = f(x1)
    dfx = df(x1)
    dfx2 = df2(x1)
    err = abs(x1 - x0)
    x0 = x1
    cont += 1
if cont < 10:
    print(f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}")
else:
    print(f" {cont} {x0:.10e} {fx:.10e} {err:.10e}")
if fx == 0:
    print(f"{x0} es raiz")
elif err < tol:
    print(f"{x1} es aproximacion a una raiz con una tolerancia:", tol)
elif dfx == 0 or dfx2 == 0:
    print(f"{x1} es una posible raiz multiple")
else:
    print(f"Fracaso en {niter} iteraciones")
