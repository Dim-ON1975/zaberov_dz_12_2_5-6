from typing import Union, TypeAlias

str_int: TypeAlias = Union[str, int]


def get_val(collection: dict, key: str_int, default: str = 'git') -> str_int:
    """
    Возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    :param collection: словарь, dict
    :param key: значение ключа, str
    :param default: строка, если нет ключа, указанная по умолчанию, str
    :return:
    """
    if key in collection:
        return collection.get(key)
    else:
        return default
