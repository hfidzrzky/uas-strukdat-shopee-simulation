# quick_sort.py
from models import Product  # Mengimpor blueprint Product dari file models.py


class QuickSortFitur:  # Membuat kelas untuk fitur Quick Sort sesuai prinsip OOP
    def __init__(
        self,
    ):  # Konstruktor untuk menginisialisasi objek saat pertama kali dibuat
        self.daftar_produk = [  # Membuat list internal berisi kumpulan data produk tiruan Shopee
            Product(
                "SP01", "Sepatu Running Adidas", 850000, 4.8
            ),  # Menambahkan produk pertama ke dalam list
            Product(
                "HP02", "iPhone 15 Pro Max", 22000000, 4.9
            ),  # Menambahkan produk kedua dengan harga tertinggi
            Product(
                "KM03", "Kemeja Flanel Uniqlo", 350000, 4.5
            ),  # Menambahkan produk ketiga ke dalam list
            Product(
                "TS04", "Tas Ransel Eiger", 450000, 4.7
            ),  # Menambahkan produk keempat ke dalam list
        ]  # Menutup deklarasi array list produk internal

    def __quick_sort_logic(
        self, arr
    ):  # Fungsi privat khusus untuk memproses rumus rekursif Quick Sort
        if (
            len(arr) <= 1
        ):  # Cek kondisi batas (base case): jika list kosong atau sisa 1 data
            return arr  # Kembalikan list tersebut karena otomatis sudah dianggap terurut
        pivot = arr[
            len(arr) // 2
        ]  # Memilih elemen yang berada di posisi tengah list sebagai poros acuan
        left = [
            x for x in arr if x.harga < pivot.harga
        ]  # Mengumpulkan semua produk yang harganya lebih murah dari pivot
        middle = [
            x for x in arr if x.harga == pivot.harga
        ]  # Mengumpulkan semua produk yang harganya sama dengan pivot
        right = [
            x for x in arr if x.harga > pivot.harga
        ]  # Mengumpulkan semua produk yang harganya lebih mahal dari pivot
        return (
            self.__quick_sort_logic(left)
            + middle
            + self.__quick_sort_logic(right)
        )  # Menggabungkan hasil sorting kelompok kiri, tengah, dan kanan kembali

    def urutkan_harga_asc(
                self,
            ):  # Fungsi publik untuk menjembatani pemanggilan dari luar file kelas
        return self.__quick_sort_logic(
            self.daftar_produk
        )  # Menjalankan fungsi rumus rahasia di atas dengan umpan data internal

    def info(
        self,
    ):  # Fungsi pendukung untuk menghasilkan teks penjelasan skenario fitur
        return """
Konteks Skenario (Quick Sort):
User ingin mengurutkan puluhan ribu hasil pencarian produk Shopee secara instan.
Sistem memilih algoritma Quick Sort demi efisiensi waktu performa yang tinggi.
Data dipecah berdasarkan nilai acuan harga tengah (Divide and Conquer).
Hasil pencarian tersusun rapi dari harga terendah dalam hitungan milidetik.
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
            "         SIMULASI OTOMATIS FILTER HARGA (ALGORITMA QUICK SORT)            "
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
            "\n[AKSI] Sistem Shopee memecah & memproses kelompok harga (Quick Sorting)... \n"
        )  # Mencetak pesan status proses algoritma ke user
        produk_rapi = (
            self.urutkan_harga_asc()
        )  # Memanggil fungsi jembatan quick sort lalu menyimpan hasilnya ke variabel
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
        ):  # Melakukan perulangan untuk menampilkan produk yang harganya sudah urut
            print(
                str(p)
            )  # Mencetak data produk rapi memanfaatkan format tabel di models.py
        print(
            "=========================================================================="
        )  # Mencetak garis tebal sebagai penutup sesi simulasi Quick Sort
