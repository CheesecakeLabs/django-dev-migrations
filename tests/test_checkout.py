import os
import shutil

import pytest

from django_nomad.git.utils import common_ancestor, diff_files
from django_nomad.git.exceptions import GitException


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


def test_common_ancestor(setup_repo):
    # Test that default argument values don't break and return the expected type.
    assert isinstance(common_ancestor("master"), str)

    # Test that if an inexistent branch is passed as argument, it raises an error.
    with pytest.raises(GitException):
        common_ancestor("master", "lalalalalalala")

    # Test that when two valid branches with an ancestor are passed as arguments, it returns
    # the expected type.
    assert isinstance(common_ancestor("master", "newbranch"), str)


def test_diff_files(setup_repo):
    # Test that when two valid branches are passed as arguments, it returns the expected type.
    assert diff_files("master", "newbranch").__iter__

    # Test that if an inexistent branch is passed as argument, it raises an error.
    with pytest.raises(GitException):
        common_ancestor("master", "lalalalalalala")
