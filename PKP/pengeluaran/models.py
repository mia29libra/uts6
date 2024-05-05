from django.db import models

class pengeluaran(models.Model):
    tgl_pengeluaran = models.CharField (max_length=50)
    belanja_bulanan =  models.CharField (max_length=50)
    tagihan = models.CharField(max_length=50)
    pembelian_lainnya = models.CharField (max_length=50)

    def __str__(self): return self.tgl_pengeluaran,self.belanja_bulanan,self.tagihan,self.pembelian_lainnya,