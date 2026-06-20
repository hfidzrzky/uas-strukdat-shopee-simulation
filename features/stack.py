# stack.py

class Stack:
    """Class Stack untuk menyimpan riwayat angka pilihan menu user di main.py."""
    
    def __init__(self, data_awal=None):
        """
        Constructor otomatis. 
        Bisa menerima data awal berupa list, contoh: stack = Stack(['1', '3'])
        """
        if data_awal is None:
            self._storage = []  # Jika tidak ada data awal, buat list kosong
        else:
            self._storage = list(data_awal)  # Jika ada data awal, konversi menjadi list baru

    def __call__(self, data_baru):
        """
        Magic method agar objek class bisa dipanggil seperti fungsi: objek(data)
        Ini memenuhi request kamu untuk cara akses: nama_objek(riwayat_pilihan)
        """
        self.push(data_baru)
        return self

    def push(self, pilihan_menu):
        """Menambahkan riwayat angka pilihan menu baru ke dalam stack."""
        # Menyimpan input pilihan menu (misal: '1', '2', '3') ke urutan paling akhir
        self._storage.append(str(pilihan_menu))

    def pop(self):
        """Mengambil dan menghapus angka pilihan terakhir (opsi Back)."""
        if self.is_empty():
            return None
        return self._storage.pop()

    def peek(self):
        """Melihat pilihan menu aktif terakhir tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self._storage[-1]

    def is_empty(self):
        """Memeriksa apakah riwayat pilihan kosong."""
        return len(self._storage) == 0

    def cetak_riwayat(self):
        """Menampilkan jejak angka pilihan menu yang ditekan user."""
        if self.is_empty():
            return "Belum ada riwayat pilihan."
        # Menggabungkan angka pilihan menu dengan tanda panah, contoh: 1 -> 3 -> 2
        return " -> ".join(self._storage)