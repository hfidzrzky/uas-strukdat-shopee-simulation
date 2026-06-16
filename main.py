from models import Product
from linkedlist import KeranjangBelanja
from graph import Graph

if __name__ == "__main__":
    print("="*60)
    print("     UAS STRUKDAT - SHOPEE SIMULATION")
    print("="*60 + "\n")

    # === TESTING KERANJANG BELANJA ===
    print("1. TESTING KERANJANG BELANJA (Linked List)")
    keranjang = KeranjangBelanja()

    p1 = Product(1, "Laptop Gaming", 8500000, 4.8)
    p2 = Product(2, "Mouse Wireless", 250000, 4.5)
    p3 = Product(3, "Keyboard Mechanical", 450000, 4.7)

    keranjang.tambah_barang(p1, 1)
    keranjang.tambah_barang(p2, 2)
    keranjang.tambah_barang(p3, 1)
    
    keranjang.tampilkan_keranjang()
    
    keranjang.hapus_barang(2)
    keranjang.tampilkan_keranjang()

    print(f"Total harga keranjang: Rp{keranjang.hitung_total():,}\n")

    # === TESTING GRAPH & DIJKSTRA ===
    print("2. TESTING RUTE PENGIRIMAN (Graph + Dijkstra)")
    g = Graph()
    g.tambah_rute("Jakarta", "Bandung", 150)
    g.tambah_rute("Jakarta", "Surabaya", 780)
    g.tambah_rute("Bandung", "Surabaya", 650)
    g.tambah_rute("Jakarta", "Semarang", 450)

    jarak, rute = g.dijkstra("Jakarta", "Surabaya")
    print(f"Jarak terpendek: {jarak} km")
    print(f"Rute: {' -> '.join(rute)}")
    print("="*60)