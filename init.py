class Product:
    def __init__(self, name, code, quant, value):
        self.name = name
        self.code = code
        self.quant = quant
        self.value = value
        self.list = [name, code, quant, value]
    def visualize(self):
        print(self.list)

def addProd():
    products = []
    i = "s"
    while i == "s":
        name = input("Digite o nome do produto: ")
        code = input("Digite o código do produto: ")
        quant = input("Digite a Quantidade em estoque: ")
        value = input("Digite o valor em real do Produto: ")
        object = [name, code, quant, value]
        
        print(object)
        i = input("Continuar s/n? ")
    
    
addProd()