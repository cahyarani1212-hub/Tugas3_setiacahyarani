# Product Requirements Document (PRD)

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Status:** Draft  
**Versi:** 1.0  
**Platform:** Website  
**Metode/Model:** Decision Tree  
**Target Prototype:** 1 Semester  

---

# 1. Ringkasan Eksekutif

## 1.1 Nama Produk

**Sistem Monitoring Minat Belajar Siswa SD Berbasis Web**

## 1.2 Deskripsi Produk

Sistem Monitoring Minat Belajar Siswa SD Berbasis Web merupakan aplikasi yang dirancang untuk membantu proses pemantauan kondisi belajar siswa sekolah dasar berdasarkan sejumlah atribut yang dikumpulkan secara terstruktur.

Sistem menggunakan algoritma **Decision Tree** untuk melakukan klasifikasi berdasarkan data yang tersedia. Decision Tree digunakan karena dapat melakukan klasifikasi dengan mempertimbangkan lebih dari satu atribut dan menghasilkan model berupa pohon keputusan.

Penelitian Sutoyo (2018) menunjukkan penerapan algoritma Decision Tree untuk klasifikasi data peserta didik dengan menggunakan beberapa atribut. Hasil penelitian tersebut menunjukkan bahwa Decision Tree dapat menghasilkan model klasifikasi yang kemudian diterapkan pada aplikasi.

## 1.3 Batasan Produk

Produk dikembangkan sebagai prototype dalam waktu satu semester dengan keterbatasan data penelitian dan biaya pemrosesan AI/ML.

> **[ASUMSI-01]** Produk digunakan oleh guru/wali kelas untuk membantu proses monitoring siswa.

> **[ASUMSI-02]** Produk dapat diakses melalui browser pada komputer maupun smartphone.

---

# 2. Problem Statement & Bukti

## 2.1 Problem Statement

> **[ASUMSI-03]** Guru membutuhkan proses monitoring yang lebih terstruktur untuk melihat kondisi belajar siswa berdasarkan beberapa atribut yang tersedia.

Problem statement dari Tugas 2 belum diberikan dalam konteks yang tersedia sehingga pernyataan di atas masih berstatus asumsi dan perlu disesuaikan dengan hasil Tugas 2.

## 2.2 Bukti Penelitian

Penelitian Sutoyo (2018) menjelaskan bahwa klasifikasi peserta didik dapat dilakukan dengan menggunakan lebih dari satu atribut dibandingkan pendekatan sederhana yang hanya menggunakan nilai akhir. Decision Tree digunakan untuk melakukan klasifikasi data peserta didik. 

Decision Tree dapat mempelajari pola klasifikasi dan prediksi dari hubungan antara atribut input dan variabel target. Hasil model dapat direpresentasikan dalam bentuk pohon keputusan. 

Dalam penelitian tersebut, atribut yang digunakan antara lain nilai rata-rata dan jumlah sesi pengerjaan kuis. Hasil klasifikasi kemudian digunakan sebagai dasar penerapan model pada aplikasi.

## 2.3 Pemisahan Fakta dan Asumsi

| Pernyataan | Status |
|---|---|
| Decision Tree dapat digunakan untuk klasifikasi data peserta didik | Fakta |
| Decision Tree dapat menggunakan lebih dari satu atribut | Fakta |
| Decision Tree menghasilkan model berbentuk pohon keputusan | Fakta |
| Guru membutuhkan monitoring siswa yang lebih terstruktur | [ASUMSI-04] |
| Indikator sosial dan emosional digunakan sebagai atribut sistem | [ASUMSI-05] |
| Sistem dapat membantu guru dalam proses monitoring | [ASUMSI-06] |
| Sistem dapat meningkatkan minat belajar siswa | [ASUMSI-07] |

Sumber: Sutoyo (2018). *Implementasi Algoritma Decision Tree untuk Klasifikasi Data Peserta Didik*.

---

# 3. Target User & Stakeholder

| Peran | Kebutuhan | Pengaruh |
|---|---|---|
| Guru/Wali Kelas | Melihat data dan hasil klasifikasi siswa | Tinggi |
| Siswa SD | Mengisi data yang diperlukan untuk monitoring | Sedang |
| Orang Tua | Mendapatkan informasi perkembangan belajar siswa | Sedang |
| Admin Sekolah | Mengelola data pengguna dan data siswa | Sedang |
| Pembimbing/Pengelola Penelitian | Memastikan sistem sesuai tujuan penelitian | Tinggi |

> **[ASUMSI-08]** Guru/wali kelas merupakan pengguna utama sistem.

> **[ASUMSI-09]** Siswa dan orang tua merupakan stakeholder pendukung.

---

# 4. Value Proposition

## 4.1 Pain yang Dikurangi

> **[ASUMSI-10]**

- Data monitoring siswa dapat menjadi sulit dipantau apabila dicatat secara terpisah.
- Guru perlu mempertimbangkan beberapa atribut untuk memperoleh gambaran kondisi belajar siswa.
- Hasil pemantauan perlu disajikan secara lebih terstruktur.

## 4.2 Gain yang Diciptakan

> **[ASUMSI-11]**

- Guru dapat melihat data monitoring siswa melalui satu sistem.
- Sistem menghasilkan klasifikasi berdasarkan data yang dimasukkan.
- Hasil klasifikasi dapat digunakan sebagai informasi pendukung dalam proses monitoring.

## 4.3 Mengapa Decision Tree Bukan Gimmick?

Decision Tree merupakan bagian inti dari proses pengolahan data karena digunakan untuk menghasilkan klasifikasi berdasarkan atribut input.

Pada penelitian Sutoyo (2018), Decision Tree digunakan untuk melakukan klasifikasi data peserta didik. Model yang dihasilkan juga dapat direpresentasikan dalam bentuk aturan `IF-THEN` yang digunakan untuk menentukan kelas.

Dengan demikian, penggunaan Decision Tree memiliki fungsi langsung terhadap output utama sistem, yaitu menghasilkan hasil klasifikasi dari data siswa.

---

# 5. Tujuan Produk & KPI

| Tujuan | KPI | Cara Mengukur |
|---|---|---|
| Menghasilkan klasifikasi siswa | Persentase data yang berhasil diklasifikasikan | Data berhasil diklasifikasikan / total data × 100% |
| Mengukur performa model | Accuracy | Menggunakan confusion matrix |
| Memastikan sistem menghasilkan output | Persentase proses klasifikasi yang menghasilkan hasil | Proses berhasil / total proses × 100% |
| Mempermudah proses monitoring | Waktu penyelesaian tugas monitoring | Pengukuran waktu penggunaan sistem |
| Memastikan prototype dapat digunakan | Task completion rate | Tugas berhasil / total tugas × 100% |

Penelitian Sutoyo menggunakan **10-fold cross-validation** dan accuracy sebagai indikator evaluasi classifier.

> **[ASUMSI-12]** Target nilai KPI akhir akan ditentukan setelah dataset tersedia dan pengujian awal dilakukan.

---

# 6. Scope Fitur 3 Bulan

## 6.1 MoSCoW Prioritization

| Prioritas | Fitur | Deskripsi |
|---|---|---|
| **Must Have** | Login | Pengguna dapat masuk ke sistem |
| **Must Have** | Kelola Data Siswa | Menambah, melihat, mengubah, dan menghapus data siswa |
| **Must Have** | Input Data Monitoring | Memasukkan data/indikator monitoring siswa |
| **Must Have** | ★ Klasifikasi Decision Tree | Mengklasifikasikan siswa berdasarkan atribut yang tersedia |
| **Must Have** | ★ Hasil Klasifikasi | Menampilkan hasil klasifikasi siswa |
| **Should Have** | Riwayat Monitoring | Menampilkan hasil monitoring sebelumnya |
| **Should Have** | Dashboard Monitoring | Menampilkan ringkasan hasil monitoring |
| **Should Have** | ★ Informasi Faktor Klasifikasi | Menampilkan atribut yang digunakan dalam hasil klasifikasi |
| **Could Have** | Filter Data | Memfilter data berdasarkan kategori atau periode |
| **Could Have** | Export Data | Mengekspor hasil monitoring |
| **Won't Have** | Diagnosis Psikologis | Sistem tidak melakukan diagnosis |
| **Won't Have** | Chatbot AI | Tidak menjadi bagian dari prototype |
| **Won't Have** | Rekomendasi Medis | Tidak memberikan rekomendasi medis/psikologis |
| **Won't Have** | Sistem Administrasi Sekolah Lengkap | Tidak mencakup seluruh administrasi sekolah |

### Keterangan

**★ = Fitur AI/ML utama**

---

# 7. Non-Goals

Produk tidak bertujuan untuk:

1. Melakukan diagnosis psikologis terhadap siswa.
2. Menggantikan keputusan guru.
3. Menentukan keputusan akademik siswa secara otomatis.
4. Memberikan rekomendasi medis.
5. Menjadi chatbot AI umum.
6. Memprediksi kondisi siswa di luar data penelitian.
7. Menjadi sistem informasi sekolah secara keseluruhan.
8. Mengelola seluruh administrasi sekolah.
9. Memberikan kesimpulan bahwa hasil klasifikasi merupakan kondisi siswa secara mutlak.

---

# 8. Asumsi & Risiko Utama

| Asumsi/Risiko | Status | Mitigasi |
|---|---|---|
| Data siswa tersedia untuk penelitian | [ASUMSI-13] | Memastikan ketersediaan data sebelum pengembangan model |
| Data memiliki atribut yang sesuai | [ASUMSI-14] | Melakukan pemeriksaan data sebelum pemodelan |
| Tersedia target/label klasifikasi | [ASUMSI-15] | Menentukan target berdasarkan dataset dan tujuan penelitian |
| Dataset memiliki jumlah data terbatas | Risiko | Menggunakan data yang tersedia dan melakukan validasi model |
| Dataset memiliki missing value | Risiko | Melakukan pemeriksaan dan pembersihan data |
| Dataset memiliki noise | Risiko | Melakukan data preparation |
| Model menghasilkan accuracy rendah | Risiko | Mengevaluasi atribut, dataset, dan model |
| Indikator sosial dan emosional belum memiliki dasar yang ditetapkan | Risiko | Menentukan indikator berdasarkan sumber penelitian yang relevan |
| Waktu pengembangan hanya satu semester | Risiko | Memprioritaskan fitur Must Have |
| Biaya pemrosesan AI terbatas | Risiko | Menggunakan model yang dapat dikembangkan dengan dataset penelitian |

---

# 9. Batasan Data

> **[ASUMSI-16]** Data yang digunakan berasal dari data siswa pada objek penelitian.

Data yang digunakan harus memiliki atribut yang dapat digunakan sebagai input klasifikasi serta target/label yang diperlukan untuk proses pembelajaran model.

Sebagai referensi, penelitian Sutoyo menggunakan atribut seperti:

- ID siswa
- Nama siswa
- Jumlah sesi pengerjaan
- Nilai rata-rata
- Kelas

Penelitian tersebut menunjukkan bahwa lebih dari satu atribut dapat digunakan dalam proses klasifikasi peserta didik.

Untuk produk ini, atribut final belum ditetapkan karena harus disesuaikan dengan data penelitian yang benar-benar tersedia.

---

# 10. Kriteria Keberhasilan Produk

Prototype dianggap memenuhi tujuan awal apabila:

- Pengguna dapat memasukkan data siswa.
- Sistem dapat menyimpan data monitoring.
- Sistem dapat melakukan klasifikasi menggunakan Decision Tree.
- Sistem dapat menampilkan hasil klasifikasi.
- Model dapat dievaluasi menggunakan dataset pengujian.
- Hasil evaluasi dapat diukur menggunakan metrik yang sesuai.
- Fitur klasifikasi memberikan fungsi nyata terhadap proses monitoring.

---

# 11. Review Checklist PRD

| Checklist | Status |
|---|---|
| Problem statement konsisten dengan Tugas 2 | ⚠️ Perlu disesuaikan dengan Tugas 2 |
| Problem statement bebas kata solusi | ⚠️ Perlu verifikasi setelah Tugas 2 tersedia |
| KPI terukur | ✅ |
| Fitur AI/ML menambah nilai nyata | ✅ |
| Fitur AI/ML bukan gimmick | ✅ |
| Non-goals jelas | ✅ |
| Tidak ada klaim tanpa bukti | ✅ |
| Asumsi diberi label `[ASUMSI-XX]` | ✅ |
| Tidak membahas arsitektur teknis | ✅ |
| Scope prototype dibatasi | ✅ |

---

# 12. Referensi

Sutoyo, I. (2018). **Implementasi Algoritma Decision Tree untuk Klasifikasi Data Peserta Didik**. Jurnal PILAR Nusa Mandiri, 14(2), 217–224.

Sumber dokumen: *Jurnal PILAR Nusa Mandiri Vol. 14 No. 2 September 2018*. :contentReference[oaicite:0]{index=0}
