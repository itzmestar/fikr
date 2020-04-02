from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'ledger_book'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('tx/', views.TransactionView.as_view(), name='tx'),
    path('balance/', views.BalanceView.as_view(), name='balance'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)