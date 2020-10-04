from django.template.defaultfilters import register


@register.filter(name="prop_bool")
def prop_bool(cert, arg):
    # print('cert')
    # print(cert)
    # print('arg')
    # print(arg)

    return cert.get_prop_bool(arg)