# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Versi:** 1.0  
**Status:** Draft  
**Platform:** Website  
**Metode/Model:** Decision Tree  
**Target Pengembangan:** 1 Semester  

---

# 1. PENDAHULUAN

## 1.1 Tujuan

Sistem Monitoring Minat Belajar Siswa SD Berbasis Web bertujuan untuk membantu proses monitoring kondisi belajar siswa melalui pengelolaan data siswa, data monitoring, dan proses klasifikasi menggunakan algoritma Decision Tree.

Sistem tidak digunakan untuk melakukan diagnosis psikologis atau medis terhadap siswa. Hasil klasifikasi digunakan sebagai informasi pendukung bagi guru dalam melakukan pemantauan terhadap kondisi belajar siswa.

---

## 1.2 Ruang Lingkup Sistem

Sistem yang dikembangkan memiliki ruang lingkup sebagai berikut:

1. Pengelolaan data siswa.
2. Penginputan data monitoring siswa.
3. Penyimpanan data hasil monitoring.
4. Pengolahan data menggunakan algoritma Decision Tree.
5. Klasifikasi minat belajar siswa berdasarkan atribut yang digunakan dalam penelitian.
6. Menampilkan hasil klasifikasi.
7. Menampilkan riwayat monitoring siswa.
8. Menampilkan ringkasan data monitoring.
9. Menampilkan faktor atau atribut yang digunakan dalam proses klasifikasi.
10. Penyediaan fitur filter data dan ekspor data apabila waktu pengembangan memungkinkan.

### Di luar ruang lingkup

Sistem tidak mencakup:

- Diagnosis gangguan psikologis siswa.
- Diagnosis kondisi medis.
- Pemberian rekomendasi medis.
- Chatbot umum berbasis AI.
- Sistem administrasi sekolah secara keseluruhan.
- Penggantian keputusan guru dalam menangani siswa.

---

## 1.3 Definisi dan Istilah

| Istilah | Definisi |
|---|---|
| Sistem | Sistem Monitoring Minat Belajar Siswa SD Berbasis Web |
| Monitoring | Proses pencatatan dan pemantauan data siswa secara berkala |
| Decision Tree | Algoritma klasifikasi yang merepresentasikan hubungan atribut dan kelas dalam bentuk struktur pohon keputusan |
| Klasifikasi | Proses mengelompokkan data ke dalam kelas atau kategori tertentu berdasarkan pola data |
| Atribut | Variabel atau karakteristik yang digunakan sebagai masukan model |
| Target/Label | Kelas atau kategori yang menjadi hasil klasifikasi |
| Dataset | Kumpulan data yang digunakan dalam proses pengolahan dan pemodelan |
| FR | Functional Requirement atau kebutuhan fungsional sistem |
| NFR | Non-Functional Requirement atau kebutuhan non-fungsional sistem |
| MoSCoW | Prioritas kebutuhan yang terdiri dari Must, Should, Could, dan Won't |

---

# 2. DESKRIPSI UMUM SISTEM

## 2.1 Pengguna dan Stakeholder

| Pengguna/Stakeholder | Peran |
|---|---|
| Guru/Wali Kelas | Menginput, memantau, dan melihat hasil klasifikasi siswa |
| Siswa | Menjadi objek data monitoring |
| Orang Tua | Pihak yang dapat menerima informasi hasil monitoring sesuai rancangan akses sistem |
| Admin Sekolah | Mengelola data pengguna dan data pendukung sistem |
| Pembimbing/Pengelola Penelitian | Melakukan pengawasan dan evaluasi terhadap sistem |

---

## 2.2 Lingkungan Operasi

Sistem dirancang untuk berjalan pada:

- Platform berbasis web.
- Browser seperti Google Chrome, Microsoft Edge, atau browser modern lainnya.
- Komputer/laptop sebagai perangkat utama pengelola sistem.
- Smartphone dapat digunakan untuk mengakses sistem apabila antarmuka telah disesuaikan.

**[ASUMSI-01]** Sistem membutuhkan koneksi jaringan untuk mengakses aplikasi web.

**[ASUMSI-02]** Sistem dikembangkan dan diuji menggunakan lingkungan lokal/server yang tersedia selama penelitian.

---

## 2.3 Asumsi

Asumsi yang digunakan dalam penyusunan kebutuhan:

- **[ASUMSI-03]** Data siswa tersedia untuk digunakan dalam penelitian.
- **[ASUMSI-04]** Tersedia atribut yang relevan untuk proses monitoring dan klasifikasi.
- **[ASUMSI-05]** Tersedia target/label yang dapat digunakan dalam proses pelatihan Decision Tree.
- **[ASUMSI-06]** Indikator sosial dan emosional memiliki dasar penelitian yang dapat digunakan sebagai atribut apabila memang dipilih dalam penelitian.
- **[ASUMSI-07]** Jumlah data yang tersedia mencukupi untuk proses pengujian model.
- **[ASUMSI-08]** Pengembangan dilakukan dalam batas waktu satu semester.

---

## 2.4 Dependensi

Sistem memiliki ketergantungan terhadap:

1. Ketersediaan dataset siswa.
2. Ketersediaan atribut monitoring.
3. Ketersediaan target/label klasifikasi.
4. Proses preprocessing data.
5. Algoritma Decision Tree.
6. Dataset pengujian untuk mengevaluasi model.
7. Lingkungan server dan database.

---

# 3. KEBUTUHAN FUNGSIONAL

Kebutuhan fungsional menggunakan format:

> Sistem harus dapat `<aksi>` `<objek>` saat `<kondisi>` → `<output>`.

| ID | Kebutuhan Fungsional | Prioritas | Metode Verifikasi |
|---|---|---|---|
| FR-01 | Sistem harus dapat melakukan autentikasi pengguna saat pengguna memasukkan username dan password yang valid → pengguna berhasil masuk ke sistem | Must | Black-box testing |
| FR-02 | Sistem harus dapat mengelola data siswa saat pengguna memiliki hak akses pengelolaan data → data siswa tersimpan atau diperbarui | Must | Black-box testing |
| FR-03 | Sistem harus dapat menyimpan data monitoring siswa saat pengguna mengisi data monitoring dengan lengkap → data monitoring tersimpan dalam database | Must | Black-box testing |
| FR-04 | ★ Sistem harus dapat melakukan klasifikasi menggunakan Decision Tree saat atribut yang dibutuhkan tersedia → sistem menghasilkan kelas hasil klasifikasi | Must | Pengujian model + Black-box testing |
| FR-05 | ★ Sistem harus dapat menampilkan hasil klasifikasi saat proses klasifikasi berhasil → hasil klasifikasi ditampilkan kepada pengguna | Must | Black-box testing |
| FR-06 | Sistem harus dapat menampilkan riwayat monitoring saat pengguna memilih data siswa → riwayat monitoring siswa ditampilkan | Should | Black-box testing |
| FR-07 | Sistem harus dapat menampilkan ringkasan data monitoring saat pengguna membuka dashboard → ringkasan data monitoring ditampilkan | Should | Black-box testing |
| FR-08 | ★ Sistem harus dapat menampilkan atribut yang digunakan dalam proses klasifikasi saat hasil klasifikasi tersedia → informasi atribut klasifikasi ditampilkan | Should | Black-box testing |
| FR-09 | Sistem harus dapat memfilter data monitoring saat pengguna memilih kriteria filter → data sesuai kriteria ditampilkan | Could | Black-box testing |
| FR-10 | Sistem harus dapat mengekspor data monitoring saat pengguna memilih fitur ekspor → file data berhasil dibuat | Could | Black-box testing |

---

# 4. KEBUTUHAN NON-FUNGSIONAL

## 4.1 Kebutuhan Non-Fungsional

| ID | Kategori ISO/IEC 25010 | Kebutuhan | Metrik | Target | Kondisi Pengukuran |
|---|---|---|---|---|---|
| NFR-01 | Functional Suitability | Sistem harus menghasilkan klasifikasi untuk data valid | Persentase proses klasifikasi berhasil | 100% data valid menghasilkan output atau status gagal yang jelas | Pengujian menggunakan dataset valid |
| NFR-02 | Functional Suitability | Model Decision Tree harus memiliki tingkat akurasi yang dapat diukur | Accuracy | **[ASUMSI-09]** Target ditentukan setelah pengujian baseline | Dataset pengujian |
| NFR-03 | Performance Efficiency | Sistem harus memberikan hasil klasifikasi dalam waktu yang dapat diterima | Waktu respons | **[ASUMSI-10]** Target ditentukan setelah pengujian prototype | Pengukuran sejak input dikirim sampai hasil diterima |
| NFR-04 | Security | Sistem harus menolak akses pengguna yang tidak terautentikasi | Persentase akses ilegal yang ditolak | 100% skenario pengujian | Pengujian akses tanpa login |
| NFR-05 | Security | Sistem harus membatasi akses berdasarkan hak pengguna | Persentase akses tidak sah yang ditolak | 100% skenario pengujian | Pengujian role pengguna |
| NFR-06 | Privacy | Data siswa hanya dapat diakses oleh pengguna yang memiliki hak akses | Persentase akses tidak sah yang ditolak | 100% skenario pengujian | Pengujian akses data siswa |
| NFR-07 | Usability | Pengguna harus dapat menyelesaikan proses monitoring utama | Task completion rate | **[ASUMSI-11]** Target ditentukan setelah user testing | Pengujian dengan guru/wali kelas |
| NFR-08 | Reliability | Sistem harus memberikan hasil yang konsisten pada input dan model yang sama | Konsistensi output | 100% untuk input dan model yang sama | Pengujian berulang |
| NFR-09 | Performance Efficiency | Sistem harus memberikan hasil atau status kegagalan pada setiap proses klasifikasi | Persentase proses yang memiliki respons | 100% | Pengujian proses klasifikasi |
| NFR-10 | Usability | Antarmuka sistem harus memungkinkan pengguna memahami hasil klasifikasi | Persentase pengguna yang memahami hasil | **[ASUMSI-12]** Target ditentukan melalui user testing | Pengujian pengguna |

---

# 5. KEBUTUHAN DATA DAN MODEL

## 5.1 Data Input

Data yang digunakan dalam sistem terdiri dari:

### Data Identitas Siswa

Contoh atribut:

- ID siswa
- Nama siswa
- Kelas
- Jenis kelamin

### Data Monitoring

Atribut monitoring ditentukan berdasarkan hasil penelitian dan ketersediaan data.

Contoh:

- Indikator sosial
- Indikator emosional
- Indikator minat belajar
- Data aktivitas belajar

**[ASUMSI-13]** Daftar atribut final belum ditetapkan karena harus disesuaikan dengan instrumen penelitian dan dataset yang diperoleh dari sekolah.

---

## 5.2 Proses Model

Alur data model:

```text
Data Siswa
    ↓
Data Monitoring
    ↓
Preprocessing Data
    ↓
Dataset
    ↓
Pembagian Data Training dan Testing
    ↓
Decision Tree
    ↓
Model Klasifikasi
    ↓
Prediksi Kelas
    ↓
Hasil Monitoring
