cat > linkedlist.py << 'EOF'
from models import Product

# =====================================================
# DOUBLY LINKED LIST - KERANJANG BELANJA
# =====================================================

class NodeKeranjang:
    """
    Node untuk Doubly Linked List.
    """
    def __init__(self, produk: Product, jumlah: int = 1):
        self.produk = produk
        self.jumlah = jumlah
        self.next = None
        self.prev = None


class KeranjangBelanja:
    """
    Implementasi Doubly Linked List untuk Keranjang Belanja.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.ukuran = 0

    def tambah_barang(self, produk: Product, jumlah: int = 1):
        node_baru = NodeKeranjang(produk, jumlah)
        
        if not self.head:
            self.head = self.tail = node_baru
        else:
            self.tail.next = node_baru
            node_baru.prev = self.tail
            self.tail = node_baru
            
        self.ukuran += 1
        print(f"✅ Berhasil ditambahkan: {produk.nama} x{jumlah}")

    def hapus_barang(self, id_produk: int) -> bool:
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
                print(f"🗑️ Barang dihapus: {current.produk.nama}")
                return True
            current = current.next
        print("❌ Barang tidak ditemukan")
        return False

    def tampilkan_keranjang(self):
        if not self.head:
            print("🛒 Keranjang belanja masih kosong.")
            return
        
        print("\n" + "="*60)
        print("             ISI KERANJANG BELANJA")
        print("="*60)
        current = self.head
        total = 0
        i = 1
        while current:
            subtotal = current.produk.harga * current.jumlah
            print(f"{i:2d}. {current.produk} × {current.jumlah} = Rp{subtotal:,}")
            total += subtotal
            current = current.next
            i += 1
        print("="*60)
        print(f"Total Belanja: Rp{total:,}")
        print("="*60 + "\n")

    def hitung_total(self) -> int:
        total = 0
        current = self.head
        while current:
            total += current.produk.harga * current.jumlah
            current = current.next
        return total
EOF