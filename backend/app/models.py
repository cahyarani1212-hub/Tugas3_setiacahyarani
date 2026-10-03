"""
Data Schema / Models
Sistem Monitoring Evaluasi Belajar Siswa Berbasis Web
Menggunakan Algoritma Decision Tree

File:
backend/app/models.py
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import date, datetime


# ============================================================
# USER
# ============================================================

class User(BaseModel):
    """Model data pengguna sistem."""

    id: int
    username: str
    password: str


# ============================================================
# STUDENT
# ============================================================

class Student(BaseModel):
    """Model data siswa."""

    id: int
    nama: str
    kelas: str
    created_at: datetime
    updated_at: datetime


class StudentCreate(BaseModel):
    """Schema untuk menambahkan data siswa."""

    nama: str = Field(..., min_length=1)
    kelas: str = Field(..., min_length=1)


class StudentUpdate(BaseModel):
    """Schema untuk memperbarui data siswa."""

    nama: Optional[str] = None
    kelas: Optional[str] = None


# ============================================================
# MONITORING
# ============================================================

class Monitoring(BaseModel):
    id: int
    student_id: int
    tanggal: date
    data_monitoring: Dict[str, Any]
    created_at: datetime


class MonitoringCreate(BaseModel):
    """Schema untuk menambahkan data monitoring."""

    student_id: int
    tanggal: date
    data_monitoring: Dict[str, Any]


# ============================================================
# CLASSIFICATION RESULT
# ============================================================

class ClassificationResult(BaseModel):
    """Model hasil klasifikasi Decision Tree."""

    id: int
    student_id: int
    monitoring_id: int
    hasil: str
    created_at: datetime


# ============================================================
# CLASSIFICATION REQUEST
# ============================================================

class ClassificationRequest(BaseModel):
    """Schema untuk melakukan klasifikasi."""

    student_id: int
    monitoring_id: int


# ============================================================
# CLASSIFICATION RESPONSE
# ============================================================

class ClassificationResponse(BaseModel):
    """Response hasil klasifikasi."""

    student_id: int
    monitoring_id: int
    hasil: str
