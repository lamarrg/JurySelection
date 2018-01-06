import unittest
from pdf import file_path_underscore


class TestJoror(unittest.TestCase):

    def test_path_underscore(self):
        print(file_path_underscore("a new hero"))
        self.assertEqual(file_path_underscore("a new hero"), "a_new_hero")


if __name__ == '__main__':
    unittest.main()