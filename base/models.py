from django.db import models
from django.contrib.auth.models import User
# Create your models here.
JENIS_KELAMIN = (
        ("1",'Laki-laki'), 
        ("2",'Perempuan')
        )

class PikR(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    deskripsi = models.TextField(null = True, blank = True)
    fileK0 = models.FileField(upload_to = 'k0/', null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.nama


class Pengurus(models.Model):
    nama = models.CharField(max_length=50)
    jenisKelamin = models.CharField(max_length=50)
    alamat = models.TextField()
    pik = models.ForeignKey(PikR, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nama
 
class Anggota(models.Model):
    nama = models.CharField(max_length=50)
    jenisKelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN, default='1')
    jabatan = models.CharField(max_length=50, default = 'Anggota')
    pik = models.ForeignKey(PikR, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama
    
class LaporanKegiatan(models.Model):
    pik = models.ForeignKey(PikR, on_delete=models.CASCADE, null=False, blank=False)
    judul = models.CharField(max_length = 100)
    deskripsi = models.TextField(null=True)
    tanggal = models.DateField()
    gambar = models.ImageField(null=True, blank=True, upload_to='laporan/')
    
    created = models.DateTimeField(auto_now_add=True, null = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.judul
    
    class Meta:
        ordering = ['-created']