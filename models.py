class Product:
    """
    Representasi entitas produk di dalam sistem e-commerce.
    Berfungsi sebagai 'Data Contract' agar struktur objek seragam
    saat diolah oleh Wafi (Search), Haris (Sort), Hafidz (Tree/Array), dan Galang (Linked List).
    """
    def __init__(self, id_produk: str, nama: str, harga: int, rating: float):
        # Type hinting (str, int, float) ditambahkan agar anggota tim tahu persis tipe datanya
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.rating = rating

    def __str__(self):
        """
        Magic method untuk memformat tampilan saat objek di-print.
        Sangat berguna untuk antarmuka CLI (Menu Program Wafi).
        """
        # Format harga dengan titik/koma ribuan
        harga_format = f"Rp {self.harga:,}"
        # Menambahkan pemisah ribuan pada harga agar terlihat seperti format Rupiah asli
        return f"║ {self.id_produk:<6} │ {self.nama:<30} │ {harga_format:<13} │ {self.rating:^7} ║"

    def __repr__(self):
        """
        Magic method untuk representasi objek saat proses debugging atau 
        saat objek berada di dalam struktur data List/Array.
        """
        return f"Product(id='{self.id_produk}', nama='{self.nama}', harga={self.harga}, rating={self.rating})"
    
class CartItem:
    """
    Representasi item spesifik di dalam keranjang belanja.
    Membungkus objek Product dengan tambahan informasi kuantitas (jumlah barang yang dibeli).
    """
    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self) -> int:
        """Menghitung total harga untuk item ini (harga produk * kuantitas)."""
        return self.product.harga * self.quantity

    def __str__(self):
        return f"{self.product.nama} (x{self.quantity}) - Subtotal: Rp {self.get_subtotal():,}"