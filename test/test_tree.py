import unittest
from unittest.mock import MagicMock
import sys
import os

# Memastikan Python mendeteksi folder root proyek 'UAS_StrukturData'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import komponen yang diuji secara mutlak dari package features
from features.tree import PriceBST, TreeNode

class TestPriceBST(unittest.TestCase):

    def setUp(self):
        """
        Mempersiapkan instance BST dan mock product dengan variasi harga 
        untuk menguji struktur pohon secara presisi.
        """
        self.bst = PriceBST()
        
        # Membuat tiruan produk (hanya menyuplai atribut 'harga' sesuai kebutuhan tree.py)
        self.p_root = MagicMock()
        self.p_root.harga = 100000  # Nilai tengah sebagai Root
        
        self.p_kiri = MagicMock()
        self.p_kiri.harga = 50000   # Lebih murah dari root (<)
        
        self.p_kanan = MagicMock()
        self.p_kanan.harga = 200000  # Lebih mahal dari root (>=)
        
        self.p_sama = MagicMock()
        self.p_sama.harga = 100000   # Nilai SAMA dengan root (uji kondisi >=)
        
        self.p_dalam_range = MagicMock()
        self.p_dalam_range.harga = 150000 # Untuk uji filter rentang sempit

    def test_initialization(self):
        """
        LOGIC TEST: Memastikan saat objek PriceBST pertama kali dibuat,
        properti root bernilai None (pohon kosong).
        """
        self.assertIsNone(self.bst.root)

    def test_insert_logic_structure(self):
        """
        LOGIC TEST: Menguji kebenaran algoritma insertion rekursif.
        Memastikan penempatan cabang kiri (<) dan kanan (>=) berjalan mutlak sesuai aturan kode.
        """
        # 1. Insert produk pertama -> Harus bertindak sebagai Root
        self.bst.insert(self.p_root)
        self.assertEqual(self.bst.root.product, self.p_root)
        
        # 2. Insert produk lebih murah -> Harus masuk ke Sub-tree Kiri dari Root
        self.bst.insert(self.p_kiri)
        self.assertEqual(self.bst.root.left.product, self.p_kiri)
        
        # 3. Insert produk lebih mahal -> Harus masuk ke Sub-tree Kanan dari Root
        self.bst.insert(self.p_kanan)
        self.assertEqual(self.bst.root.right.product, self.p_kanan)
        
        # 4. Insert produk dengan harga SAMA -> Sesuai logika 'else', harus masuk ke Kanan.
        # Karena root.right sudah terisi oleh p_kanan (200k), dan 100k < 200k,
        # maka p_sama harus berada di root.right.left (Kiri dari si p_kanan).
        self.bst.insert(self.p_sama)
        self.assertEqual(self.bst.root.right.left.product, self.p_sama)

    def test_search_by_price_range_all(self):
        """
        LOGIC TEST: Menguji apakah fungsi range search mengembalikan seluruh data
        secara berurutan (In-Order) dari termurah ke termahal saat rentang harga sangat luas.
        """
        self.bst.insert(self.p_root)  # 100k
        self.bst.insert(self.p_kiri)  # 50k
        self.bst.insert(self.p_kanan) # 200k
        
        # Cari rentang dari 10.000 hingga 300.000 (mencakup semua produk)
        hasil = self.bst.search_by_price_range(10000, 300000)
        
        # Ekspektasi berurutan dari yang paling murah: 50k -> 100k -> 200k
        ekspektasi = [self.p_kiri, self.p_root, self.p_kanan]
        self.assertEqual(hasil, ekspektasi, "Hasil pencarian harus terurut naik (In-Order)")

    def test_search_by_price_range_narrow_and_boundary(self):
        """
        LOGIC TEST: Menguji keandalan batas min/max (inklusi nilai) dan filter yang ketat.
        """
        self.bst.insert(self.p_root)        # 100k
        self.bst.insert(self.p_kiri)        # 50k
        self.bst.insert(self.p_kanan)       # 200k
        self.bst.insert(self.p_dalam_range) # 150k
        
        # Filter harga dari 100.000 s.d 160.000 
        # Produk yang harus lolos: p_root (100k) dan p_dalam_range (150k)
        hasil = self.bst.search_by_price_range(100000, 160000)
        
        ekspektasi = [self.p_root, self.p_dalam_range]
        self.assertEqual(hasil, ekspektasi)

    def test_search_by_price_range_empty(self):
        """
        LOGIC TEST: Memastikan jika tidak ada produk yang berada di dalam rentang harga,
        fungsi mengembalikan list kosong [] tanpa menimbulkan error.
        """
        self.bst.insert(self.p_root) # 100k
        self.bst.insert(self.p_kiri) # 50k
        
        # Cari harga yang terlalu murah yang tidak ada di data
        hasil = self.bst.search_by_price_range(1000, 5000)
        self.assertEqual(hasil, [])

if __name__ == '__main__':
    unittest.main()