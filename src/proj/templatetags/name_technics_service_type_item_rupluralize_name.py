from django.template.defaultfilters import register


@register.simple_tag(name="name_technics_service_type_item_rupluralize_name")
def name_technics_service_type_item_rupluralize_name(value, name_technics_service_type, *args, **kwargs):
    """
    Подбирает окончание для названия типа техники разных типов услуг.
    3 квадроцикла
    21 снегоход
    5 лошадей

    {% service_type_item_rupluralize_name number name_technics_service_type %}

    """
    if not name_technics_service_type:
        return ''
    try:
        # if isinstance(value, str):
        #     value = value.replace(",", ".")
        value = float(value)
        value = int(value)
        # raise Exception(value)
        # one, two, many = forms.split(u',')
        value = str(value)[-2:]  # 314 -> 14

        if (21 > int(value) > 4):
            return name_technics_service_type.plural_genitive

        if value.endswith('1'):
            return name_technics_service_type.singular
        elif value.endswith(('2', '3', '4')):
            return name_technics_service_type.singular_genitive
        else:
            return name_technics_service_type.plural_genitive

    except (ValueError, TypeError):
        return ''
