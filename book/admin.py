from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import Book

class BookAdmin(TranslatableAdmin):
    inlines = [TranslationInline]

admin.site.register(Book, BookAdmin)