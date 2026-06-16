from models import Product
from features.tree import PriceBST

class ProductDatabase:
    """
    ArrayList (List bawaan Python) yang bertindak sebagai database utama.
    Mengelola katalog produk dan menginisiasi indeks BST secara otomatis.
    """
    def __init__(self):
        self.catalog = []          # ArrayList penyimpanan data utama
        self.price_index = PriceBST() # Indeks BST untuk filter harga
        self._initialize_mock_data()

    def _initialize_mock_data(self):
        """Mengisi ArrayList dengan Mock Data agar program langsung bisa didemokan."""
        mock_data = [
            Product("P001", "Kemeja Flanel Shopee Brand", 150000, 4.8),
            Product("P002", "Sepatu Sneakers Running", 320000, 4.5),
            Product("P003", "Tas Ransel Waterproof", 850000, 4.9),
            Product("P004", "Kaos Polos Cotton Combed", 50000, 4.2),
            Product("P005", "Jam Tangan Digital Pria", 125000, 4.6),
            Product("P006", "Kacamata Hitam Anti UV", 75000, 4.3),
            Product("P007", "Topi Baseball Distro", 45000, 4.1),
            Product("P008", "Jaket Hoodie Polos", 200000, 4.7),
            Product("P009", "Dompet Kulit Sintetis", 90000, 4.4),
            Product("P010", "Ikat Pinggang Kanvas", 35000, 4.0),
        ]

        # Simpan ke ArrayList dan Index ke BST secara bersamaan
        for p in mock_data:
            self.catalog.append(p)
            self.price_index.insert(p)

    def get_all_products(self):
        """Mengembalikan seluruh katalog (digunakan oleh Wafi untuk ditampilkan)."""
        return self.catalog

    def filter_by_price(self, min_price, max_price):
        """Endpoint untuk mengambil produk berdasarkan rentang harga via BST."""
        return self.price_index.search_by_price_range(min_price, max_price)

# ==========================================
# BLOK PENGUJIAN MANDIRI (UNIT TEST LOKAL)
# ==========================================
def print_table(judul, data_list):
    """
    Fungsi helper untuk mencetak tabel dengan gaya UI Terminal Modern.
    """
    # Menghitung total lebar ruang di dalam bingkai (67 karakter)
    lebar_dalam = 8 + 32 + 15 + 9 + 3 
    
    # Karakter Unicode Box Drawing
    garis_judul_atas = "╔" + "═" * lebar_dalam + "╗"
    garis_judul_bawah= "╠" + "═"*8 + "╦" + "═"*32 + "╦" + "═"*15 + "╦" + "═"*9 + "╣"
    garis_tengah     = "╠" + "═"*8 + "╬" + "═"*32 + "╬" + "═"*15 + "╬" + "═"*9 + "╣"
    garis_bawah      = "╚" + "═"*8 + "╩" + "═"*32 + "╩" + "═"*15 + "╩" + "═"*9 + "╝"
    
    # 1. Mencetak Judul yang Terbingkai
    print(f"\n{garis_judul_atas}")
    print(f"║{judul:^{lebar_dalam}}║") # Judul otomatis rata tengah
    print(garis_judul_bawah)
    
    # 2. Mencetak Header Kolom (menggunakan rata tengah '^' agar rapi)
    print(f"║ {'ID':^6} │ {'Nama Produk':^30} │ {'Harga':^13} │ {'Rating':^7} ║")
    print(garis_tengah)
    
    # 3. Mencetak Isi Data
    if not data_list:
        print(f"║{'Data tidak ditemukan di rentang harga tersebut.':^{lebar_dalam}}║")
    else:
        for item in data_list:
            print(item) # Memanggil format ║ ... │ ... ║ dari models.py
            
    # 4. Mencetak Footer Tabel
    print(garis_bawah)

if __name__ == "__main__":
    # 1. Inisiasi Database
    db = ProductDatabase()
    
    # 2. Menampilkan semua produk (Array List)
    semua_produk = db.get_all_products()
    print_table("KATALOG UTAMA (ARRAY LIST)", semua_produk)

    # 3. Menampilkan hasil filter (BST)
    hasil_filter = db.filter_by_price(50000, 150000)
    print_table("HASIL FILTER HARGA: Rp50.000 - Rp150.000 (BST IN-ORDER)", hasil_filter)