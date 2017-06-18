import unittest

from .utils import common_ancestor, diff_files
from .exceptions import GitException


class TestGitModule(unittest.TestCase):
    # Tests assume there is a branch named 'master' and no branch named 'lalalalalalala'.

    def test_common_ancestor(self):
        # Test that default argument values don't break and return the expected type.
        self.assertIsInstance(common_ancestor('master'), str)

        # Test that if an inexistent branch is passed as argument, it raises an error.
        with self.assertRaises(GitException):
            common_ancestor('master', 'lalalalalalala')

        # Test that when two valid branches with an ancestor are passed as arguments, it returns
        # the expected type.
        self.assertIsInstance(common_ancestor('master', 'master'), str)

    def test_diff_files(self):
        # Test that when two valid branches are passed as arguments, it returns the expected type.
        self.assertTrue(diff_files('master', 'master').__iter__)

        # Test that if an inexistent branch is passed as argument, it raises an error.
        with self.assertRaises(GitException):
            common_ancestor('master', 'lalalalalalala')
