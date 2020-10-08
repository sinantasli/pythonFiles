
class Dosya():

    def __init__(self):

        with open("C:/Users/stasl/OneDrive/Masaüstü/metin.txt","r",encoding="utf-8") as file:

            dosyanın_icerigi=file.read()

            kelimeler=dosyanın_icerigi.split()

            self.sade_kelimeler=list()

            for i in kelimeler:

                i=i.strip()

                i=i.strip(".")

                i=i.strip("\n")

                self.sade_kelimeler.append(i)
    def tum_kelimeler(self):

        kelimeler=set()

        for i in self.sade_kelimeler:

            kelimeler.add(i)
        for i in kelimeler:
            print(i)
            print("*************************************")

    def kelime_frekansi(self):

        kelime_sözlük=dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sözlük):
                kelime_sözlük[i] +=1
            else:
                kelime_sözlük[i] =1
        for kelime ,sayi in kelime_sözlük.items():
            print(" {} kelimesi  {}  defa kullanılmış ".format(kelime,sayi))
            print("-------------------------------")

dosya=Dosya()
dosya.kelime_frekansi()