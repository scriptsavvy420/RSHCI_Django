from django import template

register = template.Library()

@register.filter
def european_number_format(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")