from rest_framework import serializers
from.models import pemasukan

class pemasukanSerializers(serializers.ModelSerializers):
    class Meta:
        model = pemasukan
        fields = ['tgl_pemasukan', 'Pemasukan_gaji', 'pendapatan_lainnya']