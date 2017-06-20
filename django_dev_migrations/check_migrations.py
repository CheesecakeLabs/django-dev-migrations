import sys

from .git.utils import common_ancestor, diff_files
from .migration.utils import filter_migration_files


def check_migrations():
    sys.stdout.write('Verifying migrations...')

    current = sys.argv[1]
    target = sys.argv[2]

    ancestor_commit = common_ancestor(current, target)
    files_diff = diff_files(ancestor_commit, current)
    migration_files = filter_migration_files(files_diff)

    if len(migration_files) > 0:
        sys.stdout.write('There are migrations applied to this branch.')
        for file in migration_files:
            sys.stdout.write(file)
    else:
        sys.stdout.write('No migrations found.')
