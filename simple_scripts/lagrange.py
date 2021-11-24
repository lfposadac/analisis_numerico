xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))
b = []

print("Lagrange")
print()
print("Resultados:")
print()
print("Polinomios interpolantes:")
print()
expresion = ""
result = 1
polim = "*"
for i in xs:
    for k in xs:
        if xs.index(i) != xs.index(k): 
            polim += (f"(x - {k})*")
            result *= i - k  
    polim = polim[0:len(polim)-1]
    print(polim[1:])
    result = 1/result
    result = ys[xs.index(i)]*result
    b.append(result)
    expresion += "("+str(result)+polim+")"+"+"
    polim = "*"
    result = 1
expresion = expresion[0:len(expresion)-1]

print()
print("Coeficientes del polinomio:")
print()
for i in b:
    print(i)
print()
print("Polinomio:")
print()
print(expresion) 




