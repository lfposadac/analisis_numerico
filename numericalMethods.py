class NM: 
    def busquedasIncrementales(self,f,x0,delta,niter):
        html="</br>Busquedas incrementales</br></br>Resultados:</br>"

        fx0 = f(x0)

        if float(fx0) == 0.0:
            html+=f"{x0} es raiz:</br>"
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
                    html+=f"{x0} es raiz</br>"
                elif float(fx1) == 0.0:
                    html+=f"{x1} es raiz</br>"
                elif float(fx0 * fx1) < 0.0:
                    html+=f"Hay un raiz entre {x0:.10e} y {x1:.10e}</br>"
            if html == "</br>Busquedas incrementales</br></br>Resultados:</br>":
                html+="No se encontraron intervalos de confianza</br>"
        return html

    def biseccion(self,f,xi,xs,tolerance,niter):
        html="</br>Biseccion</br></br>Tabla de resultados:</br>|i|********a********|********xm*******|********b********|******f(Xm)*******|********E********|</br>"

        try:
            fxi = f(xi)
            fxs = f(xs)

            if fxi == 0:
                html+=f"{xi} es una raiz</br>"
            elif fxs == 0:
                html+=f"{xs} es una raiz</br>"
            elif (fxi * fxs) < 0:
                xm = (xi + xs) / 2
                fxm = f(xm)
                count = 1
                error = tolerance + 1

                while (error > tolerance) and (fxm != 0) and (count < niter):
                    if error == tolerance + 1:
                        html+=f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}||-----------------</br>".replace(" ","|")
                    else:
                        if count < 10:
                            html+=f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                        else:
                            html+=f" {count} {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
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
                    html+=f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                else:
                    html+=f" {count} {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                if fxm == 0:
                    html+=f"{xm} es raiz</br>"
                elif error < tolerance:
                    html+=f"{xm} es aproximacion a una raiz con una tolerancia: {tolerance}</br>"
                else:
                    html+=f"Fracaso en {niter} iteracciones</br>"
            else:
                html+="El intervalo es inedacuado</br>"
        except Exception as e:
            if str(e) == 'math domain error':
                return "</br></br>El método se detuvo porque se está evaluando un punto que no está en el dominio de la función</br>"
            elif str(e) == 'division float':
                return "</br></br>El método se detuvo por que se generó una división por cero al evaluar la funcion o la derivada en un punto</br>"
        return html

    def reglaFalsa(self,f,xi,xs,tolerance,niter):
        html = "</br>Regla Falsa</br></br>Tabla de resultados:</br>|i|********a********|********xm*******|********b********|******f(Xm)*******|********E********|</br>"

        try:
            fxi = f(xi)
            fxs = f(xs)

            if fxi == 0:
                html+=f"{xi} es una raiz</br>"
            elif fxs == 0:
                html+=f"{xs} es una raiz</br>"
            elif (fxi * fxs) < 0:
                xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
                fxm = f(xm)
                count = 1
                error = tolerance + 1

                while (error > tolerance) and (fxm != 0) and (count < niter):
                    if error == tolerance + 1:
                        html+=f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}||-----------------</br>".replace(" ","|")
                    else:
                        if count < 10:
                            html+=f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                        else:
                            html+=f" {count} {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                    if (fxi * fxm) < 0:
                        xs = xm
                        fxs = fxm
                    else:
                        xi = xm
                        fxi = fxm
                    xaux = xm
                    xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
                    fxm = f(xm)
                    error = abs(xm - xaux)
                    count += 1
                if count < 10:
                    html+=f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                else:
                    html+=f" {count} {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}</br>".replace(" ","|")
                if fxm == 0:
                    html+=f"{xm} es raiz</br>"
                elif error < tolerance:
                    html+=f"{xm} es aproximacion a una raiz con una tolerancia: {tolerance}</br>"
                else:
                    html+=f"Fracaso en {niter} iteracciones</br>"
            else:
                html+="El intervalo es inedacuado</br>"
        
        except Exception as e:
            if str(e) == 'math domain error':
                return "</br></br>El método se detuvo porque se está evaluando un punto que no está en el dominio de la función</br>"
            elif str(e) == 'division float':
                return "</br></br>El método se detuvo por que se generó una división por cero al evaluar la funcion o la derivada en un punto</br>"
        
        return html

    def newton(self,f,df,tol,x0,niter):
        header = '|i|        xi       |     f(xi)      |        E       |'.replace(" ","*")
        html = f"</br>Newton</br></br>Tabla de resultados:</br>{header}</br>"

        
        try:

            fx = f(x0)
            dfx = df(x0)

            count = 0
            err = 0
            err = tol + 1
            while (err > tol) and (fx != 0) and (dfx != 0) and (count < niter):
                if err == tol + 1:
                    html+=f" {count}  {x0:.10e} {fx:.10e}|----------------</br>".replace(" ","|")
                else:
                    if count < 10:
                        html+=f" {count}  {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
                    else:
                        html+=f" {count} {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
                x1 = x0 - (fx/dfx)
                fx = f(x1)
                dfx = df(x1)
                err = abs(x1 - x0)
                x0 = x1
                count += 1
            if count < 10:
                html+=f" {count}  {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
            else:
                html+=f" {count} {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
            if fx == 0:
                html+=f"{x0} es raiz</br>"
            elif err < tol:
                html+=f"{x1} es aproximacion a una raiz con una tolerancia:{tol}</br>"
            elif dfx == 0:
                html+=f"{x1} es una posible raiz multiple</br>"
            else:
                html+="Fracaso en " + niter + " iteraciones</br>"
        
        except Exception as e:
            if str(e) == 'math domain error':
                return "</br></br>El método se detuvo porque se está evaluando un punto que no está en el dominio de la función</br>"
            elif str(e) == 'division float':
                return "</br></br>El método se detuvo por que se generó una división por cero al evaluar la funcion o la derivada en un punto</br>"
        
        return html

    def puntoFijo(self,f,g,tole,xa,niter):
        try:
            xn = g(xa)
            fx = f(xn)
            gx = g(xa)
            count = 0

            err = tole + 1

            header = '|i|        xi        |     g(xi)       |      f(xi)      |        E       |'.replace(" ","*")
            html = f"</br>Punto Fijo</br></br>Tabla de resultados:</br>{header}</br>"

            while (fx != 0) and (err > tole) and (count < niter):
                if err == tole + 1:
                    html += f" {count}  {xa:.10e} {gx:.10e} {fx:.10e}|----------------</br>".replace(" ","|")
                else:
                    if count < 10:
                        html += f" {count}  {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
                    else:
                        html += f" {count} {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
                xn = g(xa)
                fx = f(xn)
                err = abs(xn - xa)
                xa = xn
                count += 1
                gx = g(xa)
            if count < 10:
                html += f" {count}  {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
            else:
                html += f" {count} {xa:.10e} {gx:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
            if fx == 0:
                html += f"{xa} es raiz"
            elif err < tole:
                html += f"{xa} es aproximacion con una tolerancia: {tole}"
            else:
                html += f"El metodo fracaso en {niter} iteracciones"
        
        except Exception as e:
            if str(e) == 'math domain error':
                return "</br></br>El método se detuvo porque se está evaluando un punto que no está en el dominio de la función</br>"
            elif str(e) == 'division float':
                return "</br></br>El método se detuvo por que se generó una división por cero al evaluar la funcion en f o en g</br>"

        return html

    def secante(self,f,x0,x1,tol,niter):
        try:
            header = '|i|        xi       |     f(xi)      |        E       |'.replace(" ","*")
            html = f"</br>Secante</br></br>Tabla de resultados:</br>{header}</br>"
            fx0 = f(x0)

            if fx0 == 0:
                html+= f"{x0} es raiz: "
            else:
                fx1 = f(x1)
                cont = 0
                err = tol + 1
                err_aux = tol + 1
                den = fx1 - fx0
                while err_aux > tol and fx1 != 0 and den != 0 and cont < niter:
                    if err_aux == tol + 1:
                        html+= f" {cont}  {x0:.10e} {fx0:.10e}|----------------</br>".replace(" ","|")
                    else:
                        if cont < 10:
                            html+=f" {cont}  {x0:.10e} {fx0:.10e} {err_aux:.10e}</br>".replace(" ","|")
                        else:
                            html+=f" {cont} {x0:.10e} {fx0:.10e} {err_aux:.10e}</br>".replace(" ","|")
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
                    html+=f" {cont}  {x0:.10e} {fx0:.10e} {err_aux:.10e}</br>".replace(" ","|")
                else:
                    html+=f" {cont} {x0:.10e} {fx0:.10e} {err_aux:.10e}</br>".replace(" ","|")
                if fx1 == 0:
                    html+=f"{x1} es raiz</br>"
                elif err < tol:
                    html+=f"{x1} es aproximacion a una raiz con una tolerancia: {tol}</br>"
                elif den == 0:
                    html+=f"Hay una posible raiz multiple</br>"
                else:
                    html+=f"Fracasó en {niter} iteraciones</br>"

        except Exception as e:
            if str(e) == 'math domain error':
                return "</br></br>El método se detuvo porque se está evaluando un punto que no está en el dominio de la función</br>"
            elif str(e) == 'division float':
                return "</br></br>El método se detuvo por que se generó una división por cero al evaluar la funcion/br>"

        return html

    def raicesMultiples(self,f,df,df2,tol,x0,niter):
        try:
            fx = f(x0)
            dfx = df(x0)
            dfx2 = df2(x0)
            cont = 0
            err = 0
            err = tol + 1
            header = '|i|        xi       |     f(xi)      |        E       |'.replace(" ","*")
            html = f"</br>Raices Multiples</br></br>Tabla de resultados:</br>{header}</br>"

            while (err > tol) and (fx != 0) and (dfx != 0) and (dfx2 != 0) and (cont < niter):
                if err == tol + 1:
                    html+= f" {cont}  {x0:.10e} {fx:.10e}|-----------------</br>".replace(" ","|")
                else:
                    if cont < 10:
                        html+=f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
                    else:
                        html+=f" {cont} {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
                x1 = x0 - ((fx*dfx)/((dfx)**2-(fx*dfx2)))
                fx = f(x1)
                dfx = df(x1)
                dfx2 = df2(x1)
                err = abs(x1 - x0)
                x0 = x1
                cont += 1
            if cont < 10:
                html+=f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
            else:
                html+=f" {cont} {x0:.10e} {fx:.10e} {err:.10e}</br>".replace(" ","|")
            if fx == 0:
                html+=f"{x0} es raiz</br>"
            elif err < tol:
                html+=f"{x1} es aproximacion a una raiz con una tolerancia: {tol}</br>"
            elif dfx == 0 or dfx2 == 0:
                html+=f"{x1} es una posible raiz multiple</br>"
            else:
                html+=f"Fracaso en {niter} iteraciones</br>"
        
        except Exception as e:
            if str(e) == 'math domain error':
                return "</br></br>El método se detuvo porque se está evaluando un punto que no está en el dominio de la función</br>"
            elif str(e) == 'division float':
                return "</br></br>El método se detuvo por que se generó una división por cero al evaluar la funcion o las derivadas en un punto</br>"
            else:
                html + "a"
        
        return html

    def eliminacionSimple(self,A,b):
        html="</br>Eliminacion gaussiana simple</br></br>"

        Ab, html = self.eliminacion(A,b,len(A),html)
        
        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html

        x = self.sustitucionRegresiva(Ab, len(A))
        if type(x) == str:    
            html += x
            x = self.infinitasSoluciones(Ab)
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"

            return html

        html+="</br>Despues de aplicar sustitucion regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def eliminacionParcial(self,A,b):
        html="</br>Eliminacion gaussiana con pivoteo parcial</br></br>"

        Ab, html = self.eliminacionGaussianaConPivoteo(A, b, len(A), html)
        x = self.sustitucionRegresiva(Ab, len(A))

        if "diagonal" in html:
            return html

        if "no tiene solucion" in html:
            return html
        
        if type(x) == str:    
            html += x
            x = self.infinitasSoluciones(Ab)
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"

            return html

        html+="</br>Despues de aplicar sustitucion regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def eliminacionTotal(self,A,b):
        html="</br>Eliminacion gaussiana con pivoteo total</br></br>"

        Ab, marcas, html = self.eliminacionGaussianaConPivoteo(A, b, len(A), html,"")

        if "diagonal" in html:
            return html

        if "no tiene solucion" in html:
            return html
        x = self.sustitucionRegresiva(Ab, len(A))
        if type(x) == str:    
            html += x
            x = self.infinitasSoluciones(Ab)
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"

            return html
        x = self.reordenar(x, marcas)

        html+="</br>Despues de aplicar sustitucion regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def luSimple(self,A,b):
        html = ""
        etapa = 0

        L = []
        for i in range(len(A)):
            row = []
            for j in range(len(A)):
                if i != j:
                    row.append(0.0)
                else:
                    row.append(1.0)
            L.append(row)
        U = [[0.0 for i in range(len(A))] for j in range(len(A))]
        A = [[float(i) for i in j] for j in A]
        U[0] = [i for i in A[0]]
        def factorizacionLU(A, b, n, etapa, html):
            Ab, html_aux = self.formaMatrizAumentada(A,b)
            html += f"</br>{html_aux}</br>"                      
            for k in range(n-1):
                for i in range(k+1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return Ab, html
                    L[i][k] = multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= (multiplicador * Ab[k][j])
                etapa += 1
                html += f"</br>Etapa {etapa}</br></br>"
                for i in Ab:
                    result = ""
                    for j in i[:len(Ab)]:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>L:</br>"
                for i in L:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>U:</br>"
                i = Ab[etapa]
                U[etapa] = i[:len(Ab)]
                for i in U:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>"
            return Ab, html

        html=f"</br>LU con gaussiana simple:</br></br>Resultados</br></br>Etapa {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html += result+"</br>"
        Ab, html  = factorizacionLU(A,b, len(A),etapa,html)

        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html

        Lb, result = self.formaMatrizAumentada(L,b)
        z = self.sustitucionProgresiva(Lb,len(L))
        Uz, result = self.formaMatrizAumentada(U,z)
        x = self.sustitucionRegresiva(Uz,len(U))

        if type(x) == str:    
            html += x
            x = self.infinitasSoluciones(Ab)
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"

            return html

        html+="</br>Despues de aplicar sustitucion progresiva y regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def luParcial(self,A, b):
        etapa = 0
        L = []
        for i in range(len(A)):
            row = []
            for j in range(len(A)):
                if i != j:
                    row.append(0.0)
                else:
                    row.append(1.0)
            L.append(row)
        U = [[0.0 for i in range(len(A))] for j in range(len(A))]
        A = [[float(i) for i in j] for j in A]
        U[0] = [i for i in A[0]]
        def factorizacionLU(A, b, n, etapa, html):
            Ab, html_aux = self.formaMatrizAumentada(A,b) 
            html += f"</br>{html_aux}</br>" 
            marcas = [i for i in range(n)]                   
            for k in range(n-1):
                L[k][k] = 1
                Ab, mayor = self.pivoteoParcial(Ab, n, k, True)
                if mayor != k:
                    marcas = self.intercambioMarcas(marcas, mayor, k)
                mults_aux = {}
                for i in range(k+1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return Ab, html
                    mults_aux[(i,k)] = multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= (multiplicador * Ab[k][j])
                for i, j in mults_aux:
                    Ab[i][j] = mults_aux[(i,j)]
                for i, j in mults_aux:
                    L[i][j] = Ab[i][j]
                etapa += 1
                html += f"</br>Etapa {etapa}</br></br>"
                for i in Ab:
                    result = ""
                    for j in i[:len(Ab)]:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>L:</br>"
                for i in L:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>U:</br>"
                i = Ab[etapa]
                U[etapa] = i[:len(Ab)]
                for i in U:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>P:(marcas)</br>"
                result = ""
                for i in marcas:
                    l = float(i)
                    result += "{0:.10e}".format(l)+" "
                html += result+"</br>"
            return Ab, marcas, html

        html=f"</br>LU con pivoteo parcial:</br></br>Resultados</br></br>Etapa {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        Ab, marcas, html = factorizacionLU(A,b, len(A), etapa, html)

        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html

        b = self.reordenar(b, marcas)
        Lb, result = self.formaMatrizAumentada(L,b)
        z = self.sustitucionProgresiva(Lb,len(L))
        Uz, result = self.formaMatrizAumentada(U,z)
        x = self.sustitucionRegresiva(Uz,len(U))

        if type(x) ==  str:    
            html += x
            x = self.infinitasSoluciones(Ab)
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"
            return html

        html+="</br>Despues de aplicar sustitucion progresiva y regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def crout(self,A,b):
        etapa = 0
        html = f"</br>Crout</br></br>Resultados</br></br>Etapa {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"
        L, U, html = self.factorizacionDirecta(A,etapa,html,"cr")

        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html

        Lb, result = self.formaMatrizAumentada(L,b)
        z = self.sustitucionProgresiva(Lb,len(L))
        Uz, result = self.formaMatrizAumentada(U,z)
        x = self.sustitucionRegresiva(Uz,len(U))

        html+="</br>Despues de aplicar sustitucion progresiva y regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def doolittle(self, A, b):
        etapa = 0

        html = f"</br>Doolittle</br></br>Resultados</br></br>Etapa {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        L, U, html = self.factorizacionDirecta(A,etapa,html,"do")
        if "diagonal" in html:
            return html

        if "no tiene solucion" in html:
            return html

        Lb, result = self.formaMatrizAumentada(L,b)
        z = self.sustitucionProgresiva(Lb,len(L))
        Uz, result = self.formaMatrizAumentada(U,z)
        x = self.sustitucionRegresiva(Uz,len(U))

        html+="</br>Despues de aplicar sustitucion progresiva y regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def cholesky(self, A, b):
        etapa = 0

        html = f"</br>Cholesky</br></br>Resultados</br></br>Etapa {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"
        html+="</br>"
        L, U, html = self.factorizacionDirecta(A,etapa,html,"ch")
        if "imaginarios" in html:
            return html
        if "diagonal" in html:
            return html
        if "no tiene solucion" in html:
            return html

        Lb, result = self.formaMatrizAumentada(L,b)
        z = self.sustitucionProgresiva(Lb,len(L))
        Uz, result = self.formaMatrizAumentada(U,z)
        x = self.sustitucionRegresiva(Uz,len(U))

        html+="</br>Despues de aplicar sustitucion progresiva y regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html

    def jacobi(self,A,b,x0,Tol,Nmax):
        import numpy as np

        html = "</br>Jacobi</br></br>Resultados:</br>"

        C = []
        T = [[0 for i in range(len(A))] for j in range(len(A))]
        for i in range(len(A)):
            coef = 0
            if A[i][i] == 0:
                return html+f"</br>Existe un 0 en la diagonal, en la posicion {i+1},{i+1} lo que genera una división por cero cuando se desea contruir la matriz C</br>"
            C.append((1/A[i][i])*b[i])
            coef = -(1/A[i][i])
            for j in range(len(A)):
                if i != j:
                    T[i][j] = A[i][j]*coef

        html += "</br>T:</br>"
        for i in T:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        html += "</br>C:</br>"
        for i in C:
            html += f"{i}</br>"

        val, ne =  np.linalg.eig(T) # T es la matriz
        sr = max(abs(val))
        
        html += f"</br>Radio espectral:</br>{sr}</br></br>"
        if sr < 1:
            html += f"El sistema converge a la solucion unica x=Tx + c ya que p(T) < 1</br></br>"
        else:
            html += f"El sistema no converge a la solucion unica x=Tx + c ya que p(T) >= 1</br></br>"

        if self.estrictamenteDiagonalDominante(A):
            html += f"La matriz es estrictamente diagonal dominante y por lo tanto converge para cualquier aproximacion inical x0</br></br>"
        else:
            html += f"La matriz no es estrictamente diagonal dominante y por lo tanto no converge para toda aproximacion inical x0</br></br>"

        html += f"|i|E|X|</br>"
        x1 = [0 for i in range(len(A))]
        count = 0
        disp = Tol + 1

        def calcularNuevoJacobi(x0):
            for i in range(len(A)):
                sum1 = 0
                for j in range(len(A)):
                    if j != i:
                        sum1 += A[i][j]*x0[j]
                x1[i] = (b[i] - sum1)/A[i][i]
            return x1

        def norma(x1,x0):
            result = 0
            for i, j in zip(x1,x0):
                result += (i-j)**2
            from math import sqrt
            return sqrt(result)

        while disp > Tol and count <= Nmax:
            x1 = calcularNuevoJacobi(x0)
            result = [f"{i:.10e}" for i in x0]
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            html+=f"{ite} {disp:.10e} {result}</br>"
            count += 1
            disp = norma(x1,x0)
            x0 = [i for i in x1]
        if disp < Tol:
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            result = [f"{i:.10e}" for i in x0]
            html+=f"{ite} {disp:.10e} {result}</br></br>"
            html+=f"x:</br>"
            for i in x0:
                html+=f"{i}</br>"

            return html
        else:
            html+=f"Fracaso en {Nmax} iteraciones</br>"
            return html

    def gaussSeidel(self,A,b,x0,Tol,Nmax):
        from math import sqrt
        import numpy as np

        html = "</br>Gauss-Seidel</br></br>Resultados:</br>"

        H = [[0 if i >= j else -A[i][j] for i in range(len(A))] for j in range(len(A))]
        T = [[0 if i < j else A[i][j] for i in range(len(A))] for j in range(len(A))]
        T = np.array(T)
        try:
            C = list((np.linalg.inv(T)).dot(np.array(b)))
        except:
            return html + "</br>La matriz C construida es singular, lo que implica el método se detenga</br>"

        try:
            T = list((np.linalg.inv(T)).dot(np.array(H)))
        except:
            return html + "</br>La matriz T construida es singular, lo que implica el método se detenga</br>"

        html += "</br>T:</br>"
        for i in T:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        html += "</br>C:</br>"
        for i in C:
            html += f"{i}</br>"

        val, ne =  np.linalg.eig(T) # T es la matriz
        sr = max(abs(val))
        html += f"</br>Radio espectral:</br>{sr}</br></br>"

        if sr < 1:
            html += f"El sistema converge a la solucion unica x=Tx + c ya que p(T) < 1</br></br>"
        else:
            html += f"El sistema no converge a la solucion unica x=Tx + c ya que p(T) >= 1</br></br>"

        if self.estrictamenteDiagonalDominante(A):
            html += f"La matriz es estrictamente diagonal dominante y por lo tanto converge para cualquier aproximacion inical x0</br></br>"
        else:
            html += f"La matriz no es estrictamente diagonal dominante y por lo tanto no converge para toda aproximacion inical x0</br></br>"

        html += f"|i|E|X|</br>"
        x1 = [0 for i in range(len(A))]
        count = 0
        disp = Tol + 1

        def calcularNuevoSeidel(x0):
            for i in range(len(A)):
                x1[i] = x0[i]
            for i in range(len(A)):
                sum1 = 0
                for j in range(len(A)):
                    if j != i:
                        sum1 += A[i][j]*x1[j]
                x1[i] = (b[i] - sum1)/A[i][i]
            return x1

        def norma(x1,x0):
            result = 0
            for i, j in zip(x1,x0):
                result += (i-j)**2
            return sqrt(result)

        while disp > Tol and count < Nmax:
            x1 = calcularNuevoSeidel(x0)
            result = [f"{i:.10e}" for i in x0]
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            html+=f"{ite} {disp:.10e} {result}</br>"
            disp = (norma(x1,x0))
            x0 = [i for i in x1]   
            count += 1
        if disp < Tol:
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            result = [f"{i:.10e}" for i in x0]
            html+=f"{ite} {disp:.10e} {result}</br></br>"
            html+=f"x:</br>"
            for i in x0:
                html+=f"{i}</br>"

            return html
        else:
            html+=f"Fracaso en {Nmax} iteraciones</br>"
            return html

    def sor(self,A,b,x0,Tol,w,Nmax):
        from math import sqrt
        import numpy as np
        html = "</br>SOR(relajacion)</br></br>Resultados:</br></br>"
        H = [[0 if i >= j else -A[i][j] for i in range(len(A))] for j in range(len(A))]
        T = [[0 if i < j else A[i][j] for i in range(len(A))] for j in range(len(A))]
        T = np.array(T)
        try:
            C = list((np.linalg.inv(T)).dot(np.array(b)))
        except:
            return html + "</br>La matriz C construida es singular, lo que implica el método se detenga</br>"

        try:
            T = list((np.linalg.inv(T)).dot(np.array(H)))
        except:
            return html + "</br>La matriz T construida es singular, lo que implica el método se detenga</br>"

        html += "</br>T:</br>"
        for i in T:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html+=result+"</br>"

        html += "</br>C:</br>"
        for i in C:
            html += f"{i}</br>"

        val, ne =  np.linalg.eig(T) # T es la matriz
        sr = max(abs(val))
        html += f"</br>Radio espectral:</br>{sr}</br></br>"

        if sr < 1:
            html += f"El sistema converge a la solucion unica x=Tx + c ya que p(T) < 1</br></br>"
        else:
            html += f"El sistema no converge a la solucion unica x=Tx + c ya que p(T) >= 1</br></br>"

        if self.estrictamenteDiagonalDominante(A):
            html += f"La matriz es estrictamente diagonal dominante y por lo tanto converge para cualquier aproximacion inical x0</br></br>"
        else:
            html += f"La matriz no es estrictamente diagonal dominante y por lo tanto no converge para toda aproximacion inical x0</br></br>"

        x1 = [0 for i in range(len(A))]
        count = 0
        disp = Tol + 1

        def calcularNuevoSor(x0):
            for i in range(len(A)):
                sum1 = 0
                for j in range(len(A)):
                    if j != i:
                        sum1 += A[i][j]*x1[j]
                x1[i] = ((1-w)*x0[i])+(w*(b[i] - sum1)/A[i][i])
            return x1

        def norma(x1,x0):
            result = 0
            for i, j in zip(x1,x0):
                result += (i-j)**2
            return sqrt(result)

        while disp > Tol and count < Nmax:
            x1 = calcularNuevoSor(x0)
            result = [f"{i:.10e}" for i in x0]
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            html+=f"{ite} {disp:.10e} {result}</br>"
            disp = (norma(x1,x0))
            x0 = [i for i in x1]    
            count += 1
            
        if disp < Tol:
            if count <= 9:
                ite = f"0{count}"
            else:
                ite = count
            result = [f"{i:.10e}" for i in x0]
            html+=f"{ite} {disp:.10e} {result}</br></br>"
            html+=f"x:</br>"
            for i in x0:
                html+=f"{i}</br>"

            return html
        else:
            html+=f"Fracaso en {Nmax} iteraciones</br>"
            return html

    def vandermonde(self,xs,ys):
        html = "</br>Vandermonde</br></br>Resultados:</br></br>"

        A = []
        b = ys

        html += "Matriz de Vandermonde:</br></br>"

        for i in xs:
            data = [(i)**k for k in range(len(xs))]
            data = data[::-1]
            result = ""
            for i in data:
                result += f"{float(i):.10e} "
            html += result+"</br>"
            A.append(data)
        
        Ab, marcas, b = self.eliminacionGaussianaConPivoteo(A, b, len(A),html,"")

        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html
        x = self.sustitucionRegresiva(Ab, len(A))
        infinit = False
        if type(x) ==  str:
            infinit = True    
            html += x
            x = self.infinitasSoluciones(Ab)
            html+="</br>En los datos ingresados hay dos valores x iguales, aproximaremos a un polinomio con la matriz generada</br>"
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            x = self.reordenar(x, marcas)

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"
            
            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0)
                html+=f"{result:.10f}</br>"
            
            for i in range(len(x)):
                fun = eval(f"lambda t:{x[i]}")
                result = fun(0)
                x[i] = result


        html += "</br>Coeficientes del polinomio:</br></br>"
        result = ""
        for i in x:
            result += f"{float(i):.10e}</br> "
        html+=result+"</br>"

        result = ""
        coef = len(x)
        for i in x:
            coef -= 1
            if coef != 0:
                if i >= 0.0:
                    result += "+"+str(i)+"*"+"x**"+str(coef)
                else:
                    result += str(i)+"*"+"x**"+str(coef)
            else:
                if i >= 0.0:
                    result += "+"+str(i)
                else:
                    result += str(i)

        if infinit:
            html += f"</br>Aproximación a un polinomio:</br></br>{result}</br>"
        else:
            html += f"</br>Polinomio:</br></br>{result}</br>"
        return html

    def interpolanteNewtonSin(self,xs,ys):
        p = []
        b = []

        result = str(ys[0])
        b.append(ys[0]) 
        p.append(eval("lambda x: "+result))
        b.append((ys[1]-b[0])/(xs[1]-xs[0]))
        result += f"+{b[1]}*(x-{xs[0]})"
        p.append(eval("lambda x: "+result))

        det = ""

        for n in range(2,len(ys)):
            fun = p[n-1]
            den = 1
            coef = ""
            for i in xs[:n]:
                den *= (xs[n]-i)
                coef += f"(x-{i})*"
            coef = coef[:len(coef)-1]
            if den == 0:
                det = f"</br>Para hayar el polinomio {n} es necesario resolver la ecuacion (y{n}-b{n-1})/{den} lo cual genera una division por cero y por tanto se suspende el metodo</br></br>"
                break
            b.append((ys[n] - fun(xs[n]))/den)
            result += f"+{b[n]}*{coef}"
            p.append(eval("lambda x: "+result))

        html = "</br>Interpolante Newton (sin diferencias divididas)</br></br>Resultados:</br></br>Coeficientes del polinomio:</br></br>"

        if det != "":
            html += det
            return html

        for i in b:
            html += f"{i}</br>"
        html += f"</br>Polinomio:</br></br>{result}</br>"

        return html

    def interpolanteNewton(self,xs,ys):
        table = [] 
        result = ""
        
        html = "</br>Interpolante de Newton</br></br>Resultados:</br>"

        det = ""

        for i in range(len(ys)):
            row = [xs[i], ys[i]]
            index = 1
            for j in range(2,i+2):
                if (xs[i-index] - xs[i]) == 0:
                    det = "</br>Se han ingresado dos puntos x iguales, esto genera que a la hora de buscar los polinomios exista una división por 0 y debido a esto el método no termina de ejecutarse</br>"
                    break
                row.append((table[i-1][j-1] - row[len(row)-1])
                            /
                            (xs[i-index] - xs[i]))
                index+=1
            if det != "":
                break
            table.append(row)

        if det != "":
            html += det
            return html

        html+="</br>Tabla de diferencias divididas:</br></br>"
        size = len(table)
        for i in table:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            for k in range(size):
                result+="------------------"
            size -= 1
            html+=result+"</br>"

        result = ""
        html+="</br>Coeficientes del polinomio:</br></br>"
        for i in range(len(ys)):
            html+=f"{table[i][i+1]}</br>"
        html+="</br>"
        for i in range(len(ys)):
            result += f"{table[i][i+1]}"
            for j in range(i):
                result += f"*(x - {xs[j]})"
            result += "+"

        result = result[:len(result)-1]

        html+=f"Polinomio:</br></br>{result}</br>" 

        return html

    def lagrange(self,xs,ys):
        b = []

        det = ""

        html="</br>Lagrange</br></br>Resultados:</br></br>Polinomios interpolantes:</br></br>"
        expresion = ""
        result = 1
        polim = "*"
        for i in xs:
            for k in xs:
                if xs.index(i) != xs.index(k): 
                    polim += (f"(x - {k})*")
                    result *= i - k  
            polim = polim[0:len(polim)-1]
            html+=f"{polim[1:]}</br>"
            if (xs[i-index] - xs[i]) == 0:
                det = "</br>se han ingresado dos puntos x iguales, esto genera que a la hora de buscar los polinomios exista una división por 0 y debido a esto el método no termina de ejecutarse</br>"
                break
            result = 1/result
            result = ys[xs.index(i)]*result
            b.append(result)
            expresion += "("+str(result)+polim+")"+"+"
            polim = "*"
            result = 1
        expresion = expresion[0:len(expresion)-1]

        if det != "":
            return html + det

        html+="</br>Coeficientes del polinomio:</br></br>"
        for i in b:
            html+=f"{i}</br>"
        html+="</br>Polinomio:</br></br>"
        html+=f"{expresion}"

        return html  

    def lineal(self,xs,ys):
        b = ys
        a, b = self.makeMatrix(xs,b,1)
        ab, marcas, d = self.eliminacionGaussianaConPivoteo(a, b, len(a),"","")
        x = self.sustitucionRegresiva(ab, len(ab))
        html="</br>Trazadores lineales</br>"
        if type(x) ==  str:    
            html += x
            x = self.infinitasSoluciones(ab)
            html+="</br>En los datos ingresados hay dos valores x iguales, aproximaremos unos trazadores con la matriz generada</br>"
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            x = self.reordenar(x, marcas)

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"
            
            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0)
                html+=f"{result:.10f}</br>"
            
            for i in range(len(x)):
                fun = eval(f"lambda t:{x[i]}")
                result = fun(0)
                x[i] = result
            
        html += "</br>Coeficientes del polinomio:</br></br>"

        result = ""
        index = 0
        for i in x:
            if index < 2:
                index += 1
                result += f"{i:.10e} "
            else:
                html+=result+"</br>"
                result = f"{i:.10e} "
                index = 1
        html+=result+"</br></br>"
        html=self.trazas(x,1,html)

        return html

    def square(self,xs,ys):
        b = ys
        a, b = self.makeMatrix(xs,b,2)
        ab, marcas, d = self.eliminacionGaussianaConPivoteo(a, b, len(a),"","")
        x = self.sustitucionRegresiva(ab, len(ab))
        html="</br>Trazadores cuadraticos</br>"
        if type(x) ==  str:    
            html += x
            x = self.infinitasSoluciones(ab)
            html+="</br>En los datos ingresados hay dos valores x iguales, aproximaremos unos trazadores con la matriz generada</br>"
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            x = self.reordenar(x, marcas)

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"
            
            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0)
                html+=f"{result:.10f}</br>"
            
            for i in range(len(x)):
                fun = eval(f"lambda t:{x[i]}")
                result = fun(0)
                x[i] = result
        
        html+= "</br></br>Coeficientes:</br></br>"
        result = ""
        index = 0
        for i in x:
            if index < 3:
                index += 1
                result += f"{i:.10e} "
            else:
                html+=result+"</br>"
                result = f"{i:.10e} "
                index = 1
        html+=result+"</br></br>"
        html=self.trazas(x,2,html)

        return html

    def cube(self,xs,ys):
        b = ys
        a, b = self.makeMatrix(xs,b,3)
        ab, marcas, d = self.eliminacionGaussianaConPivoteo(a, b, len(a),"","")
        x = self.sustitucionRegresiva(ab, len(ab))
        html="</br>Trazadores cubicos</br>"

        if type(x) ==  str:    
            html += x
            x = self.infinitasSoluciones(ab)
            html+="</br>En los datos ingresados hay dos valores x iguales, aproximaremos unos trazadores con la matriz generada</br>"
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            x = self.reordenar(x, marcas)

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"
            
            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0)
                html+=f"{result:.10f}</br>"
            
            for i in range(len(x)):
                fun = eval(f"lambda t:{x[i]}")
                result = fun(0)
                x[i] = result
        
        html+= "</br></br>Coeficientes:</br></br>"
        result = ""
        index = 0
        for i in x:
            if index < 4:
                index += 1
                result += f"{i:.10e} "
            else:
                html+=result+"</br>"
                result = f"{i:.10e} "
                index = 1
        html+=result+"</br></br>"
        html=self.trazas(x,3,html)

        return html

    def eliminacion(self, A, b, n, html):
        Ab, html_aux = self.formaMatrizAumentada(A,b)
        html += f"</br>{html_aux}</br>"
        html+="Resultados</br></br>"
        etapa = 0
        html+=f"Etapa {etapa}</br></br>"
        etapa += 1
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html += result+"</br>"
        for k in range(n-1):
            for i in range(k+1, n):
                if Ab[k][k] == 0.0:
                    html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                    return Ab, html
                multiplicador = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= (multiplicador * Ab[k][j])
            html+=f"</br>Etapa {etapa}</br></br>"
            for i in Ab:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html+=result+"</br>"
            etapa += 1
        return Ab, html

    def formaMatrizAumentada(self,A,b):
        import numpy as np
        n = len(A[0])
        det =  np.linalg.det(np.array(A))

        for i in A:
            if n != len(i):
                return A, "La matriz A presenta ecuaciones con más o menos incognitas que otras, por lo tango el sistema es inconsistente y no tiene solucion</br>"
        ranA = np.linalg.matrix_rank(np.matrix(A))
        for a, b in zip(A, b):
            a.append(b)
        ranAb =  np.linalg.matrix_rank(np.matrix(A))
        result = 'Utilizando el teorema de Rouché-Frobenius revisar en: <a href="https://es.wikipedia.org/wiki/Teorema_de_Rouch%C3%A9%E2%80%93Frobenius">teorema</a></br>'
        if ranA == ranAb and ranAb == n:
            result += "El rango de A es igual al rango de la matriz aumentada y el rango de A es igual al numero de incognitas, entonces el sistema es compatible determinado y por esto el sistema tiene solucion unica</br>"
        elif ranA == ranAb and ranAb < n:
            result += f"El rango de A es igual al rango de la matriz aumentada pero el rango de la matriz aumentada es menor al numero de incognitas, entonces el sistema es compatible indeterminado y por esto el sistema tiene infinitas soluciones, además el determinante de la matriz es {det:.5f} y por eso el método no converge</br>"
        else:
            result += "El rango de A es menor al rango de la matriz aumentada, entonces el sistema es incompatible y no tiene solucion</br>"
        return A, result

    def sustitucionProgresiva(self,Lb, n):
        x = [Lb[0][n] / Lb[0][0]]
        while len(x) < n:
            r = 0
            for i in range(len(x)):
                r += Lb[len(x)][i]*x[i]
            r = (Lb[len(x)][n] - r)/Lb[len(x)][len(x)]
            x.append(r)
        return x

    def sustitucionRegresiva(self,Ab, n):
        x = [0 for i in range(n)]
        if Ab[n-1][n-1] == 0:
            return f"</br>Al intentar hacer sustitucion regresiva, se genera una división por 0, lo que indica que el sistema tiene infinitas soluciones</br>" 
        x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
        for i in range(n-1, -1, -1):
            sumatoria = 0
            for p in range(i+1, n):
                sumatoria += Ab[i][p] * x[p]
            if Ab[i][i] == 0:
                return f"</br>Al intentar hacer sustitucion regresiva, se genera una división por 0, lo que indica que el sistema tiene infinitas soluciones</br>"    
            x[i] = (Ab[i][n] -  sumatoria)/Ab[i][i]
        return x

    def intercambioFilas(self,Ab, filaMayor, k):
        filaAux = Ab[k]
        Ab[k] = Ab[filaMayor]
        Ab[filaMayor] = filaAux
        return Ab

    def intercambioColumnas(self,Ab, columnaMayor, k):
        columAux = [Ab[i][k] for i in range(len(Ab))]
        for i in range(len(Ab)):
            Ab[i][k] = Ab[i][columnaMayor]
        for i in range(len(Ab)):
            Ab[i][columnaMayor] = columAux[i]
        return Ab

    def pivoteoParcial(self,Ab, n, k, lu=False):
        mayor = abs(Ab[k][k])
        filaMayor = k
        for s in range(k+1, n):
            if abs(Ab[s][k]) > mayor:
                mayor = abs(Ab[s][k])
                filaMayor = s
        if mayor == 0:
            return 0
        else:
            if filaMayor != k:
                Ab = self.intercambioFilas(Ab, filaMayor, k)
            if lu:
                return Ab, filaMayor
            return Ab

    def intercambioMarcas(self,marcas, columnaMayor, k):
        marcaAux = marcas[k]
        marcas[k] = marcas[columnaMayor]
        marcas[columnaMayor] = marcaAux
        return marcas

    def pivoteoTotal(self,Ab, n, k, marcas):
        mayor = 0
        filaMayor = k
        columnaMayor = k
        for r in range(k, n):
            for s in range(k, n):
                if abs(Ab[r][s]) > mayor:
                    mayor = abs(Ab[r][s])
                    filaMayor = r
                    columnaMayor = s
        if mayor == 0:
            return 0
        else:
            if filaMayor != k:
                Ab = self.intercambioFilas(Ab, filaMayor, k)
            if columnaMayor != k:
                Ab = self.intercambioColumnas(Ab, columnaMayor, k)
                marcas = self.intercambioMarcas(marcas, columnaMayor, k)
            return Ab, marcas

    def eliminacionGaussianaConPivoteo(self,A, b, n, html, pivoteo="parcial"):
        Ab, html_aux = self.formaMatrizAumentada(A, b)
        html += f"<br>{html_aux}</br>"
        if pivoteo == "parcial" or pivoteo == "parcialLU":
            if pivoteo == "parcial":
                etapa = 0
                html+="Resultados</br></br>"
                html+=f"Etapa {etapa}</br></br>"
                for i in A:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html += result+"</br>"
                etapa += 1
            else:
                etapa = None
            pivoteo = self.pivoteoParcial
            for k in range(n-1):
                Ab = pivoteo(Ab, n, k)
                for i in range(k + 1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return Ab, html
                    multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= multiplicador * Ab[k][j]
                if etapa:
                    html+=f"</br>Etapa {etapa}</br></br>"
                    for i in Ab:
                        result = ""
                        for j in i:
                            result += f"{j:.10e} "
                        html+=result+"</br>"
                    etapa += 1
            return Ab, html
        else:
            etapa = 0
            html+="Resultados</br></br>"
            html+=f"Etapa {etapa}</br></br>"
            for i in A:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html += result+"</br>"
            etapa += 1
            pivoteo = self.pivoteoTotal
            marcas = [i for i in range(n)]
            for k in range(n-1):
                Ab, marcas = pivoteo(Ab, n, k, marcas)
                for i in range(k + 1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return Ab, marcas, html
                    multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= multiplicador * Ab[k][j]
                html+=f"</br>Etapa {etapa}</br></br>"
                for i in Ab:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=result+"</br>"
                etapa += 1
            return Ab, marcas, html

    def reordenar(self,x, marcas):
        x_aux = [i for i in x]
        orden = [i for i in range(len(x))]
        for i, j in zip(marcas,orden):
            x[i] = x_aux[j]
        return x

    def factorizacionDirecta(self,A,etapa,html,me="cr"):
        L, U =  self.inicializaLU(len(A),1.0)
        for k in range(len(A)):
            sum1 = 0
            for p in range(k):
                sum1 += L[k][p]*U[p][k]
            if me == "do":
                U[k][k] = A[k][k] - sum1
            elif me == "cr":
                L[k][k] = A[k][k] - sum1
            else:
                try:
                    L[k][k] = math.sqrt(A[k][k] - sum1)
                    U[k][k] = math.sqrt(A[k][k] - sum1)
                except:
                    html+=f"El programa no soporta numeros imaginarios y el metodo lo requiere para este ejercicio</br>"
                    return L, U, html
            for i in range(k+1,len(A)):
                sum2 = 0
                for p in range(k):
                    sum2 += L[i][p]*U[p][k]
                if me == "do":
                    if U[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return L, U, html 
                    L[i][k] = (A[i][k] - sum2)/U[k][k]
                if me == "cr":
                    L[i][k] = A[i][k] - sum2
                else:
                    if U[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return L, U, html 
                    L[i][k] = (A[i][k] - sum2)/U[k][k]
            for j in range(k+1,len(A)):
                sum3 = 0
                for p in range(k):
                    sum3 += L[k][p]*U[p][j]
                if me == "do":
                    U[k][j] = A[k][j] - sum3
                if me == "cr":
                    if L[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return L, U, html         
                    U[k][j] = (A[k][j] - sum3)/L[k][k]
                else:
                    if L[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return L, U, html   
                    U[k][j] = (A[k][j] - sum3)/L[k][k]
            etapa += 1
            html += f"</br>Etapa {etapa}</br></br>L:</br>" 
            for i in L:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html += f"{result}</br>"
            html+="</br>U:</br>"
            for i in U:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html += f"{result}</br>"
            html += "</br>"
        return L, U, html

    def inicializaLU(self,n,val):
        L = [[0 for i in range(n)] for j in range(n)]
        U = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            L[i][i]  = val
            U[i][i]  = val
        return L, U

    def makeMatrix(self,x,b,meth):
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

    def trazas(self,x,method,html):
        html+="Trazas: </br></br>"
        result = ""
        if method == 1:
            for i in range(len(x)):
                if i % 2 == 0:
                    if x[i] >= 0.0:
                        result += "+"+str(x[i])+"*"+"x"
                    else:
                        result += str(x[i])+"*"+"x"
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
                        result += str(x[i])+"*"+"x**2"
                elif j == 1:
                    if x[i] >= 0.0:
                        result += "+"+str(x[i])+"*"+"x"
                    else:
                        result += str(x[i])+"*"+"x"
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
                        result += str(x[i])+"*"+"x**3"
                elif j == 1:
                    if x[i] >= 0.0:
                        result += "+"+str(x[i])+"*"+"x**2"
                    else:
                        result += str(x[i])+"*"+"x**2"
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
            html+=f"{i}</br>"
        return html

    def estrictamenteDiagonalDominante(self,A):
        import numpy as np

        X=np.array(A)

        Sum_values_in_given_row = np.sum(abs(X),axis=1)
        if np.all(((abs(np.diag(X)))) > np.sum(abs(X),axis=1)):
            return True
        else:
            return False
    
    def infinitasSoluciones(self,Ab):
        x = []
        x.append("t")
        for i in range(len(Ab)-2,-1,-1):
            result = f"{Ab[i][len(Ab)]}"
            index = len(Ab)-1
            for j in x:
                result += f"-{Ab[i][index]}*{j}"
                index -= 1
            result = f"({result})/{Ab[i][i]}"
            x.append(result)
        return x[::-1]



