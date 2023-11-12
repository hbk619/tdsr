import parse_pytest


lines = """
=============================================================================== test session starts ===============================================================================
platform mystery -- Python 3.11.2, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 1 item

test_things.py F                                                                                                                                                            [100%]

==================================================================================== FAILURES =====================================================================================
___________________________________________________________________________________ test_answer ___________________________________________________________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_things.py:7: AssertionError
============================================================================= short test summary info =============================================================================
FAILED test_things.py::test_answer - assert 4 == 5
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
================================================================================ 1 failed in 0.01s ================================================================================"""


def test_parsing_assert_error():
    expected = ["code is assert inc(3) == 5", "assert 4 == 5", "where 4 = inc(3)", "1 failed"]
    results = parse_pytest.parse_output(lines.split('\n'))
    assert results == expected


key_error = """
================================================================== FAILURES ===================================================================
_____________________________________________________________ test_answer_correct _____________________________________________________________

    def test_answer_correct():
>       assert {}["blah"] == 1
E       KeyError: 'blah'

test_things.py:7: KeyError
=========================================================== short test summary info ===========================================================
FAILED test_things.py::test_answer_correct - KeyError: 'blah'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================== 1 failed in 0.01s =============================================================="""


def test_parsing_key_error():
    expected = ["code is assert {}[\"blah\"] == 1", "KeyError: 'blah'", "1 failed"]
    results = parse_pytest.parse_output(key_error.split('\n'))
    assert results == expected


passing_and_failed = """
================================================================================= test session starts =================================================================================
platform mystery -- Python 3.11.2, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/blah/code/tdsr
collected 3 items

test_things.py F.F                                                                                                                                                              [100%]

====================================================================================== FAILURES =======================================================================================
_____________________________________________________________________________________ test_answer _____________________________________________________________________________________

    def test_answer():
>       assert inc(3) == 5
E       assert 4 == 5
E        +  where 4 = inc(3)

test_things.py:7: AssertionError
____________________________________________________________________________________ test_parsing _____________________________________________________________________________________

    def test_parsing():
        expected = ["1 failed"]
>       results = parse_pytest.parse_output(lines)

test_things.py:37:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

lines = '\n=============================================================================== test session starts ===============...=================== 1 failed in 0.01s ================================================================================'

    def parse_output(lines):
        lines_to_say = []
        for line in lines:
            matches = error_lines.match(line)
>           if matches.group():
E           AttributeError: 'NoneType' object has no attribute 'group'

parse_pytest.py:10: AttributeError
=============================================================================== short test summary info ===============================================================================
FAILED test_things.py::test_answer - assert 4 == 5
FAILED test_things.py::test_parsing - AttributeError: 'NoneType' object has no attribute 'group'
============================================================================= 2 failed, 1 passed in 0.01s =============================================================================
"""


def test_parsing_passing_and_failed():
    expected = ["code is assert inc(3) == 5", "assert 4 == 5", "where 4 = inc(3)", "code is results = parse_pytest.parse_output(lines)", "code is if matches.group():", "AttributeError: 'NoneType' object has no attribute 'group'", "2 failed", "1 passed"]
    results = parse_pytest.parse_output(passing_and_failed.split('\n'))
    assert results == expected