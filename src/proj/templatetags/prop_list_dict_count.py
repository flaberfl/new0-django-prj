from django.template.defaultfilters import register


@register.filter(name="prop_list_dict_count")
def prop_list_dict_count(cert, arg):
    # print('cert')
    # print(cert)
    # print('arg')
    # print(arg)

    return cert.get_prop_list_dict_count(arg)
