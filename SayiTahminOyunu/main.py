import time
import random

print("-*-*-*-*-*-*-*-*-*-**\n"
      "SAYI TAHMİN OYUNU\n\n"
      "1 ile 100 arasında tahminde bulunun...\n"
      "-*-*-*-*-*-*-*-*-*-*")

random_sayi = random.randint(1,100)
tahmin_hakki = 8

while True:
      tahmin = int(input("Lütfen Tahmininizi Giriniz:"))

      if(tahmin < random_sayi):
            print("Tahmin Doğrulanıyor...")
            time.sleep(0.6)
            print("Lütfen daha büyük sayi giriniz")
            tahmin_hakki-=1
      elif(tahmin > random_sayi):
            print("Tahmin Doğrulanıyor...")
            time.sleep(0.6)
            print("Lütfen daha küçük sayi giriniz...")
            tahmin_hakki -= 1
      else:
            print("Tahmin Doğrulanıyor...")
            time.sleep(0.6)
            print("Tebrikler Doğru Tahmin...")
            break

      if(tahmin_hakki == 0):
            print("Tahmin Hakkınız Bitmiştir...")
            print("Dogru tahmin ise şudur: ",random_sayi)
            break