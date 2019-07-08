import os
import shutil

import pytest


@pytest.fixture
def setup_repo():
    repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_project")

    temp_repo = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".temptest")
    shutil.rmtree(temp_repo, ignore_errors=True)
    shutil.copytree(repo_root, temp_repo)

    git_dir = os.path.join(temp_repo, "dot.git")
    dot_git_dir = os.path.join(temp_repo, ".git")
    shutil.move(git_dir, dot_git_dir)

    os.chdir(temp_repo)
