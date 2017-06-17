import subprocess

from .exceptions import GitException


def common_ancestor(target, current='HEAD'):
    """
    Find the most recent ancestor commit that is shared between the two branches. This function
    simply calls `git-merge-base` command.

    Args:
    target (string): name of branch to compare to current.
    current (string): name of current branch. Defaults to HEAD.

    Returns:
    string: the ancestor commit SHA-1, removing the final blank-line character.

    Raises:
    GitException: if git-merge cannot find a common ancestor.
    """
    output_format = lambda o: str(o)[:-1]
    try:
        output = subprocess.check_output(
            ['git', 'merge-base', current, target],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        raise GitException(output_format(e.output))
    else:
        return output_format(output)
