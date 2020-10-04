from django.template.defaultfilters import register


@register.filter(name="prop_count")
def prop_count(cert, arg):
    # print('cert')
    # print(cert)
    # print('arg')
    # print(arg)

    return cert.get_prop_count(arg)
