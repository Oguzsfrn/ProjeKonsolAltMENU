def alan_hesapla():
    print("Alan Hesaplama seçildi.")
    print("1. Kare")
    print("2. Dikdörtgen")
    print("3. Üçgen")
    print("4. Daire")
    secim = input("Hangi şeklin alanını hesaplamak istersiniz? (1-4): ")

    if secim == "1":
        kenar = float(input("Karenin bir kenar uzunluğunu girin: "))
        print(f"Karenin alanı: {kenar * kenar}")
    elif secim == "2":
        uzunluk = float(input("Dikdörtgenin uzunluğunu girin: "))
        genislik = float(input("Dikdörtgenin genişliğini girin: "))
        print(f"Dikdörtgenin alanı: {uzunluk * genislik}")
    elif secim == "3":
        taban = float(input("Üçgenin taban uzunluğunu girin: "))
        yukseklik = float(input("Üçgenin yüksekliğini girin: "))
        print(f"Üçgenin alanı: {0.5 * taban * yukseklik}")
    elif secim == "4":
        yaricap = float(input("Dairenin yarıçapını girin: "))
        print(f"Dairenin alanı: {3.14 * yaricap * yaricap}")
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")