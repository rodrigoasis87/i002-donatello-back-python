from django.urls import path
from . import views

urlpatterns = [
    path('finances/transactions/', views.FinanzaListCreate.as_view(), name='finanza-list-create'),
    path('finances/transactions/<int:pk>/', views.FinanzaDetail.as_view(), name='finanza-detail'),
    path('finances/reports/', views.FinanceReport.as_view(), name='finance-report'),
    path('finances/ingreso-total/', views.IngresoTotal.as_view(), name='ingreso-total'),
]