# HIGH-LEVEL DESIGN (HLD)

## Sistem Monitoring Evaluasi Belajar Siswa SD Berbasis Web Menggunakan Algoritma Decision Tree

**Versi:** 0.1  
**Status:** Draft Awal  
**Platform:** Web  
**Backend:** Python Flask  
**Database:** MySQL  
**Algoritma:** Decision Tree  
**Target:** Prototype 1 Semester  

---

## 1. Gambaran Umum

Sistem Monitoring Evaluasi Belajar Siswa SD Berbasis Web merupakan aplikasi yang digunakan untuk membantu guru dalam mengelola data siswa, data evaluasi belajar, serta melihat hasil klasifikasi evaluasi belajar siswa menggunakan algoritma Decision Tree.

Sistem dirancang berbasis web sehingga dapat diakses melalui browser menggunakan perangkat komputer maupun perangkat mobile.

Algoritma Decision Tree digunakan sebagai komponen klasifikasi untuk mengolah data evaluasi belajar siswa dan menghasilkan kelas atau kategori evaluasi berdasarkan model yang telah dilatih.

> **[ASUMSI-01]** Kategori hasil evaluasi belajar ditentukan berdasarkan dataset penelitian dan hasil proses pelatihan model, karena kategori target belum ditentukan secara eksplisit pada requirements.

---

## 2. Tujuan Sistem

Tujuan sistem adalah:

1. Mengelola data siswa secara terstruktur.
2. Mengelola data evaluasi belajar siswa.
3. Melakukan proses klasifikasi menggunakan algoritma Decision Tree.
4. Menampilkan hasil klasifikasi evaluasi belajar siswa.
5. Membantu guru melakukan monitoring hasil evaluasi belajar siswa.

---

## 3. Pengguna Sistem

> **[ASUMSI-02]** Berdasarkan kebutuhan sistem yang telah dirancang sebelumnya, pengguna utama sistem adalah guru.

### 3.1 Guru

Guru dapat:

- Login ke sistem.
- Mengelola data siswa.
- Memasukkan data evaluasi belajar.
- Menjalankan proses klasifikasi.
- Melihat hasil klasifikasi.
- Melihat data monitoring evaluasi siswa.

> **[ASUMSI-03]** Admin tidak dimasukkan sebagai pengguna utama pada HLD karena belum terdapat kebutuhan fungsional admin yang diberikan pada requirements.

---

## 4. Arsitektur Sistem

Arsitektur sistem menggunakan pola client-server.

```mermaid
flowchart LR
    A[Client / Browser]
    B[Flask Backend API]
    C[Decision Tree Service]
    D[(MySQL Database)]

    A -->|HTTP/HTTPS| B
    B -->|Data Evaluasi| C
    C -->|Hasil Klasifikasi| B
    B -->|CRUD Data| D
    D -->|Data Siswa & Evaluasi| B
