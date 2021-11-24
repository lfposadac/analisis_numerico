xs = eval(input("Ingrese los x: "))
ys = eval(input("Ingrese los y: "))

table = [] 
result = ""

print("Interpolante de Newton")
print()
print("Resultados:")

for i in range(len(ys)):
    row = [xs[i], ys[i]]
    index = 1
    for j in range(2,i+2):
        row.append((table[i-1][j-1] - row[len(row)-1])
                    /
                    (xs[i-index] - xs[i]))
        index+=1
    table.append(row)

print()
print("Tabla de diferencias divididas:")
print()
for i in table:
    result = ""
    for j in i:
        result += f"{j:.10e} "
    print(result)

result = ""
print()
print("Coeficientes del polinomio:")
print()

for i in range(len(ys)):
    print(table[i][i+1])

print()
for i in range(len(ys)):
    result += f"{table[i][i+1]}"
    for j in range(i):
        result += f"*(x - {xs[j]})"
    result += "+"

result = result[:len(result)-1]

print("Polinomio:")
print()
print(result)