from django import template


register = template.Library()


@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name


@register.simple_tag
def field_verbose_name(obj, fieldnm):
    return obj._meta.get_field(fieldnm).verbose_name


@register.simple_tag
def field_help_text(obj, fieldnm):
    return obj._meta.get_field(fieldnm).help_text
