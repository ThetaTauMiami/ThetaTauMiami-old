from django.contrib import admin

# Register your models here.
from articles.models import Picture, Gallery, InGallery, Article, ArticleCategory


admin.site.register(Picture)
admin.site.register(Gallery)
admin.site.register(InGallery)
admin.site.register(Article)
admin.site.register(ArticleCategory)