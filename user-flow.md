# USER FLOW

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Dokumen:** User Flow  
**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode:** Decision Tree  
**Tahap:** Praktikum PRD → SRS → HLD → LLD

---

## 1. Tujuan

Dokumen ini mendefinisikan alur interaksi pengguna untuk fitur AI utama dan satu fitur utama lainnya pada Sistem Monitoring Minat Belajar Siswa SD Berbasis Web.

Fokus user flow:

1. **Fitur AI ★:** Klasifikasi Minat Belajar Siswa menggunakan Decision Tree.
2. **Fitur utama:** Pengisian dan penyimpanan Data Monitoring Siswa.

User flow dirancang agar pengguna memperoleh informasi mengenai status sistem selama proses validasi, analisis AI, hasil klasifikasi, maupun ketika terjadi kegagalan proses.

---

# 2. Persona dan Skenario

## 2.1 Persona Utama

**Aktor:** Guru/Wali Kelas

Guru/Wali Kelas menggunakan sistem untuk:

- memilih siswa;
- mengisi data monitoring;
- memeriksa data monitoring;
- menjalankan proses klasifikasi;
- melihat hasil klasifikasi;
- melakukan pemeriksaan ulang apabila hasil tidak meyakinkan.

> **Catatan:** Detail persona dapat disesuaikan dengan hasil Persona & Skenario pada tahap sebelumnya.

---

# 3. Fitur AI ★ — Klasifikasi Minat Belajar

## 3.1 Tujuan

Memungkinkan Guru/Wali Kelas melakukan klasifikasi terhadap data monitoring siswa menggunakan algoritma Decision Tree.

## 3.2 Titik Masuk

Guru/Wali Kelas memilih menu:

**Klasifikasi Minat Belajar**

## 3.3 Alur Utama

1. Guru login ke sistem.
2. Sistem memverifikasi autentikasi pengguna.
3. Guru memilih siswa yang akan dianalisis.
4. Sistem mengambil data monitoring siswa.
5. Sistem menampilkan data yang diperlukan untuk proses klasifikasi.
6. Guru memeriksa dan melengkapi data jika diperlukan.
7. Sistem melakukan validasi awal terhadap data.
8. Jika data tidak valid atau belum lengkap, sistem menampilkan pesan kesalahan.
9. Guru memperbaiki data.
10. Sistem melakukan validasi ulang.
11. Jika data valid, sistem mengirim data untuk proses klasifikasi.
12. Sistem menampilkan indikator **"Sedang menganalisis..."**.
13. Algoritma Decision Tree memproses data.
14. Sistem menerima hasil klasifikasi.
15. Sistem memeriksa status hasil klasifikasi.
16. Jika hasil memenuhi kondisi yang ditentukan, sistem menampilkan hasil klasifikasi.
17. Jika hasil dianggap meragukan, sistem menampilkan status **"Hasil kurang meyakinkan"**.
18. Guru dapat memeriksa atau melengkapi kembali data monitoring.
19. Jika model gagal merespons, sistem menampilkan status kegagalan.
20. Guru dapat memilih **Coba Lagi** atau kembali ke data monitoring.
21. Proses selesai.

---

# 4. Empat Status Sistem

## 4.1 Status 1 — Validasi Awal

**Kondisi:**

Pengguna sedang mengisi atau mengirim data untuk proses klasifikasi.

**Proses:**

Sistem memeriksa:

- kelengkapan data;
- format data;
- nilai data;
- atribut yang diperlukan oleh model.

**Jika tidak valid:**

```text
Data tidak valid
       ↓
Tampilkan pesan kesalahan
       ↓
Pengguna memperbaiki data
       ↓
Validasi ulang
