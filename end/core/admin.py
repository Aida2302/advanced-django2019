from django.contrib import admin

from core.models import Article, ArticleImage, FavoriteArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'city', 'category', 'color', 'creator')
    fields = ('name', 'description', 'price', 'city', 'category', 'color', 'creator')


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'image')
    fields = ('article', 'image')


@admin.register(FavoriteArticle)
class FavoriteArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user')
    fields = ('article', 'user')

