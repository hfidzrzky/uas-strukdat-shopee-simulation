# stack.py
# Karena ini merepresentasikan riwayat navigasi belanja, aku tidak memakai models.py yang dibuat Hafidz
# Karena models.py nya hanya memuat objek Produk belanjaan saja
# Jadi aku inisialisasi data rute navigasi produknya sendiri di sini

class Stack:  # Memakai OOP sesuai poin B.3 untuk membuat struktur data Stack
    def __init__(self):  # Bikin inti diri sendiri dari kelas stack (konstruktor objek)
        # Menggunakan list standar sebagai penyimpanan internal (inti struktur diatur manual)
        self.__storage = ["Beranda Shopee", "Hasil Pencarian: Sepatu", "Detail Produk: Adidas Running"]  # Isinya list riwayat halaman awal

    def push(self, item):  # Bikin attribut atau fungsi .push untuk menambah data ke stack
        # Menambahkan elemen halaman ke tumpukan paling atas.
        self.__storage.append(item)  # Pake fungsi .append bawaan python untuk menambah di akhir list

    def pop(self):  # Bikin attribut atau fungsi .pop untuk menghapus data dari stack
        # Menghapus dan mengembalikan elemen dari tumpukan paling atas.
        if self.is_empty():  # Cek dlu apakah listnya kosong atau ada isinyaa menggunakan fungsi is_empty
            raise IndexError("Pop dari Stack yang kosong! Kamu sudah berada di Beranda utama.")  # Ini untuk handle errornyaaa jika kosong
        return self.__storage.pop()  # Kalau tidak kosong, langsung di pop elemen terakhirnya dari list

    def peek(self):  # Bikin attribut atau fungsi .peek untuk mengintip data teratas stack
        # Melihat elemen teratas tanpa menghapusnya.
        if self.is_empty():  # Cek dlu apakah listnya kosong atau ada isinya sebelum diintip
            return None  # Jika kosong, mengembalikan nilai kosong juga agar aman
        return self.__storage[-1]  # Ini logic di pythonnya, pake -1 untuk melihat elemen terakhir di list

    def is_empty(self):  # Bikin attribut atau fungsi .is_empty untuk cek kondisi kosong
        # Memeriksa apakah stack kosong.
        return len(self.__storage) == 0  # Akan menghasilkan nilai true jika panjang list adalah nol
 
    def size(self):  # Bikin attribut atau fungsi .size untuk melihat ukuran jumlah data
        # Mengembalikan jumlah elemen di dalam stack.
        return len(self.__storage)  # Ini akan hitung elemen dengan fungsi len() bawaan python

    def display(self):  # Bikin attribut atau fungsi .display untuk visualisasi data ke luar kelas
        # Mengembalikan list salinan untuk kebutuhan visualisasi CLI.
        return list(self.__storage)  # Mengembalikan nilai listnya dalam bentuk duplikat agar aman

    def info(self):  # Bikin attribut atau fungsi .info untuk skenario cerita fitur navigasi
        return """
        Konteks: Seorang user sedang mencari sepatu running di Shopee.
        Dia membuka Beranda, mengetik kata kunci pencarian, lalu masuk
        ke halaman detail produk salah satu sepatu terlaris.\n"""  # Ini sebagai konteks awal cerita e-commerce

    def riwayatnavigasi(self):  # Ini sengaja dibuat langsung, agar untuk pemanggilannya hanya menggunakan Stack.riwayatnavigasi
        """Menjalankan seluruh simulasi Stack secara otomatis dan interaktif"""
        print(self.info())  # Mencetak teks konteks skenario di awal jalannya simulasi program
        print("==================================================")  # Cetak garis pembatas atas hiasan visual CLI
        print("       SIMULASI OTOMATIS FITUR NAVIGASI (STACK)   ")  # Cetak judul utama simulasi halaman stack di terminal
        print("==================================================")  # Cetak garis pembatas bawah hiasan visual CLI
        
        # 1. Menampilkan data awal (Display)
        print(f"[STATUS] Alur Halaman Terbuka Saat Ini:\n  --> " + " -> ".join(self.display()))  # Tampilkan susunan halaman aktif saat ini
        
        input("\n👉 [INTERAKTIF] Tekan ENTER untuk mengintip halaman aktif saat ini... ")  # Menahan layar demi interaksi menanti enter dari user
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        # 2. Mengintip halaman teratas (Peek)
        print(f"[PEEK]   User sedang melihat halaman: '{self.peek()}'")  # Tampilkan halaman teratas menggunakan fungsi peek buatan sendiri
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi
        
        input("\n👉 [INTERAKTIF] Tekan ENTER untuk simulasi menambah barang ke Keranjang Belanja... ")  # Menahan layar demi interaksi menanti enter dari user
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        # 3. Simulasi Navigasi ke Halaman Baru Lagi (Push)
        halaman_baru = "Keranjang Belanja"  # Menentukan nama halaman baru yang akan dibuka oleh user di aplikasi
        print(f"[AKSI]   User klik ikon keranjang. Masuk halaman baru --->")  # Beri tahu aksi perpindahan halaman yang sedang dilakukan user
        self.push(halaman_baru)  # Memasukkan halaman baru ke dalam tumpukan menggunakan fungsi push internal
        print(f"[PUSH]   Berhasil masuk ke: '{halaman_baru}'")  # Tampilkan status sukses push halaman baru ke layar terminal
        print(f"[PEEK]   Halaman aktif paling atas saat ini: '{self.peek()}'")  # Intip kembali halaman teratas yang baru saja dimasukkan
        print(f"[STATUS] Tumpukan Saat Ini: {self.display()}")  # Tampilkan seluruh isi list stack terbaru setelah ditambah halaman baru
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi
        
        input("\n👉 [INTERAKTIF] Tekan ENTER untuk simulasi menekan tombol KEMBALI... ")  # Menahan layar demi interaksi menanti enter dari user
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        # 4. Simulasi Tombol Kembali / Back (Pop)
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")  # Beri tahu aksi tombol kembali mulai dijalankan sistem
        try:  # Membuka blok proteksi try untuk menghindari program menu utama crash mendadak
            halaman_keluar = self.pop()  # Mengeluarkan halaman teratas menggunakan fungsi pop dan ditampung variabel
            print(f"[POP]    Keluar dari: '{halaman_keluar}'")  # Tampilkan halaman yang berhasil dibuang dari list riwayat
            print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")  # Tampilkan halaman aktif setelah sukses mundur satu langkah
            print(f"[STATUS] Sisa Tumpukan: {self.display()}")  # Tampilkan sisa elemen halaman di dalam list stack saat ini
        except IndexError as e:  # Menangkap error jika ternyata list stack kedapatan sudah kosong total
            print(f"[HANDLE ERROR] {e}")  # Cetak pesan error halus ke layar terminal tanpa mematikan program utama
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi
        
        input("\n👉 [INTERAKTIF] Tekan ENTER untuk proses Back berurutan (Mundur ke Pencarian)... ")  # Menahan layar demi interaksi menanti enter dari user
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        # 5. User keluar dari halaman detail produk dengan back navigasi berurutan
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")  # Beri tahu aksi tombol kembali dijalankan kembali oleh user
        try:  # Membuka blok proteksi try untuk menghindari program menu utama crash mendadak
            halaman_keluar = self.pop()  # Mengeluarkan halaman teratas menggunakan fungsi pop untuk kedua kalinya di simulasi
            print(f"[POP]    Keluar dari: '{halaman_keluar}'")  # Tampilkan halaman detail produk yang berhasil dibuang dari riwayat
            print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")  # Tampilkan halaman aktif yang kini menjadi tumpukan paling atas kembali
            print(f"[STATUS] Sisa Tumpukan: {self.display()}")  # Tampilkan sisa elemen halaman yang masih ada di dalam memori list
        except IndexError as e:  # Menangkap error jika ternyata list stack kedapatan sudah kosong total
            print(f"[HANDLE ERROR] {e}")  # Cetak pesan error halus ke layar terminal tanpa mematikan program utama
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        input("\n👉 [INTERAKTIF] Tekan ENTER untuk proses Back berurutan (Mundur ke Beranda)... ")  # Menahan layar demi interaksi menanti enter dari user
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        # 6. User keluar dari halaman pencarian hingga tersisa beranda saja di dalam list
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")  # Beri tahu aksi tombol kembali dijalankan lagi untuk ketiga kalinya
        try:  # Membuka blok proteksi try untuk menghindari program menu utama crash mendadak
            halaman_keluar = self.pop()  # Mengeluarkan halaman teratas menggunakan fungsi pop ketiga kalinya di simulasi ini
            print(f"[POP]    Keluar dari: '{halaman_keluar}'")  # Tampilkan halaman hasil pencarian sepatu yang resmi dibuang dari list
            print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")  # Tampilkan halaman beranda shopee sebagai pertahanan halaman terakhir aplikasi
            print(f"[STATUS] Sisa Tumpukan: {self.display()}")  # Tampilkan sisa elemen yang kini tinggal menyisakan beranda shopee saja
        except IndexError as e:  # Menangkap error jika ternyata list stack kedapatan sudah kosong total
            print(f"[HANDLE ERROR] {e}")  # Cetak pesan error halus ke layar terminal tanpa mematikan program utama
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        input("\n👉 [INTERAKTIF] Tekan ENTER untuk mencoba memaksa Back saat sudah di Beranda... ")  # Menahan layar demi interaksi menanti enter dari user
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi

        # 7. Mencoba mengeluarkan Beranda Shopee (Uji coba penanganan tumpukan kosong)
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")  # Beri tahu aksi tombol kembali dijalankan paksa saat di beranda utama
        try:  # Membuka blok proteksi try untuk menghindari program menu utama crash mendadak
            halaman_keluar = self.pop()  # Mengeluarkan halaman beranda menggunakan fungsi pop keempat kalinya (memicu kondisi kosong)
            print(f"[POP]    Keluar dari: '{halaman_keluar}'")  # Bagian ini otomatis tidak akan berjalan karena langsung terpicu error
            print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")  # Bagian ini otomatis tidak akan berjalan karena langsung terpicu error
            print(f"[STATUS] Sisa Tumpukan: {self.display()}")  # Bagian ini otomatis tidak akan berjalan karena langsung terpicu error
        except IndexError as e:  # Menangkap error karena list kosong berhasil dideteksi dengan baik oleh fungsi is_empty()
            print(f"[HANDLE ERROR] {e}")  # Sukses menampilkan pesan rahasia handle error pop dari stack kosong tanpa membuat program mati
        print("-" * 50)  # Cetak garis pembatas putus-putus antar langkah simulasi
        
        print("==================================================")  # Cetak garis pembatas penutup sesi keseluruhan simulasi interaktif stack
        0
        