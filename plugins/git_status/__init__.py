import plugins.git_status.parse_git_status


def parse_output(lines):
    return parse_git_status.parse_output(lines)
