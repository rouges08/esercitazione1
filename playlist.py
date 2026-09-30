class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.brani = []

    def aggiungi(self, brano):
        self.brani.append(brano)

    def rimuovi(self, titolo):
        self.brani = [b for b in self.brani if b.get_titolo() != titolo]

    def brani_corti(self):
        return [b for b in self.brani if b.short_song()]

    def durata_totale(self):
        return sum(b.get_durata() for b in self.brani)

    def __str__(self):
        return f"Playlist '{self.nome}': {len(self.brani)} brani"