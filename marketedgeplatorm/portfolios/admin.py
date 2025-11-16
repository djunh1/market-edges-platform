from django.contrib import admin
from .models import Portfolio, Tag, Review, Category, Stock

# Register your models here.
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Stock)
admin.site.register(Tag)
admin.site.register(Review)