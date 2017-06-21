import os
import sys

from django.core.management.base import BaseCommand

from django_dev_migrations.git.exceptions import GitHookAlreadyExists
from django_dev_migrations.git.utils import find_git_directory


class Command(BaseCommand):
    help = """
        Creates a post-checkout executable file inside git hooks folder that checks migration
        files.
    """

    def __init__(self, *args, **kwargs):
        git_path = find_git_directory()
        hooks_path = os.path.join(git_path, 'hooks')
        self.post_checkout_path = os.path.abspath(os.path.join(hooks_path, 'post-checkout'))
        return super().__init__(*args, **kwargs)

    def add_arguments(self, *args):
        pass

    def handle(self, *args, **kwargs):
        if self.has_post_checkout_file():
            raise GitHookAlreadyExists()

        self.copy_hook_to_post_checkout_folder()
        sys.stdout.write('post-checkout file was created...')

    def has_post_checkout_file(self):
        """
        Verify if there is a file called post-checkout inside the git hooks folder

        Returns:
        bool: True, if the file is exists.
        """
        return os.path.exists(self.post_checkout_path)

    def create_user_env_python_shebang(self):
        """
        Generate a python shebang string based on user environment (if using virtualenv for
        instance). Source copied from `flake8/src/flake8/main/git.py`.

        Returns:
        string: the formatted shebang
        """
        if sys.executable is not None:
            return sys.executable
        return '/usr/bin/env python'

    def copy_hook_to_post_checkout_folder(self):
        """
        Create a post-checkout file and add content from `post-checkout.py` to it, adding the a
        shebang based on user environment to top of file.
        """
        with open(self.post_checkout_path, 'w') as f:
            shebang = self.create_user_env_python_shebang()
            f.write(HOOK_TEMPLATE.format(shebang=shebang))


HOOK_TEMPLATE = """#!{shebang}

import sys

from django.core.management import call_command

if __name__ == '__main__':
    if len(sys.argv) > 3:
        current = sys.argv[1]
        target = sys.argv[2]
        sys.exit(call_command('check_migrations', (current, target)))
"""
