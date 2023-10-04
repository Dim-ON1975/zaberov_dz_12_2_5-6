import pytest
from typing import Union
from utils.dicts import get_val

data1 = {'vcs': 'mercurial', 1: 2023}
data2 = {}


@pytest.mark.parametrize('dict_col, key, def_col, expected', [
    (data1, 'vcs', '', 'mercurial'),
    (data1, 1, '', 2023),
    (data1, 'vcs', 'git', 'mercurial'),
    (data1, 'vc', 'git', 'git'),
    (data1, 1, 'git', 2023),
    (data1, 0, 'git', 'git'),
    (data2, 'vcs', 'git', 'git'),
    (data2, 1, 'git', 'git'),
    (data2, 'vcs', 'bazaar', 'bazaar'),
    (data2, 1, 'bazaar', 'bazaar'),
    (data2, 0, 'bazaar', 'bazaar')
])
def test_get_val(dict_col: dict, key: Union[str, int], def_col: str, expected: str):
    assert get_val(dict_col, key, def_col) == expected
