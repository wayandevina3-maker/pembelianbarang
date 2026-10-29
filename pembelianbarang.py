print("=== PROGRAM PEMBELIAN BARANG ===")

print("\nDAFTAR BARANG")
print("1. Buku tulis  - Rp5.000")
print("2. Pulpen      - Rp3.000")
print("3. Pensil      - Rp2.000")
print("4. Penghapus   - Rp2.000")
print("5. Penggaris   - Rp4.000")

pilihan = int(input("\nPilih nomor barang              : "))

if pilihan == 1:
    barang = "Buku tulis"
    harga = 5000
elif pilihan == 2:
    barang = "Pulpen"
    harga = 3000
elif pilihan == 3:
    barang = "Pensil"
    harga = 2000
elif pilihan == 4:
    barang = "Penghapus"
    harga = 2000
elif pilihan == 5:
    barang = "Penggaris"
    harga = 4000
else:
    print("Nomor barang tidak tersedia!")
    exit()

jumlah = int(input("Masukkan jumlah barang          : "))

total = harga * jumlah

diskon = jumlah >= 3 or total >= 100000

member = input("Apakah Anda member? (ya/tidak)  : ").lower() == "ya"
diskon_member = diskon and member

tidak_diskon = not diskon

if diskon:
    potongan = total * 10 / 100
else:
    potongan = 0

bayar = total - potongan

print("\n======= STRUK PEMBELIAN =======")
print("Nama barang        :", barang)
print("Harga satuan       : Rp", harga)
print("Jumlah barang      :", jumlah)
print("Total harga        : Rp", total)
print("Diskon             : 10%" if diskon else "Diskon             : 0%")
print("Potongan harga     : Rp", int(potongan))
print("Total pembayaran   : Rp", int(bayar))
print("Member             :", member)
print("Diskon member      :", diskon_member)
print("Tidak dapat diskon :", tidak_diskon)

if diskon:
    print("Selamat, Anda mendapat diskon!")
else:
    print("Maaf, Anda tidak mendapat diskon.")