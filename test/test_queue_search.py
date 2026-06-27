# tests/test_queue_search.py
# ============================================================================
# Unit test untuk modul Wafi: Queue (FIFO) dan Binary Search.
# Jalankan dari root repo:  python -m unittest discover -v
# ============================================================================

import os
import sys
import unittest

# Pastikan root repo ada di sys.path agar import modul berhasil saat
# test dijalankan langsung maupun via discover.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models import Product
from features.queue_search import (
    Queue,
    binary_search_by_id,
    binary_search_by_name,
    sort_by_id,
    sort_by_name,
)

class TestQueue(unittest.TestCase):
    """Menguji perilaku FIFO dari struktur data Queue."""

    def setUp(self):
        self.q = Queue()

    def test_queue_kosong_di_awal(self):
        self.assertTrue(self.q.is_empty())
        self.assertEqual(self.q.size(), 0)
        self.assertIsNone(self.q.front())
        self.assertIsNone(self.q.dequeue())

    def test_enqueue_menambah_ukuran(self):
        self.q.enqueue("A")
        self.q.enqueue("B")
        self.assertFalse(self.q.is_empty())
        self.assertEqual(self.q.size(), 2)
        self.assertEqual(self.q.front(), "A")

    def test_urutan_fifo(self):
        for item in ["A", "B", "C"]:
            self.q.enqueue(item)
        self.assertEqual(self.q.dequeue(), "A")
        self.assertEqual(self.q.dequeue(), "B")
        self.assertEqual(self.q.dequeue(), "C")
        self.assertTrue(self.q.is_empty())

    def test_display_mengembalikan_salinan(self):
        self.q.enqueue("A")
        salinan = self.q.display()
        salinan.append("X")  # tidak boleh memengaruhi antrian asli
        self.assertEqual(self.q.size(), 1)


class TestBinarySearch(unittest.TestCase):
    """Menguji pencarian produk berdasarkan ID dan Nama."""

    def setUp(self):
        self.catalog = [
            Product("P005", "Mouse Wireless", 75000, 4.7),
            Product("P001", "Keyboard Mekanik", 350000, 4.8),
            Product("P010", "Headset Gaming", 250000, 4.5),
            Product("P003", "Webcam 1080p", 180000, 4.2),
        ]

    def test_cari_by_id_ditemukan(self):
        terurut = sort_by_id(self.catalog)
        hasil = binary_search_by_id(terurut, "P010")
        self.assertIsNotNone(hasil)
        self.assertEqual(hasil.nama, "Headset Gaming")

    def test_cari_by_id_tidak_ditemukan(self):
        terurut = sort_by_id(self.catalog)
        self.assertIsNone(binary_search_by_id(terurut, "P999"))

    def test_cari_by_nama_ditemukan_case_insensitive(self):
        terurut = sort_by_name(self.catalog)
        hasil = binary_search_by_name(terurut, "mouse wireless")
        self.assertIsNotNone(hasil)
        self.assertEqual(hasil.id_produk, "P005")

    def test_cari_by_nama_tidak_ditemukan(self):
        terurut = sort_by_name(self.catalog)
        self.assertIsNone(binary_search_by_name(terurut, "Produk Hantu"))

    def test_sort_by_id_tidak_mengubah_asli(self):
        sort_by_id(self.catalog)
        self.assertEqual(self.catalog[0].id_produk, "P005")  # urutan asli utuh


if __name__ == "__main__":
    unittest.main()
