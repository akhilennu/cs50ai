from logging import BASIC_FORMAT
import tictactoe as t
import test_helper as helper
import unittest

class TestTicTacToe(unittest.TestCase):

    def test_player(self):
        for test_case in helper.test_cases:
            self.assertEqual(t.player(test_case["board"]),test_case["player"])

    def test_terminal(self):
        self.assertTrue(t.terminal([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']]))

    def test_result(self):
        board = [['O', 'O', 'X'], ['X', 'O', 'X'], [t.EMPTY, 'X', t.EMPTY]]
        tmp = t.result(board,(2,2))
        self.assertEqual(tmp,[['O', 'O', 'X'], ['X', 'O', 'X'], [t.EMPTY, 'X', 'O']])
        self.assertEqual(board,[['O', 'O', 'X'], ['X', 'O', 'X'], [t.EMPTY, 'X', t.EMPTY]])

    def test_minimax(self):
        self.assertEqual(t.minimax([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', t.EMPTY]]),(2,2))
        self.assertEqual(t.minimax([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', t.EMPTY, t.EMPTY]]),(2,2))
        self.assertEqual(t.minimax([['O', 'O', 'X'], ['X', 'O', 'X'], [t.EMPTY, 'X', t.EMPTY]]),(2,2))

if __name__ == '__main__':
    unittest.main()
