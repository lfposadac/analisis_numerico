import math
from math import *

f = eval("lambda x:"+input("Ingrese la funcion: "))
xi = float(input("Ingrese xi: "))
xs = float(input("Ingrese xs: "))
tolerance = float(input("Ingrese la tolerancia: "))
niter = float(input("Ingrese el maximo de iteraccion: "))

print("""
Biseccion
Tabla de resultados: 
|i|        a        |        xm       |        b        |      f(Xm)       |        E        |
""")

fxi = f(xi)
fxs = f(xs)

if fxi == 0:
    print(f"{xi} es una raiz")
elif fxs == 0:
    print(f"{xs} es una raiz")
elif (fxi * fxs) < 0:
    xm = (xi + xs) / 2
    fxm = f(xm)
    count = 1
    error = tolerance + 1

    while (error > tolerance) and (fxm != 0) and (count < niter):
        if error == tolerance + 1:
            print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}")
        else:
            if count < 10:
                print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
            else:
                print(f" {count} {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
        if (fxi * fxm) < 0:
            xs = xm
            fxs = fxm
        else:
            xi = xm
            fxi = fxm
        xaux = xm
        xm = (xi + xs) / 2
        fxm = f(xm)
        error = abs((xm - xaux))
        count += 1
    if count < 10:
        print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
    else:
        print(f" {count} {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
    if fxm == 0:
        print(f"{xm} es raiz")
    elif error < tolerance:
        print(f"{xm} es aproximacion a una raiz con una tolerancia:",tolerance)
    else:
        print(f"Fracaso en {niter} iteracciones")
else:
    print("El intervalo es inedacuado")
