from gaussiana import eliminacionGaussianaConPivoteo, sustitucionRegresiva, reordenar

def makeMatrix(x,b,meth):
    if meth == 1:
        a = [[0 for i in range((len(x)-1)*2)] for j in range((len(x)-1)*2)]
        a[0][0] = x[0]
        a[0][1] = 1
        a[1][0] = x[1]
        a[1][1] = 1

        j = 2
        for i in range(2,len(x)):
            a[i][j] = x[i]
            a[i][j+1] = 1
            j += 2
        
        i = 1
        j = 0
        for k in range(len(x),((len(x)*2)-2)):
            b += [0]
            a[k][j] = x[i]
            a[k][j+1] = 1
            a[k][j+2] = -x[i]
            a[k][j+3] = -1
            i += 1
            j += 2
        
    elif meth == 2:
        a = [[0 for i in range((len(x)-1)*3)] for j in range((len(x)-1)*3)]
        a[0][0] = x[0]**2
        a[0][1] = x[0]
        a[0][2] = 1
        a[1][0] = x[1]**2
        a[1][1] = x[1]
        a[1][2] = 1

        j = 3
        for i in range(2,len(x)):
            a[i][j] = x[i]**2
            a[i][j+1] = x[i]
            a[i][j+2] = 1
            j += 3  

        i = 1
        j = 0
        for k in range(len(x),((len(x)*2)-2)):
            b += [0]
            a[k][j] = x[i]**2
            a[k][j+1] = x[i]
            a[k][j+2] = 1
            a[k][j+3] = -(x[i]**2)
            a[k][j+4] = -x[i]
            a[k][j+5] = -1 
            i += 1
            j += 3
        
        i = 1
        j = 0
        for k in range(((len(x)*2)-2),len(a)-1):
            b += [0]
            a[k][j] = 2*x[i]
            a[k][j+1] = 1
            a[k][j+2] = 0
            a[k][j+3] = -2*x[i]
            a[k][j+4] = -1
            a[k][j+5] = 0 
            i += 1
            j += 3
        
        b += [0]
        a[len(a)-1][0] = 2
    
    else:
        a = [[0 for i in range((len(x)-1)*4)] for j in range((len(x)-1)*4)]
        a[0][0] = x[0]**3
        a[0][1] = x[0]**2
        a[0][2] = x[0]
        a[0][3] = 1
        a[1][0] = x[1]**3
        a[1][1] = x[1]**2
        a[1][2] = x[1]
        a[1][3] = 1

        j = 4
        for i in range(2,len(x)):
            a[i][j] = x[i]**3
            a[i][j+1] = x[i]**2
            a[i][j+2] = x[i]
            a[i][j+3] = 1
            j += 4  

        i = 1
        j = 0
        for k in range(len(x),((len(x)*2)-2)):
            b += [0]
            a[k][j] = x[i]**3
            a[k][j+1] = x[i]**2
            a[k][j+2] = x[i]
            a[k][j+3] = 1
            a[k][j+4] = -(x[i]**3)
            a[k][j+5] = -(x[i]**2)
            a[k][j+6] = -x[i]
            a[k][j+7] = -1
            i += 1
            j += 4
        
        i = 1
        j = 0
        for k in range(((len(x)*2)-2),((len(x)*3)-4)):
            b += [0]
            a[k][j] = 3*(x[i]**2)
            a[k][j+1] = 2*x[i]
            a[k][j+2] = 1
            a[k][j+3] = 0
            a[k][j+4] = -(3*(x[i]**2))
            a[k][j+5] = -(2*x[i])
            a[k][j+6] = -1
            a[k][j+7] = 0 
            i += 1
            j += 4
        
        i = 1
        j = 0
        for k in range(((len(x)*3)-4),((len(x)*4)-6)):
            b += [0]
            a[k][j] = 6*x[i]
            a[k][j+1] = 2
            a[k][j+2] = 0
            a[k][j+3] = 0
            a[k][j+4] = -6*x[i]
            a[k][j+5] = -2
            a[k][j+6] = 0
            a[k][j+7] = 0 
            i += 1
            j += 4
        
        b += [0]*2
        a[len(a)-2][0] = 6*x[0]
        a[len(a)-2][1] = 2
        a[len(a)-1][len(a)-4] = 6*x[len(x)-1]
        a[len(a)-1][len(a)-3] = 2

    return a, b

def trazas(x,method):
    print("Trazas: ")
    print()
    result = ""
    if method == 1:
        for i in range(len(x)):
            if i % 2 == 0:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+"*"+"x"
                else:
                    result += str(x[i])+"x"
            else:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+";"
                else:
                    result += str(x[i])+";"

    elif method == 2:
        j = 0
        for i in range(len(x)):
            if j == 0:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+"*"+"x**2"
                else:
                    result += str(x[i])+"x**2"
            elif j == 1:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+"*"+"x"
                else:
                    result += str(x[i])+"x"
            else:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+";"
                else:
                    result += str(x[i])+";"
                j = -1
            j += 1
    else:
        j = 0
        for i in range(len(x)):
            if j == 0:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+"*"+"x**3"
                else:
                    result += str(x[i])+"x**3"
            elif j == 1:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+"*"+"x**2"
                else:
                    result += str(x[i])+"x**2"
            elif j == 2:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+"*"+"x"
                else:
                    result += str(x[i])+"x"
            else:
                if x[i] >= 0.0:
                    result += "+"+str(x[i])+";"
                else:
                    result += str(x[i])+";"
                j = -1
            j += 1

    for i in result.split(";"):
        print(i)

if __name__ == "__main__":
    x = eval(input("Ingrese x: "))
    y = eval(input("Ingrese y: "))
    meth = eval(input("Metodo (1,2,3): "))
    b = y
    a, b = makeMatrix(x,b,meth)
    ab, marcas = eliminacionGaussianaConPivoteo(a, b, len(a),"")
    x = sustitucionRegresiva(ab, len(ab))
    x = reordenar(x,marcas)
    print()
    print("X:")
    print()
    print(x)
    print()
    trazas(x,meth)