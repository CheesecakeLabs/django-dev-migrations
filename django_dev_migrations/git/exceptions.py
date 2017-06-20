class GitException(Exception):
    """
    Git-command-related exception.
    """
    pass


class GitDirNotFound(GitException):
    """
    A git folder was not found, probably the user haven't initialized git repo.
    """
    message = 'Cannot find git directory, have you run: `git init`?'
