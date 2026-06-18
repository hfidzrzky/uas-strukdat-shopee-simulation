import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Memastikan Python mendeteksi folder root proyek 'UAS_StrukturData'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mencegah ImportError jika berkas models dan features.tree belum lengkap/tidak ditemukan saat testing
sys.modules['models'] = MagicMock()
sys.modules['features.tree'] = MagicMock()

# Import kelas yang akan diuji
from features.array_list import ProductDatabase

class TestProductDatabase(unittest.TestCase):

    @patch('features.array_list.PriceBST')
    @patch('features.array_list.Product')
    def setUp(self, mock_product, mock_bst):
        """
        Set up lingkungan testing sebelum setiap fungsi test dijalankan.
        Menggunakan teknik Mocking untuk mengisolasi kelas ProductDatabase.
        """
        self.MockProduct = mock_product
        self.MockBST = mock_bst
        
        # Mengatur agar PriceBST() mengembalikan instance mock yang bisa kita lacak
        self.mock_bst_instance = self.MockBST.return_value
        
        # Inisialisasi objek database yang akan diuji
        self.db = ProductDatabase()

    def test_initialization_and_mock_data_population(self):
        """
        LOGIC TEST: Memastikan saat inisialisasi, 10 data mock masuk ke dalam 
        ArrayList (catalog) dan di-insert ke dalam BST secara sinkron.
        """
        # 1. Memastikan jumlah data yang masuk ke catalog (ArrayList) tepat 10 produk
        self.assertEqual(len(self.db.catalog), 10, "Jumlah data di catalog harus tepat 10")
        
        # 2. Memastikan metode insert pada BST dipanggil tepat 10 kali
        self.assertEqual(self.mock_bst_instance.insert.call_count, 10, "Metode insert pada BST harus dipanggil 10 kali")

    def test_get_all_products(self):
        """
        LOGIC TEST: Memastikan get_all_products mengembalikan list catalog yang sebenarnya
        tanpa manipulasi atau perubahan tipe data.
        """
        katalog_produk = self.db.get_all_products()
        
        # Memastikan tipe data yang dikembalikan adalah List (ArrayList bawaan Python)
        self.assertIsInstance(katalog_produk, list)
        # Memastikan isinya sama persis dengan properti internal catalog
        self.assertEqual(katalog_produk, self.db.catalog)

    def test_filter_by_price_delegation(self):
        """
        LOGIC TEST: Memastikan method filter_by_price mendelegasikan tugasnya 
        ke BST dengan melemparkan argumen harga yang benar dan mengembalikan hasilnya.
        """
        # Membuat data tiruan yang seolah-olah dikembalikan oleh BST pencarian harga
        mock_search_result = [MagicMock(), MagicMock()]
        self.mock_bst_instance.search_by_price_range.return_value = mock_search_result
        
        # Panggil endpoint filter pada rentang harga tertentu
        min_harga, max_harga = 50000, 150000
        hasil_filter = self.db.filter_by_price(min_harga, max_harga)
        
        # 1. Verifikasi: Apakah ProductDatabase memanggil BST dengan parameter yang tepat?
        self.mock_bst_instance.search_by_price_range.assert_called_once_with(min_harga, max_harga)
        
        # 2. Verifikasi: Apakah return value dari BST diteruskan kembali ke pemanggil?
        self.assertEqual(hasil_filter, mock_search_result, "Hasil filter harus sesuai dengan yang dikembalikan oleh BST")

if __name__ == '__main__':
    unittest.main()