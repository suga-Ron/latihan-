import json
import os

# Nama file penyimpanan
FILE_DATA = "data_inventaris.json"

# Fungsi untuk memuat data dari file
def muat_data():
    if not os.path.exists(FILE_DATA):
        return {}
    with open(FILE_DATA, 'r') as file:
        return json.load(file)

# Fungsi untuk menyimpan data ke file
def simpan_data(data):
    with open(FILE_DATA, 'w') as file:
        json.dump(data, file, indent=4)

# Memuat data saat program dimulai
inventory = muat_data()

def tambah_barang():
    id_barang = input("Masukkan ID Barang: ")
    nama = input("Masukkan Nama Barang: ")
    jumlah = int(input("Masukkan Jumlah: "))
    
    inventory[id_barang] = {
        "nama": nama,
        "jumlah": jumlah
    }
    simpan_data(inventory) # Simpan setiap ada perubahan
    print(f"Barang {nama} berhasil ditambahkan/diupdate.")

def lihat_inventory():
    print("\n--- Data Inventaris Gudang ---")
    if not inventory:
        print("Gudang kosong.")
    else:
        print(f"{'ID':<10} | {'Nama Barang':<20} | {'Jumlah':<10}")
        print("-" * 45)
        for id_barang, data in inventory.items():
            print(f"{id_barang:<10} | {data['nama']:<20} | {data['jumlah']:<10}")
    print("-----------------------------\n")

def hapus_barang():
    id_barang = input("Masukkan ID Barang yang akan dihapus: ")
    if id_barang in inventory:
        del inventory[id_barang]
        simpan_data(inventory) # Simpan setelah menghapus
        print("Barang berhasil dihapus.")
    else:
        print("ID Barang tidak ditemukan.")

# Menu Utama
while True:
    print("Menu:")
    print("1. Tambah/Update Barang")
    print("2. Lihat Inventaris")
    print("3. Hapus Barang")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        lihat_inventory()
    elif pilihan == "3":
        hapus_barang()
    elif pilihan == "4":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")