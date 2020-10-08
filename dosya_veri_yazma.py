import time

with open ("C:/Users/stasl/OneDrive/Masaüstü/yeni.txt","r+" ,encoding="utf-8") as file :
    girilen = input("Veriyi giriniz .")
    içerik = "{}\n".format(girilen)
    file.write(içerik)
    file.seek(0)
    time.sleep(2)
    print("veri yazıldı.")


