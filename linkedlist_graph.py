from models import Product
import heapq

# ====================== 1. DOUBLY LINKED LIST - KERANJANG BELANJA ======================
class NodeKeranjang:
    def __init__(self, produk: Product, jumlah: int = 1):
        self.produk = produk
        self.jumlah = jumlah
        self.next = None
        self.prev = None


class KeranjangBelanja:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ukuran = 0

    def tambah_barang(self, produk: Product, jumlah: int = 1):
        """Menambahkan barang ke keranjang belanja"""
        node_baru = NodeKeranjang(produk, jumlah)
        
        if not self.head:
            self.head = self.tail = node_baru
        else:
            self.tail.next = node_baru
            node_baru.prev = self.tail
            self.tail = node_baru
        self.ukuran += 1
        print(f"✅ Berhasil ditambahkan: {produk.nama} x{jumlah}")

    def hapus_barang(self, id_produk: int):
        """Menghapus barang dari keranjang berdasarkan ID"""
        current = self.head
        while current:
            if current.produk.id_produk == id_produk:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.ukuran -= 1
                print(f"🗑️  Barang dihapus: {current.produk.nama}")
                return True
            current = current.next
        print("❌ Barang tidak ditemukan di keranjang")
        return False

    def tampilkan_keranjang(self):
        """Menampilkan isi keranjang belanja"""
        if not self.head:
            print("🛒 Keranjang belanja kosong")
            return
        
        print("\n🛒 === ISI KERANJANG BELANJA ===")
        current = self.head
        total = 0
        i = 1
        while current:
            subtotal = current.produk.harga * current.jumlah
            print(f"{i}. {current.produk} × {current.jumlah} = Rp{subtotal:,}")
            total += subtotal
            current = current.next
            i += 1
        print(f"Total Belanja: Rp{total:,}")
        print("================================\n")

    def hitung_total(self):
        """Menghitung total harga keranjang"""
        total = 0
        current = self.head
        while current:
            total += current.produk.harga * current.jumlah
            current = current.next
        return total


# ====================== 2. GRAPH + ALGORITMA DIJKSTRA - RUTE PENGIRIMAN ======================
class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_rute(self, kota_asal, kota_tujuan, jarak):
        """Menambahkan rute antar kota"""
        if kota_asal not in self.graph:
            self.graph[kota_asal] = []
        if kota_tujuan not in self.graph:
            self.graph[kota_tujuan] = []
        
        self.graph[kota_asal].append((kota_tujuan, jarak))
        self.graph[kota_tujuan].append((kota_asal, jarak))  # undirected graph

    def dijkstra(self, start, end):
        """Mencari rute terpendek menggunakan Algoritma Dijkstra"""
        if start not in self.graph or end not in self.graph:
            return float('inf'), []
        
        pq = [(0, start, [start])]
        jarak_terpendek = {kota: float('inf') for kota in self.graph}
        jarak_terpendek[start] = 0
        
        while pq:
            jarak_sekarang, kota_sekarang, jalur = heapq.heappop(pq)
            
            if kota_sekarang == end:
                return jarak_sekarang, jalur
            
            if jarak_sekarang > jarak_terpendek[kota_sekarang]:
                continue
                
            for tetangga, bobot in self.graph[kota_sekarang]:
                jarak_baru = jarak_sekarang + bobot
                if jarak_baru < jarak_terpendek[tetangga]:
                    jarak_terpendek[tetangga] = jarak_baru
                    heapq.heappush(pq, (jarak_baru, tetangga, jalur + [tetangga]))
        
        return float('inf'), []  # Tidak ada jalur


# ====================== TESTING (untuk dijalankan sendiri) ======================
if __name__ == "__main__":
    # Contoh produk
    p1 = Product(1, "Laptop Gaming", 8500000, 4.8)
    p2 = Product(2, "Mouse Wireless", 250000, 4.5)

    # Testing Keranjang Belanja
    keranjang = KeranjangBelanja()
    keranjang.tambah_barang(p1, 1)
    keranjang.tambah_barang(p2, 2)
    keranjang.tampilkan_keranjang()
    
    keranjang.hapus_barang(2)
    keranjang.tampilkan_keranjang()

    # Testing Graph & Dijkstra
    g = Graph()
    g.tambah_rute("Jakarta", "Bandung", 150)
    g.tambah_rute("Jakarta", "Surabaya", 780)
    g.tambah_rute("Bandung", "Surabaya", 650)

    jarak, rute = g.dijkstra("Jakarta", "Surabaya")
    print(f"📦 Jarak terpendek ke Surabaya: {jarak} km")
    print(f"Rute: {' -> '.join(rute)}")