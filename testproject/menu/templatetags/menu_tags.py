from django import template
from django.db.models import Prefetch
from django.utils.safestring import mark_safe

from menu.models import MenuItem

register = template.Library()

def is_item_or_descendant_active(item, current_path):
    if current_path.startswith(item.get_absolute_url()):
        return True
    for child in item.children.all():
        if is_item_or_descendant_active(child, current_path):
            return True
    return False

def render_item(item, current_path, level=0, force_show=False):
    is_active = current_path.startswith(item.get_absolute_url())
    child_items = item.children.all()
    children = ''
    if child_items:
        show_children = is_active or force_show or is_item_or_descendant_active(item, current_path)
        children_html = ''.join([render_item(child, current_path, level + 1, show_children) for child in child_items])
        children = f'<ul style="{"" if show_children else "display: none;"}">{children_html}</ul>'
    active_class = "active" if is_active else ""
    return f'<li class="{active_class}"><a href="{item.get_absolute_url()}">{item.name}</a>{children}</li>'

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_path = context.get('request').path
    menu_items = MenuItem.objects.filter(menu_name=menu_name, parent__isnull=True).prefetch_related(
        Prefetch('children', queryset=MenuItem.objects.all())
    )
    menu_html = ''.join([render_item(item, current_path) for item in menu_items])
    return mark_safe(f'<ul>{menu_html}</ul>')
