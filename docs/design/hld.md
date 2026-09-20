# HIGH-LEVEL DESIGN (HLD)

## Sistem Monitoring Minat Belajar Siswa SD Berbasis Web

**Dokumen:** High-Level Design  
**Versi:** 1.0  
**Status:** Draft  
**Platform:** Web  
**Metode AI:** Decision Tree  
**Tahap:** PRD → SRS → HLD → LLD  
**Konstrain:** Prototype 1 semester, satu fitur AI inti, biaya minimal

---

# 1. Tujuan HLD

HLD ini menjelaskan rancangan arsitektur tingkat tinggi untuk Sistem Monitoring Minat Belajar Siswa SD Berbasis Web.

Fokus utama arsitektur adalah:

- pengelolaan data siswa;
- pencatatan data monitoring;
- klasifikasi minat belajar menggunakan Decision Tree;
- penyimpanan hasil klasifikasi;
- penanganan kegagalan atau tidak tersedianya model;
- keamanan dan privasi data siswa.

HLD tidak membahas detail class, method, struktur SQL, atau implementasi kode karena bagian tersebut termasuk LLD.

---

# 2. Arsitektur Sistem

## 2.1 Diagram Arsitektur

```mermaid
flowchart LR
    U[Guru / Wali Kelas / Admin] --> C[Web Client]

    C --> API[Backend API]

    API --> AUTH[Authentication & Authorization]
    API --> MON[Monitoring Service]
    API --> STUDENT[Student Data Service]
    API --> CLASS[Classification Service]

    CLASS --> PRE[Preprocessing]
    PRE --> DT[Decision Tree Model]
    DT --> POST[Postprocessing]

    API --> DB[(MySQL Database)]

    POST --> DB
    MON --> DB
    STUDENT --> DB
    AUTH --> DB

    CLASS --> FALLBACK[Fallback Handler]
    FALLBACK --> C
