class Brano:
    def __init__(self, titolo, autore, durata):
        self._titolo = titolo
        self._autore = autore
        self._durata = durata  # in secondi

    def get_titolo(self):
        return self._titolo

    def set_titolo(self, titolo):
        self._titolo = titolo

    def get_autore(self):
        return self._autore

    def set_autore(self, autore):
        self._autore = autore

    def get_durata(self):
        return self._durata

    def set_durata(self, durata):
        self._durata = durata

    def short_song(self):
        """Un brano è 'corto' se dura meno di 3 minuti."""
        return self._durata < 180

    def __str__(self):
        minuti, secondi = divmod(self._durata, 60)
        return f"{self._titolo} - {self._autore} ({minuti}:{secondi:02d})"