class Customer:
    def __init__(self, name, age, total_purchase):
        self.name = name
        self.age = age
        self.total_purchase = total_purchase
        self.discount = 0

    def calculate_discount(self):
        if self.age >= 60 and self.total_purchase >= 120000:
            self.discount = 0.5
        elif self.age >= 50 and self.total_purchase >= 100000:
            self.discount = 0.35
        elif self.age >= 40 and self.total_purchase >= 70000:
            self.discount = 0.2

    def display_discount(self):
        print(f"{self.name} mendapatkan diskon sebesar {self.discount * 100}%")
        print(f"{self.name} maka harga yang harus di bayar adalah Rp {self.total_purchase -(self.discount * self.total_purchase)}")


num_customers = int(input("Masukkan jumlah pelanggan yang belanja: "))
customers = []

if num_customers >= 5:
    for i in range(num_customers):
        print(f"Data pelanggan ke-{i + 1}:")
        name = input("Nama pelanggan: ")
        age = int(input("Umur ibu pelanggan: "))
        total_purchase = float(input("Total harga belanjaan (Rp): "))
        customer = Customer(name, age, total_purchase)
        customer.calculate_discount()
        customer.display_discount()
else:
    print("Maaf, tidak ada diskon karena jumlah pelanggan kurang dari 5")
