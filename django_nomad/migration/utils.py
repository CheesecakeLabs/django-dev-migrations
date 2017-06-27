import re

from django.conf import settings
from django.db import connections, DEFAULT_DB_ALIAS
from django.db.migrations.recorder import MigrationRecorder


MIGRATION_MODULE_TEMPLATE = '[\w\-\.]*/{}/[\w\-\. ]+\.py$'


def filter_migration_files(files_list):
    """
    Separate migration files from a list of files.

    Args:
    files_list (list): a list of file names.

    Returns:
    list: files corresponding to migration files.
    """
    # Remove pycache files from list
    clean_files_list = list(
        filter(lambda f: not re.compile('.*__pycache__.*').match(f), files_list)
    )

    # Get list of migration folders
    default_migration_folder = MIGRATION_MODULE_TEMPLATE.format('migrations')
    other_migration_folders = [
        MIGRATION_MODULE_TEMPLATE.format(module.replace('.', '/'))
        for _, module in settings.MIGRATION_MODULES.items()
    ]

    # Compile regex that matches migration folders
    generic_migration_folder_list = other_migration_folders + [default_migration_folder]
    generic_migration_folder_regex = re.compile('|'.join(generic_migration_folder_list))

    return list(filter(lambda f: generic_migration_folder_regex.match(f), clean_files_list))


def extract_migration_info_from_path(path):
    """
    Extract the migration app and name from a migration path, with format:
        [.../]<app>/<migrations-module>/<migration-name>.py

    Args:
    path (string): migration file path.

    Returns:
    app, name (tuple): migration information
    """
    path_split = path.split('/')
    app = path_split[-3]
    name = path_split[-1].replace('.py', '')
    return app, name


def is_migration_applied(app, name):
    """
    Check on migrations database table if the given migration is applied to the database.

    Args:
    app (string): django app to which the migration belongs.
    name (string): migration name.

    Returns:
    bool: True, if the migration is applied.
    """
    db_connection = connections[DEFAULT_DB_ALIAS]
    recorder = MigrationRecorder(db_connection)
    migrations = recorder.applied_migrations()
    return migrations.intersection({(app, name)})


def get_migration_operations(file_content, app, name):
    """
    Execute file content (expecting it is a migration file), instantiate a migraiton and get its
    operations attribute.

    Args:
    file_content (string): a whole migration file content.
    app (string): name of app to which the migration belongs.
    name (string): migration name.

    Returns:
    list: migration operations for given file content, app and name.
    """
    exec(file_content, globals())

    if globals().get('Migration'):
        migration = Migration(app, name)
        return migration.operations

    return []
