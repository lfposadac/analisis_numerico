"""
Este código convierte num en cualquier base a otra base
Como trabajar:
Primero pedimos los datos necesarios, luego separamos el número
en dos partes, la parte anterior al punto y la parte posterior al punto.
Luego transformamos el número por completo incluyendo tanto la parte anterior
el punto y la parte que va después del punto a base 10 si es necesario 
(si ya está en base 10 se omite). 
Luego tomamos la parte que va antes del punto y transformamos
a la base deseada siguiendo el mecanismo de multiplicar por la base:
axb ^ n + a1xb ^ n-1 ...
Luego tomamos la parte posterior al punto y la transformamos en el
base deseada con el método de los cocientes, dividir el número entre
la base (num / base) y luego cuando el divisor es menor que
la base toma todos los cocientes de izquierda a derecha.
Para evitar que el número crezca hasta el infinito, evaluamos cada
tiempo que calculamos un nuevo cociente si ya hemos alcanzado 
el resultado. Conocemos el resultado porque usando una función para pasar el número
 a la base 10, lo comparamos con la base 10 original.
Para terminar agregamos la parte anterior al punto y la que va después
el punto y mostrar el resultado
"""

"""
Descripción: Obtener número, base y base para la transformación, 
número separado antes y después de "."
Tipo: Vacío
Param:
    
    num: número de transformación
    base: base original del número
    baseTo: base para después de la transformación
Regreso:
    Nada
"""

num = input( "Dame un num:" )
base = int(input("Dame la base del número:" ))
baseTo = int(input( "Dame la base para convertir:" ))
num = num.split( "." ) #Separe las partes del número


def  to10Base ( num , base , test = "" , comparate = "" ):
    """
    Descripción: transforma cualquier número en base 10 
    ya que primero se pasa una base 10 y luego se puede llevar a otra base
    y si pasa valores de comparación con la prueba y compara variables,
    identificar si son iguales, para evitar crear números periódicos más adelante
    Tipo: booleano para comparar
    o lista para solo transformación
    Param:
        
        num: número de transformación
        base: base original del número
        prueba: número original si necesitas comparar los números 
        comparar: este número se transformará y evaluará
         más tarde para verificar si ya se ha alcanzado el número deseado
    Regreso:
        num: número solo para transformación
        falso: si al calcular la pieza después
         el punto supera las 98 unidades, interrumpimos el proceso de comparación
        float (num [0] + "." + num [1])! = float (prueba): Comparamos si la parte después del punto 
         que estamos calculando ya ha alcanzado el resultado esperado
    """

    if test != "" and comparate != "":
        num = str(comparate).split(".")

    total = 0

    if base != 10:
        auxNum = num[0]
        weight = len(auxNum)

        for number in auxNum:
            weight -= 1
            total += int(number)*(int(base)**(weight))

        if len(num) == 2:
            auxNum = num[1]
            weight = len(auxNum)

            for index in range(1,weight+1):
                exponent = int("-"+str(index))
                total += int(auxNum[index-1])*(base**(exponent))

        num = str(total).split(".")

        if test != "" and comparate != "":
            if len(comparate.split(".")[1]) > 100:
                return False
            return float(num[0] + "." + num[1]) != float(test)
    
    return num

num = to10Base(num=num,base=base) #convertir el número original a base 10

# dependiendo de si el número tiene parte después del punto o no elegimos cómo procesar los datos
if len(num) == 2:
    numToBaseFirst = int(num[0]) #primera parte del número, antes del punto
    numToBaseSecond = int(num[1]) # segunda parte del número, después del punto
    num = float(num[0] + "." + num[1])

else:
    numToBaseFirst = int(num[0])
    num = int(num[0])
    numToBaseSecond = ""

testAux = num   # esta constante mantiene el valor original del número, ya que se modificará más adelante

def toBaseFirst(number, base):
    """
    Descripción: Transforma la primera parte del número.
     a la base deseada usando el método de división y manteniendo los cocientes
    Tipo: cuerda
    Param:
        
        número: número para la transformación
        base: base final
    Regreso:
        cadena con número en la base deseada
    """
    if number == "": # si el número está vacío, devuelva el resultado vacío
         return ""
    
    number = int(number) # número de cadena a número int
    total = ""  # resultado final
    while True: # simulación para ciclo do-while
        total_aux = number
        module = number % base
        number = number // base
        total += str(module)

        if (total_aux // base ) < base:
            total += str(total_aux // base)
            return total[::-1] # invertir la cadena

def toBaseSecond(number, base, first, toBase):
    """
    Descripción: Transforma la segunda parte del número.
     a la base deseada usando el método de multiplicación y
     manteniendo la parte antes del punto después de la multiplicación
    Tipo: cuerda
    Param:
        
        número: número para la transformación
        base: base final
    Regreso:
        cadena con número en la base deseada
    """
    data = [] # números después del punto
    auxNumber = float("0." + str(number)) #number parte después de la multiplicación en cada iteración

    totalFloat = auxNumber * base  #total number después de la multiplicación en cada iteración

    total = first + "." + (str(totalFloat).split("."))[0] # almacenamiento para el resultado final y para comparar si ya hemos alcanzado el resultado

    while(((str(auxNumber).split("."))[1] != "0") and (to10Base("", baseTo, testAux, total))):
        totalFloat = auxNumber * base
        data.append((str(totalFloat).split("."))[0])
        auxNumber = float("0."+(str(totalFloat).split(".")[1]))

        total = ""

        for floatNumber in data:
            total += floatNumber

        total = first + "." + str(total)

    index = 0  # posición para el primer número diferente de 0 en el resultado
    for digit in total: 
        if digit != "0": # elimina los ceros a la izquierda
            if index != 0:
                return total[index-1:]
            return total
        index += 1

"""
dependiendo de si el número tiene parte después del punto
 o no o si supera la base a la que podemos transformarnos, se muestra una salida u otra
"""

if baseTo < 10 and baseTo != 10 and numToBaseSecond != "":
    first = toBaseFirst(numToBaseFirst, baseTo)
    print("The number is:", toBaseSecond(numToBaseSecond, baseTo, first, base))

elif baseTo > 10:
    print("This program only work until base 10")

elif baseTo != 10:
    print("The number is: ", toBaseFirst(numToBaseFirst,baseTo))

else:
    print("The number is: ", testAux)