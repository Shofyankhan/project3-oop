from Geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        #its first time called function
        self.alas = alas
        self.tinggi = tinggi
    def info(self):
        return f'object Segitiga, dengan alas {self.alas} dan juga tinggi {self.tinggi}'

    def hitung_luas(self, ):
        return self.alas * self.tinggi