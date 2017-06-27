from django.core.management.base import BaseCommand

from django_nomad.git.utils import common_ancestor, diff_files, get_file_content_from_commit
from django_nomad.migration.utils import (
    extract_migration_info_from_path,
    filter_migration_files,
    get_migration_operations,
    is_migration_applied,
)
from ..utils import print_color


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('current')
        parser.add_argument('target')

    def handle(self, *args, **kwargs):
        print_color('Verifying migrations...', 'BLUE')

        current = kwargs['current']
        target = kwargs['target']

        # Find all migration files between previous branch and common ancestor commit
        ancestor_commit = common_ancestor(current, target)
        files_diff = diff_files(ancestor_commit, current)
        migration_files = filter_migration_files(files_diff)

        # Filter applied migrations only
        applied_migration_files = []
        for migration_file in migration_files:
            app, name = extract_migration_info_from_path(migration_file)
            if is_migration_applied(app, name):
                applied_migration_files.append((migration_file, app, name))

        # Get migration operations and feedback print messages
        if len(applied_migration_files) > 0:
            print_color('There are nomad migrations applied to this branch:', 'RED')

            for migration in applied_migration_files:
                print_color('    {}'.format(migration[0]), 'RED')
                print_color('    Operations:'.format(migration[0]), 'RED')

                file_content = get_file_content_from_commit(migration[0], current)
                operations = get_migration_operations(file_content, migration[1], migration[2])
                for operation in operations:
                    print_color('        {}'.format(operation), 'RED')

                print('')
        else:
            print_color('No nomad migrations found', 'GREEN')
