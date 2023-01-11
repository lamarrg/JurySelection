import unittest
from pdf import file_path_underscore
from juror import JurorModel


class TestJoror(unittest.TestCase):

    def test_path_underscore(self):
        print(file_path_underscore("a new hero"))
        self.assertEqual(file_path_underscore("a new hero"), "a_new_hero")

    # def test_add_juror(self):
    #     new_juror = JurorModel(foreign_key=1, name="Mr Kennedy", age=42, occupation="wrassler", details="i scream my own name into a mic")
    #     new_juror.save_to_db()



if __name__ == '__main__':
    unittest.main()