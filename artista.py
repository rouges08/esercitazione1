class Artista:
    def __init__(self, nome, nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita
        self.brani = []

    def aggiungi_brano(self, brano):
        self.brani.append(brano)

    def numero_brani(self):
        return len(self.brani)

    def __str__(self):
        return f"{self.nome} ({self.nazionalita}), {self.numero_brani()} brani"