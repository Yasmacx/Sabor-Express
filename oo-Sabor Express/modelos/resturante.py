class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        # self = referencia + atributos obrigatorios
        #todo restaurante vai ser criado com as mesmas caract.
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #add objetos na lista

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
 

restaurante_praca = Restaurante('Bistro', 'Italiana') 
restaurante_pizza = Restaurante('Pizza Place', 'Fast food')
#com def init, precisa colocar as infos no () do restaurante


# dir = mostra as propoiedades dos objetos ou classe
# vars = mostra as caracteristicas colocadas pela gnt dos atributos da classe, em formato de dicionario
Restaurante.listar_restaurantes()
