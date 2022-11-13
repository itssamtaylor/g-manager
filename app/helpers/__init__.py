def get_from_dict(keys: str, items: dict):
    value = items
    for key in keys.split('.'):
        v = value.get(key)
        if v is not None:
            value = v
        else:
            return None

    return value
