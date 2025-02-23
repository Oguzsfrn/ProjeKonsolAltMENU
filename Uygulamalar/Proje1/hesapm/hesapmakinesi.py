def toplama():
    print("Toplama işlemi seçildi.")
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a + b}")

def cikarma():
    print("Çıkarma işlemi seçildi.")
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a - b}")

def carpma():
    print("Çarpma işlemi seçildi.")
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    print(f"Sonuç: {a * b}")

def bolme():
    print("Bölme işlemi seçildi.")
    a = float(input("Birinci sayıyı girin: "))
    b = float(input("İkinci sayıyı girin: "))
    if b != 0:
        print(f"Sonuç: {a / b}")
    else:
        print("Hata: Bir sayı sıfıra bölünemez.")

def hmmenu():
    while True:
        print("\033[1;32;40m")
        print("╔═════════════════════╗")
        print("║   HESAP MAKİNESİ    ║")
        print("║                     ║")
        print("║  1-Toplama          ║")
        print("║  2-Çıkarma          ║")
        print("║  3-Çarpma           ║")
        print("║  4-Bölme            ║")
        print("║  5-Çıkış            ║")
        print("║                     ║")
        print("║    Seçimiz nedir?   ║")
        print("╚═════════════════════╝")
        secim = input()

        if secim == "1":
            toplama()
        elif secim == "2":
            cikarma()
        elif secim == "3":
            carpma()
        elif secim == "4":
            bolme()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

hmmenu()