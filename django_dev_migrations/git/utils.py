import subprocess

from .exceptions import GitDirNotFound, GitException


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
    try:
        output = subprocess.check_output(
            ['git', 'merge-base', current, target],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        raise GitException(e.output.decode('utf-8')[:-1])
    else:
        return output.decode('utf-8')[:-1]


def diff_files(target, current='HEAD'):
    """
    Get list of changed files between two commit refs.

    Args:
    target (string): name of branch to compare to current.
    current (string): name of current branch. Defaults to HEAD.

    Returns:
    list: name of files that were changed between current and target.

    Raises:
    GitException: if any error occur while executing diff.
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
        return list(filter(bool, output.split('\n')))


def get_file_content_from_commit(file_name, commit_ref):
    """
    Get the content a file from a given commit reference.

    Args:
    file_name (string): the file path.
    commit_ref (string): the commit SHA-1 reference.

    Returns:
    string: the given file content.

    Raises:
    GitException: if any error occur while executing show.
    """
    try:
        bin_output = subprocess.check_output(
            ['git', 'show', '{}:{}'.format(commit_ref, file_name)],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        raise GitException('Could not get file {} from {}'.format(file_name, commit_ref))
    else:
        return bin_output.decode('utf-8')


def find_git_directory():
    """
    Search for git directory (in case the user in not on the project root).

    Returns:
    string: path to git directory
    """
    try:
        bin_output = subprocess.check_output(
            ['git', 'rev-parse', '--git-dir'],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        raise GitDirNotFound()
    else:
        return bin_output.decode('utf-8')[:-1]
