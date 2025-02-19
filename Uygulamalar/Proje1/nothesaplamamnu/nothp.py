def harf_notu_hesapla(ortalama):
    if ortalama >= 90: return 'AA'
    if ortalama >= 85: return 'BA'
    if ortalama >= 80: return 'BB'
    if ortalama >= 75: return 'CB'
    if ortalama >= 70: return 'CC'
    if ortalama >= 65: return 'DC'
    if ortalama >= 60: return 'DD'
    return 'FF'

def not_hesapla():
    notlar = []
    while (not_degeri := input("Not değerini girin (çıkmak için 'q' yazın): ")) != 'q':
        try:
            not_degeri = float(not_degeri)
            if 0 <= not_degeri <= 100:
                notlar.append(not_degeri)
            else:
                print("Lütfen 0 ile 100 arasında bir not girin.")
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")
    
    if not notlar:
        print("Not girmediniz.")
    else:
        ortalama = sum(notlar) / len(notlar)
        print(f"Not Ortalamanız: {ortalama:.2f}\nHarf Notunuz: {harf_notu_hesapla(ortalama)}")

# Programı çalıştır
not_hesapla()
