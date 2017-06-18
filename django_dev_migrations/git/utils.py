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
    output_format = lambda o: o.decode('utf-8')[:-1]
    try:
        output = subprocess.check_output(
            ['git', 'merge-base', current, target],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        raise GitException(output_format(e.output))
    else:
        return output_format(output)


def diff_files(target, current='HEAD'):
    """
    Get list of changed files between two commit refs.

    Args:
    target (string): name of branch to compare to current.
    current (string): name of current branch. Defaults to HEAD.

    Returns:
    list: name of files that were changed between current and target.
    """
    try:
        bin_output = subprocess.check_output(
            ['git', 'diff', current, target, '--name-only'],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        raise GitException('Error getting diff between commits {} and {}'.format(
            current,
            target
        ))
    else:
        output = bin_output.decode('utf-8')

        # Remove empty strings
        return filter(bool, output.split('\n'))

