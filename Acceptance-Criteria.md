# ACCEPTANCE CRITERIA

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Dokumen:** Acceptance Criteria  
**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode:** Decision Tree  
**Tahap:** Praktikum PRD → SRS → HLD → LLD

---

# 1. Tujuan

Dokumen ini mendefinisikan kriteria penerimaan dan skenario pengujian untuk setiap User Story pada Sistem Monitoring Minat Belajar Siswa SD Berbasis Web.

Acceptance Criteria menggunakan pola:

- **Given** — kondisi awal
- **When** — tindakan atau pemicu
- **Then** — hasil yang diharapkan dan dapat diuji

Khusus fitur AI ★, pengujian mencakup:

1. Happy path.
2. Edge case.
3. Kegagalan respons atau timeout.

---

# 2. Ukuran Pengujian

> **Catatan:** SRS sebelumnya belum menetapkan angka final untuk NFR latency, accuracy, dan confidence threshold. Angka berikut merupakan **[USULAN]** untuk kebutuhan draft pengujian dan dapat diganti setelah disepakati dengan pembimbing.

| Parameter | Nilai Pengujian | Status |
|---|---:|---|
| Waktu respons klasifikasi | ≤ 3 detik | [USULAN] |
| Akurasi minimum model | ≥ 80% | [USULAN] |
| Timeout proses klasifikasi | > 3 detik tanpa respons | [USULAN] |
| Confidence threshold | ≥ 70% untuk hasil meyakinkan | [USULAN] |
| Percobaan login tidak valid | Sistem menolak akses | SRS |
| Data monitoring tidak lengkap | Sistem menolak penyimpanan/proses | SRS |

---

# 3. US-01 — Login Pengguna

**Prioritas:** Must  
**Aktor:** Guru/Wali Kelas, Admin Sekolah  
**Use Case:** UC-01 Authenticate User

## Scenario: Login dengan data valid

**Given** pengguna telah memiliki akun aktif dan halaman login tersedia.

**When** pengguna memasukkan username/email dan password yang benar lalu menekan tombol login.

**Then** sistem memverifikasi kredensial dan menampilkan halaman utama dalam waktu **≤ 3 detik**. **[USULAN]**

**Metode Uji:** Unit Test + Integration Test + User Acceptance Test.

---

## Scenario: Login dengan password salah

**Given** pengguna memiliki akun terdaftar.

**When** pengguna memasukkan password yang salah.

**Then** sistem menolak login dan menampilkan pesan **"Username/email atau password salah."** tanpa membuka halaman utama.

**Metode Uji:** Unit Test + Integration Test.

---

# 4. US-02 — Menambah Data Siswa

**Prioritas:** Must  
**Aktor:** Admin Sekolah  
**Use Case:** UC-02 Manage Student Data

## Scenario: Menambahkan data siswa valid

**Given** Admin telah login dan berada pada halaman data siswa.

**When** Admin memasukkan seluruh data siswa yang diwajibkan dan menekan tombol simpan.

**Then** sistem memvalidasi data, menyimpan satu data siswa baru, dan menampilkan pesan **"Data siswa berhasil disimpan."**

**Metode Uji:** Unit Test + Integration Test.

---

## Scenario: Menambahkan data siswa tidak lengkap

**Given** Admin berada pada formulir tambah data siswa.

**When** Admin menekan tombol simpan dengan minimal satu field wajib kosong.

**Then** sistem tidak menyimpan data dan menampilkan informasi bahwa field yang wajib diisi harus dilengkapi.

**Metode Uji:** Unit Test.

---

# 5. US-03 — Mengubah Data Siswa

**Prioritas:** Must  
**Aktor:** Admin Sekolah  
**Use Case:** UC-02 Manage Student Data

## Scenario: Mengubah data siswa valid

**Given** data siswa telah tersedia di database.

**When** Admin mengubah data siswa dengan nilai yang valid dan menekan tombol simpan.

**Then** sistem memperbarui data siswa dan menampilkan pesan **"Data siswa berhasil diperbarui."**

**Metode Uji:** Integration Test.

---

## Scenario: Mengubah data dengan nilai tidak valid

**Given** Admin sedang mengubah data siswa.

**When** Admin memasukkan data yang tidak sesuai dengan format yang ditentukan lalu menekan tombol simpan.

**Then** sistem menolak perubahan dan menampilkan pesan kesalahan pada field yang tidak valid.

**Metode Uji:** Unit Test.

---

# 6. US-04 — Menghapus Data Siswa

**Prioritas:** Must  
**Aktor:** Admin Sekolah  
**Use Case:** UC-02 Manage Student Data

## Scenario: Menghapus data siswa

**Given** data siswa tersedia dan Admin memiliki hak akses penghapusan.

**When** Admin memilih siswa dan mengonfirmasi penghapusan.

**Then** sistem menghapus data siswa dan menampilkan pesan **"Data siswa berhasil dihapus."**

**Metode Uji:** Integration Test.

---

## Scenario: Membatalkan penghapusan

**Given** Admin telah memilih data siswa dan dialog konfirmasi penghapusan ditampilkan.

**When** Admin memilih tombol batal.

**Then** sistem tidak menghapus data dan data siswa tetap tersedia.

**Metode Uji:** Unit Test + User Acceptance Test.

---

# 7. US-05 — Mengisi Data Monitoring Siswa

**Prioritas:** Must  
**Aktor:** Guru/Wali Kelas  
**Use Case:** UC-03 Record Monitoring Data

## Scenario: Menyimpan data monitoring valid

**Given** Guru telah login, siswa telah dipilih, dan seluruh field monitoring yang diwajibkan tersedia.

**When** Guru mengisi seluruh data dengan nilai valid lalu menekan tombol simpan.

**Then** sistem menyimpan data monitoring dan menampilkan pesan **"Data monitoring berhasil disimpan."**

**Metode Uji:** Integration Test.

---

## Scenario: Menyimpan data monitoring tidak lengkap

**Given** Guru telah memilih siswa dan membuka formulir monitoring.

**When** Guru menekan tombol simpan dengan minimal satu atribut wajib belum diisi.

**Then** sistem tidak menyimpan data dan menampilkan pesan **"Data monitoring belum lengkap."**

**Metode Uji:** Unit Test.

---

# 8. US-06 ★ — Melakukan Klasifikasi Minat Belajar

**Prioritas:** Must  
**Aktor:** Guru/Wali Kelas  
**Use Case:** UC-04 Perform Student Classification

## Scenario: Happy Path — Klasifikasi berhasil

**Given** Guru telah login, data siswa tersedia, data monitoring lengkap, model Decision Tree tersedia, dan seluruh atribut yang diperlukan memiliki nilai valid.

**When** Guru memilih siswa dan menekan tombol **Klasifikasi**.

**Then** sistem melakukan validasi, menampilkan status **"Sedang menganalisis..."**, menjalankan Decision Tree, dan menampilkan hasil klasifikasi dalam waktu **≤ 3 detik**. **[USULAN]**

**Metode Uji:** Integration Test + User Acceptance Test.

---

## Scenario: Edge Case — Data input berada pada batas valid

**Given** data monitoring siswa berisi nilai atribut pada batas minimum atau maksimum yang masih diperbolehkan oleh sistem.

**When** Guru menjalankan proses klasifikasi.

**Then** sistem menerima data apabila seluruh nilai masih berada dalam rentang valid, menjalankan Decision Tree, dan menghasilkan status klasifikasi tanpa error.

**Metode Uji:** Unit Test + Integration Test.

---

## Scenario: Timeout — Model tidak memberikan respons

**Given** data monitoring valid dan proses klasifikasi telah dimulai.

**When** Decision Tree tidak memberikan respons selama lebih dari **3 detik**. **[USULAN]**

**Then** sistem menghentikan proses yang menunggu respons, tidak menampilkan hasil sebagai klasifikasi berhasil, dan menampilkan pesan **"Klasifikasi belum dapat dilakukan. Silakan coba kembali."**

**Metode Uji:** Integration Test.

---

# 9. US-07 ★ — Melihat Hasil Klasifikasi

**Prioritas:** Must  
**Aktor:** Guru/Wali Kelas  
**Use Case:** UC-05 View Classification Result

## Scenario: Menampilkan hasil klasifikasi yang meyakinkan

**Given** proses Decision Tree berhasil dan tingkat confidence hasil mencapai minimal **70%**. **[USULAN]**

**When** sistem menerima hasil klasifikasi.

**Then** sistem menampilkan hasil klasifikasi dan informasi tingkat confidence kepada Guru/Wali Kelas.

**Metode Uji:** Integration Test + User Acceptance Test.

---

## Scenario: Hasil klasifikasi kurang meyakinkan

**Given** Decision Tree berhasil memberikan hasil tetapi tingkat confidence berada di bawah **70%**. **[USULAN]**

**When** sistem menerima hasil klasifikasi.

**Then** sistem menampilkan status **"Hasil kurang meyakinkan"** dan menyediakan pilihan untuk memeriksa atau melengkapi data monitoring.

**Metode Uji:** Integration Test.

---

## Scenario: Hasil klasifikasi tidak tersedia

**Given** proses klasifikasi gagal atau model tidak memberikan hasil.

**When** Guru membuka halaman hasil klasifikasi.

**Then** sistem tidak menampilkan hasil klasifikasi palsu dan menampilkan informasi **"Hasil klasifikasi belum tersedia."**

**Metode Uji:** Integration Test.

---

# 10. US-08 — Melihat Riwayat Monitoring

**Prioritas:** Should  
**Aktor:** Guru/Wali Kelas  
**Use Case:** UC-06 View Monitoring History

## Scenario: Melihat riwayat siswa

**Given** terdapat minimal satu data monitoring siswa yang tersimpan.

**When** Guru memilih menu riwayat monitoring dan memilih seorang siswa.

**Then** sistem menampilkan data monitoring yang tersimpan untuk siswa tersebut.

**Metode Uji:** Integration Test + User Acceptance Test.

---

## Scenario: Riwayat belum tersedia

**Given** siswa belum memiliki data monitoring.

**When** Guru membuka riwayat monitoring siswa tersebut.

**Then** sistem menampilkan pesan **"Belum terdapat data monitoring."**

**Metode Uji:** Integration Test.

---

# 11. US-09 — Melihat Ringkasan Monitoring

**Prioritas:** Should  
**Aktor:** Guru/Wali Kelas  
**Use Case:** UC-07 View Monitoring Summary

## Scenario: Menampilkan ringkasan monitoring

**Given** terdapat data monitoring siswa yang tersimpan.

**When** Guru membuka menu ringkasan monitoring.

**Then** sistem menampilkan ringkasan berdasarkan data yang tersedia di database.

**Metode Uji:** Integration Test + User Acceptance Test.

---

## Scenario: Tidak terdapat data monitoring

**Given** belum terdapat data monitoring siswa.

**When** Guru membuka menu ringkasan monitoring.

**Then** sistem menampilkan informasi **"Belum terdapat data monitoring."** dan tidak menampilkan ringkasan yang dibuat dari data kosong.

**Metode Uji:** Integration Test.

---

# 12. US-10 ★ — Melihat Atribut Klasifikasi

**Prioritas:** Should  
**Aktor:** Guru/Wali Kelas  
**Use Case:** UC-08 View Classification Attributes

## Scenario: Menampilkan atribut model

**Given** model Decision Tree telah tersedia dan atribut model telah ditentukan.

**When** Guru membuka informasi atribut klasifikasi.

**Then** sistem menampilkan seluruh atribut yang digunakan oleh model Decision Tree.

**Metode Uji:** Integration Test + User Acceptance Test.

---

## Scenario: Model belum tersedia

**Given** model Decision Tree belum tersedia atau belum berhasil dimuat.

**When** Guru membuka informasi atribut klasifikasi.

**Then** sistem menampilkan pesan **"Informasi atribut klasifikasi belum tersedia."**

**Metode Uji:** Integration Test.

---

# 13. Ringkasan Skenario Pengujian

| User Story | Happy Path | Edge Case | Failure/Timeout | Jumlah |
|---|---:|---:|---:|---:|
| US-01 | ✓ | - | ✓ | 2 |
| US-02 | ✓ | ✓ | - | 2 |
| US-03 | ✓ | ✓ | - | 2 |
| US-04 | ✓ | ✓ | - | 2 |
| US-05 | ✓ | ✓ | - | 2 |
| US-06 ★ | ✓ | ✓ | ✓ | 3 |
| US-07 ★ | ✓ | ✓ | ✓ | 3 |
| US-08 | ✓ | ✓ | - | 2 |
| US-09 | ✓ | ✓ | - | 2 |
| US-10 ★ | ✓ | ✓ | - | 2 |

**Total skenario:** 22 skenario.

---

# 14. Tabel Keterlacakan

| User Story | Use Case | Acceptance Criteria | Metode Uji | FR |
|---|---|---|---|---|
| US-01 | UC-01 | Login valid/tidak valid | Unit + Integration + UAT | FR-01 |
| US-02 | UC-02 | Tambah data valid/tidak lengkap | Unit + Integration | FR-02 |
| US-03 | UC-02 | Ubah data valid/tidak valid | Unit + Integration | FR-02 |
| US-04 | UC-02 | Hapus/batal hapus | Unit + Integration + UAT | FR-02 |
| US-05 | UC-03 | Simpan valid/tidak lengkap | Unit + Integration | FR-03 |
| US-06 ★ | UC-04 | Happy path/edge/timeout | Unit + Integration + UAT | FR-04 |
| US-07 ★ | UC-05 | Hasil yakin/meragukan/tidak tersedia | Integration + UAT | FR-05 |
| US-08 | UC-06 | Riwayat tersedia/tidak tersedia | Integration + UAT | FR-06 |
| US-09 | UC-07 | Ringkasan tersedia/tidak tersedia | Integration + UAT | FR-07 |
| US-10 ★ | UC-08 | Atribut tersedia/model tidak tersedia | Integration + UAT | FR-08 |

---

# 15. Pemetaan Acceptance Criteria terhadap NFR

| NFR | Acceptance Criteria Terkait | Ukuran |
|---|---|---|
| NFR-02 Accuracy | US-06, US-07 | Akurasi model ≥ 80% [USULAN] |
| NFR-03 Latency | US-06 | Respons klasifikasi ≤ 3 detik [USULAN] |
| NFR-08 Reliability | US-06 | Input dan model yang sama menghasilkan output yang konsisten |
| NFR-09 Performance | US-06, US-07 | Sistem menghasilkan hasil atau status kegagalan |
| NFR-10 Usability | US-06, US-07, US-10 | Status dan hasil dapat dipahami pengguna |

---

# 16. Metode Pengujian

## 16.1 Unit Test

Digunakan untuk menguji fungsi individual seperti:

- validasi login;
- validasi data siswa;
- validasi data monitoring;
- validasi nilai atribut;
- validasi input Decision Tree;
- penanganan hasil kosong.

## 16.2 Integration Test

Digunakan untuk menguji hubungan antar-komponen:

```text
Form Monitoring
      ↓
Validasi
      ↓
Database
      ↓
Model Decision Tree
      ↓
Hasil Klasifikasi
      ↓
Halaman Hasil
```

Integration Test terutama digunakan pada:

- UC-03;
- UC-04 ★;
- UC-05 ★;
- UC-06;
- UC-07;
- UC-08 ★.

## 16.3 User Acceptance Test

Dilakukan bersama Guru/Wali Kelas untuk memastikan:

- alur mudah dipahami;
- status proses dapat dikenali;
- hasil klasifikasi dapat dibaca;
- pesan kesalahan dapat dipahami;
- pengguna memiliki jalan keluar ketika proses AI gagal.

---

# 17. Kriteria Lulus Fitur AI ★

Fitur klasifikasi dianggap memenuhi acceptance criteria apabila:

1. Data valid dapat diproses oleh Decision Tree.
2. Sistem menampilkan indikator proses selama analisis.
3. Hasil berhasil ditampilkan apabila model memberikan respons valid.
4. Proses dengan data batas valid tidak menghasilkan error.
5. Timeout tidak menghasilkan hasil palsu.
6. Hasil dengan confidence di bawah threshold diberi status meragukan.
7. Pengguna dapat mencoba kembali setelah kegagalan.
8. Pengguna dapat kembali ke data monitoring.
9. Akurasi model mencapai minimal **80% [USULAN]** pada dataset pengujian.
10. Waktu respons klasifikasi berada pada atau di bawah **3 detik [USULAN]** pada kondisi pengujian yang ditentukan.

---

# 18. Catatan Penting

Angka berikut masih berupa **[USULAN]**, bukan angka final dari SRS:

- **≤ 3 detik** untuk batas respons;
- **> 3 detik** sebagai kondisi timeout;
- **≥ 80%** sebagai target akurasi;
- **≥ 70%** sebagai confidence threshold.

Nilai final perlu ditentukan berdasarkan kesepakatan dengan pembimbing, karakteristik dataset, hasil eksperimen Decision Tree, dan kemampuan sistem yang sebenarnya.

Acceptance Criteria tidak boleh menyatakan model "akurat" tanpa ukuran. Oleh karena itu, pengujian model menggunakan metrik yang dapat dihitung, sedangkan keberhasilan fungsi sistem diuji melalui kondisi input dan output yang dapat diamati.

---

# 19. Checklist Review Tahap 4

- [x] Semua skenario menggunakan **Given, When, Then**.
- [x] Setiap User Story memiliki minimal 2 skenario.
- [x] User Story AI ★ memiliki happy path.
- [x] User Story AI ★ memiliki edge case.
- [x] User Story AI ★ memiliki failure/timeout scenario.
- [x] Kondisi pengujian dapat diamati.
- [x] Batas waktu menggunakan angka.
- [x] Target akurasi menggunakan angka.
- [x] Confidence threshold menggunakan angka.
- [x] Pesan error ditentukan.
- [x] Kegagalan model ditangani.
- [x] Pengguna memiliki jalur fallback.
- [x] Metode uji ditentukan.
- [x] Acceptance Criteria terhubung dengan Use Case.
- [x] Acceptance Criteria terhubung dengan Functional Requirement.
- [x] Parameter yang belum ditetapkan dalam SRS diberi label **[USULAN]**.

---

# 20. Alur Pengujian Fitur AI ★

```text
DATA MONITORING
      ↓
VALIDASI INPUT
      ↓
┌─────────────────┐
│ DATA VALID?     │
└─────────────────┘
   ↓           ↓
 TIDAK         YA
   ↓           ↓
Error       KIRIM DATA
               ↓
       SEDANG MENGANALISIS
               ↓
         DECISION TREE
               ↓
       ┌───────────────┐
       │ RESPONS ≤ 3s? │
       └───────────────┘
          ↓         ↓
         YA        TIDAK
          ↓         ↓
      CEK HASIL   TIMEOUT
          ↓         ↓
    ┌──────────┐   FALLBACK
    │ ≥ 70% ?  │   ↓
    └──────────┘   Coba Lagi /
      ↓      ↓     Kembali
     YA     TIDAK
      ↓      ↓
    HASIL   HASIL
   YAKIN   MERAGUKAN
      ↓      ↓
      └──┬───┘
         ↓
       SELESAI
```
