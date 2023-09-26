print("""
Nama : IFNU UMAR
Nim  : 2309106060

Program menghitung 20 input:
--- Jumlah Genap dan Ganjil dalam list
--- Mengurutkan angka dalam list
""")
def Inputuser():
    data_numerik =[]
    while len(data_numerik)< 20: 
        while True:
            try:
                data = int(input(f"Masukan angka random ke {len(data_numerik)+ 1}: "))
                if data > 0:
                    data_numerik.append(data)
                    break
                else:
                    print("Data yang di masukan harus bilangan bulat COBA LAGI !!")
            except ValueError:
                print("Data yang anda masukan tidak valdi!")

def TampilanData():
    print("Data yang telah anda input : ")
    print(data_numerik)
    
def GenapGanjil():
    Genap = []
    Ganjil = []
    for i in data_numerik:
        if i % 2 == 0:
            Genap.append(i)
        else:
            Ganjil.append(i)
    print("List angka genap : ")
    print(Genap)
    print(f"Maka jumlah angka genap : {len(Genap)}")
    print("List angka ganjil : ")
    print(Ganjil)
    print(f"Maka jumlah angka ganjil : {len(Ganjil)}")
    
def SortData():
    print("data yang di urutkan dari bilangan terkecil : ")
    data_numerik.sort()
    print(data_numerik)
    print("data yang di urutkan dari bilangan terbesar : ")
    data_numerik.sort(reverse = True)
    print(data_numerik)

while True:
    Inputuser()
    print()
    TampilanData()
    print()
    GenapGanjil()
    print()
    SortData()
    data_numerik.clear()
    ulangi = input("Ulangi program ? (y/n)").lower()
    if ulangi != "y":
        print("Program selesai")
        break
