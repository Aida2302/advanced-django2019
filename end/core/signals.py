import shutil

from django.db.models.signals import post_delete
from django.dispatch import receiver

from core.models import Article, ArticleImage


def document_path(document):
    path = document.path
    shutil.rmtree(path)


@receiver(post_delete, sender=Article)
def article_deleted(sender, instance, **kwargs):
    print(instance.id)
    doc = ArticleImage.objects.get(article_id=instance.id)
    print(doc)
    document_path(document=doc)
