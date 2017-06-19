import re

from django.conf import settings
settings.configure()


def filter_migration_files(files_list):
    """
    Separate migration files from a list of files.

    Args:
    files_list (list): a list of file names.

    Returns:
    list: files corresponding to migration files.
    """
    # Remove pycache files from list
    clean_files_list = filter(lambda f: r'.*__pycache__.*'.match(f), files_list)

    # Get list of migration folders
    default_migration_folder = '^[\w\-\.]*/migrations/[\w\-\. ]+\.py$'
    other_migration_folders = [
        '^[\w\-\.]*/{}.py$'.format(odule.replace('.', '/'))
        for _, module in settings.MIGRATION_MODULES.items()
    ]

    # Compile regex that matches migration folders
    generic_migration_folder_list = other_migration_folders + [default_migration_folder]
    generic_migration_folder_regex = re.compile('|'.join(generic_migration_folder_list))

    return list(filter(lambda f: generic_migration_folder_regex.match(f), clean_files_list))
