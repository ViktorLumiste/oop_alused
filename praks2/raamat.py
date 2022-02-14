class Raamat():
    def __init__(self, pealkiri, autor, hind, reiting):
        self.pealkiri = pealkiri
        self.autor = autor
        self.hind = hind
        self.reiting = reiting
    def __repr__(self):
        return self.pealkiri