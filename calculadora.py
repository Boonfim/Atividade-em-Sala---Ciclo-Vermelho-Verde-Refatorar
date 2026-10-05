class Produto:
    def __init__(self, preco_base):
        self.preco_base = preco_base
        
    # preco final 
    def preco_final(self):
        return self.preco_base + self.calcular_imposto() - self.calcular_desconto()
    
    def calcular_imposto(self):
        pass
    
    def calcular_desconto(self):
        pass
    

# classes filhas
class Livro(Produto):
    def calcular_imposto(self):
        return self.preco_base * 0.00

    def calcular_desconto(self):
        return self.preco_base * 0.10
    
class Eletronico(Produto):
    def calcular_imposto(self):
        return self.preco_base * 0.20

    def calcular_desconto(self):
        return self.preco_base * 0.05
    
class Alimento(Produto):
    def calcular_imposto(self):
        return self.preco_base * 0.05

    def calcular_desconto(self):
        return self.preco_base * 0.00
        
        

def calcular_preco_final(preco_base, categoria):
    if categoria == "Livro":
        produto = Livro(preco_base)
    elif categoria == "Eletrônico":
        produto = Eletronico(preco_base)
    elif categoria == "Alimento":
        produto = Alimento(preco_base)
    else:
        raise ValueError("Categoria inválida")
    
    return produto.preco_final()