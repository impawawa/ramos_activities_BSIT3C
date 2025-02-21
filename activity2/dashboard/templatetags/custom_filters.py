from django import template

register = template.Library()

@register.filter
def format_currency(value):
    """Adds a dollar sign to numerical values, assuming it's revenue."""
    try:
        return f"${value}"
    except ValueError:
        return value  # If the value isn't a number, return it unchanged
