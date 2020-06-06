from rest_framework import routers
from django.urls import path
from core.views import AccountViewSet, TransactionViewSet, AccountDetailAPIView

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet, base_name='core')
router.register(r'account', TransactionViewSet, base_name='core')

urlpatterns = [
    path('account/my/deposit/', AccountDetailAPIView.as_view())
] + router.urls

