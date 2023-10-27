from django import template
from django.utils.safestring import mark_safe
from menu.models import MenuItem


register = template.Library()





@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name=None):
    try:
        path = context['request'].path_info.strip('/')
    except KeyError:
        path = ''
    if not menu_name:
        menu_name = path
    menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children__children').all()
    current_menu = MenuItem.objects.filter(name=menu_name).first()
    if not menu_items.exists():
        return mark_safe('<div class="container"><h3>Menu items not found</h3></div>')
    if menu_name and not current_menu:
        return mark_safe('<div class="container"><h3>Menu item not found</h3></div>')
    ancestors = []
    while current_menu:
        ancestors.append(current_menu)
        current_menu = current_menu.parent
    return mark_safe(generate(menu_items, None, ancestors))





def generate(items, cur, ancestors):
    result = f'<div class="container"><div class="accordion" id="accordion{cur}">'
    for item in items:
        result+=f'<div><div id="heading{item.pk}">'
        result+='<h5 class="mb-0">'
        result+=f'<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{item.pk}" aria-expanded="{str(item in ancestors).lower()}" aria-controls="collapse{item.pk}">'
        result+=f'<a href="{item.get_absolute_url()}">{item.name}</a></button></h5></div>'
        result+=f'<div id="collapse{item.pk}" class="collapse {"show" if item in ancestors else "" }" aria-labelledby="heading{item.pk}" data-parent="#accordion{cur}">'
        result+=generate(item.children.all(),item,ancestors)
        result+='</div></div></div></div>'
    return result