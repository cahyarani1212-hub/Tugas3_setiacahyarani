# API Contract

## Sistem Monitoring Evaluasi Belajar Siswa Berbasis Web Menggunakan Algoritma Decision Tree

**Versi:** 1.0  
**Status:** Draft Awal  
**Backend:** Python Flask  
**Database:** MySQL  
**API Style:** REST API  
**Format Data:** JSON

---

## 1. Tujuan

Dokumen API Contract digunakan untuk menjelaskan kesepakatan struktur komunikasi antara client dan server pada Sistem Monitoring Evaluasi Belajar Siswa Berbasis Web.

Dokumen ini menjadi acuan dalam penyusunan REST API dan memastikan endpoint, request, response, serta struktur data tetap konsisten dengan LLD, OpenAPI, ERD, dan models.py.

---

## 2. Base URL

```text
http://localhost:5000/api
```

---

## 3. Format Komunikasi

API menggunakan:

- HTTP/HTTPS
- REST API
- JSON sebagai format request dan response
- HTTP Status Code sebagai indikator hasil proses

---

## 4. Daftar Endpoint

| No | Method | Endpoint | Fungsi |
|---|---|---|---|
| 1 | POST | `/api/login` | Autentikasi pengguna |
| 2 | GET | `/api/students` | Menampilkan data siswa |
| 3 | POST | `/api/students` | Menambahkan data siswa |
| 4 | PUT | `/api/students/{id}` | Mengubah data siswa |
| 5 | DELETE | `/api/students/{id}` | Menghapus data siswa |
| 6 | POST | `/api/monitoring` | Menyimpan data monitoring |
| 7 | POST | `/api/classification` | Melakukan klasifikasi Decision Tree |
| 8 | GET | `/api/monitoring/history/{student_id}` | Menampilkan riwayat monitoring |
| 9 | GET | `/api/monitoring/summary` | Menampilkan ringkasan monitoring |
| 10 | GET | `/api/monitoring/filter` | Melakukan filtering data monitoring |
| 11 | GET | `/api/monitoring/export` | Mengekspor data monitoring |

---

## 5. Authentication

### Endpoint

```text
POST /api/login
```

### Request

```json
{
  "username": "admin",
  "password": "password"
}
```

### Response Berhasil

```json
{
  "message": "Login berhasil",
  "token": "example-token"
}
```

### Status Code

| Status | Keterangan |
|---|---|
| 200 | Login berhasil |
| 401 | Username atau password tidak valid |
| 422 | Data request tidak valid |
| 500 | Kesalahan server |

---

## 6. Student Management

### 6.1 Mendapatkan Data Siswa

```text
GET /api/students
```

Response:

```json
{
  "data": [
    {
      "id": 1,
      "nama": "Nama Siswa",
      "kelas": "X-A",
      "created_at": "2026-10-03T08:00:00",
      "updated_at": "2026-10-03T08:00:00"
    }
  ]
}
```

---

### 6.2 Menambahkan Data Siswa

```text
POST /api/students
```

Request:

```json
{
  "nama": "Nama Siswa",
  "kelas": "X-A"
}
```

Response:

```json
{
  "message": "Data siswa berhasil ditambahkan",
  "data": {
    "id": 1,
    "nama": "Nama Siswa",
    "kelas": "X-A"
  }
}
```

Status:

- 201 Created
- 400 Bad Request
- 422 Unprocessable Entity
- 500 Internal Server Error

---

### 6.3 Mengubah Data Siswa

```text
PUT /api/students/{id}
```

Request:

```json
{
  "nama": "Nama Siswa Baru",
  "kelas": "X-B"
}
```

Response:

```json
{
  "message": "Data siswa berhasil diperbarui"
}
```

Status:

- 200 OK
- 400 Bad Request
- 404 Not Found
- 422 Unprocessable Entity
- 500 Internal Server Error

---

### 6.4 Menghapus Data Siswa

```text
DELETE /api/students/{id}
```

Response:

```json
{
  "message": "Data siswa berhasil dihapus"
}
```

Status:

- 200 OK
- 404 Not Found
- 500 Internal Server Error

---

## 7. Monitoring

### Endpoint

```text
POST /api/monitoring
```

Request:

```json
{
  "student_id": 1,
  "tanggal": "2026-10-03",
  "data_monitoring": {
    "indikator_1": "nilai",
    "indikator_2": "nilai"
  }
}
```

Response:

```json
{
  "id": 1,
  "student_id": 1,
  "tanggal": "2026-10-03",
  "data_monitoring": {
    "indikator_1": "nilai",
    "indikator_2": "nilai"
  },
  "created_at": "2026-10-03T08:00:00"
}
```

### Status Code

| Status | Keterangan |
|---|---|
| 201 | Data monitoring berhasil disimpan |
| 400 | Request tidak valid |
| 404 | Data siswa tidak ditemukan |
| 422 | Format data tidak valid |
| 500 | Kesalahan server |

---

## 8. Classification

### Endpoint

```text
POST /api/classification
```

### Request

```json
{
  "student_id": 1,
  "monitoring_id": 1
}
```

### Proses

Data monitoring diproses melalui tahapan:

1. Validasi data
2. Preprocessing
3. Pemrosesan Decision Tree
4. Prediksi kelas
5. Penyimpanan hasil klasifikasi
6. Pengiriman hasil kepada client

### Response

```json
{
  "student_id": 1,
  "monitoring_id": 1,
  "hasil": "Hasil Klasifikasi"
}
```

### Status Code

| Status | Keterangan |
|---|---|
| 200 | Klasifikasi berhasil |
| 400 | Data klasifikasi tidak valid |
| 404 | Data siswa atau monitoring tidak ditemukan |
| 422 | Data request tidak sesuai |
| 500 | Kesalahan proses klasifikasi |

> Catatan: kelas target Decision Tree masih dalam tahap penentuan sehingga nilai `hasil` belum ditetapkan secara final.

---

## 9. Monitoring History

### Endpoint

```text
GET /api/monitoring/history/{student_id}
```

Digunakan untuk menampilkan riwayat monitoring berdasarkan siswa.

Response:

```json
{
  "student_id": 1,
  "data": [
    {
      "id": 1,
      "tanggal": "2026-10-03",
      "data_monitoring": {
        "indikator_1": "nilai",
        "indikator_2": "nilai"
      }
    }
  ]
}
```

---

## 10. Monitoring Summary

### Endpoint

```text
GET /api/monitoring/summary
```

Digunakan untuk menampilkan ringkasan data monitoring.

Response:

```json
{
  "total_siswa": 10,
  "total_monitoring": 25,
  "total_hasil_klasifikasi": 25
}
```

---

## 11. Monitoring Filter

### Endpoint

```text
GET /api/monitoring/filter
```

Digunakan untuk melakukan penyaringan data monitoring berdasarkan parameter yang tersedia.

Contoh:

```text
GET /api/monitoring/filter?student_id=1
```

Response:

```json
{
  "data": [
    {
      "id": 1,
      "student_id": 1,
      "tanggal": "2026-10-03"
    }
  ]
}
```

---

## 12. Monitoring Export

### Endpoint

```text
GET /api/monitoring/export
```

Digunakan untuk mengekspor data monitoring.

Format file ekspor akan ditentukan pada tahap implementasi berdasarkan kebutuhan sistem.

---

## 13. Error Response

Format error secara umum:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Data request tidak valid"
  }
}
```

Kode HTTP yang digunakan:

| HTTP Status | Penggunaan |
|---|---|
| 200 | Request berhasil |
| 201 | Data berhasil dibuat |
| 400 | Request tidak valid |
| 401 | Tidak terautentikasi |
| 403 | Tidak memiliki akses |
| 404 | Data tidak ditemukan |
| 422 | Validasi data gagal |
| 500 | Kesalahan server |

---

## 14. Keamanan dan Privasi

API dirancang dengan beberapa pertimbangan keamanan:

1. Password pengguna tidak dikirimkan dalam response API.
2. Password harus disimpan dalam bentuk hash pada implementasi database.
3. Endpoint yang membutuhkan autentikasi harus melakukan pemeriksaan akses.
4. Input dari client harus divalidasi.
5. Data monitoring siswa tidak dikirim ke layanan AI eksternal.
6. Response API hanya mengembalikan data yang diperlukan.

---

## 15. Keterkaitan dengan ERD

API menggunakan entitas yang terdapat pada ERD:

| Entitas | Penggunaan |
|---|---|
| USER | Autentikasi pengguna |
| STUDENT | Data siswa |
| MONITORING | Data monitoring |
| CLASSIFICATION_RESULT | Hasil klasifikasi |

---

## 16. Keterkaitan dengan models.py

Struktur data API disesuaikan dengan model pada:

```text
backend/app/models.py
```

Model utama:

- `User`
- `Student`
- `StudentCreate`
- `StudentUpdate`
- `Monitoring`
- `MonitoringCreate`
- `ClassificationResult`
- `ClassificationRequest`
- `ClassificationResponse`

---

## 17. Keterkaitan dengan LLD

API Contract mengacu pada rancangan endpoint yang telah ditentukan pada LLD awal.

Tidak ada endpoint tambahan di luar kebutuhan fungsional yang telah ditetapkan.

Mapping utama:

| Functional Requirement | Endpoint |
|---|---|
| FR-01 Authentication | `/api/login` |
| FR-02 Manage Student Data | `/api/students` |
| FR-03 Record Monitoring Data | `/api/monitoring` |
| FR-04 Decision Tree Classification | `/api/classification` |
| FR-05 Display Classification Result | `/api/classification` |
| FR-06 Monitoring History | `/api/monitoring/history/{student_id}` |
| FR-07 Monitoring Summary | `/api/monitoring/summary` |
| FR-08 Classification Attributes | `/api/classification` |
| FR-09 Filtering | `/api/monitoring/filter` |
| FR-10 Export | `/api/monitoring/export` |

---

## 18. Asumsi dan Hal yang Belum Final

| ID | Asumsi / Hal Belum Final | Status |
|---|---|---|
| ASUMSI-01 | Indikator monitoring belum ditetapkan secara final | Perlu validasi |
| ASUMSI-02 | Kelas target Decision Tree belum ditetapkan secara final | Perlu validasi |
| ASUMSI-03 | Format ekspor belum ditentukan | Perlu keputusan |
| ASUMSI-04 | Hak akses pengguna masih perlu dirinci | Perlu validasi |
| ASUMSI-05 | Struktur dataset pelatihan Decision Tree belum final | Perlu validasi |

---

## 19. Status Dokumen

| Komponen | Status |
|---|---|
| Daftar endpoint | Selesai |
| Request schema | Selesai |
| Response schema | Selesai |
| Error response | Selesai |
| Mapping ERD | Selesai |
| Mapping models.py | Selesai |
| Mapping LLD | Selesai |
| Indikator monitoring | Belum final |
| Target klasifikasi | Belum final |
| Format export | Belum final |

---

**Dokumen ini merupakan rancangan awal dan akan diperbarui apabila terdapat perubahan pada LLD, OpenAPI, ERD, atau models.py.**
