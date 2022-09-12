from main.models import CategoryModel
from django import template

register = template.Library()


@register.simple_tag()
def category_info(request):
    m = request.session['categories']
    if m:  # [2, 3, 4, 5]
        return CategoryModel.objects.filter(id__in=m)
    return None
