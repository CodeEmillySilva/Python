class Reta:
    def __init__(self, numa, numb):
        self.numa=numa
        self.numb=numb
    
    def mostrarNuma(self):
        return self.numa
    
    def mudarNuma(self, novoNuma):
        self.numa=novoNuma

    def mostrarNumb(self):
        return self.numb
    
    def mudarNumb(self, novoNumb):
        self.numb=novoNumb

    def intercepta(self, stra):

        denominador = self.numa-stra.mostrarNuma()

        if (denominador==0):
            return False
        else:
            return True

    def estaNaReta(self, point):

        verificacao = (self.mostrarNuma()*point.mostrarNumx())+self.mostrarNumb()

        if(verificacao==point.mostrarNumy()):
            return True
        else:
            return False
        
    def __str__(self):
        return "y = " + str(self.mostrarNuma()) + "x + " + str(self.mostrarNumb()) + "\n"
