# LOW-LEVEL DESIGN (LLD) AWAL

## Sistem Monitoring Evaluasi Belajar Siswa SD Berbasis Web Menggunakan Algoritma Decision Tree

**Versi:** 0.1  
**Status:** Draft Awal  
**Platform:** Web  
**Backend:** Python Flask  
**Database:** MySQL  
**Machine Learning:** Decision Tree  
**Pola Arsitektur:** Client-Server  

> **Catatan:** Dokumen ini merupakan LLD awal yang diturunkan dari HLD. 
> ID FR/NFR harus disesuaikan kembali dengan SRS hasil revisi.

---

# 1. Ruang Lingkup LLD

LLD ini menjelaskan rancangan teknis untuk fitur utama sistem:

1. Pengelolaan data siswa.
2. Pengelolaan data evaluasi belajar.
3. Klasifikasi evaluasi belajar menggunakan Decision Tree.

Detail yang dibahas meliputi:

- modul dan class;
- atribut utama;
- method utama;
- skema data;
- API;
- alur klasifikasi;
- error handling;
- fallback;
- traceability terhadap kebutuhan sistem.

---

# 2. Stack dan Pola Sistem

| Komponen | Teknologi |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Database | MySQL |
| Machine Learning | Decision Tree |
| API | REST API |
| Development | Visual Studio Code |
| Browser | Chrome/Firefox/Browser modern |

## 2.1 Pola Sistem

Sistem menggunakan pola client-server.

```text
+----------------------+
|      Web Client      |
| HTML/CSS/JavaScript  |
+----------+-----------+
           |
           | HTTP/HTTPS
           v
+----------------------+
|    Flask Backend     |
|       REST API       |
+-----+-----------+----+
      |           |
      |           |
      v           v
+----------+  +----------------+
|  MySQL   |  | Decision Tree  |
| Database |  | Classification |
+----------+  +----------------+
