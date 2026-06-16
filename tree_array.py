# tree_array.py

from models import Product

class TreeNode:
    """
    Representasi node pada Binary Search Tree.
    Setiap node menyimpan objek Product dan referensi ke anak kiri/kanan.
    """
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class PriceBST:
    """
    Struktur data Binary Search Tree khusus untuk mengindeks harga produk.
    Kiri: Harga lebih murah. Kanan: Harga lebih mahal atau sama.
    """
    def __init__(self):
        self.root = None

    def insert(self, product):
        """Memasukkan produk ke dalam BST berdasarkan harga."""
        if not self.root:
            self.root = TreeNode(product)
        else:
            self._insert_recursive(self.root, product)

    def _insert_recursive(self, node, product):
        # Jika harga lebih murah, masukkan ke sub-tree kiri
        if product.harga < node.product.harga:
            if node.left is None:
                node.left = TreeNode(product)
            else:
                self._insert_recursive(node.left, product)
        # Jika harga lebih mahal atau SAMA, masukkan ke sub-tree kanan
        else:
            if node.right is None:
                node.right = TreeNode(product)
            else:
                self._insert_recursive(node.right, product)

    def search_by_price_range(self, min_price, max_price):
        """
        Mencari produk dalam rentang harga menggunakan In-Order Traversal.
        Mengembalikan list berisi produk yang terurut dari harga termurah.
        """
        result = []
        self._range_search_recursive(self.root, min_price, max_price, result)
        return result

    def _range_search_recursive(self, node, min_price, max_price, result):
        if node is None:
            return

        # OPTIMASI: Hanya telusuri cabang kiri jika harga minimal masih lebih kecil 
        # dari harga node saat ini (memotong cabang yang tidak relevan)
        if min_price < node.product.harga:
            self._range_search_recursive(node.left, min_price, max_price, result)

        # IN-ORDER TRAVERSAL: Proses node saat ini jika masuk dalam rentang harga
        if min_price <= node.product.harga <= max_price:
            result.append(node.product)

        # OPTIMASI: Hanya telusuri cabang kanan jika harga maksimal masih lebih besar 
        # dari harga node saat ini
        if max_price >= node.product.harga:
            self._range_search_recursive(node.right, min_price, max_price, result)


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
if __name__ == "__main__":
    # 1. Inisiasi Database
    db = ProductDatabase()
    
    print("=== KATALOG UTAMA (ARRAY LIST) ===")
    for prod in db.get_all_products():
        print(prod)

    print("\n=== HASIL FILTER HARGA (BST IN-ORDER TRAVERSAL) ===")
    # Mencari produk dengan harga Rp 50.000 sampai Rp 150.000
    hasil_filter = db.filter_by_price(50000, 150000)
    
    if hasil_filter:
        for prod in hasil_filter:
            print(prod)
    else:
        print("Tidak ada produk di rentang harga tersebut.")