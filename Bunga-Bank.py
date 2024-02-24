# Script python sederhana untuk menghitung bunga dalam sistem perbankan
# https://github.com/anon9497

# Fungsi untuk menghitung bunga sederhana
def bunga_sederhana(p, r, t):
    # p = pokok pinjaman
    # r = suku bunga per tahun (dalam persen)
    # t = waktu pinjaman (dalam tahun)
    return p * r * t / 100

# Fungsi untuk menghitung bunga majemuk
def bunga_majemuk(p, r, t, n):
    # p = pokok pinjaman
    # r = suku bunga per tahun (dalam persen)
    # t = waktu pinjaman (dalam tahun)
    # n = jumlah periode bunga per tahun
    return p * (1 + r / n) ** (n * t)

# Fungsi untuk menghitung bunga anuitas
def bunga_anuitas(p, r, n):
    # p = pokok pinjaman
    # r = suku bunga per periode (dalam persen)
    # n = jumlah periode pinjaman
    return p * r * (1 + r) ** n / ((1 + r) ** n - 1)

# Program utama
print("Selamat datang di Aplikasi Perhitungan Bunga!")
print("Silakan pilih jenis bunga yang ingin dihitung:")
print("1. Bunga Sederhana")
print("2. Bunga Majemuk")
print("3. Bunga Anuitas")
pilih = int(input("Masukkan pilihan Anda (1/2/3): "))
if pilih == 1: # Jika memilih bunga sederhana
    p = float(input("Masukkan pokok pinjaman: "))
    r = float(input("Masukkan suku bunga per tahun (dalam persen): "))
    t = float(input("Masukkan waktu pinjaman (dalam tahun): "))
    b = bunga_sederhana(p, r, t) # Panggil fungsi bunga sederhana
    print("Bunga yang harus dibayar adalah", b, "rupiah")
elif pilih == 2: # Jika memilih bunga majemuk
    p = float(input("Masukkan pokok pinjaman: "))
    r = float(input("Masukkan suku bunga per tahun (dalam persen): "))
    t = float(input("Masukkan waktu pinjaman (dalam tahun): "))
    n = int(input("Masukkan jumlah periode bunga per tahun: "))
    b = bunga_majemuk(p, r, t, n) # Panggil fungsi bunga majemuk
    print("Bunga yang harus dibayar adalah", b, "rupiah")
elif pilih == 3: # Jika memilih bunga anuitas
    p = float(input("Masukkan pokok pinjaman: "))
    r = float(input("Masukkan suku bunga per periode (dalam persen): "))
    n = int(input("Masukkan jumlah periode pinjaman: "))
    b = bunga_anuitas(p, r, n) # Panggil fungsi bunga anuitas
    print("Angsuran yang harus dibayar setiap periode adalah", b, "rupiah")
else: # Jika memilih selain 1, 2, atau 3
    print("Pilihan tidak valid!")
