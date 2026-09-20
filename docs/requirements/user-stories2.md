# USER STORIES

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Dokumen:** User Stories  
**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode:** Decision Tree  
**Tahap:** Praktikum PRD → SRS → HLD → LLD

---

# 1. Tujuan

Dokumen ini menggabungkan User Stories, Use Case, User Flow, Acceptance Criteria, dan tabel keterlacakan untuk Sistem Monitoring Minat Belajar Siswa SD Berbasis Web.

Fokus utama sistem:

1. Pengelolaan data siswa.
2. Pengisian data monitoring siswa.
3. Klasifikasi minat belajar menggunakan algoritma Decision Tree.
4. Penyajian hasil klasifikasi.
5. Penanganan hasil yang kurang meyakinkan dan kegagalan proses klasifikasi.

---

# 2. Aktor Sistem

| Aktor | Peran |
|---|---|
| Guru/Wali Kelas | Mengisi data monitoring, menjalankan klasifikasi, dan melihat hasil |
| Admin Sekolah | Mengelola data siswa |
| Sistem | Melakukan validasi, menyimpan data, dan menjalankan proses klasifikasi |
| Decision Tree | Melakukan proses klasifikasi berdasarkan data monitoring |

---

# 3. Daftar User Stories

## US-01 — Login Pengguna

**Prioritas:** Must

**Aktor:** Guru/Wali Kelas, Admin Sekolah

### User Story

> Sebagai pengguna, saya ingin melakukan login agar dapat mengakses fitur sistem sesuai dengan hak akses saya.

### Acceptance Criteria

- [ ] Pengguna dapat memasukkan username/email dan password.
- [ ] Sistem melakukan validasi kredensial.
- [ ] Pengguna dengan data login valid dapat masuk ke sistem.
- [ ] Pengguna dengan data login tidak valid mendapatkan pesan kesalahan.
- [ ] Pengguna yang belum login tidak dapat mengakses fitur yang membutuhkan autentikasi.

### Use Case

**UC-01 Authenticate User**

---

# 4. US-02 — Menambah Data Siswa

**Prioritas:** Must

**Aktor:** Admin Sekolah

### User Story

> Sebagai Admin Sekolah, saya ingin menambahkan data siswa agar siswa dapat terdaftar dalam sistem monitoring.

### Acceptance Criteria

- [ ] Admin dapat membuka fitur data siswa.
- [ ] Admin dapat memasukkan data siswa.
- [ ] Sistem melakukan validasi data.
- [ ] Data siswa valid dapat disimpan.
- [ ] Sistem menampilkan informasi bahwa data berhasil disimpan.
- [ ] Data tidak valid tidak disimpan.

### Use Case

**UC-02 Manage Student Data**

---

# 5. US-03 — Mengubah Data Siswa

**Prioritas:** Must

**Aktor:** Admin Sekolah

### User Story

> Sebagai Admin Sekolah, saya ingin mengubah data siswa agar informasi siswa tetap sesuai dengan kondisi terbaru.

### Acceptance Criteria

- [ ] Admin dapat memilih data siswa.
- [ ] Admin dapat mengubah data siswa.
- [ ] Sistem melakukan validasi perubahan.
- [ ] Data yang valid dapat diperbarui.
- [ ] Sistem menampilkan informasi bahwa data berhasil diperbarui.

### Use Case

**UC-02 Manage Student Data**

---

# 6. US-04 — Menghapus Data Siswa

**Prioritas:** Must

**Aktor:** Admin Sekolah

### User Story

> Sebagai Admin Sekolah, saya ingin menghapus data siswa agar data yang sudah tidak diperlukan tidak digunakan dalam sistem.

### Acceptance Criteria

- [ ] Admin dapat memilih siswa.
- [ ] Sistem meminta konfirmasi sebelum penghapusan.
- [ ] Admin dapat membatalkan proses penghapusan.
- [ ] Data dihapus setelah admin memberikan konfirmasi.
- [ ] Sistem menampilkan status penghapusan.

### Use Case

**UC-02 Manage Student Data**

---

# 7. US-05 — Mengisi Data Monitoring Siswa

**Prioritas:** Must

**Aktor:** Guru/Wali Kelas

### User Story

> Sebagai Guru/Wali Kelas, saya ingin mencatat data monitoring siswa agar perkembangan indikator sosial, emosional, dan minat belajar siswa dapat tersimpan dalam sistem.

### Acceptance Criteria

- [ ] Guru dapat memilih siswa.
- [ ] Guru dapat mengisi data monitoring.
- [ ] Sistem memeriksa kelengkapan data.
- [ ] Sistem memeriksa validitas data.
- [ ] Data valid dapat disimpan.
- [ ] Data tidak lengkap atau tidak valid tidak dapat diproses.
- [ ] Sistem menampilkan status penyimpanan data.

### Use Case

**UC-03 Record Monitoring Data**

---

# 8. US-06 ★ — Melakukan Klasifikasi Minat Belajar

**Prioritas:** Must

**Aktor:** Guru/Wali Kelas

**Fitur:** AI ★

### User Story

> Sebagai Guru/Wali Kelas, saya ingin menjalankan klasifikasi menggunakan Decision Tree agar data monitoring siswa dapat diproses menjadi hasil klasifikasi minat belajar.

### Acceptance Criteria

- [ ] Guru dapat memilih siswa yang akan dianalisis.
- [ ] Sistem mengambil data monitoring yang diperlukan.
- [ ] Sistem melakukan validasi sebelum data dikirim untuk klasifikasi.
- [ ] Sistem tidak mengirim data yang tidak lengkap atau tidak valid.
- [ ] Sistem menampilkan indikator bahwa proses klasifikasi sedang berlangsung.
- [ ] Decision Tree memproses data yang valid.
- [ ] Sistem menerima hasil klasifikasi jika model berhasil.
- [ ] Sistem tidak menampilkan hasil palsu ketika model gagal merespons.
- [ ] Pengguna dapat mencoba kembali ketika proses gagal.
- [ ] Pengguna dapat kembali ke data monitoring.

### Use Case

**UC-04 Perform Student Classification**

---

# 9. US-07 ★ — Melihat Hasil Klasifikasi

**Prioritas:** Must

**Aktor:** Guru/Wali Kelas

**Fitur:** AI ★

### User Story

> Sebagai Guru/Wali Kelas, saya ingin melihat hasil klasifikasi agar dapat mengetahui hasil pengolahan data monitoring siswa.

### Acceptance Criteria

- [ ] Sistem menampilkan hasil setelah proses klasifikasi berhasil.
- [ ] Hasil ditampilkan berdasarkan data yang diproses.
- [ ] Jika hasil tidak tersedia, sistem menampilkan informasi yang sesuai.
- [ ] Jika hasil kurang meyakinkan, sistem memberikan status bahwa hasil perlu diperiksa kembali.
- [ ] Sistem tidak menyatakan hasil meragukan sebagai hasil yang pasti.

### Use Case

**UC-05 View Classification Result**

---

# 10. US-08 — Melihat Riwayat Monitoring

**Prioritas:** Should

**Aktor:** Guru/Wali Kelas

### User Story

> Sebagai Guru/Wali Kelas, saya ingin melihat riwayat monitoring siswa agar dapat melihat data monitoring yang telah dicatat sebelumnya.

### Acceptance Criteria

- [ ] Guru dapat membuka riwayat monitoring.
- [ ] Sistem menampilkan data monitoring yang tersimpan.
- [ ] Guru dapat melihat data berdasarkan siswa.
- [ ] Sistem hanya menampilkan data yang dapat diakses oleh pengguna.

### Use Case

**UC-06 View Monitoring History**

---

# 11. US-09 — Melihat Ringkasan Monitoring

**Prioritas:** Should

**Aktor:** Guru/Wali Kelas

### User Story

> Sebagai Guru/Wali Kelas, saya ingin melihat ringkasan data monitoring agar dapat memperoleh gambaran data siswa yang telah dicatat.

### Acceptance Criteria

- [ ] Sistem menampilkan ringkasan data monitoring.
- [ ] Ringkasan berdasarkan data yang tersimpan.
- [ ] Data dapat ditampilkan berdasarkan siswa.
- [ ] Sistem tidak menampilkan data yang tidak memiliki sumber dalam database.

### Use Case

**UC-07 View Monitoring Summary**

---

# 12. US-10 ★ — Melihat Atribut Klasifikasi

**Prioritas:** Should

**Aktor:** Guru/Wali Kelas

**Fitur:** AI ★

### User Story

> Sebagai Guru/Wali Kelas, saya ingin mengetahui atribut yang digunakan dalam proses klasifikasi agar saya dapat memahami data yang menjadi dasar hasil klasifikasi.

### Acceptance Criteria

- [ ] Sistem menampilkan atribut yang digunakan dalam klasifikasi.
- [ ] Atribut yang ditampilkan sesuai dengan atribut yang digunakan model.
- [ ] Sistem tidak menampilkan atribut yang tidak digunakan sebagai dasar klasifikasi.
- [ ] Informasi ditampilkan dengan bahasa yang dapat dipahami pengguna.

### Use Case

**UC-08 View Classification Attributes**

---

# 13. Daftar Use Case

| ID | Use Case | Aktor Utama | Prioritas | Fitur AI |
|---|---|---|---|---|
| UC-01 | Authenticate User | Guru/Wali Kelas, Admin Sekolah | Must | Tidak |
| UC-02 | Manage Student Data | Admin Sekolah | Must | Tidak |
| UC-03 | Record Monitoring Data | Guru/Wali Kelas | Must | Tidak |
| UC-04 | Perform Student Classification | Guru/Wali Kelas | Must | ★ |
| UC-05 | View Classification Result | Guru/Wali Kelas | Must | ★ |
| UC-06 | View Monitoring History | Guru/Wali Kelas | Should | Tidak |
| UC-07 | View Monitoring Summary | Guru/Wali Kelas | Should | Tidak |
| UC-08 | View Classification Attributes | Guru/Wali Kelas | Should | ★ |

---

# 14. Use Case Detail

## UC-01 — Authenticate User

**Primary Actor:** Guru/Wali Kelas, Admin Sekolah

**Precondition:**
- Pengguna telah memiliki akun.
- Sistem tersedia.

**Main Flow:**

1. Pengguna membuka halaman login.
2. Pengguna memasukkan username/email.
3. Pengguna memasukkan password.
4. Sistem memvalidasi data login.
5. Sistem mengizinkan pengguna masuk.
6. Sistem menampilkan halaman utama sesuai hak akses.

**Alternative Flow:**

- Jika data login tidak valid, sistem menampilkan pesan kesalahan.
- Pengguna dapat mencoba login kembali.

**Postcondition:**

Pengguna berhasil masuk ke sistem atau tetap berada pada halaman login.

---

# 15. UC-02 — Manage Student Data

**Primary Actor:** Admin Sekolah

**Precondition:**

- Admin telah login.
- Admin memiliki hak akses pengelolaan data siswa.

**Main Flow:**

1. Admin membuka menu data siswa.
2. Sistem menampilkan data siswa.
3. Admin memilih tambah, ubah, atau hapus data.
4. Sistem melakukan validasi.
5. Sistem menyimpan perubahan.
6. Sistem menampilkan status proses.

**Alternative Flow:**

- Data tidak valid → sistem menampilkan pesan kesalahan.
- Penghapusan dibatalkan → data tetap tersimpan.

**Postcondition:**

Data siswa tersimpan sesuai perubahan yang dilakukan.

---

# 16. UC-03 — Record Monitoring Data

**Primary Actor:** Guru/Wali Kelas

**Precondition:**

- Guru telah login.
- Data siswa tersedia.

**Main Flow:**

1. Guru membuka menu monitoring.
2. Guru memilih siswa.
3. Sistem menampilkan data siswa.
4. Guru mengisi data monitoring.
5. Sistem melakukan validasi.
6. Data valid disimpan.
7. Sistem menampilkan status berhasil.

**Alternative Flow:**

- Data tidak lengkap → sistem meminta pengguna melengkapi data.
- Data tidak valid → sistem meminta pengguna memperbaiki data.

**Postcondition:**

Data monitoring siswa tersimpan.

---

# 17. UC-04 ★ — Perform Student Classification

**Primary Actor:** Guru/Wali Kelas

**Supporting Actor:** Decision Tree

**Precondition:**

- Guru telah login.
- Data siswa tersedia.
- Data monitoring tersedia.
- Atribut yang diperlukan tersedia.
- Model Decision Tree tersedia.

**Main Flow:**

1. Guru memilih siswa.
2. Sistem mengambil data monitoring.
3. Sistem melakukan validasi data.
4. Jika data valid, sistem menyiapkan data untuk model.
5. Sistem mengirim data ke proses klasifikasi.
6. Sistem menampilkan status **"Sedang menganalisis..."**.
7. Decision Tree memproses data.
8. Sistem menerima hasil klasifikasi.
9. Sistem meneruskan hasil ke proses tampilan hasil.

**Alternative Flow:**

- Data tidak lengkap → sistem meminta pengguna melengkapi data.
- Data tidak valid → sistem meminta pengguna memperbaiki data.

### AI Exception Handling

#### E1 — Input Tidak Valid

Jika data monitoring tidak lengkap atau tidak valid:

1. Sistem menghentikan proses klasifikasi.
2. Sistem menampilkan informasi kesalahan.
3. Pengguna memperbaiki data.
4. Pengguna dapat menjalankan klasifikasi kembali.

#### E2 — Timeout/Koneksi Gagal

Jika proses klasifikasi tidak memberikan respons:

1. Sistem menghentikan proses setelah batas waktu yang ditentukan.
2. Sistem tidak menampilkan hasil sebagai hasil berhasil.
3. Sistem menampilkan status bahwa klasifikasi belum dapat dilakukan.
4. Pengguna dapat memilih **Coba Lagi**.
5. Pengguna dapat kembali ke data monitoring.

> **[ASUMSI]** Batas waktu numerik belum ditentukan pada SRS.

#### E3 — Hasil Kurang Meyakinkan

Jika hasil klasifikasi berada di bawah ambang keyakinan yang ditentukan:

1. Sistem menampilkan status **"Hasil kurang meyakinkan"**.
2. Sistem tidak memperlakukan hasil tersebut sebagai hasil yang pasti.
3. Pengguna dapat memeriksa data monitoring.
4. Pengguna dapat melengkapi data.
5. Pengguna dapat melakukan klasifikasi kembali.

> **[ASUMSI]** Nilai *confidence threshold* belum ditentukan pada SRS.

**Postcondition:**

- Hasil klasifikasi berhasil tersedia; atau
- Sistem memberikan status kegagalan/hasil kurang meyakinkan.

---

# 18. UC-05 ★ — View Classification Result

**Primary Actor:** Guru/Wali Kelas

**Precondition:**

- Proses klasifikasi telah dijalankan.

**Main Flow:**

1. Sistem menerima hasil klasifikasi.
2. Sistem memeriksa status hasil.
3. Sistem menampilkan hasil klasifikasi.
4. Guru melihat hasil.

**Alternative Flow:**

- Hasil tidak tersedia → sistem menampilkan informasi bahwa hasil belum tersedia.
- Hasil kurang meyakinkan → sistem menampilkan status tersebut.
- Proses gagal → sistem memberikan pilihan untuk mencoba kembali.

**Postcondition:**

Guru mengetahui hasil atau status klasifikasi.

---

# 19. UC-06 — View Monitoring History

**Primary Actor:** Guru/Wali Kelas

**Precondition:**

- Guru telah login.
- Data monitoring tersedia.

**Main Flow:**

1. Guru membuka menu riwayat monitoring.
2. Sistem mengambil data monitoring.
3. Sistem menampilkan riwayat.
4. Guru memilih data yang ingin dilihat.

**Postcondition:**

Riwayat monitoring dapat dilihat oleh Guru/Wali Kelas.

---

# 20. UC-07 — View Monitoring Summary

**Primary Actor:** Guru/Wali Kelas

**Precondition:**

- Guru telah login.
- Data monitoring tersedia.

**Main Flow:**

1. Guru membuka menu ringkasan.
2. Sistem mengambil data monitoring.
3. Sistem mengolah data menjadi ringkasan.
4. Sistem menampilkan ringkasan kepada guru.

**Postcondition:**

Guru dapat melihat ringkasan monitoring.

---

# 21. UC-08 ★ — View Classification Attributes

**Primary Actor:** Guru/Wali Kelas

**Precondition:**

- Model Decision Tree tersedia.
- Atribut klasifikasi telah ditentukan.

**Main Flow:**

1. Guru membuka informasi atribut klasifikasi.
2. Sistem mengambil informasi atribut yang digunakan.
3. Sistem menampilkan atribut.
4. Guru melihat informasi atribut yang menjadi dasar proses klasifikasi.

**Postcondition:**

Guru dapat mengetahui atribut yang digunakan oleh model.

---

# 22. User Flow

## 22.1 Fitur AI ★

```text
LOGIN
  ↓
PILIH SISWA
  ↓
AMBIL DATA MONITORING
  ↓
PERIKSA / LENGKAPI DATA
  ↓
VALIDASI AWAL
  │
  ├── Tidak Valid
  │      ↓
  │   Tampilkan Pesan Kesalahan
  │      ↓
  │   Perbaiki Data
  │      ↓
  │   Validasi Ulang
  │
  └── Valid
         ↓
     KIRIM DATA
         ↓
   SEDANG MENGANALISIS
         ↓
    DECISION TREE
         ↓
   MODEL BERHASIL?
      │         │
     YA       TIDAK
      │         │
      ↓         ↓
  CEK HASIL   FALLBACK
      │         │
      ↓         ├── Coba Lagi
 HASIL YAKIN?  └── Kembali
    │      │
   YA    TIDAK
    │      │
    ↓      ↓
 Tampilkan  Hasil
 Hasil      Meragukan
    │      │
    └──┬───┘
       ↓
    SELESAI
