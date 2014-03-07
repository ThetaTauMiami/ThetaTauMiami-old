from django.contrib import admin

# Register your models here.
from articles.models import Picture, Gallery, Article, ArticleCategory


admin.site.register(Picture)
admin.site.register(Gallery)
admin.site.register(Article)
admin.site.register(ArticleCategory)