from rest_framework import serializers
from.models import pengeluaran

class pengeluaranSerializers(serializers.ModelSerializers):
    class Meta:
        model = pengeluaran
        fields = ['tgl_pengeluaran', 'belanja_bulanan', 'tagihan', 'pengeluaran_lainnya']