# E-Commerce Logic System Simulation (CLI)
**Tugas Akhir Semester (UAS) Mata Kuliah Struktur Data - Universitas Teknologi Bandung**

## Deskripsi Proyek
Proyek ini merupakan simulasi sistem logika *backend* dari platform *e-commerce* (terinspirasi dari arsitektur fitur Shopee) yang diimplementasikan menggunakan **Python berbasis Command-Line Interface (CLI)**. 

Fokus utama dari pengembangan aplikasi ini adalah penerapan dan pengintegrasian berbagai **Struktur Data Linear dan Non-Linear** serta **Algoritma Pencarian & Pengurutan** secara manual menggunakan prinsip Object-Oriented Programming (OOP) tanpa bergantung pada *library* eksternal untuk struktur intinya.

Setiap struktur data yang digunakan bukan sekadar ditempelkan, melainkan memiliki justifikasi logis yang merepresentasikan penyelesaian masalah pada dunia nyata di dalam sistem belanja *online*.

## ⚙️ Integrasi Struktur Data & Algoritma
Berikut adalah pemetaan logika sistem dan struktur data yang kami bangun di dalam proyek ini:

### 1. Struktur Data Penyimpanan & Indeks
* **Array (ArrayList):** Berfungsi sebagai basis data (katalog) utama untuk menyimpan seluruh objek `Product` secara berurutan.
* **Binary Search Tree (BST):** Diimplementasikan sebagai indeks filter harga. Memungkinkan pengguna mencari dan menampilkan produk dalam rentang harga tertentu secara optimal melalui *in-order traversal*.

### 2. Fitur Transaksi & Keranjang Belanja
* **Doubly Linked List:** Menangani sistem Keranjang Belanja (*Cart*). Pengguna dapat dengan mudah menambah, menavigasi, dan menghapus barang tertentu dari tengah keranjang sebelum melakukan proses *checkout*.
* **Queue (Antrian):** Menangani simulasi *Checkout* pesanan atau *Flash Sale* dengan prinsip FIFO (*First In First Out*), memastikan pesanan pertama diproses lebih awal.

### 3. Logistik & Navigasi Antarmuka
* **Stack (Tumpukan):** Mengelola riwayat navigasi antarmuka CLI (*Back Navigation*) dan mengaktifkan fitur *Undo* jika pengguna membatalkan penambahan barang ke keranjang.
* **Graph (Adjacency List/Matrix):** Mensimulasikan rute pengiriman paket (Shopee Express). Menggunakan algoritma *Shortest Path* untuk menentukan jarak tempuh terpendek dan estimasi ongkos kirim antarkota.

### 4. Algoritma Pencarian & Pengurutan (Searching & Sorting)
* **Binary Search:** Melakukan pencarian spesifik terhadap nama atau ID Produk di dalam katalog secara efisien dengan kompleksitas waktu yang rendah.
* **Quick Sort:** Menyortir katalog produk secara dinamis berdasarkan urutan **Harga Termurah hingga Termahal**.
* **Merge Sort / Bubble Sort:** Menyortir katalog produk berdasarkan **Rating Produk Tertinggi**.

## Panduan Instalasi & Eksekusi Program

Program ini dapat dijalankan pada terminal atau *command prompt* tanpa memerlukan instalasi *library* tambahan. Seluruh modul dibuat menggunakan standar bawaan Python.
1. **Clone repositori ini ke dalam direktori lokal Anda:**
```bash
   git clone [https://github.com/username-kalian/nama-repo-kalian.git](https://github.com/username-kalian/nama-repo-kalian.git)
```
2. Masuk ke dalam folder proyek:
```Bash
   cd nama-repo-kalian
```
Jalankan program utama:
```Bash
   python main.py
```
Catatan: Program sudah dilengkapi dengan Mock Data (Data Tiruan) untuk katalog produk, sehingga fitur pencarian, filter, dan keranjang dapat langsung diuji coba saat program dijalankan.

## Pengujian Sistem (Unit Testing)

Untuk memastikan integritas setiap struktur data dan ketepatan algoritma yang kami bangun, sistem ini dilengkapi dengan pengujian otomatis (*Automated Testing*) menggunakan *library* bawaan Python, yakni `unittest`. Pengujian mencakup validasi operasi CRUD pada struktur data dasar hingga akurasi algoritma *Sorting* dan *Shortest Path*.

**Langkah-langkah menjalankan Unit Test:**
Pastikan Anda berada di direktori utama repositori (*root folder*). Anda tidak perlu menginstal *library* tambahan apa pun.

**Menjalankan semua test sekaligus:**
   Untuk mengeksekusi seluruh skenario pengujian yang ada di dalam folder `tests/`, jalankan perintah berikut di terminal:
   ```bash
   python -m unittest discover -v
   ```
(Flag -v atau verbose digunakan agar terminal menampilkan rincian dari setiap fungsi yang sedang diuji).

Menjalankan pengujian pada modul spesifik:
Jika hanya ingin menguji satu bagian logika tertentu (misalnya logika Linked List untuk fitur keranjang belanja), gunakan perintah berikut:

```Bash
python -m unittest tests/test_linkedlist_graph.py
```

***

### Penyesuaian Struktur Folder

Agar perintah `python -m unittest discover` di atas bisa berjalan dengan mulus tanpa *error*, pastikan kamu mengarahkan tim (khususnya anggota yang bertugas sebagai *QA & Analyst*) untuk membuat satu folder khusus bernama `tests` di dalam repositori utama.

Struktur repositori akhirnya akan terlihat sangat profesional seperti ini:

```text
📁 UAS_StrukturData/
│
├── 📁 tests/                     # 👈 Folder khusus unit test
│   ├── __init__.py               # File kosong agar Python mengenali folder ini sebagai modul
│   ├── test_queue_search.py      # Pengujian logic milik Wafi
│   ├── test_stack_sorting.py     # Pengujian logic milik Haris
│   ├── test_tree_array.py        # Pengujian logic milik Hafidz
│   └── test_linkedlist_graph.py  # Pengujian logic milik Galang
│
├── models.py              
├── queue_search.py        
├── stack_sorting.py       
├── tree_array.py          
├── linkedlist_graph.py    
├── main.py                
└── README.md
```

## 👨‍💻 Tim Pengembang (Kelompok)
Sistem ini dirancang dan dikembangkan secara kolaboratif dengan pembagian tugas spesifik berdasarkan modul Class masing-masing:
1. Wafi – Queue (Flash Sale), Binary Search (Product Find), CLI Architecture Integrator
2. Haris – Stack (Navigation History), Quick Sort (Price Filter), Merge Sort (Rating Filter)
3. Hafidz – Binary Tree (Price Range Indexing), ArrayList (Core Database Catalog)
4. Galang – Doubly Linked List (Cart Management), Graph (Logistics Routing)
