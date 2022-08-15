from django import template

register = template.Library()


@register.filter
def tem_grupo(user, nome_grupo):
    return user.groups.filter(name=nome_grupo).exists()