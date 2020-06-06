import logging
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from core.models import Article, FavoriteArticle, ArticleImage
from core.serializers import ArticleFullSerializer, ArticleSerializer, ArticleImageSerializer, \
    FavoriteArticleSerializer, FavoriteArticleMySerializer

logger = logging.getLogger(__name__)


class ArticleViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_serializer_class(self):
        if self.action == 'perform_create':
            return ArticleSerializer
        if self.action == 'get_creators':
            return ArticleFullSerializer
        return ArticleSerializer

    @permission_classes([IsAuthenticated])
    def perform_create(self, serializer):
        ser = serializer.save(name=self.request.data['name'],
                              description=self.request.data['description'],
                              price=self.request.data['price'],
                              city=self.request.data['city'],
                              category=self.request.data['category'],
                              color=self.request.data['color'],
                              creator=self.request.user)
        logger.info(f"{self.request.user} created article: {serializer.data.get('name')}")
        return ser

    @action(methods=['get'], detail=False)
    def get_creators(self, request):
        ser = self.get_serializer(self.queryset, many=True)

        return ser.data

    def get_queryset(self):
        return self.queryset


class ArticleImageViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleImageSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    queryset = ArticleImage.objects.all()

    def get_queryset(self):
        return self.queryset.all()

    def perform_create(self, serializer):
        return serializer.save()


class FavoriteArticleViewSet(mixins.RetrieveModelMixin,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             mixins.DestroyModelMixin,
                             viewsets.GenericViewSet):
    queryset = FavoriteArticle.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser, JSONParser)
    serializer_class = FavoriteArticleSerializer

    def get_serializer_class(self):
        if self.action == 'get_my':
            return FavoriteArticleMySerializer
        return FavoriteArticleSerializer

    def perform_create(self, serializer):
        return serializer.save(article=Article.objects.get(id=self.request.data['article']),
                               user=self.request.user)

    def get_queryset(self):
        return self.queryset

    @action(methods=['get'], detail=True)
    def get_my(self, request, pk):
        fav = FavoriteArticle.objects.get(user=pk)
        ser = self.get_serializer(fav)
        return Response(ser.data)
