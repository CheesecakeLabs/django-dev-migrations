from django.core.management import call_command


def test_command(setup_repo, db):
    call_command("check_nomad_migrations", "master", "newbranch")
    call_command("check_nomad_migrations", "newbranch", "master")
