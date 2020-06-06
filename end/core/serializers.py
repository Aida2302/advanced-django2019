from core.models import Article, ArticleImage, FavoriteArticle
from rest_framework import serializers


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'

    def get_document_url(self, obj):
        if obj.document:
            return self.context['request'].build_absolute_uri(obj.document.url)
        return None


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('creator',)


class ArticleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ('creator',)


class ArticleFullSerializer(ArticleShortSerializer):
    class Meta(ArticleShortSerializer.Meta):
        fields = ArticleShortSerializer.Meta.fields + 'creator'


class FavoriteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArticle
        fields = '__all__'
        read_only_fields = ('user',)


class FavoriteArticleMySerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = FavoriteArticle
        fields = ('id', 'article')
