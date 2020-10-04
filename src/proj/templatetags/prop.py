from django.template.defaultfilters import register
# from django import template
# register = template.Library()

# import demjson
# from agr.models import Certificate


@register.filter(name="prop")
def prop(cert, arg):
    # print('cert')
    # print(cert)
    # print('arg')
    # print(arg)

    return cert.get_prop(arg)

# @register.filter
# def lower(value):
#     return value.lower()
