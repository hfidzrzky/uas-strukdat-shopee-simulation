# bubble_sort.py
from models import Product  # Mengimpor blueprint Product dari file models.py


class BubbleSortFitur:  # Membuat kelas untuk fitur Bubble Sort sesuai prinsip OOP
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

    def urutkan_harga_asc(
                self,
            ):  # Fungsi utama algoritma Bubble Sort untuk mengurutkan harga termurah
        arr = list(
            self.daftar_produk
        )  # Menyalin list produk ke variabel baru agar data asli tidak rusak
        n = len(arr)  # Mengambil informasi jumlah total elemen yang ada di dalam list
        for i in range(
            n
        ):  # Loop luar untuk mengontrol berapa banyak lintasan pemeriksaan data
            for j in range(
                0, n - i - 1
            ):  # Loop dalam untuk membandingkan dua produk yang posisinya bersebelahan
                if (
                    arr[j].harga > arr[j + 1].harga
                ):  # Cek jika harga produk kiri lebih mahal dari produk kanan
                    arr[j], arr[j + 1] = (
                        arr[j + 1],
                        arr[j],
                    )  # Tukar posisi kedua produk tersebut secara langsung (Swap)
        return arr  # Mengembalikan list baru yang kondisinya sudah terurut rapi

    def info(
        self,
    ):  # Fungsi pendukung untuk menghasilkan teks penjelasan skenario fitur
        return """
Konteks Skenario (Bubble Sort):
User sedang membuka halaman pencarian produk di aplikasi Shopee.
Secara default, susunan produk muncul acak berdasarkan rekomendasi sistem.
User kemudian menekan tombol filter 'Harga Terendah' di layar.
Sistem memproses pengurutan data belanjaan menggunakan metode Bubble Sort.
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
            "         SIMULASI OTOMATIS FILTER HARGA (ALGORITMA BUBBLE SORT)           "
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
            "\n[AKSI] Sistem Shopee sedang melakukan penukaran posisi (Bubble Sorting)... \n"
        )  # Mencetak pesan status proses algoritma ke user
        produk_rapi = (
            self.urutkan_harga_asc()
        )  # Memanggil fungsi bubble sort harga lalu menyimpan hasilnya ke variabel
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
        )  # Mencetak garis tebal sebagai penutup sesi simulasi Bubble Sort
