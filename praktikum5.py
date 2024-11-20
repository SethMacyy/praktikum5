def hitung_nilai_akhir(tugas, uts, uas):
    return round((0.4 * tugas) + (0.3 * uts) + (0.3 * uas), 2)

data_mahasiswa = []

while True:
    print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]:", end=" ")
    pilihan = input().lower()

    if pilihan == 't':  # Tambah data
        print("\nTambah Data")
        nim = input("NIM     : ")
        nama = input("Nama    : ")
        nilai_uts = int(input("Nilai UTS : "))
        nilai_uas = int(input("Nilai UAS : "))
        nilai_tugas = int(input("Nilai Tugas : "))

        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
        data_mahasiswa.append({
            "nim": nim,
            "nama": nama,
            "uts": nilai_uts,
            "uas": nilai_uas,
            "tugas": nilai_tugas,
            "akhir": nilai_akhir
        })

    elif pilihan == 'l':  # Lihat data
        print("\nDaftar Nilai")
        print("="*70)
        print("| NO |    NIM    |     NAMA     | TUGAS | UTS | UAS |  AKHIR  |")
        print("="*70)
        for i, mhs in enumerate(data_mahasiswa, start=1):
            print(f"| {i:2} | {mhs['nim']:10} | {mhs['nama']:12} | {mhs['tugas']:5} | {mhs['uts']:3} | {mhs['uas']:3} | {mhs['akhir']:7.2f} |")
        print("="*70)

    elif pilihan == 'k':  # Keluar
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
