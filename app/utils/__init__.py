import re


def camel_to_snake(x: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', x)

    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(word: str) -> str:
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
