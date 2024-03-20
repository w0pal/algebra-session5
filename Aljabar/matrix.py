# Fungsi untuk membuat matriks
def buat_matriks(bar, kol):
    matriks = []
    for i in range(bar):
        row = []
        for j in range(kol):
            row.append(0)  # Isi matriks dengan nilai awal 0
        matriks.append(row)
    return matriks

# Fungsi untuk mencetak matriks
def cetak_matriks(matriks):
    for row in matriks:
        print(row)

# Fungsi untuk penjumlahan dua matriks
def tambah_matriks(matriks1, matriks2):
    hasil = []
    for i in range(len(matriks1)):
        row = []
        for j in range(len(matriks1[0])):
            row.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(row)
    return hasil

# Fungsi untuk perkalian dua matriks
def kali_matriks(matriks1, matriks2):
    hasil = []
    for i in range(len(matriks1)):
        row = []
        for j in range(len(matriks2[0])):
            total = 0
            for k in range(len(matriks2)):
                total += matriks1[i][k] * matriks2[k][j]
            row.append(total)
        hasil.append(row)
    return hasil

# Contoh penggunaan
matriks1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matriks2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

print("Matriks 1:")
cetak_matriks(matriks1)

print("\nMatriks 2:")
cetak_matriks(matriks2)

print("\nPenjumlahan Matriks:")
hasil_tambah = tambah_matriks(matriks1, matriks2)
cetak_matriks(hasil_tambah)

print("\nPerkalian Matriks:")
hasil_kali = kali_matriks(matriks1, matriks2)
cetak_matriks(hasil_kali)
