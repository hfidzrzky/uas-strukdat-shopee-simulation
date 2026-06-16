# queue_search.py
# ==================================================
# Nama  : Wafi
# Queue dan Binary Search
#
# Queue digunakan untuk simulasi antrian checkout.
# Binary Search digunakan untuk mencari produk
# berdasarkan ID atau nama produk.
# ==================================================


class Queue:
    # Implementasi Queue (FIFO)
    # Data yang masuk lebih dulu akan diproses lebih dulu.

    def __init__(self):
        # Menyimpan data antrian
        self.items = []

    def enqueue(self, data):
        # Menambahkan data ke belakang antrian
        self.items.append(data)

    def dequeue(self):
        # Mengambil data yang berada di paling depan
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        # Melihat data paling depan tanpa menghapusnya
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        # Mengecek apakah antrian kosong
        return len(self.items) == 0

    def size(self):
        # Mengembalikan jumlah data dalam antrian
        return len(self.items)

    def display(self):
        # Menampilkan seluruh isi antrian
        return list(self.items)


def binary_search_by_id(products, target_id):
    # Mencari produk berdasarkan ID menggunakan Binary Search.
    # Syarat: products harus sudah terurut menaik berdasarkan id_produk.
    left = 0
    right = len(products) - 1

    while left <= right:
        mid = (left + right) // 2

        if products[mid].id_produk == target_id:
            return products[mid]
        elif products[mid].id_produk < target_id:
            left = mid + 1
        else:
            right = mid - 1

    return None


def binary_search_by_name(products, target_name):
    # Mencari produk berdasarkan nama menggunakan Binary Search.
    # Syarat: products harus sudah terurut alfabetis berdasarkan nama.
    target = target_name.strip().lower()
    left = 0
    right = len(products) - 1

    while left <= right:
        mid = (left + right) // 2
        current = products[mid].nama.strip().lower()

        if current == target:
            return products[mid]
        elif current < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def sort_by_id(products):
    # Mengurutkan salinan produk berdasarkan id_produk (untuk binary search by ID).
    return sorted(products, key=lambda p: p.id_produk)


def sort_by_name(products):
    # Mengurutkan salinan produk berdasarkan nama (untuk binary search by name).
    return sorted(products, key=lambda p: p.nama.strip().lower())
