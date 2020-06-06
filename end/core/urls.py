from rest_framework import routers

from core.views import ArticleViewSet, ArticleImageViewSet, FavoriteArticleViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, base_name='core')
router.register(r'images', ArticleImageViewSet, base_name='core')
router.register(r'favorites', FavoriteArticleViewSet, base_name='core')

urlpatterns = router.urls
