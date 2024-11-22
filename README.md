# PRAKTIKUM 5

## Step 1 : Fungsi

![foto](ss/ss1.png)

Bagian pertama kode mendefinisikan sebuah fungsi bernama hitung_nilai_akhir. Fungsi ini memiliki tiga parameter: tugas, uts, dan uas, yang mewakili nilai tugas, nilai Ujian Tengah Semester (UTS), dan nilai Ujian Akhir Semester (UAS). Fungsi ini menggunakan rumus perhitungan nilai akhir: 
Nilai Akhir=(40%×Tugas)+(30%×UTS)+(30%×UAS)
Setelah nilai dihitung, fungsi menggunakan fungsi bawaan Python round untuk membulatkan hasilnya menjadi dua angka di belakang koma. Hasil akhir dikembalikan ke pemanggil fungsi.

## Step 2 : Variabel

![foto](ss/ss2.png)

Variabel data_mahasiswa adalah sebuah list kosong yang digunakan untuk menyimpan data mahasiswa. Nantinya, setiap data mahasiswa akan ditambahkan ke dalam list ini dalam bentuk dictionary (kamus). Setiap dictionary berisi informasi lengkap tentang mahasiswa, termasuk NIM, nama, nilai tugas, UTS, UAS, dan nilai akhir.

## Step 3 : Menu Utama (Perulangan While)

![foto](ss/ss3.png)

Bagian ini adalah inti dari program, berupa perulangan while yang terus berjalan hingga pengguna memilih untuk keluar dari program. Pada setiap iterasi, program menampilkan menu pilihan utama berupa beberapa opsi: Lihat, Tambah, Ubah, Hapus, Cari, dan Keluar. Pilihan pengguna diambil menggunakan fungsi input dan diubah menjadi huruf kecil (lower()) agar program bisa menangani input tanpa mempermasalahkan huruf besar atau kecil.

## Step 4 : Menambah Data 

![foto](ss/ss4.png)

Ketika pengguna memilih opsi Tambah Data ('t'), program meminta input untuk setiap data mahasiswa: NIM, Nama, Nilai UTS, Nilai UAS, dan Nilai Tugas. Data ini diinput satu per satu melalui fungsi input, kemudian nilai-nilai numerik (UTS, UAS, Tugas) diubah menjadi tipe integer menggunakan int().

Setelah semua data diterima, nilai akhir mahasiswa dihitung dengan memanggil fungsi hitung_nilai_akhir. Selanjutnya, data mahasiswa disimpan dalam dictionary yang berisi semua informasi tadi:

![foto](ss/ss5.png)

Dictionary ini kemudian ditambahkan ke list data_mahasiswa menggunakan fungsi append.

## Step 5 : Melihat Daftar Nilai

![foto](ss/ss6.png)

Jika pengguna memilih untuk Melihat Daftar Nilai ('l'), program mencetak judul tabel dan kolom-kolom data, yaitu: NO, NIM, Nama, Tugas, UTS, UAS, dan Nilai Akhir. Batas tabel ditandai dengan garis =.

Untuk setiap mahasiswa yang tersimpan di list data_mahasiswa, program mencetak data dalam format tabel menggunakan perulangan for:

## Step 6 : Keluar dari Program

![foto](ss/ss7.png)

Jika pengguna memilih Keluar ('k'), program mencetak pesan bahwa program telah selesai dan menggunakan perintah break untuk keluar dari perulangan while, sehingga program berhenti berjalan.

## Step 7 : Opsi Tidak Valid

![foto](ss/ss8.png)

Jika pengguna memasukkan pilihan yang tidak tersedia dalam menu (selain l, t, atau k), program akan memberikan pesan kesalahan sederhana dan kembali menampilkan menu.

## Step 8 : Run Program
Tahap akhir adalah uji coba code program yang sudah dibuat dengan mencoba berbagai kemungkinan yang ada.

### Case 1 : Menu Utama
Ketika program pertama kali dijalankan, akan muncul menu seperti ini:

![foto](ss/ss9.png)

### Case 2 : Tambah Data (T)
Jika Anda memilih opsi T untuk menambahkan data, program akan meminta Anda untuk mengisi informasi berikut:

![foto](ss/ss10.png)

### Case 3 : Lihat Data (L)
Jika Anda memilih opsi L untuk melihat data yang telah dimasukkan, output yang ditampilkan akan berupa tabel seperti berikut:

![foto](ss/ss11.png)

### Case 4 : Keluar Program (K)

Jika Anda memilih opsi K, program akan berhenti tanpa pesan tambahan.

### Case 5 : Error Handling (Input Tidak Valid)
Jika Anda memasukkan pilihan menu yang tidak valid, program akan menampilkan pesan seperti berikut dan kembali ke menu utama:

![foto](ss/ss12.png)

### Output :
Hasil dari output:

![foto](ss/ss13.png)

# Kesimpulan
Kesimpulan dari program ini adalah bahwa ia dirancang sebagai alat sederhana namun efektif untuk mengelola data mahasiswa. Program ini memungkinkan pengguna untuk menambahkan informasi mahasiswa, seperti NIM, nama, nilai tugas, UTS, dan UAS, sekaligus menghitung nilai akhir berdasarkan bobot yang telah ditentukan. Program memberikan kemudahan melalui menu berbasis teks, sehingga pengguna dapat memilih berbagai opsi dengan cepat, seperti menambah data, melihat daftar mahasiswa, atau keluar dari program.

# FLOWCHART
