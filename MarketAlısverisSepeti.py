class Market:
    def __init__(self):
        try:
            # product.txt dosyasını açmayı deneriz, yoksa oluştururuz
            self.filename = "product.txt"
            self.file = open(self.filename, "a+")
        except IOError:
            print("Dosya açılamadı!")
            self.file = None
        else:
            print("Market sistemi başlatıldı.")

    def __del__(self):
        if self.file:
            self.file.close()
            print("Dosya kapatıldı.")
    def list_product(self):
        try:
            with open(self.filename, "r") as file:
                products = file.readlines()
                if products:
                    print("Ürünler Listeleniyor:")
                    for product in products:
                        name, category, price, stock = product.strip().split(",")
                        print(f"Ad: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")
                else:
                    print("Ürün bulunmamaktadır.")
        except FileNotFoundError:
            print("Ürün verisi bulunamadı. Lütfen dosyanın varlığını kontrol edin.")

    def add_product(self):
        name = input("Ürün adı: ")
        category = input("Kategori: ")
        price = input("Fiyat: ")
        stock = input("Stok miktarı: ")

        with open(self.filename, "a") as file:
            file.write(f"{name},{category},{price},{stock}\n")
        print("Ürün başarıyla eklendi.")

    def delete_product(self):
        product_to_delete = input("Silmek istediğiniz ürün adını girin: ")

        with open(self.filename, "r") as file:
            lines = file.readlines()

        with open(self.filename, "w") as file:
            found = False
            for line in lines:
                if product_to_delete not in line:
                    file.write(line)
                else:
                    found = True
            if found:
                print("Ürün başarıyla silindi.")
            else:
                print("Ürün bulunamadı.")


def main():
    market = Market()

    while True:
        print("\n--- Market Menü ---")
        print("1. Ürünleri Listele")
        print("2. Ürün Ekle")
        print("3. Ürün Sil")
        print("4. Çıkış")

        choice = input("Bir seçenek girin (1/2/3/4): ")

        if choice == '1':
            market.list_product()
        elif choice == '2':
            market.add_product()
        elif choice == '3':
            market.delete_product()
        elif choice == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.")

    del market  # Market nesnesi yıkıcı metot ile dosyayı kapatacaktır.


if __name__ == "__main__":
    main()
