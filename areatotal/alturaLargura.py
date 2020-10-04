class AlturaLargura(): 
    def __init__(self, altura, largura): 
        self.altura = altura 
        self.largura = largura 
        self.total = altura*largura
        
    def __str__(self):
        return f"Altura: {self.altura} - Largura: {self.largura} - Area Total: {self.total}"
    
    def setAltura(self, altura): 
        self.altura = altura 
    
    def setLargura(self, largura): 
        self.largura = largura 
    
    def getAltura(self): 
        return self.altura 
        
    def getLargura(self): 
        return self.largura

    def getTotal(self): 
        return self.total

    def calculaTotal(self):
        self.total = self.altura*self.largura

     

   