import math
from math import *

f = eval("lambda x:"+input("Ingrese la funcion f: "))
x0 = float(input("Ingrese x0: "))
x1 = float(input("Ingrese x1: "))
tol = float(input("Ingrese la tolerancia: "))
niter = float(input("Ingrese el maximo de iteraccion: "))

fx0 = f(x0)
print("""
Secante
Tabla de resultados: 
|i|        xi       |      f(xi)     |        E       |
""")

if fx0 == 0:
    print(f"{x0} es raiz: ")
else:
    fx1 = f(x1)
    cont = 0
    err = tol + 1
    err_aux = tol + 1
    den = fx1 - fx0
    while err_aux > tol and fx1 != 0 and den != 0 and cont < niter:
        if err_aux == tol + 1:
            print(f" {cont}  {x0:.10e} {fx0:.10e}")
        else:
            if cont < 10:
                print(f" {cont}  {x0:.10e} {fx0:.10e} {err_aux:.10e}")
            else:
                print(f" {cont} {x0:.10e} {fx0:.10e} {err_aux:.10e}")
        err_aux = err
        x2 = x1 - fx1 * (x1 - x0)/den
        err = abs(x2 - x1)
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = f(x1)
        den = fx1 - fx0
        cont += 1
    if cont < 10:
        print(f" {cont}  {x0:.10e} {fx0:.10e} {err_aux:.10e}")
    else:
        print(f" {cont} {x0:.10e} {fx0:.10e} {err_aux:.10e}")
    if fx1 == 0:
        print(f"{x1} es raiz ")
    elif err < tol:
        print(f"{x1} es aproximacion a una raiz con una tolrancia: ", tol)
    elif den == 0:
        print("Hay una posible raiz multiple")
    else:
        print(f"Fracasó en {niter} iteraciones: ")