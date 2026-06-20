import sys
import os
import unittest

# =========================================================
# Memastikan Python mendeteksi folder root proyek
# =========================================================
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from features.graph import Graph


class TestGraphDijkstra(unittest.TestCase):

    def setUp(self):
        """Dijalankan sebelum setiap test case dijalankan"""
        self.graph = Graph()
        
        # Setup data rute pengiriman (simulasi logistik Shopee)
        self.graph.tambah_rute("Jakarta", "Bandung", 150)
        self.graph.tambah_rute("Jakarta", "Surabaya", 780)
        self.graph.tambah_rute("Bandung", "Surabaya", 650)
        self.graph.tambah_rute("Jakarta", "Semarang", 450)
        self.graph.tambah_rute("Semarang", "Surabaya", 300)
        self.graph.tambah_rute("Bandung", "Semarang", 200)

    # =========================================================
    # TEST CASE - FUNGSIONALITAS GRAPH
    # =========================================================

    def test_tambah_rute(self):
        """LOGIC TEST: Memastikan rute dapat ditambahkan dan graph bersifat undirected"""
        # Cek apakah rute Jakarta -> Bandung ada
        self.assertIn(("Bandung", 150), self.graph.graph["Jakarta"])
        # Cek apakah rute dua arah (undirected)
        self.assertIn(("Jakarta", 150), self.graph.graph["Bandung"])

    def test_dijkstra_rute_terpendek(self):
        """
        LOGIC TEST: Memastikan algoritma Dijkstra mengembalikan rute dan jarak terpendek
        Kasus: Jakarta ke Surabaya
        """
        jarak, rute = self.graph.dijkstra("Jakarta", "Surabaya")
        
        self.assertIsNotNone(jarak)
        self.assertLess(jarak, float('inf'), "Harus ada rute yang ditemukan")
        self.assertEqual(rute[0], "Jakarta", "Rute harus dimulai dari start")
        self.assertEqual(rute[-1], "Surabaya", "Rute harus berakhir di tujuan")
        
        print(f"✅ Rute terpendek Jakarta → Surabaya: {rute} | Jarak: {jarak} km")

    def test_dijkstra_rute_optimal(self):
        """
        LOGIC TEST: Memastikan Dijkstra memilih rute paling optimal
        (Jakarta -> Semarang -> Surabaya lebih pendek daripada langsung)
        """
        jarak, rute = self.graph.dijkstra("Jakarta", "Surabaya")
        # Rute optimal seharusnya melewati Semarang (total ~750 km)
        self.assertIn("Semarang", rute)

    def test_dijkstra_tidak_ada_rute(self):
        """LOGIC TEST: Menguji kasus ketika tidak ada rute antara dua kota"""
        jarak, rute = self.graph.dijkstra("Jakarta", "Bali")
        self.assertEqual(jarak, float('inf'), "Jarak harus infinity jika tidak ada rute")
        self.assertEqual(rute, [], "Rute harus kosong jika tidak ada jalur")

    def test_graph_kosong(self):
        """LOGIC TEST: Menguji perilaku Dijkstra pada graph yang belum ada rutenya"""
        graph_kosong = Graph()
        jarak, rute = graph_kosong.dijkstra("Jakarta", "Surabaya")
        self.assertEqual(jarak, float('inf'))
        self.assertEqual(rute, [])

    def test_tambah_rute_sama(self):
        """LOGIC TEST: Memastikan penambahan rute yang sama tidak error"""
        self.graph.tambah_rute("Jakarta", "Bandung", 150)  # tambah ulang
        self.assertIn(("Bandung", 150), self.graph.graph["Jakarta"])


if __name__ == '__main__':
    unittest.main(verbosity=2)