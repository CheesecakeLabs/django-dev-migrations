import pytest

from django_nomad.git.utils import common_ancestor, diff_files
from django_nomad.git.exceptions import GitException


def test_common_ancestor(setup_repo):
    # Test that default argument values don't break
    assert common_ancestor("master") == "526ffeb3e63144bf20e7117974ac4a397a09c1b9"

    # Test that if an inexistent branch is passed as argument, it raises an error.
    with pytest.raises(GitException):
        common_ancestor("master", "lalalalalalala")

    # Test that when two valid branches with an ancestor are passed as arguments
    assert (
        common_ancestor("master", "newbranch")
        == "526ffeb3e63144bf20e7117974ac4a397a09c1b9"
    )


def test_diff_files(setup_repo):
    # Test that when two valid branches are passed as arguments, it returns the
    # expected number of files
    assert len(diff_files("master", "newbranch")) == 2

    # Test that if an inexistent branch is passed as argument, it raises an error.
    with pytest.raises(GitException):
        common_ancestor("master", "lalalalalalala")
