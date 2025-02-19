import  hesapm.hesapmakinesi
import  oyunlar.oyun
import  nothesaplamamnu.nothp

def anamenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═══════════════════════╗")
    print("║     Uygulamalar       ║")
    print("║                       ║")
    print("║  1-Hesap makinesi     ║")
    print("║  2-Oyunlar            ║")
    print("║  3-Alan Hesaplama     ║")
    print("║  4-Not Hesaplama      ║")
    print("║  5-Çarpım Tablosu     ║")
    print("║  6-....               ║")
    print("║  7-Çıkış              ║")
    print("║                       ║")
    print("║    Seçimiz nedir?     ║")
    print("╚═══════════════════════╝")
    secim = input()
    if secim == "1" :
        hesapm.hesapmakinesi.hmmenu()
        anamenu()
    if secim == "2" :
        oyunlar.oyun.oyunmn()
        anamenu()
    if secim == "3" :
        ()
        anamenu()
    if secim == "4" :
        nothesaplamamnu.nothp.not_hesapla()
        anamenu()
    else:
        anamenu()
    # 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚
    # 188 ╝


anamenu()
