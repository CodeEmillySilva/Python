class Ponto2D:
    def __init__ (self, numx, numy):
        self.numx=numx
        self.numy=numy

    def mostrarNumx(self):
        return self.numx
    
    def mudarNumx(self, novoNumx):
        self.numx=novoNumx

    def mostrarNumy(self):
        return self.numy
    
    def mudarNumy(self, novoNumy):
        self.numy=novoNumy


    def __str__(self):
        return "Ponto: (" + str(self.numx) + "," + str(self.numy) + ")" + "\n"
