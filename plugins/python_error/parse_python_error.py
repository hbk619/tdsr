import re

file_name_matcher = re.compile(r"\".+/(.+\..+)\"")
line_matcher = re.compile(r",\s(line\s\d+),")
method_matcher = re.compile(r",\sin\s(.+)")


def parse_output(lines):
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
