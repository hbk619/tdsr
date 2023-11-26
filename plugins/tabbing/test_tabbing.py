from tabbing.tabbing import parse_output

cd = """
bin/ include/ lib/
'➜  venv git:(plugins) ✗ cd include/'
"""


def test_cd():
    expected = ["bin include selected lib"]
    results = parse_output(cd.split('\n'))
    assert results == expected

cd_sym_link = """
bin/ include/ lib@/
'➜  venv git:(plugins) ✗ cd lib/'
"""


def test_cd_symlink():
    expected = ["bin include lib@ selected"]
    results = parse_output(cd_sym_link.split('\n'))
    assert results == expected

cd_sym_link_without_slash = """
bin/ include/ lib@
'➜  venv git:(plugins) ✗ cd lib/'
"""


def test_cd_symlink():
    expected = ["bin include lib@ selected"]
    results = parse_output(cd_sym_link.split('\n'))
    assert results == expected


cd_nothing = """
'➜  venv git:(plugins) ✗ cd include/'
"""


def test_cd_nothing_to_tab_to():
    expected = ["Nothing listed"]
    results = parse_output(cd_nothing.split('\n'))
    assert results == expected
