import sys

from django.core.management.base import BaseCommand

from django_nomad.git.utils import common_ancestor, diff_files
from django_nomad.migration.utils import (
    extract_migration_info_from_path,
    filter_migration_files,
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

        ancestor_commit = common_ancestor(current, target)
        files_diff = diff_files(ancestor_commit, current)
        migration_files = filter_migration_files(files_diff)

        applied_migration_files = []
        for migration in migration_files:
            app, name = extract_migration_info_from_path(migration)
            if is_migration_applied(app, name):
                applied_migration_files.append(migration)

        if len(applied_migration_files) > 0:
            print_color('There are nomad migrations applied to this branch:', 'RED')
            for file in applied_migration_files:
                print_color('    {}'.format(file), 'RED')
        else:
            print_color('No nomad migrations found', 'GREEN')
