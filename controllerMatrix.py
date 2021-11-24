class ControllerMatrix:
#Luis Fernando Posada Cano
    def __init__(self, n=False, result=False):
        self.__n = n
        self.__result = result
    
    def setN(self,n):
        if n:
            self.__n = int(n)
        else:
            self.__n = n

    def getN(self):
        return self.__n

    def setResult(self,result):
        self.__result = result
    
    def getResult(self):
        return self.__result

    def makeMatrix(self,data):
        m = []
        for i in range(len(data)):
            print(str(i))
            m.append(data[str(i)].split())
        m = [list(map(float,i)) for i in m]
            
        return str(m)



