from django.db import models
from translations.models import Translatable
from django.utils.translation import ugettext_lazy as _

class Book(Translatable):
    name = models.CharField(
        verbose_name = _('name'),
        help_text = _('Name of the book'),
        max_length = 255,
    )
    description = models.CharField(
        verbose_name=_('description'),
        help_text=_('Description of the book'),
        max_length=64,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

    class TranslatableMeta:
        fields = ['name', 'description']
