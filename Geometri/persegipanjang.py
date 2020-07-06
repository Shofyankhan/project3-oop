from Geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        #its first time called function
        self.p = p
        self.l = l
    def info(self):
        return f'object persegi panjang, dengan panjang {self.p} dan juga lebar {self.l}'

    def hitung_luas(self, ):
        return self.p * self.l