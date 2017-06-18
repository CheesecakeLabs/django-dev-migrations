import unittest

from git.utils import common_ancestor
from .exceptions import GitException


class TestGitModule(unittest.TestCase):
    def test_common_ancestor(self):
        # Test cases assume there is a branch named 'master' and no branch named 'lalalalalalala'.

        # Test that default argument values don't break and return the expected type.
        self.assertIsInstance(common_ancestor('master'), str)

        # Test that if an inexistent branch is passed as argument, it raises an error.
        with self.assertRaises(GitException):
            common_ancestor('master', 'lalalalalalala')

        # Test that when two valid branches with an ancestor are passed as arguments, it returns
        # the expected type.
        self.assertIsInstance(common_ancestor('master', 'master'), str)