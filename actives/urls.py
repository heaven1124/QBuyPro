from django.urls import path
from .views import ActiveGoodsView, qbuy_api, query_qbuy_api

app_name = 'actives'
urlpatterns = [
    path('info/', ActiveGoodsView.as_view(), name='info'),
    path('qbuy/<goods_id>/', qbuy_api, name='qbuy'),
    path('query_qbuy/<goods_id>/', query_qbuy_api, name='query_qbuy')
]