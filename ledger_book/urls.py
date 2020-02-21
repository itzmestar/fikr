from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'ledger_book'
urlpatterns = [
    #path('tx/', views.balance_view),
    path('balance/', views.BalanaceView.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)