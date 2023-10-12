from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Rss)
class RssTranslationOptions(TranslationOptions):
    fields = ('name', )

