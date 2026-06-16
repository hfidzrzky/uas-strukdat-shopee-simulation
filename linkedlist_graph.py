from models import Product
import heapq

# =====================================================
# 1. DOUBLY LINKED LIST - KERANJANG BELANJA
# =====================================================

class NodeKeranjang:
    """
    Node untuk Doubly Linked List.
    Setiap node menyimpan produk dan jumlahnya.
    """
    def __init__(self, produk: Product, jumlah: int = 1):
        self.produk = produk          # Objek Product
        self.jumlah = jumlah          # Jumlah barang yang dibeli
        self.next = None              # Pointer ke node berikutnya
        self.prev = None              # Pointer ke node sebelumnya (doubly)


class KeranjangBelanja:
    """
    Implementasi Doubly Linked List untuk fitur Keranjang Belanja.
    Memungkinkan penambahan, penghapusan, dan penampilan barang dengan mudah.
    """
    def __init__(self):
        self.head = None              # Node pertama (awal keranjang)
        self.tail = None              # Node terakhir (akhir keranjang)
        self.ukuran = 0               # Jumlah total item di keranjang

    def tambah_barang(self, produk: Product, jumlah: int = 1):
        """Menambahkan barang baru ke keranjang belanja"""
        node_baru = NodeKeranjang(produk, jumlah)
        
        if not self.head:             # Jika keranjang kosong
            self.head = self.tail = node_baru
        else:
            self.tail.next = node_baru
            node_baru.prev = self.tail
            self.tail = node_baru
            
        self.ukuran += 1
        print(f" Berhasil ditambahkan ke keranjang: {produk.nama} x{jumlah}")

    def hapus_barang(self, id_produk: int) -> bool:
        """Menghapus barang dari keranjang berdasarkan ID produk"""
        current = self.head
        while current:
            if current.produk.id_produk == id_produk:
                # Hapus node (handle head, tail, dan tengah)
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.ukuran -= 1
                print(f" Barang berhasil dihapus: {current.produk.nama}")
                return True
            current = current.next
        print(" Barang tidak ditemukan di keranjang")
        return False

    def tampilkan_keranjang(self):
        """Menampilkan seluruh isi keranjang belanja"""
        if not self.head:
            print(" Keranjang belanja masih kosong.")
            return
        
        print("\n" + "="*50)
        print("             ISI KERANJANG BELANJA")
        print("="*50)
        current = self.head
        total = 0
        i = 1
        while current:
            subtotal = current.produk.harga * current.jumlah
            print(f"{i:2d}. {current.produk} × {current.jumlah} = Rp{subtotal:,}")
            total += subtotal
            current = current.next
            i += 1
        print("="*50)
        print(f"Total Belanja: Rp{total:,}")
        print("="*50 + "\n")

    def hitung_total(self) -> int:
        """Menghitung total harga semua barang di keranjang"""
        total = 0
        current = self.head
        while current:
            total += current.produk.harga * current.jumlah
            current = current.next
        return total


# =====================================================
# 2. GRAPH + ALGORITMA DIJKSTRA - RUTE PENGIRIMAN
# =====================================================

class Graph:
    """
    Implementasi Graph menggunakan Adjacency List.
    Digunakan untuk simulasi rute logistik pengiriman barang.
    """
    def __init__(self):
        self.graph = {}               # Dictionary untuk menyimpan rute antar kota

    def tambah_rute(self, kota_asal: str, kota_tujuan: str, jarak: int):
        """Menambahkan rute dua arah antar kota beserta jaraknya"""
        if kota_asal not in self.graph:
            self.graph[kota_asal] = []
        if kota_tujuan not in self.graph:
            self.graph[kota_tujuan] = []
        
        self.graph[kota_asal].append((kota_tujuan, jarak))
        self.graph[kota_tujuan].append((kota_asal, jarak))  # undirected graph

    def dijkstra(self, start: str, end: str):
        """
        Mencari rute terpendek menggunakan Algoritma Dijkstra.
        Menggunakan Priority Queue (heapq) untuk efisiensi.
        """
        if start not in self.graph or end not in self.graph:
            return float('inf'), []
        
        pq = [(0, start, [start])]                    # (jarak, kota, jalur)
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
        
        return float('inf'), []   # Tidak ada rute yang ditemukan


# ====================== TESTING ======================
if __name__ == "__main__":
    print("=== TESTING MODUL GALANG ===\n")
    
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
    print(f" Jarak terpendek: {jarak} km")
    print(f"Rute: {' -> '.join(rute)}")