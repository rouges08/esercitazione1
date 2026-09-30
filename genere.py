class Genere:
    def __init__(self, nome, descrizione=""):
        self.nome = nome
        self.descrizione = descrizione

    def __str__(self):
        return f"Genere: {self.nome}" + (f" - {self.descrizione}" if self.descrizione else "")