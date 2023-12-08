from plugins.python_error import parse_output


name_error = """➜  tdsr git:(master) ✗ python3 test.py
Traceback (most recent call last):
  File "/some/path/tdsr/test.py", line 10, in <module>
    level1()
  File "/some/path/tdsr/test.py", line 8, in level1
    return level2()
  File "/some/path/tdsr/test.py", line 5, in level2
    return level3()
  File "/some/path/tdsr/test.py", line 2, in level3
    blah()
NameError: name 'blah' is not defined"""


def test_name_error():
    expected = ["NameError: name 'blah' is not defined", "Code is     blah()", "File test.py", "line 2", "Method level3"]
    lines = name_error.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


syntax_error = """  File "/some/path/tdsr/test.py", line 2
    blah(
        ^
SyntaxError: '(' was never closed"""


def test_syntax_error():
    expected = ["SyntaxError: '(' was never closed", "Code is     blah(", "File test.py", "line 2", "Problem at blah("]
    lines = syntax_error.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected