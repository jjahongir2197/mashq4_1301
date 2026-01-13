class Buyurtma:
    def __init__(self, mijoz):
        self.mijoz = mijoz
        self.mahsulotlar = []
        self.holat = "Yangi"

    def mahsulot_qoshish(self, nom, narx):
        self.mahsulotlar.append((nom, narx))

    def umumiy_summa(self):
        summa = 0
        for mahsulot in self.mahsulotlar:
            summa += mahsulot[1]
        return summa

    def tasdiqlash(self):
        if len(self.mahsulotlar) > 0:
            self.holat = "Tasdiqlandi"
        else:
            print("Buyurtma bo‘sh!")

    def malumot(self):
        print("Mijoz:", self.mijoz)
        print("Holat:", self.holat)
        print("Mahsulotlar:")
        for m in self.mahsulotlar:
            print("-", m[0], m[1], "so‘m")
        print("Jami:", self.umumiy_summa(), "so‘m")


buyurtma = Buyurtma("Dilshod")
buyurtma.mahsulot_qoshish("Telefon", 2500000)
buyurtma.mahsulot_qoshish("Quloqchin", 200000)
buyurtma.tasdiqlash()
buyurtma.malumot()
