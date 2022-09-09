from modeltranslation.translator import translator, TranslationOptions
from .models import PostModel


class PostModelTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


translator.register(PostModel, PostModelTranslationOptions)
