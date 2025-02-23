import calendar

def takvim_goster():
    print("Takvim Uygulaması seçildi.")
    yil = int(input("Yılı girin: "))
    ay = int(input("Ayı girin (1-12): "))

    if 1 <= ay <= 12:
        print(calendar.month(yil, ay))
    else:
        print("Geçersiz ay, lütfen tekrar deneyin.")