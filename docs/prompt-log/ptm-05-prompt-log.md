# PTM-05 Prompt Log

## Sistem Monitoring Evaluasi Belajar Siswa Berbasis Web Menggunakan Algoritma Decision Tree

**Versi:** 1.0  
**Status:** Draft  
**Penggunaan AI:** AI digunakan sebagai co-pilot dalam penyusunan dokumen rancangan sistem.

---

## 1. Tujuan Prompt Log

Dokumen ini digunakan untuk mencatat penggunaan AI dalam proses penyusunan rancangan teknis sistem.

AI digunakan untuk membantu:

- menerjemahkan LLD menjadi rancangan OpenAPI;
- menyusun rancangan ERD;
- menyusun data schema;
- memeriksa konsistensi antar dokumen;
- membantu menemukan bagian rancangan yang masih belum lengkap;
- memberikan saran perbaikan terhadap dokumen teknis.

Keputusan akhir terhadap rancangan tetap dilakukan berdasarkan LLD, kebutuhan sistem, dan hasil validasi.

---

# D.1 Prompt Session — OpenAPI

## D.1.1 Input

Dokumen yang digunakan sebagai acuan:

- PRD
- SRS
- Functional Requirements
- User Stories
- Acceptance Criteria
- HLD
- LLD Awal

## D.1.2 Tujuan

Menyusun rancangan REST API berdasarkan kebutuhan sistem dan LLD.

## D.1.3 Prompt yang digunakan

```text
Berdasarkan dokumen LLD awal, functional requirements,
user stories, dan acceptance criteria yang diberikan,
buat rancangan OpenAPI Specification 3.0 untuk Sistem
Monitoring Evaluasi Belajar Siswa Berbasis Web Menggunakan
Algoritma Decision Tree.

Pastikan endpoint yang dibuat hanya berasal dari kebutuhan
yang telah ditentukan pada LLD dan user stories.

Untuk setiap endpoint tentukan:
- HTTP method
- path
- request schema
- response schema
- HTTP status code
- error response

Gunakan format JSON dan jangan menambahkan fitur baru
di luar kebutuhan sistem.
Jika terdapat informasi yang belum ditentukan, tandai
dengan [ASUMSI-XX].
```

## D.1.4 Hasil AI

AI menghasilkan rancangan endpoint utama:

- `POST /api/login`
- `GET /api/students`
- `POST /api/students`
- `PUT /api/students/{id}`
- `DELETE /api/students/{id}`
- `POST /api/monitoring`
- `POST /api/classification`
- `GET /api/monitoring/history/{student_id}`
- `GET /api/monitoring/summary`
- `GET /api/monitoring/filter`
- `GET /api/monitoring/export`

Hasil kemudian disesuaikan dengan LLD sebelum digunakan.

## D.1.5 Evaluasi

Hasil AI diperiksa terhadap:

- Functional Requirements
- User Stories
- Acceptance Criteria
- LLD Awal

Perubahan dilakukan apabila terdapat endpoint, parameter, atau response yang tidak sesuai dengan kebutuhan sistem.

---

# D.2 Prompt Session — ERD dan Data Schema

## D.2.1 Input

Dokumen yang digunakan:

- LLD Awal
- OpenAPI Specification
- API Contract

## D.2.2 Tujuan

Menyusun ERD dan data schema yang konsisten dengan endpoint API.

## D.2.3 Prompt yang digunakan

```text
Berdasarkan LLD awal dan OpenAPI Specification,
buat rancangan Entity Relationship Diagram (ERD)
dan data schema untuk Sistem Monitoring Evaluasi
Belajar Siswa Berbasis Web Menggunakan Algoritma
Decision Tree.

Gunakan entitas yang telah terdapat pada LLD.

Tentukan:
- primary key
- foreign key
- atribut
- tipe data
- hubungan antarentitas

Kemudian buat schema yang dapat digunakan sebagai
acuan models.py.

Pastikan struktur ERD dan models.py konsisten dengan
request dan response pada OpenAPI.

Jangan menambahkan entitas baru yang tidak terdapat
pada rancangan sebelumnya.

Jika ada informasi yang belum final, tandai dengan
[ASUMSI-XX].
```

## D.2.4 Hasil AI

Entitas utama yang digunakan:

1. USER
2. STUDENT
3. MONITORING
4. CLASSIFICATION_RESULT

Relasi utama:

```text
STUDENT 1 ---- N MONITORING

STUDENT 1 ---- N CLASSIFICATION_RESULT

MONITORING 1 ---- 0..1 CLASSIFICATION_RESULT
```

Hasil kemudian dituangkan ke dalam:

```text
docs/db/erd.md
```

dan:

```text
backend/app/models.py
```

## D.2.5 Evaluasi

ERD dan models.py diperiksa dengan membandingkan:

- nama entitas;
- atribut;
- primary key;
- foreign key;
- tipe data;
- relasi;
- request dan response API.

---

# D.3 Iteration / Revision

## D.3.1 Masalah yang ditemukan

Pada rancangan awal terdapat beberapa bagian yang belum dapat ditentukan secara final, terutama:

- indikator monitoring;
- kelas target Decision Tree;
- struktur dataset;
- format export;
- hak akses pengguna.

## D.3.2 Prompt Iterasi

```text
Periksa kembali rancangan OpenAPI, ERD,
dan models.py berdasarkan LLD.

Identifikasi bagian yang:
1. belum konsisten;
2. belum memiliki definisi yang jelas;
3. masih membutuhkan keputusan;
4. berpotensi menyebabkan perbedaan antara
   database dan API.

Jangan membuat asumsi baru tanpa menandainya.
Gunakan [ASUMSI-XX] untuk bagian yang belum final.
```

## D.3.3 Tindakan Perbaikan

Setelah dilakukan pemeriksaan, bagian yang belum final dicatat sebagai asumsi dan tidak dibuat terlalu spesifik.

Contohnya:

```text
data_monitoring
```

sementara digunakan sebagai struktur data fleksibel karena indikator monitoring belum ditetapkan secara final.

---

# D.4 Validasi Hasil AI

Hasil yang dibuat dengan bantuan AI tidak langsung digunakan tanpa pemeriksaan.

Validasi dilakukan dengan cara:

- membandingkan endpoint dengan LLD;
- membandingkan entitas dengan ERD;
- membandingkan request/response dengan models.py;
- memastikan tidak ada fitur baru di luar kebutuhan;
- memeriksa bagian yang masih berupa asumsi;
- melakukan revisi apabila ditemukan ketidaksesuaian.

---

# D.5 Daftar Asumsi

| ID | Asumsi | Tindakan |
|---|---|---|
| ASUMSI-01 | Indikator monitoring belum final | Menunggu validasi |
| ASUMSI-02 | Kelas target Decision Tree belum final | Menunggu penentuan dataset |
| ASUMSI-03 | Format export belum ditentukan | Ditentukan pada tahap implementasi |
| ASUMSI-04 | Hak akses pengguna belum dirinci | Perlu validasi |
| ASUMSI-05 | Dataset pelatihan belum final | Ditentukan pada tahap penelitian |

---

# D.6 Kesimpulan Penggunaan AI

AI digunakan sebagai alat bantu dalam proses perancangan dan dokumentasi teknis.

AI tidak digunakan untuk menentukan kebutuhan penelitian secara mandiri.

Keputusan mengenai struktur sistem, kebutuhan fungsional, indikator monitoring, data penelitian, dan algoritma tetap mengacu pada dokumen kebutuhan, LLD, serta hasil validasi.

Dokumen hasil AI diperiksa dan disesuaikan sebelum digunakan dalam repository.
