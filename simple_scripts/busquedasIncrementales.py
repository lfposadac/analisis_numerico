import math
from math import *

f = eval("lambda x:"+input("Ingrese la funcion: "))
x0 = float(input("Ingrese x0: "))
delta = float(input("Ingrese delta: "))
niter = float(input("Ingrese el numero maximo de iteracciones: "))

print("""
Busqueda incrementales
Resultados:
""")

fx0 = f(x0)

if float(fx0) == 0.0:
    print(f"{x0} es raiz:")
else:
    x1 = x0 + delta
    count = 1
    fx1 = f(x1)

    while (count < niter):
        x0 = x1
        fx0 = fx1
        x1 = x0 + delta
        fx1 = f(x1)
        count += 1
        if float(fx0) == 0.0:
            print(f"{x0} es raiz")
        if float(fx1) == 0.0:
            print(f"{x1} es raiz")
        if float(fx0 * fx1) < 0.0:
            print(f"Hay un raiz entre {x0:.10e} y {x1:.10e}")