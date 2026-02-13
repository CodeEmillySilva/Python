from ObjetoSobrepostoException import ObjetoSobrepostoException

class EspacoGeometrico:
    def __init__(self):
        self.stra=[]
        self.point=[]

    def adicionarReta(self,reta):

        for cada in self.stra:
            if (reta.intercepta(cada)):
                raise ObjetoSobrepostoException()
            
        self.stra.append(reta)


    def adicionarPonto(self,ponto):
            
        for cada in self.stra:
            if (cada.estaNaReta(ponto)):
                raise ObjetoSobrepostoException()
            
        self.point.append(ponto)
    
    def __str__(self):

        apanhado = "Retas que existem no espaço:\n"

        for reta in self.stra:
            apanhado = apanhado + "- " + str(reta) + "\n"

        apanhado = apanhado + "Pontos que existem no espaço:\n"

        for ponto2D in self.point:
            apanhado = apanhado + "- " + str(ponto2D) + "\n"

        return apanhado
