from django.urls import path
from .views import ActiveGoodsView

app_name = 'actives'
urlpatterns = [
    path('info/', ActiveGoodsView.as_view(), name='info')
]