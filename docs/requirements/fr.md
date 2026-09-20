# FUNCTIONAL REQUIREMENTS (FR)

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode/Model:** Decision Tree  
**Dokumen Acuan:** SRS dan User Stories

---

## 1. TUJUAN

Dokumen ini mendefinisikan kebutuhan fungsional yang harus tersedia pada Sistem Monitoring Minat Belajar Siswa SD Berbasis Web.

Functional Requirement digunakan sebagai dasar untuk:

- Menentukan fungsi utama sistem.
- Menentukan prioritas pengembangan menggunakan MoSCoW.
- Menghubungkan kebutuhan sistem dengan User Story.
- Menjadi dasar pengujian fungsional.
- Menjadi acuan implementasi fitur.

---

## 2. DAFTAR FUNCTIONAL REQUIREMENTS

### 2.1 Must Have

| ID | Functional Requirement | User Story | Kategori | Metode Verifikasi |
|---|---|---|---|---|
| FR-01 | Sistem harus dapat melakukan autentikasi pengguna saat pengguna memasukkan kredensial yang valid → pengguna berhasil masuk ke sistem | US-01 | Fitur Inti | Black-box Testing |
| FR-02 | Sistem harus dapat mengelola data siswa saat Admin Sekolah memiliki hak akses pengelolaan data → data siswa dapat ditambahkan, diperbarui, atau dihapus | US-02, US-03, US-04 | Fitur Inti | Black-box Testing |
| FR-03 | Sistem harus dapat menyimpan data monitoring siswa saat Guru/Wali Kelas mengisi data monitoring dengan lengkap → data monitoring tersimpan | US-05 | Fitur Inti | Black-box Testing |
| FR-04 ★ | Sistem harus dapat melakukan klasifikasi menggunakan algoritma Decision Tree saat data dan atribut yang diperlukan tersedia → sistem menghasilkan kelas hasil klasifikasi | US-06 | Fitur AI ★ | Pengujian Model + Black-box Testing |
| FR-05 ★ | Sistem harus dapat menampilkan hasil klasifikasi saat proses klasifikasi berhasil → hasil klasifikasi siswa ditampilkan | US-07 | Fitur AI ★ | Black-box Testing |

---

### 2.2 Should Have

| ID | Functional Requirement | User Story | Kategori | Metode Verifikasi |
|---|---|---|---|---|
| FR-06 | Sistem harus dapat menampilkan riwayat monitoring saat Guru/Wali Kelas memilih data seorang siswa → riwayat monitoring siswa ditampilkan | US-08 | Fitur Inti | Black-box Testing |
| FR-07 | Sistem harus dapat menampilkan ringkasan data monitoring saat Guru/Wali Kelas membuka bagian ringkasan monitoring → informasi ringkasan ditampilkan | US-09 | Fitur Inti | Black-box Testing |
| FR-08 ★ | Sistem harus dapat menampilkan atribut yang digunakan dalam proses klasifikasi saat hasil klasifikasi tersedia → informasi atribut klasifikasi ditampilkan | US-10 | Fitur AI ★ | Black-box Testing |

---

## 3. DETAIL FUNCTIONAL REQUIREMENTS

### FR-01 — Autentikasi Pengguna

**Prioritas:** Must  
**Kategori:** Fitur Inti  
**User Story:** US-01

#### Deskripsi

Sistem harus menyediakan proses autentikasi agar Guru/Wali Kelas atau pengguna yang memiliki hak akses dapat masuk ke sistem.

#### Kondisi

Pengguna memasukkan kredensial yang valid.

#### Output

Pengguna berhasil masuk dan dapat mengakses fitur sesuai hak aksesnya.

#### Acceptance Criteria

- Kredensial valid → login berhasil.
- Kredensial tidak valid → login ditolak.
- Pengguna yang belum login tidak dapat mengakses fitur yang membutuhkan autentikasi.

---

### FR-02 — Pengelolaan Data Siswa

**Prioritas:** Must  
**Kategori:** Fitur Inti  
**User Story:** US-02, US-03, US-04

#### Deskripsi

Sistem harus dapat menyediakan pengelolaan data siswa yang dibutuhkan sebagai dasar proses monitoring.

#### Aktivitas

1. Menambahkan data siswa.
2. Memperbarui data siswa.
3. Menghapus data siswa yang sudah tidak diperlukan.

#### Output

Data siswa tersimpan dan dapat digunakan dalam proses monitoring.

#### Acceptance Criteria

- Data siswa yang valid dapat ditambahkan.
- Data siswa yang tersimpan dapat diperbarui.
- Data siswa yang dipilih dapat dihapus sesuai hak akses.
- Data siswa yang tersimpan dapat digunakan dalam proses monitoring.

---

### FR-03 — Pencatatan Data Monitoring

**Prioritas:** Must  
**Kategori:** Fitur Inti  
**User Story:** US-05

#### Deskripsi

Sistem harus dapat menerima dan menyimpan data monitoring siswa yang dimasukkan oleh Guru/Wali Kelas.

#### Kondisi

Guru/Wali Kelas memasukkan data monitoring dengan lengkap.

#### Output

Data monitoring tersimpan dan dapat digunakan untuk proses berikutnya.

#### Acceptance Criteria

- Data monitoring yang lengkap dapat disimpan.
- Data monitoring yang belum lengkap mendapatkan validasi.
- Data monitoring tersimpan pada siswa yang sesuai.
- Data yang tersimpan dapat digunakan dalam proses klasifikasi apabila memenuhi persyaratan model.

---

### FR-04 ★ — Klasifikasi Decision Tree

**Prioritas:** Must  
**Kategori:** Fitur AI ★  
**User Story:** US-06

#### Deskripsi

Sistem harus dapat melakukan klasifikasi menggunakan algoritma Decision Tree berdasarkan atribut yang telah ditentukan dalam dataset penelitian.

#### Kondisi

Data dan atribut yang dibutuhkan untuk klasifikasi tersedia.

#### Input

Data monitoring siswa dan atribut yang digunakan oleh model.

#### Proses

```text
Data Monitoring
       ↓
Pemeriksaan Data
       ↓
Data yang Memenuhi Persyaratan
       ↓
Decision Tree
       ↓
Proses Klasifikasi
