import typing
import json
import app.config
import app.helpers


def _load_lang() -> dict[str, typing.Any]:
    file_name = 'lang/' + app.config.get('app.lang', 'en') + '.json'
    return json.loads(open(file_name, 'r').read())


_lang = _load_lang()


def get(keys: str):
    return app.helpers.get_from_dict(keys, _lang)


def replace(key, *items):
    value = get(key)
    for var in items:
        value = value.replace('{' + str(var[0]) + '}', str(var[1]))

    return value
