import csv
import os

FILE = "data.csv"

# ===============================
# INPUT ANGKA (VALIDASI)
# ===============================
def input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit():
            return nilai
        else:
            print("❌ Harus angka!")

# ===============================
# BACA DATA CSV
# ===============================
def baca_data():
    data = []
    if os.path.exists(FILE):
        with open(FILE, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data

# ===============================
# SIMPAN DATA CSV
# ===============================
def simpan_data(data):
    with open(FILE, mode="w", newline="") as f:
        fieldnames = ["kode", "weekly", "qty"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# ===============================
# CREATE
# ===============================
def tambah_barang():
    kode = input("Kode barang: ")
    weekly = input("Weekly: ")
    qty = input_angka("Qty: ")

    data = baca_data()

    # CEK KODE DOUBLE
    for d in data:
        if d["kode"] == kode:
            print("❌ Kode barang sudah ada!")
            return

    data.append({
        "kode": kode,
        "weekly": weekly,
        "qty": qty
    })

    simpan_data(data)
    print("✅ Barang berhasil ditambahkan")

# ===============================
# READ
# ===============================
def lihat_barang():
    data = baca_data()
    if not data:
        print("📦 Data kosong")
        return

    print("\nDAFTAR BARANG")
    print("-" * 40)
    for d in data:
        print(f"{d['kode']} | Weekly: {d['weekly']} | Qty: {d['qty']}")

# ===============================
# UPDATE
# ===============================
def update_qty():
    kode = input("Masukkan kode barang: ")
    data = baca_data()

    for d in data:
        if d["kode"] == kode:
            d["qty"] = input_angka("Qty baru: ")
            simpan_data(data)
            print("🔄 Qty berhasil diupdate")
            return

    print("❌ Barang tidak ditemukan")

# ===============================
# DELETE
# ===============================
def hapus_barang():
    kode = input("Masukkan kode barang: ")
    data = baca_data()

    data_baru = [d for d in data if d["kode"] != kode]

    if len(data) == len(data_baru):
        print("❌ Barang tidak ditemukan")
    else:
        simpan_data(data_baru)
        print()
