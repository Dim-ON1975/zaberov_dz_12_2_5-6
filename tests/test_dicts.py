from utils.dicts import get_val

data1 = {'vcs': 'mercurial', 1: 2023}
data2 = {}


def test_get_val():
    assert get_val(data1, 'vcs') == 'mercurial'
    assert get_val(data1, 1) == 2023
    assert get_val(data1, 'vcs', 'git') == 'mercurial'
    assert get_val(data1, 'vc', 'git') == 'git'
    assert get_val(data1, 1, 'git') == 2023
    assert get_val(data1, 0, 'git') == 'git'
    assert get_val(data2, 'vcs', 'git') == 'git'
    assert get_val(data2, 1, 'git') == 'git'
    assert get_val(data2, 'vcs', 'bazaar') == 'bazaar'
    assert get_val(data2, 1, 'bazaar') == 'bazaar'
    assert get_val(data2, 0, 'bazaar') == 'bazaar'
