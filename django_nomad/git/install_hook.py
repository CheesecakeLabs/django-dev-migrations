import os
import sys

from django_nomad.git.exceptions import GitHookAlreadyExists
from django_nomad.git.utils import find_git_directory


HOOK_TEMPLATE = """#!{shebang}

import os
import sys

if __name__ == '__main__':
    if len(sys.argv) > 3:
        current = sys.argv[1]
        target = sys.argv[2]
        is_branch = int(sys.argv[3])

        if not is_branch:
            sys.exit(0)
        else:
            output = os.system('python manage.py check_nomad_migrations %s %s' % (current, target))
            if output > 0:
                print('An error happened checking migrations.')
"""


def create_user_env_python_shebang():
    """
    Generate a python shebang string based on user environment (if using virtualenv for
    instance). Source copied from `flake8/src/flake8/main/git.py`.

    Returns:
    string: the formatted shebang
    """
    if sys.executable is not None:
        return sys.executable
    return "/usr/bin/env python"


def has_post_checkout_file(post_checkout_path):
    """
    Verify if there is a file called post-checkout inside the git hooks folder with
    content different than the migrations hook.

    Returns:
    bool: True, if the file is exists.
    """
    if os.path.exists(post_checkout_path):
        with open(post_checkout_path, "r") as post_checkout_hook:
            content = post_checkout_hook.read()
            return "python manage.py check_nomad_migrations" not in content
    return False


def install_checkout_hook():
    """
    Creates a post-checkout executable file inside git hooks folder that checks
    migration files
    """
    git_path = find_git_directory()
    hooks_path = os.path.join(git_path, "hooks")
    post_checkout_path = os.path.abspath(os.path.join(hooks_path, "post-checkout"))

    if has_post_checkout_file(post_checkout_path):
        raise GitHookAlreadyExists()

    with open(post_checkout_path, "w") as f:
        shebang = create_user_env_python_shebang()
        f.write(HOOK_TEMPLATE.format(shebang=shebang))


def uninstall_checkout_hook():
    """
    Removes the django-nomad post-checkout executable file
    """
    pass
