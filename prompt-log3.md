# PROMPT LOG

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Dokumen:** Prompt Log  
**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode:** Decision Tree  
**Tahap:** PRD → SRS → User Stories → Use Case → User Flow → Acceptance Criteria

---

# 1. Tujuan

Dokumen ini digunakan untuk mencatat penggunaan AI selama proses perancangan Sistem Monitoring Minat Belajar Siswa SD Berbasis Web.

Prompt Log berisi:

1. Prompt yang diberikan kepada AI.
2. Tujuan penggunaan prompt.
3. Ringkasan hasil generate awal dari AI.
4. Koreksi atau penyesuaian manual oleh tim.
5. Keputusan akhir yang digunakan dalam dokumen proyek.

Dokumen ini dibuat untuk menjaga keterlacakan proses pengembangan dan membedakan hasil generate AI dengan keputusan yang telah diperiksa atau disesuaikan secara manual.

---

# 2. Aturan Penggunaan AI

AI digunakan sebagai alat bantu dalam:

- menyusun struktur dokumen;
- membuat rancangan awal User Story;
- menyusun Use Case;
- membuat alur pengguna;
- menyusun Acceptance Criteria;
- membantu mengidentifikasi edge case;
- membantu menyusun dokumentasi teknis.

AI **tidak digunakan sebagai pengganti keputusan tim**.

Setiap hasil generate AI harus diperiksa dan disesuaikan dengan:

- kebutuhan sistem;
- kondisi objek penelitian;
- SRS;
- PRD;
- kemampuan sistem yang sebenarnya;
- arahan dosen/pembimbing.

---

# 3. Log Prompt

## PL-01 — Penyusunan PRD

**Tanggal:** 2026-09-15  
**Tujuan:** Membuat rancangan awal Product Requirements Document.

### Prompt

> Buatkan PRD untuk sistem monitoring minat belajar siswa SD berbasis web menggunakan algoritma Decision Tree berdasarkan indikator sosial dan emosional. Sistem harus memiliki fitur yang benar-benar berjalan dan bukan hanya menampilkan informasi.

### Hasil Generate Awal

AI menghasilkan struktur PRD yang terdiri dari:

- Executive Summary;
- Problem Statement;
- Target User;
- Stakeholder;
- Value Proposition;
- Goals;
- Scope;
- Non-Goals;
- Assumptions;
- Risks;
- Requirements.

### Koreksi Manual

Tim melakukan penyesuaian terhadap:

- ruang lingkup sistem;
- peran pengguna;
- fitur yang benar-benar diperlukan;
- pemisahan fitur AI dengan fitur sistem biasa;
- batasan agar sistem tidak melakukan diagnosis psikologis;
- penandaan informasi yang belum memiliki bukti sebagai `[ASUMSI]`.

### Keputusan Akhir

PRD digunakan sebagai dasar penyusunan SRS.

---

# 4. PL-02 — Penyusunan SRS

**Tanggal:** 2026-09-15  
**Tujuan:** Mengubah kebutuhan produk menjadi Software Requirements Specification.

### Prompt

> Berdasarkan PRD sistem monitoring minat belajar siswa SD berbasis web menggunakan Decision Tree, buatkan SRS yang berisi functional requirements, non-functional requirements, data requirements, business rules, security, error handling, limitations, dan traceability.

### Hasil Generate Awal

AI menghasilkan Functional Requirements:

- FR-01 Login;
- FR-02 Pengelolaan data siswa;
- FR-03 Data monitoring;
- FR-04 Klasifikasi menggunakan Decision Tree;
- FR-05 Menampilkan hasil klasifikasi;
- FR-06 Riwayat monitoring;
- FR-07 Ringkasan monitoring;
- FR-08 Menampilkan atribut klasifikasi;
- FR-09 Filter;
- FR-10 Export.

### Koreksi Manual

Tim melakukan pemeriksaan terhadap:

- kesesuaian fitur dengan kebutuhan penelitian;
- pembagian fitur Must, Should, dan Could;
- pemisahan fitur AI dan non-AI;
- keamanan data siswa;
- batasan sistem agar tidak melakukan diagnosis;
- penggunaan `[ASUMSI]` untuk nilai yang belum ditentukan.

### Keputusan Akhir

FR-04 dan FR-05 ditetapkan sebagai fitur AI utama.

---

# 5. PL-03 — Penyusunan User Stories

**Tanggal:** 2026-09-16  
**Tujuan:** Menjabarkan kebutuhan sistem menjadi User Story.

### Prompt

> Buatkan User Stories untuk sistem monitoring minat belajar siswa SD berbasis web berdasarkan SRS. Gunakan format sebagai [role], saya ingin [goal], sehingga [benefit]. Pisahkan fitur AI yang menggunakan Decision Tree dan beri tanda ★.

### Hasil Generate Awal

AI menghasilkan beberapa User Story untuk:

- login;
- pengelolaan data siswa;
- input monitoring;
- klasifikasi Decision Tree;
- melihat hasil klasifikasi;
- riwayat;
- ringkasan monitoring;
- atribut klasifikasi.

### Koreksi Manual

Tim memeriksa apakah setiap User Story:

- memiliki aktor yang jelas;
- memiliki tujuan yang dapat dilakukan sistem;
- sesuai dengan FR;
- tidak terlalu luas;
- tidak mengandung fitur yang belum direncanakan.

FR-02 yang awalnya berupa satu kebutuhan pengelolaan data siswa kemudian dipecah menjadi:

- US-02 menambah data;
- US-03 mengubah data;
- US-04 menghapus data.

### Keputusan Akhir

Digunakan 10 User Story:

- US-01 Login;
- US-02 Tambah data siswa;
- US-03 Ubah data siswa;
- US-04 Hapus data siswa;
- US-05 Input monitoring;
- US-06 ★ Klasifikasi minat belajar;
- US-07 ★ Melihat hasil klasifikasi;
- US-08 Riwayat monitoring;
- US-09 Ringkasan monitoring;
- US-10 ★ Atribut klasifikasi.

---

# 6. PL-04 — Penyusunan Use Case

**Tanggal:** 2026-09-16  
**Tujuan:** Membuat Use Case berdasarkan User Stories.

### Prompt

> Berdasarkan User Stories sistem monitoring minat belajar siswa SD, buatkan Use Case yang memiliki primary actor, supporting actor, precondition, main flow, alternative flow, exception, dan traceability ke Functional Requirement.

### Hasil Generate Awal

AI menghasilkan Use Case:

- UC-01 Authenticate User;
- UC-02 Manage Student Data;
- UC-03 Record Monitoring Data;
- UC-04 Perform Student Classification;
- UC-05 View Classification Result;
- UC-06 View Monitoring History;
- UC-07 View Monitoring Summary;
- UC-08 View Classification Attributes.

### Koreksi Manual

Tim menambahkan perhatian khusus pada proses AI:

- validasi input;
- model tidak tersedia;
- timeout;
- kegagalan koneksi;
- hasil dengan confidence rendah.

Tim juga memastikan bahwa AI tidak dianggap sebagai pengambil keputusan akhir terhadap siswa.

### Keputusan Akhir

UC-04 menjadi Use Case utama untuk proses Decision Tree.

---

# 7. PL-05 — Penyusunan User Flow

**Tanggal:** 2026-09-16  
**Tujuan:** Menjelaskan alur interaksi pengguna dengan sistem.

### Prompt

> Buatkan user flow untuk sistem monitoring minat belajar siswa SD. Fokus pada alur input data monitoring dan klasifikasi menggunakan Decision Tree. Tampilkan kondisi validasi awal, proses AI, hasil, timeout, kegagalan AI, dan fallback.

### Hasil Generate Awal

AI menghasilkan alur:

```text
Login
  ↓
Pilih Siswa
  ↓
Data Monitoring
  ↓
Validasi
  ↓
Decision Tree
  ↓
Hasil Klasifikasi
