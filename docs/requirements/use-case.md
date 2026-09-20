# USE CASE SPECIFICATION

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode/Model:** Decision Tree  

---

# 1. DAFTAR USE CASE

Use Case prioritas yang digunakan dalam dokumen ini:

| ID | Nama Use Case | Prioritas | Kategori | User Story | FR Asal |
|---|---|---|---|---|---|
| UC-01 | Melakukan Autentikasi Pengguna | Must | Fitur Inti | US-01 | FR-01 |
| UC-02 | Mengelola Data Siswa | Must | Fitur Inti | US-02, US-03, US-04 | FR-02 |
| UC-03 | Mencatat Data Monitoring | Must | Fitur Inti | US-05 | FR-03 |
| UC-04 ★ | Melakukan Klasifikasi Siswa | Must | Fitur AI ★ | US-06 | FR-04 ★ |
| UC-05 ★ | Melihat Hasil Klasifikasi | Must | Fitur AI ★ | US-07 | FR-05 ★ |
| UC-06 | Melihat Riwayat Monitoring | Should | Fitur Inti | US-08 | FR-06 |
| UC-07 | Melihat Ringkasan Monitoring | Should | Fitur Inti | US-09 | FR-07 |
| UC-08 ★ | Melihat Atribut Klasifikasi | Should | Fitur AI ★ | US-10 | FR-08 ★ |

---

# 2. AKTOR

## 2.1 Aktor Utama

| Aktor | Peran |
|---|---|
| Guru/Wali Kelas | Melakukan monitoring siswa, memasukkan data monitoring, menjalankan klasifikasi, dan melihat hasil klasifikasi |
| Admin Sekolah | Mengelola data siswa dan data pendukung sistem |

## 2.2 Aktor Pendukung

| Aktor | Peran |
|---|---|
| Database | Menyimpan dan mengambil data siswa, data monitoring, dan hasil klasifikasi |
| Layanan Inferensi Decision Tree | Memproses data yang diberikan sistem dan menghasilkan hasil klasifikasi |

**Catatan:** Decision Tree pada rancangan ini merupakan model klasifikasi yang digunakan sistem. SRS belum menetapkan layanan AI eksternal/API tertentu.

**[ASUMSI-01]** Layanan inferensi dapat berupa modul/model klasifikasi yang berjalan pada lingkungan aplikasi, bukan necessarily layanan AI pihak ketiga.

---

# 3. UC-01 — MELAKUKAN AUTENTIKASI PENGGUNA

## Aktor

**Aktor Utama:** Guru/Wali Kelas / Admin Sekolah  
**Aktor Pendukung:** Database

## Precondition

1. Pengguna telah memiliki akun.
2. Data akun telah tersedia di database.
3. Sistem dapat mengakses database.

## Postcondition

Pengguna berhasil masuk ke sistem dan memperoleh akses sesuai haknya.

## Alur Utama

1. Pengguna memberikan kredensial akun.
2. Sistem menerima kredensial.
3. Sistem memeriksa data akun pada database.
4. Database mengembalikan informasi akun.
5. Sistem memverifikasi kredensial.
6. Sistem menentukan hak akses pengguna.
7. Sistem memberikan akses ke fungsi sesuai hak pengguna.
8. Proses autentikasi selesai.

## Alur Alternatif

### A1 — Kredensial Tidak Sesuai

1. Sistem menerima kredensial.
2. Sistem melakukan pemeriksaan ke database.
3. Data tidak sesuai.
4. Sistem menolak autentikasi.
5. Pengguna tetap berada di kondisi belum terautentikasi.

## Alur Eksepsi

### E1 — Database Tidak Dapat Diakses

1. Sistem mencoba memeriksa kredensial.
2. Database tidak memberikan respons.
3. Sistem menghentikan proses autentikasi.
4. Sistem memberikan status kegagalan kepada pengguna.
5. Pengguna dapat mencoba kembali setelah layanan tersedia.

---

# 4. UC-02 — MENGELOLA DATA SISWA

## Aktor

**Aktor Utama:** Admin Sekolah  
**Aktor Pendukung:** Database

## Precondition

1. Admin Sekolah telah terautentikasi.
2. Admin memiliki hak pengelolaan data siswa.
3. Database tersedia.

## Postcondition

Data siswa berhasil ditambahkan, diperbarui, atau dihapus sesuai tindakan yang dilakukan.

## Alur Utama

1. Admin memilih operasi pengelolaan data siswa.
2. Sistem menerima data atau identitas siswa yang akan dikelola.
3. Sistem memvalidasi data.
4. Sistem mengirimkan operasi ke database.
5. Database memproses perubahan.
6. Sistem menerima status operasi.
7. Sistem memberikan hasil operasi kepada Admin.

## Alur Alternatif

### A1 — Menambahkan Siswa

1. Admin memberikan data siswa baru.
2. Sistem memvalidasi data.
3. Sistem menyimpan data ke database.
4. Database mengonfirmasi penyimpanan.
5. Sistem menyatakan data berhasil ditambahkan.

### A2 — Memperbarui Siswa

1. Admin memilih data siswa yang tersedia.
2. Admin memberikan perubahan data.
3. Sistem memvalidasi perubahan.
4. Sistem memperbarui database.
5. Sistem mengonfirmasi perubahan.

### A3 — Menghapus Siswa

1. Admin memilih data siswa.
2. Sistem memastikan data siswa tersedia.
3. Admin memberikan konfirmasi penghapusan.
4. Sistem menghapus data sesuai aturan sistem.
5. Sistem memberikan status operasi.

## Alur Eksepsi

### E1 — Data Tidak Valid

1. Sistem menerima data siswa.
2. Sistem menemukan data yang tidak memenuhi persyaratan.
3. Sistem menolak penyimpanan.
4. Sistem memberikan informasi kesalahan.

### E2 — Database Gagal

1. Sistem mengirimkan operasi ke database.
2. Database tidak dapat memproses permintaan.
3. Sistem membatalkan perubahan.
4. Sistem memberikan status kegagalan.

---

# 5. UC-03 — MENCATAT DATA MONITORING

## Aktor

**Aktor Utama:** Guru/Wali Kelas  
**Aktor Pendukung:** Database

## Precondition

1. Guru/Wali Kelas telah terautentikasi.
2. Data siswa telah tersedia.
3. Guru/Wali Kelas memiliki hak untuk melakukan monitoring.
4. Database tersedia.

## Postcondition

Data monitoring siswa berhasil tersimpan dan dapat digunakan untuk proses klasifikasi.

## Alur Utama

1. Guru/Wali Kelas memilih siswa yang akan dimonitor.
2. Sistem mengambil data siswa dari database.
3. Guru/Wali Kelas memberikan data monitoring.
4. Sistem memeriksa kelengkapan data.
5. Sistem menyimpan data monitoring ke database.
6. Database mengonfirmasi penyimpanan.
7. Sistem menyatakan data monitoring berhasil dicatat.

## Alur Alternatif

### A1 — Data Belum Lengkap

1. Guru/Wali Kelas memberikan data monitoring.
2. Sistem menemukan atribut wajib yang belum tersedia.
3. Sistem tidak menyimpan data.
4. Guru/Wali Kelas melengkapi data.
5. Sistem melakukan validasi kembali.

## Alur Eksepsi

### E1 — Database Tidak Tersedia

1. Sistem mencoba menyimpan data monitoring.
2. Database tidak memberikan respons.
3. Sistem tidak menganggap data berhasil tersimpan.
4. Sistem memberikan status kegagalan.
5. Guru/Wali Kelas dapat mencoba kembali.

---

# 6. UC-04 ★ — MELAKUKAN KLASIFIKASI SISWA

## Aktor

**Aktor Utama:** Guru/Wali Kelas  
**Aktor Pendukung:** Layanan Inferensi Decision Tree, Database

## Precondition

1. Guru/Wali Kelas telah terautentikasi.
2. Data siswa tersedia.
3. Data monitoring tersedia.
4. Atribut yang dibutuhkan model tersedia.
5. Model Decision Tree telah tersedia untuk proses klasifikasi.
6. Layanan inferensi dapat digunakan.

## Postcondition

Sistem memperoleh hasil klasifikasi atau status bahwa klasifikasi tidak dapat dilakukan.

## Alur Utama

1. Guru/Wali Kelas memilih data siswa yang akan diklasifikasikan.
2. Sistem mengambil data monitoring siswa dari database.
3. Sistem memeriksa kelengkapan dan validitas data.
4. Sistem membentuk input sesuai atribut model.
5. Sistem mengirimkan input ke layanan inferensi Decision Tree.
6. Layanan inferensi memproses input menggunakan model Decision Tree.
7. Layanan inferensi mengembalikan hasil klasifikasi.
8. Sistem menerima hasil klasifikasi.
9. Sistem menyimpan hasil klasifikasi apabila penyimpanan diperlukan.
10. Sistem meneruskan hasil untuk ditampilkan pada proses UC-05.
11. Proses klasifikasi selesai.

## Alur Alternatif

### A1 — Data Monitoring Tidak Lengkap

1. Sistem mengambil data monitoring.
2. Sistem menemukan atribut yang dibutuhkan belum tersedia.
3. Sistem tidak mengirimkan data ke model.
4. Sistem memberikan status bahwa data belum memenuhi persyaratan.
5. Guru/Wali Kelas melengkapi data monitoring.
6. Proses klasifikasi dapat dilakukan kembali.

### A2 — Data Berada di Luar Rentang yang Diharapkan

1. Sistem menerima data monitoring.
2. Sistem melakukan validasi.
3. Sistem menemukan nilai yang tidak sesuai dengan ketentuan data.
4. Sistem menolak input untuk klasifikasi.
5. Sistem memberikan status validasi kepada Guru/Wali Kelas.

---

## 6.1 Alur Eksepsi Khusus AI

### E1 — Kualitas Masukan Data Rendah

1. Sistem melakukan pemeriksaan kualitas data sebelum dikirim ke layanan inferensi.
2. Sistem menemukan data kosong, tidak valid, atau kualitas data tidak memenuhi persyaratan model.
3. Sistem tidak mengirimkan input ke layanan inferensi.
4. Sistem memberikan status bahwa kualitas data belum memenuhi persyaratan.
5. Guru/Wali Kelas memperbaiki atau melengkapi data.
6. Sistem dapat melakukan klasifikasi kembali setelah data memenuhi persyaratan.

**Catatan:** Pada sistem berbasis data terstruktur, istilah "buram" lebih tepat dipahami sebagai data tidak terbaca, tidak lengkap, atau tidak valid apabila input berasal dari sumber yang perlu dibaca terlebih dahulu.

### E2 — Timeout atau Gagal Koneksi ke Layanan AI

1. Sistem mengirimkan data ke layanan inferensi.
2. Sistem tidak menerima respons dalam batas waktu yang ditentukan.
3. Sistem menghentikan penantian terhadap permintaan tersebut.
4. Sistem tidak menyatakan bahwa klasifikasi berhasil.
5. Sistem memberikan status bahwa layanan klasifikasi sedang tidak tersedia.
6. Sistem mempertahankan data monitoring yang telah tersimpan.
7. Guru/Wali Kelas dapat mencoba proses klasifikasi kembali.

**Batas latency:** **[ASUMSI-02]** Nilai batas waktu respons belum ditetapkan secara numerik dalam SRS saat ini dan harus ditentukan berdasarkan hasil pengujian prototype.

### E3 — Low Confidence

1. Layanan inferensi menghasilkan prediksi.
2. Layanan inferensi memberikan nilai keyakinan model.
3. Sistem membandingkan nilai tersebut dengan ambang batas yang ditentukan.
4. Nilai keyakinan berada di bawah ambang batas.
5. Sistem tidak memperlakukan hasil tersebut sebagai klasifikasi yang cukup meyakinkan.
6. Sistem memberikan status bahwa hasil memiliki tingkat keyakinan rendah.
7. Guru/Wali Kelas dapat melakukan pemeriksaan atau pengumpulan data tambahan.
8. Klasifikasi dapat dilakukan kembali setelah data diperbaiki atau dilengkapi.

**Ambang confidence:** **[ASUMSI-03]** Nilai ambang batas belum ditentukan dalam SRS dan harus ditetapkan berdasarkan hasil evaluasi model.

---

# 7. UC-05 ★ — MELIHAT HASIL KLASIFIKASI

## Aktor

**Aktor Utama:** Guru/Wali Kelas  
**Aktor Pendukung:** Database

## Precondition

1. Guru/Wali Kelas telah terautentikasi.
2. Data siswa tersedia.
3. Proses klasifikasi telah berhasil.
4. Hasil klasifikasi tersedia.

## Postcondition

Guru/Wali Kelas memperoleh informasi hasil klasifikasi sebagai informasi pendukung monitoring.

## Alur Utama

1. Sistem menerima hasil klasifikasi dari proses UC-04.
2. Sistem mengaitkan hasil dengan data siswa.
3. Sistem mengambil informasi pendukung yang diperlukan.
4. Sistem memberikan hasil klasifikasi kepada Guru/Wali Kelas.
5. Guru/Wali Kelas memperoleh informasi hasil klasifikasi.
6. Proses selesai.

## Alur Alternatif

### A1 — Belum Ada Hasil Klasifikasi

1. Guru/Wali Kelas meminta hasil klasifikasi.
2. Sistem tidak menemukan hasil klasifikasi.
3. Sistem memberikan status bahwa klasifikasi belum tersedia.
4. Guru/Wali Kelas dapat menjalankan UC-04.

## Alur Eksepsi Khusus AI

### E1 — Hasil Model Tidak Tersedia

1. Sistem meminta hasil klasifikasi.
2. Hasil dari layanan inferensi tidak tersedia atau tidak tersimpan.
3. Sistem tidak menampilkan hasil sebagai klasifikasi yang berhasil.
4. Sistem memberikan status bahwa hasil belum tersedia.
5. Guru/Wali Kelas dapat mengulangi proses klasifikasi.

### E2 — Low Confidence

1. Sistem menerima hasil dengan confidence di bawah ambang batas.
2. Sistem menandai hasil sebagai confidence rendah.
3. Sistem tidak memperlakukan hasil sebagai hasil klasifikasi yang meyakinkan.
4. Guru/Wali Kelas diberikan informasi bahwa hasil perlu diperiksa lebih lanjut.

---

# 8. UC-06 — MELIHAT RIWAYAT MONITORING

## Aktor

**Aktor Utama:** Guru/Wali Kelas  
**Aktor Pendukung:** Database

## Precondition

1. Guru/Wali Kelas telah terautentikasi.
2. Data monitoring telah tersedia.

## Postcondition

Riwayat monitoring siswa dapat dilihat.

## Alur Utama

1. Guru/Wali Kelas memilih siswa.
2. Sistem meminta riwayat monitoring dari database.
3. Database mengembalikan data yang tersedia.
4. Sistem memberikan riwayat monitoring kepada Guru/Wali Kelas.
5. Proses selesai.

## Alur Alternatif

### A1 — Belum Ada Riwayat

1. Sistem meminta data riwayat.
2. Database tidak memiliki catatan monitoring.
3. Sistem memberikan informasi bahwa riwayat belum tersedia.

## Alur Eksepsi

### E1 — Database Tidak Tersedia

1. Sistem meminta riwayat.
2. Database tidak memberikan respons.
3. Sistem memberikan status kegagalan.
4. Pengguna dapat mencoba kembali.

---

# 9. UC-07 — MELIHAT RINGKASAN MONITORING

## Aktor

**Aktor Utama:** Guru/Wali Kelas  
**Aktor Pendukung:** Database

## Precondition

1. Guru/Wali Kelas telah terautentikasi.
2. Data monitoring tersedia.

## Postcondition

Guru/Wali Kelas memperoleh ringkasan data monitoring yang tersedia.

## Alur Utama

1. Guru/Wali Kelas meminta ringkasan monitoring.
2. Sistem mengambil data monitoring dari database.
3. Sistem mengolah data yang tersedia sesuai kebutuhan ringkasan.
4. Sistem memberikan ringkasan kepada Guru/Wali Kelas.
5. Proses selesai.

## Alur Alternatif

### A1 — Data Monitoring Belum Tersedia

1. Sistem meminta data monitoring.
2. Tidak terdapat data yang dapat diringkas.
3. Sistem memberikan informasi bahwa ringkasan belum tersedia.

## Alur Eksepsi

### E1 — Database Gagal Diakses

1. Sistem meminta data.
2. Database tidak memberikan respons.
3. Sistem menghentikan proses.
4. Sistem memberikan status kegagalan.

---

# 10. UC-08 ★ — MELIHAT ATRIBUT KLASIFIKASI

## Aktor

**Aktor Utama:** Guru/Wali Kelas  
**Aktor Pendukung:** Layanan Inferensi Decision Tree, Database

## Precondition

1. Guru/Wali Kelas telah terautentikasi.
2. Model Decision Tree tersedia.
3. Informasi atribut model tersedia.

## Postcondition

Guru/Wali Kelas memperoleh informasi mengenai atribut yang digunakan dalam proses klasifikasi.

## Alur Utama

1. Guru/Wali Kelas meminta informasi atribut klasifikasi.
2. Sistem mengambil informasi atribut dari model atau penyimpanan terkait.
3. Sistem memeriksa ketersediaan informasi.
4. Sistem memberikan informasi atribut kepada Guru/Wali Kelas.
5. Proses selesai.

## Alur Alternatif

### A1 — Informasi Atribut Tidak Tersedia

1. Sistem meminta informasi atribut.
2. Informasi atribut tidak tersedia.
3. Sistem memberikan status bahwa informasi belum tersedia.
4. Hasil klasifikasi tidak diubah.

## Alur Eksepsi Khusus AI

### E1 — Model Tidak Tersedia

1. Sistem meminta informasi atribut model.
2. Model Decision Tree tidak tersedia.
3. Sistem tidak memberikan informasi atribut yang tidak terverifikasi.
4. Sistem memberikan status bahwa informasi model belum tersedia.

---

# 11. RINGKASAN PENANGANAN EKSEPSI AI

| Kondisi | Respons Sistem | Dampak |
|---|---|---|
| Kualitas data rendah | Klasifikasi tidak dijalankan dan pengguna diminta memperbaiki data | Tidak ada hasil klasifikasi |
| Timeout layanan inferensi | Permintaan dihentikan setelah batas waktu | Data monitoring tetap tersimpan |
| Gagal koneksi | Sistem memberikan status kegagalan dan menyediakan percobaan ulang | Tidak ada klaim klasifikasi berhasil |
| Low confidence | Hasil ditandai sebagai confidence rendah | Hasil tidak dianggap cukup meyakinkan |
| Model tidak tersedia | Proses klasifikasi tidak dijalankan | Pengguna mendapat status kegagalan |
| Data tidak lengkap | Data tidak dikirim ke model | Pengguna perlu melengkapi data |

---

# 12. KAITAN USE CASE, USER STORY, DAN FR

| Use Case | User Story | FR | Prioritas |
|---|---|---|---|
| UC-01 | US-01 | FR-01 | Must |
| UC-02 | US-02, US-03, US-04 | FR-02 | Must |
| UC-03 | US-05 | FR-03 | Must |
| UC-04 ★ | US-06 | FR-04 ★ | Must |
| UC-05 ★ | US-07 | FR-05 ★ | Must |
| UC-06 | US-08 | FR-06 | Should |
| UC-07 | US-09 | FR-07 | Should |
| UC-08 ★ | US-10 | FR-08 ★ | Should |

---

# 13. BATASAN LAYANAN AI

Berdasarkan SRS yang tersedia, sistem menggunakan **Decision Tree** sebagai model klasifikasi.

Namun, SRS belum menetapkan:

1. Nama layanan/API AI eksternal.
2. Penyedia layanan inferensi.
3. Nilai batas latency secara numerik.
4. Nilai ambang confidence.
5. Mekanisme khusus untuk menghitung confidence.
6. Spesifikasi server inferensi.

Oleh karena itu, nilai tersebut ditandai sebagai **[ASUMSI]** dan tidak ditetapkan secara sembarang dalam Use Case.

---

# 14. CHECKLIST REVIEW TAHAP 2

| Checklist | Status | Keterangan |
|---|---|---|
| Layanan inferensi AI/model dicatat sebagai aktor pendukung | ✓ | Layanan Inferensi Decision Tree |
| Database dicatat sebagai aktor pendukung | ✓ | Database digunakan pada alur data |
| Ada penanganan kualitas input rendah | ✓ | UC-04 E1 |
| Ada penanganan timeout | ✓ | UC-04 E2 |
| Ada penanganan gagal koneksi | ✓ | UC-04 E2 |
| Ada penanganan low confidence | ✓ | UC-04 E3 |
| Ada fallback ketika klasifikasi gagal | ✓ | Pengguna dapat memperbaiki data atau mencoba kembali |
| Alur utama menggunakan langkah bernomor | ✓ | Setiap UC memiliki alur berurutan |
| Alur tidak berfokus pada desain UI | ✓ | Fokus pada interaksi dan logika sistem |
| Setiap UC memiliki Precondition | ✓ | ✓ |
| Setiap UC memiliki Postcondition | ✓ | ✓ |
| Setiap UC memiliki hubungan ke FR | ✓ | ✓ |
| Setiap UC memiliki hubungan ke User Story | ✓ | ✓ |
| Batas latency numerik tersedia | ⚠️ | Belum ditentukan dalam SRS |
| Ambang confidence tersedia | ⚠️ | Belum ditentukan dalam SRS |
