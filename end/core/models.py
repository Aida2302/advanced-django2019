from django.db import models
from users.models import MainUser
from utils.validators import article_image_size, article_image_extension


class Article(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    city = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    color = models.CharField(max_length=100)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.FileField(upload_to='projects/', validators=[article_image_size, article_image_extension], null=True)

    class Meta:
        verbose_name = 'ArticleImage'
        verbose_name_plural = 'ArticleImages'

    def __str__(self):
        return self.article


class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.article
