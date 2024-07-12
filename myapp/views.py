from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import F
from django.db.models import Sum
from django.http import JsonResponse
from .models import Finanza
from .serializer import FinanzaSerializer
from datetime import date


class FinanzaListCreate(generics.ListCreateAPIView):
    queryset = Finanza.objects.all()
    serializer_class = FinanzaSerializer

class FinanzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finanza.objects.all()
    serializer_class = FinanzaSerializer
    

class FinanceReport(APIView):
    def get(self, request):
        # Cálculos para el reporte
        today = date.today()
        current_year = today.year
        current_month = today.month

        # Ventas del mes actual
        ventas_mes_actual = Finanza.objects.filter(fecha__year=current_year, fecha__month=current_month).aggregate(total_ventas_mes=Sum('monto'))['total_ventas_mes'] or 0

        # Ventas del día actual
        ventas_dia_actual = Finanza.objects.filter(fecha=today).aggregate(total_ventas_dia=Sum('monto'))['total_ventas_dia'] or 0

        ventas_temporada_actual = Finanza.objects.filter(fecha__year=current_year).aggregate(total_ventas_temporada=Sum('monto'))['total_ventas_temporada'] or 0

        mes_mas_vendido = Finanza.objects.filter(fecha__year=current_year).values('fecha__month').annotate(total_ventas_mes=Sum('monto')).order_by('-total_ventas_mes').first()
        if mes_mas_vendido:
            mes_mas_vendido = mes_mas_vendido['fecha__month']
        else:
            mes_mas_vendido = None

        mes_costos_superaron_ventas = Finanza.objects.filter(tipo='costo').values('fecha__month').annotate(total_costos_mes=Sum('monto')).filter(total_costos_mes__gt=F('monto')).order_by('fecha__month').first()
        if mes_costos_superaron_ventas:
            mes_costos_superaron_ventas = mes_costos_superaron_ventas['fecha__month']
        else:
            mes_costos_superaron_ventas = None

        report_data = {
            'ventas_mes_actual': ventas_mes_actual,
            'ventas_dia_actual': ventas_dia_actual,
            'ventas_temporada_actual': ventas_temporada_actual,
            'mes_mas_vendido': mes_mas_vendido,
        }

        return JsonResponse(report_data)