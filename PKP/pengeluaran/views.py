from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import pengeluaran
from .serializers import pengeluaranSerializers


@csrf_exempt
def pengeluaran_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET' :
        pengeluaran = pengeluaran.objects.all()
        serializers = pengeluaranSerializers(pengeluaran, many=True)
        return JsonResponse(serializers.data, safe=False)
   
    elif request.method == 'POST' :
         data = JSONParser() .parse(request)
         serializers =pengeluaranSerializers(data=data)
         if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
         return JsonResponse(serializers.errors, status=400)

    