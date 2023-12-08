import re

file_name_matcher = re.compile(r"\".+/(.+\..+)\"")
line_matcher = re.compile(r",\s(line\s\d+),?")
method_matcher = re.compile(r",\sin\s(.+)")
syntax_word = re.compile(r"(\w+)")


def parse_syntax_error(lines):
    errors = [lines[0], f"Code is {lines[2]}"]
    indicating_caret = lines[1].index("^")
    for line in lines[2:]:
        if file_name_matcher.search(line):
            file = get_match(line, file_name_matcher)
            if file:
                errors.append(f"File {file}")
            line_number = get_match(line, line_matcher)
            if line_number:
                errors.append(line_number)
            break

    bad_line = lines[2]
    bad_section = bad_line[0:indicating_caret]
    bad_word_matches = syntax_word.search(bad_section)
    if bad_word_matches:
        bad_word = bad_word_matches.groups()[0]
        errors.append(f"Problem at {bad_word}{bad_line[indicating_caret]}")
    return errors


def parse_output(lines):
    if lines[0].startswith('SyntaxError:'):
        return parse_syntax_error(lines)

    errors = [lines[0], f"Code is {lines[1]}"]
    for line in lines[2:]:
        if file_name_matcher.search(line):
            file = get_match(line, file_name_matcher)
            if file:
                errors.append(f"File {file}")
            line_number = get_match(line, line_matcher)
            if line_number:
                errors.append(line_number)
            method = get_match(line, method_matcher)
            if method:
                errors.append(f"Method {method}")
            break

    return errors


def get_match(line, matcher):
    line_matches = matcher.search(line)
    if line_matches:
        return line_matches.groups()[0]
