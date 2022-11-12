import typing
import app.config
import json


def _load_lang() -> dict[str, typing.Any]:
    file_name = 'lang/' + app.config.get_loaded()['app']['lang'] + '.json'
    return json.loads(open(file_name, 'r').read())


_lang = _load_lang()


def get(item):
    value = _lang
    for key in item.split('.'):
        v = value.get(key)
        if v is not None:
            value = v
        else:
            return None

    return value


def replace(key, *items):
    value = get(key)
    for var in items:
        value = value.replace('{' + str(var[0]) + '}', str(var[1]))

    return value
