import random

def oyunmn():
    while True:
        print("\033[1;32;40m")
        print("╔═════════════════════╗")
        print("║       OYUNLAR       ║")
        print("║                     ║")
        print("║  1-Yazı Tura        ║")
        print("║  2-Taş Kağıt Makas  ║")
        print("║  3-Çıkış            ║")
        print("║                     ║")
        print("║    Seçimiz nedir?   ║")
        print("╚═════════════════════╝")
        secim = input()

        if secim == "1":
            yazi_tura()
        elif secim == "2":
            tas_kagit_makas()
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

def yazi_tura():
    print("Yazı Tura Oyunu seçildi.")
    sonuc = random.choice(["Yazı", "Tura"])
    print(f"Sonuç: {sonuc}")

def tas_kagit_makas():
    print("Taş Kağıt Makas Oyunu seçildi.")
    secimler = ["Taş", "Kağıt", "Makas"]
    bilgisayar_secimi = random.choice(secimler)
    oyuncu_secimi = input("Seçiminizi yapın (Taş, Kağıt, Makas): ")

    if oyuncu_secimi not in secimler:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        return

    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
    print(f"Sizin seçiminiz: {oyuncu_secimi}")

    if bilgisayar_secimi == oyuncu_secimi:
        print("Berabere!")
    elif (bilgisayar_secimi == "Taş" and oyuncu_secimi == "Makas") or \
         (bilgisayar_secimi == "Kağıt" and oyuncu_secimi == "Taş") or \
         (bilgisayar_secimi == "Makas" and oyuncu_secimi == "Kağıt"):
        print("Bilgisayar kazandı!")
    else:
        print("Siz kazandınız!")