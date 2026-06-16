# stack.py
# karena ini mempresentasikan riwayat navigasi, aku tidak memakai models.py yang dibuat hafidz,
# karna models.py nya hanya memuat Produk
# Jadi aku inisialisasi data navigasinya sendiri 

class Stack: #Memakai OOP sesuai point B.3
    def __init__(self): #bikin inti diri sendiri dari kelas stack
        # Menggunakan list standar sebagai penyimpanan internal (inti struktur diatur manual)
        self.__storage = ["Beranda Shopee", "Pulsa, Tagihan & Tiket", "Tv Kabel & Internet", "Biznet Home"] #isinya list kosong

    def push(self, item): #bikin attribut .push 
        #Menambahkan elemen ke tumpukan paling atas.
        self.__storage.append(item) #pake .append

    def pop(self): #bikin attribut .pop
        #Menghapus dan mengembalikan elemen dari tumpukan paling atas.
        if self.is_empty(): #cek dlu apakah listnya kosong atau ada isinyaa
            raise IndexError("Pop dari Stack yang kosong!") #ini untuk handle errornyaaa
        return self.__storage.pop() # kalau tidak kosong, langsung di pop

    def peek(self): #bikin attribut .peek
        # Melihat elemen teratas tanpa menghapusnya.
        if self.is_empty(): #cek dlu apakah listnya kosong atau ada isinya
            return None # jika kosong, mengembalikan nilai kosong juga
        return self.__storage[-1] #ini logic di pythonnya, pake -1 untuk melihat elemen terakhir

    def is_empty(self): #bikin attribut .is_empty
        #Memeriksa apakah stack kosong.
        return len(self.__storage) == 0 #akan menghasilkan nilai true
 
    def size(self): #bikin attribut .size
        #Mengembalikan jumlah elemen di dalam stack.
        return len(self.__storage) #ini akan hitung elemen dengan fungsi len()

    def display(self): #bikin attribut .display
        #Mengembalikan list salinan untuk kebutuhan visualisasi CLI.
        return list(self.__storage) # mengembalikan nilai listnya

    def info(self): #bikin attribut .info
        return ("""
        Konteks: Seorang user hendak top up internet biznet home
        melalui aplikasi shopee\n""") #ini sebagai konteks awal

    def riwayatnavigasi(self): #ini sengaja dibuat langsung, agar untuk pemanggilannya hanya menggunakan Stack.riwayatnavigasi
        """Menjalankan seluruh simulasi Stack secara otomatis"""
        print(self.info())
        print("==================================================")
        print("       SIMULASI OTOMATIS FITUR NAVIGASI (STACK)   ")
        print("==================================================")
        
        # 1. Menampilkan data awal (Display)
        print(f"[STATUS] Alur Halaman Terbuka Saat Ini:\n  --> " + " -> ".join(self.display()))
        
        # 2. Mengintip halaman teratas (Peek)
        print(f"[PEEK]   User sedang melihat halaman: '{self.peek()}'")
        print("-" * 50)
        
        # 3. Simulasi Tombol Kembali / Back (Pop)
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")
        halaman_keluar = self.pop()
        print(f"[POP]    Keluar dari: '{halaman_keluar}'")
        print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")
        print(f"[STATUS] Sisa Tumpukan: {self.display()}")
        print("-" * 50)
        
        # 4. Simulasi Navigasi ke Halaman Baru Lagi (Push)
        halaman_baru = "Metode Pembayaran (ShopeePay)" #diawal hanya sampai biznet home, dsini ditambahkan navigasi baru
        print(f"[AKSI]   User klik lanjut untuk bayar. Masuk halaman baru --->")
        self.push(halaman_baru)
        print(f"[PUSH]   Berhasil masuk ke: '{halaman_baru}'")
        print(f"[PEEK]   Halaman aktif paling atas saat ini: '{self.peek()}'")
        print(f"[STATUS] Tumpukan Akhir: {self.display()}")
        print("-" * 50)
        
        # 5. Urusan Top up selesai, user keluar dari shopee dengan back navigasi berurutan
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")
        halaman_keluar = self.pop()
        print(f"[POP]    Keluar dari: '{halaman_keluar}'")
        print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")
        print(f"[STATUS] Sisa Tumpukan: {self.display()}")
        print("-" * 50)

        # 5. Urusan Top up selesai, user keluar dari shopee dengan back navigasi berurutan
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")
        halaman_keluar = self.pop()
        print(f"[POP]    Keluar dari: '{halaman_keluar}'")
        print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")
        print(f"[STATUS] Sisa Tumpukan: {self.display()}")
        print("-" * 50)

        # 6. Urusan Top up selesai, user keluar dari shopee dengan back navigasi berurutan
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")
        halaman_keluar = self.pop()
        print(f"[POP]    Keluar dari: '{halaman_keluar}'")
        print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")
        print(f"[STATUS] Sisa Tumpukan: {self.display()}")
        print("-" * 50)
        
        # 7. Urusan Top up selesai, user keluar dari shopee dengan back navigasi berurutan
        print("[AKSI]   User menekan tombol 'KEMBALI' (Back) <---")
        halaman_keluar = self.pop()
        print(f"[POP]    Keluar dari: '{halaman_keluar}'")
        print(f"[PEEK]   Sekarang user mundur ke halaman: '{self.peek()}'")
        print(f"[STATUS] Sisa Tumpukan: {self.display()}")
        print("-" * 50)
        
        print("==================================================")