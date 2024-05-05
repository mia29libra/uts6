from django.db import models

class pemasukan(models.Model):
    tgl_pemasukan = models.CharField (max_length=50)
    pemasukan_gaji=  models.CharField (max_length=50)
    pendapatan_lainnya = models.CharField(max_length=50)

    def __str__(self): return self.tgl_pemasukan,self.pemasukan_gaji,self.pendapatan_lainnya,