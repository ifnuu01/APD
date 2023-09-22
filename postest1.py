print("Nama : Ifnu Umar")
print("NIM  : 2309106060")
print("Program konversi rupiah ke Dollar , Yen ,dan Euro")

def Konversi_dollar(rupiah):
    usd = 0.000065
    return rupiah * usd
def Konversi_yen(rupiah):
    yen = 0.0096
    return rupiah * yen 
def Konversi_euro(rupiah):
    euro = 0.00006
    return rupiah * euro


while True:
    try:
        rupiah = float(input("Masukan nominal Rupiah : "))
        print(f"Nominal yang anda masukan Rp {rupiah}")
        print()
        if rupiah > 0 :
            while True:
                konver = input("Pilih konversi yang di inginkan untuk Dollar,Yen dan Euro ketik (USD/YEN/EURO) : ").upper()
                if konver == "USD" or konver =="YEN" or konver =="EURO":
                    if konver == "USD":
                        dol = Konversi_dollar(rupiah)
                        print(f"Nilai hasil konversi dari Rupiah Rp {rupiah} ke Dollar menjadi {dol} US$")
                    elif konver == "YEN":
                        jep = Konversi_yen(rupiah)
                        print(f"Nilai hasil konversi dari Rupiah Rp {rupiah} ke Yen menjadi {jep} ¥")
                    elif konver == "EURO":
                        eur = Konversi_euro(rupiah)
                        print(f"Nilai hasil konversi dari Rupiah Rp {rupiah} ke Euro menjadi {eur} €")
                    konulang = input("Ingin mengkonversi yang lain ? (y/n) :").lower()
                    if konulang != "y":
                        break
                else:
                    print("Ketik salah satu huruf yang telah di tunjukan untuk mengkonversi rupiah. Coba lagi !!!")
            ulangi = input("Apakah Anda ingin mengulang program(y/n)? ").lower()
            if ulangi != "y":
                break
        else:
            print("Masukan nominal yang benar !!")
    except ValueError:
        print("Anda salah memasukan nominal !!")
