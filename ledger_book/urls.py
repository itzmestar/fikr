from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'ledger_book'
urlpatterns = [
    path('source/', views.SourceView.as_view(), name='source'),
    path('person/', views.PersonView.as_view(), name='person'),
    path('tx/', views.TransactionView.as_view(), name='tx'),
    path('balance/', views.BalanceView.as_view(), name='balance'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)