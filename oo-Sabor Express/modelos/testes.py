class musica:
    nome = ''
    artista = ''
    duracao = int #numero

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = musica('Bohemian Rhapsody','Queen', 355)

musica2 = musica('Imagine', 'John Lennon', 183)

musica3 = musica('Shape of You','Ed Sheeran', 234 )

print(musica1)