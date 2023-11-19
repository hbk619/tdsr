from plugins.git_status import parse_output

status = """On branch my-branchie
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified:   ma/path/to/staged.md

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   a_modified_file
modified:   path/to/a_modified_file

Untracked files:
(use "git add <file>..." to include in what will be committed)
.hidden
some/folder/thing/untracked.md"""


def test_git_status_committed():
    expected = ["modified:   ma/path/to/staged.md"]
    lines = status.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected

no_changes = """On branch my-branchie
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   a_modified_file
modified:   path/to/a_modified_file

Untracked files:
(use "git add <file>..." to include in what will be committed)
.hidden
some/folder/thing/untracked.md"""


def test_git_status_committed_no_changes():
    expected = ["No staged files"]
    lines = no_changes.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected
