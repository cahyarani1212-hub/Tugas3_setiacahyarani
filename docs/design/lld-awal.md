# LOW-LEVEL DESIGN (LLD)

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Dokumen:** Low-Level Design  
**Versi:** 1.0  
**Status:** Draft  
**Platform:** Web  
**Backend:** Python + Flask  
**Database:** MySQL  
**Metode AI:** Decision Tree  
**Pola Arsitektur:** Client-Server  
**Tahap:** PRD → SRS → HLD → LLD

---

# 1. Tujuan LLD

LLD ini menerjemahkan desain HLD menjadi rancangan teknis yang lebih detail dan siap digunakan sebagai dasar implementasi kode.

Fokus LLD:

1. Authentication.
2. Pengelolaan data siswa.
3. Pencatatan data monitoring.
4. Klasifikasi minat belajar menggunakan Decision Tree.
5. Penyimpanan dan penampilan hasil klasifikasi.
6. Penanganan error dan kegagalan model.

LLD tidak mengubah requirement yang telah ditetapkan pada SRS.

---

# 2. Fitur Must yang Diimplementasikan

Berdasarkan SRS, fitur Must yang menjadi fokus implementasi adalah:

| ID | Fitur | Prioritas | Komponen |
|---|---|---|---|
| FR-01 | Login pengguna | Must | Authentication |
| FR-02 | Pengelolaan data siswa | Must | Student Data Service |
| FR-03 | Pencatatan data monitoring | Must | Monitoring Service |
| FR-04 ★ | Klasifikasi menggunakan Decision Tree | Must | Classification Service |
| FR-05 ★ | Menampilkan hasil klasifikasi | Must | Classification Result |

Fitur Should dan Could tidak menjadi fokus utama LLD ini.

---

# 3. Struktur Modul

Struktur modul tingkat implementasi:

```text
Web Client
    │
    ▼
Flask Backend
    │
    ├── Authentication
    │
    ├── Student Management
    │
    ├── Monitoring
    │
    └── Classification
            │
            ├── Validation
            ├── Preprocessing
            ├── Decision Tree Model
            ├── Postprocessing
            └── Fallback
                    │
                    ▼
                 MySQL
