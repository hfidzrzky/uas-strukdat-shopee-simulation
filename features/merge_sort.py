# merge_sort.py
from models import Product  # Mengimpor blueprint Product dari file models.py
from features.array_list import ProductDatabase as db #import database dari array_list.py

class MergeSortFitur:  # Membuat kelas untuk fitur Merge Sort sesuai prinsip OOP
    def __init__(
        self,
    ):  # Konstruktor untuk menginisialisasi objek saat pertama kali dibuat
        self.daftar_produk = db().get_all_products()  # ini konfigurasi ke variabel lokal agar database bisa digunakan

    def _merge_sort_proses(self, arr):
        # Fungsi internal (helper) rekursif untuk memecah list produk menjadi bagian kecil
        if len(arr) <= 1:
            return arr # Base case: jika isi list tinggal 1 atau kosong, langsung kembalikan karena sudah pasti terurut

        mid = len(arr) // 2  # Mencari titik tengah list produk untuk membagi dua kelompok
        left_half = arr[:mid]  # Memotong list produk dari indeks awal sampai batas tengah (bagian kiri)
        right_half = arr[mid:]  # Memotong list produk dari indeks batas tengah sampai akhir (bagian kanan)

        self._merge_sort_proses(left_half)  # Memanggil dirinya sendiri secara rekursif untuk terus memecah bagian kiri
        self._merge_sort_proses(right_half)  # Memanggil dirinya sendiri secara rekursif untuk terus memecah bagian kanan

        i = j = k = 0  # Inisialisasi tiga pointer pembantu: i untuk kiri, j untuk kanan, k untuk list utama

        # Proses menggabungkan (Conquer & Merge) kedua sub-list kembali sambil mengurutkan ratingnya
        while i < len(left_half) and j < len(right_half):
            if left_half[i].rating <= right_half[j].rating:  # Cek jika rating produk di sub-list kiri lebih murah atau sama
                arr[k] = left_half[i]  # Masukkan produk dari bagian kiri ke list utama
                i += 1  # Geser pointer indeks bagian kiri ke depan
            else:
                arr[k] = right_half[j]  # Jika rating produk di kanan lebih murah, masukkan produk kanan ke list utama
                j += 1  # Geser pointer indeks bagian kanan ke depan
            k += 1  # Geser pointer penulisan di list utama ke depan

        # Membersihkan sisa elemen di sub-list kiri jika sub-list kanan sudah habis duluan
        while i < len(left_half):
            arr[k] = left_half[i]  # Pindahkan sisa produk bagian kiri langsung ke list utama
            i += 1  # Geser pointer sub-list kiri
            k += 1  # Geser pointer list utama

        # Membersihkan sisa elemen di sub-list kanan jika sub-list kiri sudah habis duluan
        while j < len(right_half):
            arr[k] = right_half[j]  # Pindahkan sisa produk bagian kanan langsung ke list utama
            j += 1  # Geser pointer sub-list kanan
            k += 1  # Geser pointer list utama

    def urutkan_rating_asc(
                self,
            ):  # Fungsi utama yang akan dipanggil untuk mengurutkan rating termurah
        arr = list(
            self.daftar_produk
        )  # Menyalin list produk ke variabel baru agar data asli tidak rusak
        self._merge_sort_proses(arr)  # Menjalankan proses rekursif merge sort pada list duplikat tersebut
        return arr  # Mengembalikan list baru yang kondisinya sudah terurut rapi oleh merge sort

    def info(
        self,
    ):  # Fungsi pendukung untuk menghasilkan teks penjelasan skenario fitur
        return """
Konteks Skenario (Merge Sort):
User sedang membuka halaman pencarian produk di aplikasi Shopee.
Secara default, susunan produk muncul acak berdasarkan rekomendasi sistem.
User kemudian menekan tombol filter 'Rating Terendah' di layar.
Sistem memproses pengurutan data belanjaan menggunakan metode Merge Sort.
--------------------------------------------------------------------------"""  # Penutup teks informasi string multiline

    def simulasi_sort(
        self,
    ):  # Fungsi satu tombol otomatis yang nantinya dipanggil oleh Wafi di main.py
        print(
            self.info()
        )  # Mencetak teks penjelasan skenario ke dalam jendela terminal CLI
        print(
            "=========================================================================="
        )  # Mencetak garis pembatas hiasan visual atas
        print(
            "          SIMULASI OTOMATIS FILTER RATING (ALGORITMA MERGE SORT)           "
        )  # Mencetak judul utama proses simulasi
        print(
            "=========================================================================="
        )  # Mencetak garis pembatas hiasan visual bawah
        print(
            "║ ID     │ Nama Produk                    │ Harga         │ Rating  ║"
        )  # Mencetak header tabel manual menyesuaikan cetakan models.py
        print(
            "--------------------------------------------------------------------------"
        )  # Mencetak garis tipis pembatas antara header dan data
        for (
            p
        ) in (
            self.daftar_produk
        ):  # Melakukan perulangan untuk membaca setiap produk acak sebelum disortir
            print(
                str(p)
            )  # Mencetak data produk acak menggunakan magic method __str__ dari models.py
        print(
            "--------------------------------------------------------------------------"
        )  # Mencetak garis pembatas bawah data mentah acak
        print(
            "\n[AKSI] Sistem Shopee sedang memecah dan menggabungkan data (Merge Sorting)... \n"
        )  # Mencetak pesan status proses algoritma ke user
        produk_rapi = (
            self.urutkan_rating_asc()
        )  # Memanggil fungsi merge sort rating lalu menyimpan hasilnya ke variabel
        print(
            "║ ID     │ Nama Produk                    │ Harga         │ Rating  ║"
        )  # Mencetak ulang susunan header tabel untuk hasil akhir
        print(
            "--------------------------------------------------------------------------"
        )  # Mencetak garis tipis pembatas header tabel hasil akhir
        for (
            p
        ) in (
            produk_rapi
        ):  # Melakukan perulangan untuk menampilkan produk yang ratingnya sudah urut
            print(
                str(p)
            )  # Mencetak data produk rapi memanfaatkan format tabel di models.py
        print(
            "=========================================================================="
        )  # Mencetak garis tebal sebagai penutup sesi simulasi Merge Sort