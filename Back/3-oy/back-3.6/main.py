class Texnika:
    def __init__(self, nomi, narxi, rangi):
        self.nomi = nomi
        self.narxi = narxi
        self.rangi = rangi
    
class Avtomobil(Texnika):
    def __init__(self, nomi, narxi, rangi, matori, max_speed):
        super().__init__(nomi, narxi, rangi, )
        self.matori = matori
        self.max_speed = max_speed


