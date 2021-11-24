import math
from math import *

f = eval("lambda x:"+input("Ingrese la funcion: "))
df = eval("lambda x:"+input("Ingrese la derivada de la funcion: "))
tol = float(input("Ingrese la tolerancia: "))
x0 = float(input("Ingrese x0: "))
niter = float(input("Ingrese el maximo de iteraciones: "))

print("""
Newton
Tabla de resultados: 
|i|        xi        |     f(xi)      |        E       | 
""")

fx = f(x0)
dfx = df(x0)

count = 0
err = 0
err = tol + 1

while (err > tol) and (fx != 0) and (dfx != 0) and (count < niter):
    if err == tol + 1:
        print(f" {count}  {x0:.10e} {fx:.10e}")
    else:
        if count < 10:
            print(f" {count}  {x0:.10e} {fx:.10e} {err:.10e}")
        else:
            print(f" {count} {x0:.10e} {fx:.10e} {err:.10e}")
    x1 = x0 - (fx/dfx)
    fx = f(x1)
    dfx = df(x1)
    err = abs(x1 - x0)
    x0 = x1
    count += 1
if count < 10:
    print(f" {count}  {x0:.10e} {fx:.10e} {err:.10e}")
else:
    print(f" {count} {x0:.10e} {fx:.10e} {err:.10e}")
if fx == 0:
    print(f"{x0} es raiz")
elif err < tol:
    print(f"{x1} es aproximacion a una raiz con una tolerancia:", tol)
elif dfx == 0:
    print(f"{x1} es una posible raiz multiple")
else:
    print("Fracaso en " + niter + " iteraciones")