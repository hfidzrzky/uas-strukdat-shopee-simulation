import os
import sys

#Struktur data dan algoritma 
from features.queue_search import (        # Wafi
    Queue,
    binary_search_by_id,
    binary_search_by_name,
    sort_by_id,
    sort_by_name,
)
from features.array_list import ProductDatabase, print_table  # Hafidz
from features.quick_sort import QuickSortFitur                # Haris
<<<<<<< HEAD
from features.bubble_sort import BubbleSortFitur              # Haris
from features.stack import Stack                              # Haris
from features.linkedlist import KeranjangBelanja             # Galang
from features.graph import Graph                              # Galang


# TAMPILAN CLI 

=======
from features.merge_sort import MergeSortFitur              # Haris
from features.stack import Stack                              # Haris
from features.linkedlist import KeranjangBelanja             # Galang
from features.graph import Graph                              # Galang
stack = Stack()
kamus_menu = {}

# TAMPILAN CLI 
>>>>>>> main
class C:
    # Kumpulan kode warna ANSI untuk mempercantik output terminal
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    MERAH = "\033[91m"
    HIJAU = "\033[92m"
    KUNING = "\033[93m"
    BIRU = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    PUTIH = "\033[97m"
    ABU = "\033[90m"

<<<<<<< HEAD

=======
>>>>>>> main
def enable_ansi():
    # Mengaktifkan pewarnaan ANSI
    if os.name == "nt":
        os.system("")
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

<<<<<<< HEAD

=======
>>>>>>> main
def clear_screen():
    # Membersihkan layar terminal lintas platform
    os.system("cls" if os.name == "nt" else "clear")

<<<<<<< HEAD

=======
>>>>>>> main
def warna(teks, *kode):
    # Membungkus teks dengan satu/lebih kode warna lalu mereset di akhir
    return "".join(kode) + str(teks) + C.RESET

<<<<<<< HEAD

=======
>>>>>>> main
def banner():
    logo = r"""
   ____  _   _  ___  ____  ____  _____   ____ ___ __  __
  / ___|| | | |/ _ \|  _ \| ____|| ____| / ___|_ _|  \/  |
  \___ \| |_| | | | | |_) |  _|  |  _|   \___ \| || |\/| |
   ___) |  _  | |_| |  __/| |___ | |___   ___) | || |  | |
  |____/|_| |_|\___/|_|   |_____||_____| |____/___|_|  |_|
"""
    print(warna(logo, C.BOLD, C.KUNING))
    print(warna("        Simulasi Sistem Belanja Online - Struktur Data",
                C.CYAN))
    print(warna("        UAS Struktur Data | Tim: Wafi, Haris, Hafidz, Galang",
                C.ABU))

<<<<<<< HEAD

def garis(char="─", panjang=60, kode=C.ABU):
    print(warna(char * panjang, kode))


=======
def garis(char="─", panjang=60, kode=C.ABU):
    print(warna(char * panjang, kode))

>>>>>>> main
def header(judul, ikon=""):
    teks = f"{ikon}  {judul}" if ikon else judul
    lebar = 58
    print()
    print(warna("╔" + "═" * lebar + "╗", C.CYAN))
    print(warna("║", C.CYAN) + warna(f" {teks:<{lebar - 1}}", C.BOLD, C.PUTIH)
          + warna("║", C.CYAN))
    print(warna("╚" + "═" * lebar + "╝", C.CYAN))

<<<<<<< HEAD

def opsi(kode, label, ikon="", badge=""):
=======
def opsi(kode, label, ikon="", badge=""):
    kamus_menu[str(kode)] = label
>>>>>>> main
    nomor = warna(f"  [{kode}]", C.BOLD, C.KUNING)
    ikon_txt = f" {ikon} " if ikon else " "
    print(f"{nomor}{ikon_txt} {label}{badge}")

<<<<<<< HEAD

def sukses(pesan):
    print(warna(f"  ✔ {pesan}", C.HIJAU))


def gagal(pesan):
    print(warna(f"  ✖ {pesan}", C.MERAH))


def info(pesan):
    print(warna(f"  • {pesan}", C.KUNING))


def pause():
    input(warna("\n  Tekan Enter untuk kembali ke menu...", C.DIM))


def tanya(prompt):
    return input(warna(prompt, C.PUTIH)).strip()


def tanya_pilihan(prompt="\n  ➤ Pilih menu: "):
    return input(warna(prompt, C.CYAN)).strip()


=======
def sukses(pesan):
    print(warna(f"  ✔ {pesan}", C.HIJAU))

def gagal(pesan):
    print(warna(f"  ✖ {pesan}", C.MERAH))

def info(pesan):
    print(warna(f"  • {pesan}", C.KUNING))

def pause():
    input(warna("\n  Tekan Enter untuk kembali ke menu...", C.DIM))

def tanya(prompt):
    return input(warna(prompt, C.PUTIH)).strip()

def tanya_pilihan(prompt="\n  ➤ Pilih menu: "):
    return input(warna(prompt, C.CYAN)).strip()

>>>>>>> main
def tanya_int(prompt):
    nilai = tanya(prompt)
    try:
        return int(nilai)
    except ValueError:
        gagal("Input harus berupa angka.")
        return None

<<<<<<< HEAD

def tanya_id(prompt):
    return tanya(prompt).upper()


=======
def tanya_id(prompt):
    return tanya(prompt).upper()

>>>>>>> main
# ============================================================================
# HELPER TAMPILAN PRODUK dan STRUKTUR
# ============================================================================

def tampilkan_produk(judul, products):
    # Menampilkan daftar produk
    print_table(judul, products)

def tampilkan_struktur_queue(antrian):
    # Memvisualkan isi Queue sebagai alur FIFO (depan -> belakang)
    header("STRUKTUR ANTRIAN (Queue - FIFO)", "🧱")
    antrean = antrian.display()
    if not antrean:
        info("Antrian kosong. Belum ada pesanan yang di-checkout.")
        return

    kotak = [warna(f"[ {p.nama} ]", C.BOLD, C.CYAN) for p in antrean]
    rantai = warna("  →  ", C.ABU).join(kotak)
    print()
    print("  " + warna("DEPAN", C.HIJAU) + warna("  ⟶  ", C.ABU)
          + rantai + warna("  ⟶  ", C.ABU) + warna("BELAKANG", C.MERAH))
    print("  " + warna("(keluar duluan / dequeue)", C.DIM)
          + " " * 6 + warna("(masuk terakhir / enqueue)", C.DIM))
    print()
    info(f"Jumlah elemen: {antrian.size()}")
    info(f"Front (dilayani berikutnya): {antrian.front().nama}")

<<<<<<< HEAD

=======
>>>>>>> main
def bangun_graph_pengiriman():
    # Menyiapkan graph rute logistik antar-kota gudang (mock data demo)
    g = Graph()
    rute = [
        ("Jakarta", "Bandung", 150),
        ("Jakarta", "Semarang", 450),
        ("Bandung", "Semarang", 370),
        ("Semarang", "Yogyakarta", 110),
        ("Semarang", "Surabaya", 310),
        ("Yogyakarta", "Surabaya", 330),
        ("Bandung", "Yogyakarta", 400),
    ]
    for kota_asal, kota_tujuan, jarak in rute:
        g.tambah_rute(kota_asal, kota_tujuan, jarak)
    return g

<<<<<<< HEAD

=======
>>>>>>> main
# ============================================================================
# MENU: KATALOG, PENCARIAN, CHECKOUT, FILTER HARGA
# ============================================================================

def menu_katalog(db):
    tampilkan_produk("KATALOG PRODUK", db.get_all_products())

<<<<<<< HEAD

=======
>>>>>>> main
def menu_pencarian(db):
    catalog = db.get_all_products()
    header("CARI PRODUK (Binary Search)", "🔍")
    opsi("1", "Cari berdasarkan ID (mis. P001)")
    opsi("2", "Cari berdasarkan Nama")
    opsi("0", "Kembali")
    pilihan = tanya_pilihan("\n  ➤ Pilih metode pencarian: ")

    if pilihan == "1":
        target = tanya_id("  Masukkan ID produk: ")
        hasil = binary_search_by_id(sort_by_id(catalog), target)
    elif pilihan == "2":
        target = tanya("  Masukkan nama produk: ")
        hasil = binary_search_by_name(sort_by_name(catalog), target)
    elif pilihan == "0":
        return
    else:
        gagal("Pilihan tidak valid.")
        return

    if hasil:
        sukses("Produk ditemukan!")
        tampilkan_produk("PRODUK DITEMUKAN", [hasil])
    else:
        gagal("Produk tidak ditemukan.")

<<<<<<< HEAD

=======
>>>>>>> main
def menu_filter_harga(db):
    header("FILTER RENTANG HARGA (BST In-Order)", "💰")
    min_harga = tanya_int("  Harga minimal (Rp): ")
    if min_harga is None:
        return
    max_harga = tanya_int("  Harga maksimal (Rp): ")
    if max_harga is None:
        return
    if min_harga > max_harga:
        gagal("Harga minimal tidak boleh lebih besar dari maksimal.")
        return

    hasil = db.filter_by_price(min_harga, max_harga)
    tampilkan_produk(f"HASIL FILTER: Rp{min_harga:,} - Rp{max_harga:,}", hasil)

<<<<<<< HEAD

=======
>>>>>>> main
def menu_checkout(db, antrian):
    catalog = db.get_all_products()
    header("ANTRIAN CHECKOUT (Queue / FIFO)", "🧾")
    opsi("1", "Masuk antrian checkout (enqueue)")
    opsi("2", "Proses pesanan terdepan (dequeue)")
    opsi("3", "Lihat antrian saat ini")
    opsi("4", "Lihat Struktur Queue (FIFO)")
    opsi("0", "Kembali")
    pilihan = tanya_pilihan("\n  ➤ Pilih aksi: ")
<<<<<<< HEAD

=======
    Stack(pilihan)
>>>>>>> main
    if pilihan == "1":
        target = tanya_id("  Masukkan ID produk yang ingin di-checkout: ")
        produk = binary_search_by_id(sort_by_id(catalog), target)
        if produk:
            antrian.enqueue(produk)
            sukses(f"'{produk.nama}' masuk antrian checkout.")
        else:
            gagal("Produk dengan ID tersebut tidak ada di katalog.")
    elif pilihan == "2":
        diproses = antrian.dequeue()
        if diproses:
            sukses(f"Memproses pesanan: {diproses.nama}")
        else:
            info("Antrian checkout kosong.")
    elif pilihan == "3":
        antrean = antrian.display()
        if not antrean:
            info("Antrian checkout kosong.")
        else:
            print(warna(f"\n  Total {antrian.size()} pesanan menunggu:",
                        C.BOLD, C.PUTIH))
            for i, p in enumerate(antrean, start=1):
                depan = warna(" (terdepan)", C.HIJAU) if i == 1 else ""
                print(f"   {warna(i, C.KUNING)}. {p.nama}{depan}")
    elif pilihan == "4":
        tampilkan_struktur_queue(antrian)
    elif pilihan == "0":
        return
    else:
        gagal("Pilihan tidak valid.")

<<<<<<< HEAD

=======
>>>>>>> main
# ============================================================================
# MENU: SORTING dan RIWAYAT NAVIGASI 
# ============================================================================

def menu_sorting():
    header("URUTKAN PRODUK (Sorting - modul Haris)", "↕")
    opsi("1", "Quick Sort (harga termurah)")
<<<<<<< HEAD
    opsi("2", "Bubble Sort (harga termurah)")
=======
    opsi("2", "Merge Sort (rating terendah)")
>>>>>>> main
    opsi("0", "Kembali")
    pilihan = tanya_pilihan("\n  ➤ Pilih algoritma: ")

    if pilihan == "1":
<<<<<<< HEAD
        QuickSortFitur().simulasi_sort()
    elif pilihan == "2":
        BubbleSortFitur().simulasi_sort()
=======
        stack("Sub-Menu: Quick Sort")
        QuickSortFitur().simulasi_sort()
    elif pilihan == "2":
        stack("Sub-Menu: Merge Sort")
        MergeSortFitur().simulasi_sort()
>>>>>>> main
    elif pilihan == "0":
        return
    else:
        gagal("Pilihan tidak valid.")

<<<<<<< HEAD

def menu_navigasi_stack():
    header("RIWAYAT NAVIGASI (Stack - modul Haris)", "🧭")
    Stack().riwayatnavigasi()
=======
def menu_navigasi_stack():
    header("RIWAYAT NAVIGASI (Stack - modul Haris)", "🧭")
    print(stack.cetak_riwayat())
>>>>>>> main


# ============================================================================
# MENU: KERANJANG (Linked List) dan PENGIRIMAN (Graph) 
# ============================================================================

def menu_keranjang(db, keranjang):
    header("KERANJANG BELANJA (Doubly Linked List - modul Galang)", "🛒")
    opsi("1", "Tambah barang ke keranjang")
    opsi("2", "Hapus barang dari keranjang")
    opsi("3", "Lihat isi keranjang")
    opsi("0", "Kembali")
    pilihan = tanya_pilihan("\n  ➤ Pilih aksi: ")

    catalog = db.get_all_products()
    if pilihan == "1":
        target = tanya_id("  Masukkan ID produk: ")
        produk = binary_search_by_id(sort_by_id(catalog), target)
        if not produk:
            gagal("Produk tidak ditemukan di katalog.")
            return
        jumlah = tanya_int("  Jumlah: ")
        if jumlah is None or jumlah < 1:
            gagal("Jumlah tidak valid.")
            return
        keranjang.tambah_barang(produk, jumlah)
    elif pilihan == "2":
        target = tanya_id("  Masukkan ID produk yang ingin dihapus: ")
        keranjang.hapus_barang(target)
    elif pilihan == "3":
        keranjang.tampilkan_keranjang()
    elif pilihan == "0":
        return
    else:
        gagal("Pilihan tidak valid.")

<<<<<<< HEAD

=======
>>>>>>> main
def menu_pengiriman():
    header("SIMULASI PENGIRIMAN (Graph / Dijkstra - modul Galang)", "🚚")
    g = bangun_graph_pengiriman()

    print(warna("  Kota gudang tersedia:", C.PUTIH))
    print("   " + ", ".join(sorted(g.graph.keys())))

    asal = tanya("\n  Kota asal: ").title()
    tujuan = tanya("  Kota tujuan: ").title()
    if asal not in g.graph or tujuan not in g.graph:
        gagal("Kota asal/tujuan tidak terdaftar.")
        return

    jarak, jalur = g.dijkstra(asal, tujuan)
    if not jalur:
        gagal("Tidak ada rute yang menghubungkan kedua kota.")
        return

    TARIF_PER_KM = 2500
    ongkir = jarak * TARIF_PER_KM
    print()
    sukses(f"Rute terpendek: {warna(' → '.join(jalur), C.BOLD, C.CYAN)}")
    info(f"Total jarak    : {jarak} km")
    info(f"Estimasi ongkir: Rp{ongkir:,} (Rp{TARIF_PER_KM:,}/km)")

<<<<<<< HEAD

=======
>>>>>>> main
# ============================================================================
# MENU UTAMA dan ALUR PROGRAM
# ============================================================================

def tampilkan_menu_utama(antrian):
    clear_screen()
    banner()
    header("MENU UTAMA", "🏬")

    badge_antrian = ""
    if not antrian.is_empty():
        badge_antrian = warna(f"  (antrian: {antrian.size()})", C.HIJAU)

    opsi("1", "Lihat Katalog Produk", "📦")
    opsi("2", "Cari Produk (Binary Search)", "🔍")
    opsi("3", "Urutkan Produk (Sorting)", "↕")
    opsi("4", "Filter Rentang Harga (BST)", "💰")
    opsi("5", "Keranjang Belanja (Linked List)", "🛒")
    opsi("6", "Checkout (Queue)", "🧾", badge=badge_antrian)
    opsi("7", "Simulasi Pengiriman (Graph)", "🚚")
    opsi("8", "Riwayat Navigasi (Stack)", "🧭")
    opsi("0", "Keluar", "🚪")
    garis()

<<<<<<< HEAD

=======
>>>>>>> main
def main():
    enable_ansi()
    db = ProductDatabase()
    antrian_checkout = Queue()
    keranjang = KeranjangBelanja()

    aksi = {
        "1": lambda: menu_katalog(db),
        "2": lambda: menu_pencarian(db),
        "3": lambda: menu_sorting(),
        "4": lambda: menu_filter_harga(db),
        "5": lambda: menu_keranjang(db, keranjang),
        "6": lambda: menu_checkout(db, antrian_checkout),
        "7": lambda: menu_pengiriman(),
        "8": lambda: menu_navigasi_stack(),
    }

    while True:
        tampilkan_menu_utama(antrian_checkout)
        pilihan = tanya_pilihan("  ➤ Pilih menu: ")

        if pilihan == "0":
<<<<<<< HEAD
=======
            stack(pilihan)
>>>>>>> main
            clear_screen()
            banner()
            print(warna(
                "\n  Terima kasih telah berbelanja. Sampai jumpa! 👋\n",
                C.BOLD, C.HIJAU))
            break

        handler = aksi.get(pilihan)
        if handler:
<<<<<<< HEAD
=======
            nama_terpilih = kamus_menu.get(pilihan, f"Menu {pilihan}")
            stack(nama_terpilih)
>>>>>>> main
            handler()
            pause()
        else:
            gagal("Pilihan tidak valid, coba lagi.")
            pause()

<<<<<<< HEAD

=======
>>>>>>> main
if __name__ == "__main__":
    main()
