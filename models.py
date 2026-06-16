# models.py - Data Contract Product

class Product:
    def __init__(self, id_produk, nama, harga, rating):
        self.id_produk = id_produk
        self.nama = nama
        self.harga = harga
        self.rating = rating

    def __str__(self):
        return f"[{self.id_produk}] {self.nama} - Rp{self.harga} (Rating: {self.rating})"