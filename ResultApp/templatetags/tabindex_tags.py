from django import template

register = template.Library()


@register.filter
def tabindex(value, index):
    value.field.widget.attrs['tabindex'] = index
    return value