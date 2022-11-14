def get_from_dict(keys: str, items: dict):
    value = items
    for key in keys.split('.'):
        v = value.get(key)
        if v is not None:
            value = v
        else:
            return None

    return value


def build_instance(obj, *args, **kwargs):
    if callable(obj):
        return obj(*args, **kwargs)
    else:
        return obj


def get_name_from_obj(obj):
    return obj.__name__ if callable(obj) else obj.__class__.__name__


def build_key_instance_tuple(obj_or_tuple, *args, **kwargs):
    if isinstance(obj_or_tuple, tuple):
        return obj_or_tuple[0], build_instance(obj_or_tuple, *args, **kwargs)
    else:
        return get_name_from_obj(obj_or_tuple), build_instance(obj_or_tuple, *args, **kwargs)
