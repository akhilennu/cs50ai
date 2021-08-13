import tictactoe as t
import test_helper as helper
import unittest

class TestTicTacToe(unittest.TestCase):

    def test_player(self):
        for test_case in helper.test_cases:
            self.assertEqual(t.player(test_case["board"]),test_case["player"])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
