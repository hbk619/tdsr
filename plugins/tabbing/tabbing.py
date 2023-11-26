import re


def parse_output(lines):
    words_to_say = []
    options = []
    command = ""
    for line in lines:
        if line:
            if "cd " in line:
                command = line
            else:
                options += line.split()

    for option in options:
        selected = ""
        if re.sub('@/?$', '', option) in command:
            selected = " selected"

        words_to_say.append(re.sub('/$', '', option) + selected)

    return [" ".join(words_to_say)] if len(words_to_say) else ['Nothing listed']
