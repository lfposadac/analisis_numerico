from math import *
class ControllerNM:
#Luis Fernando Posada Cano
    def __init__(self, calculator, method=False, result=False):
        self.__method = method
        self.__result = result
        self.__calculator = calculator

    def setUp(self, data):
        from time import time
        self.__start_time = time()
        try:
            if self.getCategory() == 0:
                f = eval("lambda x:"+data['f'])
                x0 = eval(data['x0'])
                delta = eval(data['delta'])
                niter = eval(data['niter'])
                self.__html = self.__calculator.busquedasIncrementales(f,x0,delta,niter)

            elif self.getCategory() == 1:
                f = eval("lambda x:"+data['f'])
                xi = eval(data['xi'])
                xs = eval(data['xs'])
                tolerance = eval(data['tolerance'])
                niter = eval(data['niter'])
                if self.getMethod() == 'biseccion':
                    self.__html = self.__calculator.biseccion(f,xi,xs,tolerance,niter)
                elif self.getMethod() == 'regla falsa':
                    self.__html = self.__calculator.reglaFalsa(f,xi,xs,tolerance,niter)
                else:
                    print('melo')
                    self.__html = self.__calculator.secante(f,xi,xs,tolerance,niter)

            elif self.getCategory() == 2:
                f = eval("lambda x:"+data['f'])
                df = eval("lambda x:"+data['df'])
                tol = eval(data['tol'])
                x0 = eval(data['x0'])
                tol = eval(data['tol'])
                niter = eval(data['niter'])
                self.__html =  self.__calculator.newton(f,df,tol,x0,niter)
            
            elif self.getCategory() == 3:
                f = eval("lambda x:"+data['f'])
                g = eval("lambda x:"+data['g'])
                tole = eval(data['tole'])
                xa = eval(data['xa'])
                niter = eval(data['niter'])
                self.__html = self.__calculator.puntoFijo(f,g,tole,xa,niter)
            
            elif self.getCategory() == 4:
                f = eval("lambda x:"+data['f'])
                df = eval("lambda x:"+data['df'])
                df2 = eval("lambda x:"+data['df2'])
                tol = eval(data['tol'])
                x0 = eval(data['x0'])
                niter = eval(data['niter'])
                self.__html = self.__calculator.raicesMultiples(f,df,df2,tol,x0,niter)


            elif self.getCategory() == 5:
                A = eval(data['A'])
                b = self.tranfB(eval(data['b']))
                if len(A) != len(b):
                    self.__html = "</br>La matriz A y el arreglo b tienen diferentes tamaños  (n), por consiguiente no se pueden utilizar para ejecutar el método</br></b>"
                elif len(A[0]) != len(A):
                    self.__html = "</br>La matriz ingresada no es cuadrada y el metodo solo funciona con matrizes cuadradas</br>"
                else:
                    if self.getMethod() == 'eliminacion gaussiana simple':
                        self.__html = self.__calculator.eliminacionSimple(A,b)
                    elif self.getMethod() == 'eliminacion gaussiana con pivoteo parcial':
                        self.__html = self.__calculator.eliminacionParcial(A,b)
                    elif self.getMethod() == 'eliminacion gaussiana con pivoteo total':
                        self.__html = self.__calculator.eliminacionTotal(A,b)
                    elif self.getMethod() == 'lu simple':
                        self.__html = self.__calculator.luSimple(A,b)
                    elif self.getMethod() == 'lu parcial':
                        self.__html = self.__calculator.luParcial(A,b)
                    elif self.getMethod() == 'crout':
                        self.__html = self.__calculator.crout(A,b)
                    elif self.getMethod() == 'doolittle':
                        self.__html = self.__calculator.doolittle(A,b)
                    elif self.getMethod() == 'cholesky':
                        self.__html = self.__calculator.cholesky(A,b)
            
            elif self.getCategory() == 6:
                A = eval(data['A'])
                b = self.tranfB(eval(data['b']))
                x0 = self.tranfB(eval(data['x0']))
                tol = eval(data['Tol'])
                Nmax = eval(data['Nmax'])
                if len(A) != len(b):
                    self.__html = "</br>La matriz A y el arreglo b tienen diferentes tamaños  (n), por consiguiente no se pueden utilizar para ejecutar el método</br>"
                elif len(A[0]) != len(A):
                    self.__html = "</br>La matriz ingresada no es cuadrada y el metodo solo funciona con matrizes cuadradas</br>"
                else:
                    if self.getMethod() == 'jacobi':
                        self.__html = self.__calculator.jacobi(A,b,x0,tol,Nmax)
                    elif self.getMethod() == 'gauss seidel':
                        self.__html = self.__calculator.gaussSeidel(A,b,x0,tol,Nmax)

            elif self.getCategory() == 7:
                A = eval(data['A'])
                b = self.tranfB(eval(data['b']))
                x0 = self.tranfB(eval(data['x0']))
                if len(A) != len(b):
                    self.__html = "</br>La matriz A y el arreglo b tienen diferentes tamaños  (n), por consiguiente no se pueden utilizar para ejecutar el método</br>"
                elif len(A[0]) != len(A):
                    self.__html = "</br>La matriz ingresada no es cuadrada y el metodo solo funciona con matrizes cuadradas</br>"
                else:
                    tol = eval(data['Tol'])
                    w = eval(data['w'])
                    Nmax = eval(data['Nmax'])
                    self.__html = self.__calculator.sor(A,b,x0,tol,w,Nmax)
            
            elif self.getCategory() == 8:
                xs = self.tranfB(eval(data['xs']))
                ys = self.tranfB(eval(data['ys']))
                if len(xs) != len(xs):
                    self.__html = "</br>El tamaño de los datos de x es diferente al tamaño de los datos de y, por lo tanto no se puedenn utilizar estos datos para ejecutar el método</br>"
                else:
                    if self.getMethod() == 'vandermonde':
                        self.__html = self.__calculator.vandermonde(xs,ys)
                    elif self.getMethod() == 'interpolante de newton sin diferencias':
                        self.__html = self.__calculator.interpolanteNewtonSin(xs,ys)
                    elif self.getMethod() == 'interpolante de newton':
                        self.__html = self.__calculator.interpolanteNewton(xs,ys)
                    elif self.getMethod() == 'lagrange':
                        self.__html = self.__calculator.lagrange(xs,ys)
                    elif self.getMethod() == 'trazadores lineales':
                        self.__html = self.__calculator.lineal(xs,ys)
                    elif self.getMethod() == 'trazadores cuadraticos':
                        self.__html = self.__calculator.square(xs,ys)
                    elif self.getMethod() == 'trazadores cubicos':
                        self.__html = self.__calculator.cube(xs,ys)
        except Exception as e:
            self.__html = "</br>los datos ingresados son inapropiados o el sistema no tiene solución</br></br>"
            self.__html += f"El error generado es: {e}"

    def setMethod(self, method):
        if method:
            self.__method = method.lower().strip()
        else:
            self.__method = method

    def getMethod(self):
        return self.__method
    
    def setResult(self, result):
        self.__result = result
    
    def getResult(self):
        return self.__result
    
    def getCategory(self):
        if self.getMethod() == 'busquedas incrementales':
            return 0

        elif (self.getMethod() == 'biseccion' 
        or self.getMethod() == 'regla falsa'
        or self.getMethod() == 'secante'):
            return 1
        
        elif self.getMethod() == 'newton':
            return 2

        elif self.getMethod() == 'punto fijo':
            return 3

        elif self.getMethod() == 'raices multiples':
            return 4

        elif (self.getMethod() == 'eliminacion gaussiana simple' 
        or self.getMethod() == 'eliminacion gaussiana con pivoteo parcial'
        or self.getMethod() == 'eliminacion gaussiana con pivoteo total'
        or self.getMethod() == 'lu simple'
        or self.getMethod() == 'lu parcial'
        or self.getMethod() == 'crout'
        or self.getMethod() == 'doolittle'
        or self.getMethod() == 'cholesky'):
            return 5
        
        elif (self.getMethod() == 'jacobi'
        or self.getMethod() == 'gauss seidel'):
            return 6
        
        elif self.getMethod() == 'sor':
            return 7

        elif (self.getMethod() == 'vandermonde'
        or self.getMethod() == 'interpolante de newton sin diferencias'
        or self.getMethod() == 'interpolante de newton'
        or self.getMethod() == 'lagrange'
        or self.getMethod() == 'trazadores lineales'
        or self.getMethod() == 'trazadores cuadraticos'
        or self.getMethod() == 'trazadores cubicos'):
            return 8

    def getHtml(self):
        from time import time
        end_time = time() - self.__start_time
        return self.__html + f"</br>El tiempo de ejecución del metodo fue de: {end_time:.10f} segundos</br>"

    def tranfB(self,b):
        result = []
        if type(b[0]) == type([]):
            for i in b:
                result.append(i[0])
            return result
        else:
            return b




