import math
from math import *

f = eval("lambda x:"+input("Ingrese la funcion f: "))
g = eval("lambda x:"+input("Ingrese la funcion g: "))
tole = float(input("Ingrese la tolerancia: "))
xa = float(input("Ingrese xa: "))
niter = float(input("Ingrese el numero maximo de iteracciones: "))

xn = g(xa)
fx = f(xn)
gx = g(xa)
count = 0

err = tole + 1

print("""
Punto fijo
Tabla de resultados: 
|i|        xi        |     g(xi)       |      f(xi)      |        E       | 
""")
while (fx != 0) and (err > tole) and (count < niter):
    if err == tole + 1:
        print(f" {count}  {xa:.10e} {gx:.10e} {fx:.10e}")
    else:
        if count < 10:
            print(f" {count}  {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}")
        else:
           print(f" {count} {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}")
    xn = g(xa)
    fx = f(xn)
    err = abs(xn - xa)
    xa = xn
    count += 1
    gx = g(xa)
if count < 10:
    print(f" {count}  {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}")
else:
    print(f" {count} {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}")
if fx == 0:
    print(f"{xa} es raiz")
elif err < tole:
    print(f"{xa} es aproximacion con una tolerancia:",tole)
else:
    print(f"El metodo fracaso en {niter} iteracciones")