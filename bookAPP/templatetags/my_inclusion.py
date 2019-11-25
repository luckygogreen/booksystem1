from django import template
register = template.Library()

@register.inclusion_tag('result.html')
def first_inclusion(n):
    n = 1 if n < 1 else int(n)
    data = ["第{}项".format(i) for i in range(1, n + 1)]
    return {"data": data}