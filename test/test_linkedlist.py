import sys
import os
import unittest

# =========================================================
# Memastikan Python mendeteksi folder root proyek
# =========================================================
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import Product
from features.linkedlist import KeranjangBelanja


class TestKeranjangBelanja(unittest.TestCase):

    def setUp(self):
        """Dijalankan sebelum setiap test case dijalankan"""
        self.keranjang = KeranjangBelanja()
        self.p1 = Product(1, "Laptop Gaming", 8500000, 4.8)
        self.p2 = Product(2, "Mouse Wireless", 250000, 4.5)
        self.p3 = Product(3, "Keyboard Mechanical", 450000, 4.7)

    # =========================================================
    # TEST CASE - FUNGSIONALITAS DASAR
    # =========================================================

    def test_keranjang_awal_kosong(self):
        """LOGIC TEST: Memastikan keranjang baru dibuat dalam keadaan kosong"""
        self.assertEqual(self.keranjang.ukuran, 0, "Ukuran keranjang awal harus 0")
        self.assertIsNone(self.keranjang.head, "Head harus None saat keranjang kosong")
        self.assertIsNone(self.keranjang.tail, "Tail harus None saat keranjang kosong")

    def test_tambah_barang(self):
        """LOGIC TEST: Memastikan fungsi tambah_barang bekerja dengan benar"""
        self.keranjang.tambah_barang(self.p1, 1)
        self.assertEqual(self.keranjang.ukuran, 1)
        self.assertEqual(self.keranjang.head, self.keranjang.tail)

    def test_tambah_multiple_barang(self):
        """LOGIC TEST: Memastikan penambahan multiple barang dan doubly linked list terbentuk"""
        self.keranjang.tambah_barang(self.p1, 1)
        self.keranjang.tambah_barang(self.p2, 2)
        self.keranjang.tambah_barang(self.p3, 1)
        
        self.assertEqual(self.keranjang.ukuran, 3)
        self.assertIsNotNone(self.keranjang.head)
        self.assertIsNotNone(self.keranjang.tail)

    def test_hitung_total(self):
        """LOGIC TEST: Memastikan perhitungan total harga benar"""
        self.keranjang.tambah_barang(self.p1, 2)
        self.keranjang.tambah_barang(self.p2, 4)
        total = self.keranjang.hitung_total()
        
        expected = (8500000 * 2) + (250000 * 4)
        self.assertEqual(total, expected, "Total harga harus sesuai perhitungan")

    def test_hapus_barang(self):
        """LOGIC TEST: Memastikan fungsi hapus_barang dapat menghapus node dengan benar"""
        self.keranjang.tambah_barang(self.p1, 1)
        self.keranjang.tambah_barang(self.p2, 1)
        self.keranjang.tambah_barang(self.p3, 1)
        
        # Hapus barang di tengah
        self.assertTrue(self.keranjang.hapus_barang(2))
        self.assertEqual(self.keranjang.ukuran, 2)

    def test_hapus_barang_tidak_ada(self):
        """LOGIC TEST: Menguji kasus ketika barang yang dihapus tidak ditemukan"""
        self.keranjang.tambah_barang(self.p1, 1)
        self.assertFalse(self.keranjang.hapus_barang(999))

    def test_kosongkan_keranjang(self):
        """LOGIC TEST: Memastikan fungsi kosongkan_keranjang bekerja dengan benar"""
        self.keranjang.tambah_barang(self.p1, 5)
        self.keranjang.tambah_barang(self.p2, 3)
        self.keranjang.kosongkan_keranjang()
        
        self.assertEqual(self.keranjang.ukuran, 0)
        self.assertIsNone(self.keranjang.head)
        self.assertIsNone(self.keranjang.tail)


if __name__ == '__main__':
    unittest.main(verbosity=2)