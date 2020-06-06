from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.views import APIView

from core.models import Account, Transaction
from core.serializers import AccountSerializer, TransactionSerializer

import logging

logger = logging.getLogger(__name__)


class AccountViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Account.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def perform_create(self, serializer):
        logger.info(f"{self.request.user} opened account")
        logger.warning('HAHAHAHAHA')
        logger.error('AAAAAAAAAAAAAAAAAAAAAA')
        logger.critical('NONONONONONONONONONO')
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset

    @action(methods=['GET'], detail=False)
    def me(self, request):
        accounts = Account.objects.filter(owner=request.user)
        serializer = self.get_serializer(accounts, many=True)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def deposit(self, request, pk):
        account = Account.objects.get(pk)
        amount = request.data['amount']
        account.balance += amount
        serializer = self.get_serializer(account, many=False)
        return serializer.save(owner=self.request.user)


class TransactionViewSet(mixins.RetrieveModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset

    def perform_create(self, serializer):
        return serializer.save(amount=self.request.data['amount'],
                               account=Account.objects.get(id=self.request.data['account']))


class AccountDetailAPIView(APIView):
    http_method_names = ['get', 'post', 'delete']
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        account = request.data['balance']
        amount = self.request.data['amount']
        account.balance += amount
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        pass
