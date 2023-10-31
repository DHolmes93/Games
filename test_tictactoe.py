import unittest
import tictactoe
import random

class TicTacToeTestCase(unittest.TestCase):
    
    def test_do_top_left_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]     # Check if top left cell is empty
        result = tictactoe.do_top_left(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][0], None)

        # self.assertTrue(False)

    def test_do_top_left_cell_has_value(self):
        token = "X"
        board = [["X", None, None], [None, None, None], [None, None, None]] # Check if top left cell has value and put token in cell
        result = tictactoe.do_top_left(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][0], "X")


    def test_do_top_left_cell_has_wrong_value(self):
        token = "O"
        board = [["X", None, None], [None, None, None], [None, None, None]]
        result = tictactoe.do_top_left(board, token)
        self.assertFalse(result)
        self.assertEqual(board[0][0], "X")

    def test_do_top_middle_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]     # Check if top middle cell is empty
        result = tictactoe.do_top_middle(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][1], None)

    def test_do_top_middle_cell_has_value(self):
        token = "O"
        board = [[None, "O", None], [None, None, None], [None, None, None]] # Check if top middle cell has value
        result = tictactoe.do_top_middle(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][1], "O")

    def test_do_top_middle_cell_has_wrong_value(self):
        token = "O"
        board = [[None, "X", None], [None, None, None], [None, None, None]]
        result = tictactoe.do_top_middle(board, token)
        self.assertFalse(result)
        self.assertEqual(board[0][1], "X")

    def test_do_top_right_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]     # Check if top right cell is empty
        result = tictactoe.do_top_right(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][2], None)

    def test_do_top_right_cell_has_value(self):
        token = "X"
        board = [[None, None, "X"], [None, None, None], [None, None, None]] # Check if top right cell has value
        result = tictactoe.do_top_right(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][2], "X")

    def test_do_top_right_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, "X"], [None, None, None], [None, None, None]]
        result = tictactoe.do_top_right(board, token)
        self.assertFalse(result)
        self.assertEqual(board[0][2], "X")

    def test_do_middle_left_cell_has_value(self):
        token = "X"
        board = [[None, None, None], ["X", None, None], [None, None, None]] # Check if middle left cell has value
        result = tictactoe.do_middle_left(board, token)
        self.assertFalse(result)
        self.assertEqual(board[1][0], "X")

    def test_do_middle_left_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]     # Check if middle left cell is empty
        result = tictactoe.do_middle_left(board, token)
        self.assertTrue(result)
        self.assertEqual(board[1][0], None)

    def test_do_middle_left_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, None], ["X", None, None], [None, None, None]]
        result = tictactoe.do_middle_left(board, token)
        self.assertFalse(result)
        self.assertEqual(board[1][0], "X")


    def test_do_center_cell_has_value(self):
        token = "X"
        board = [[None, None, None], [None, "X", None], [None, None, None]] # Check if center cell has value
        result = tictactoe.do_center(board, token)
        self.assertTrue(result)
        self.assertEqual(board[1][1], "X")

    def test_do_center_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]     # Check if middle right cell is empty
        result = tictactoe.do_center(board, token)
        self.assertTrue(result)
        self.assertEqual(board[1][1], None)

    def test_do_center_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, None], [None, "X", None], [None, None, None]]
        result = tictactoe.do_center(board, token)
        self.assertFalse(result)
        self.assertEqual(board[1][1], "X")

    def test_do_middle_right_cell_has_value(self):
        token = "X"
        board = [[None, None, None], [None, None, "X"], [None, None, None]] # Check if middle right cell has token
        result = tictactoe.do_middle_right(board, token)
        self.assertTrue(result)
        self.assertEqual(board[1][2], "X")

    def test_do_middle_right_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]    # Check if middle right cell is empty
        result = tictactoe.do_middle_right(board, token)
        self.assertTrue(result)
        self.assertEqual(board[1][2], None)

    def test_do_middle_right_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, None], [None, None, "X"], [None, None, None]]
        result = tictactoe.do_middle_right(board, token)
        self.assertFalse(result)
        self.assertEqual(board[1][2], "X")

    def test_do_bottom_left_cell_has_value(self):
        token = "X"
        board = [[None, None, None], [None, None, None], ["X", None, None]] # Check if bottom left cell has value
        result = tictactoe.do_bottom_left(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][0], "X")
    
    def test_do_bottom_left_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]    # Check if bottom left cell is empty
        result = tictactoe.do_bottom_left(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][0], None)

    def test_do_bottom_left_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, None], [None, None, None], ["X", None, None]]
        result = tictactoe.do_bottom_left(board, token)
        self.assertFalse(result)
        self.assertEqual(board[2][0], "X")

    def test_do_bottom_middle_cell_has_value(self):
        token = "X"
        board = [[None, None, None], [None, None, None], [None, "X", None]] # Check if bottom middle cell has token
        result = tictactoe.do_bottom_middle(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][1], "X")

    def test_do_bottom_middle_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]    # Check if bottom middle cell is empty
        result = tictactoe.do_bottom_middle(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][1], None)

    def test_do_bottom_middle_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, None], [None, None, None], [None, "X", None]]
        result = tictactoe.do_bottom_middle(board, token)
        self.assertFalse(result)
        self.assertEqual(board[2][1], "X")


    def test_do_bottom_right_cell_has_value(self):
        token = "X"
        board = [[None, None, None], [None, None, None], [None, None, "X"]] # Check if bottom right cell has token
        result = tictactoe.do_bottom_right(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][2], "X")

    def test_do_bottom_right_empty_cell(self):
        token = None
        board = [[None, None, None], [None, None, None], [None, None, None]]    # Check if bottom right cell is empty
        result = tictactoe.do_bottom_right(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][2], None)

    def test_do_bottom_right_cell_has_wrong_value(self):
        token = "O"
        board = [[None, None, None], [None, None, None], [None, None, "X"]] # Check if bottom right cell has wrong value
        result = tictactoe.do_bottom_right(board, token)
        self.assertFalse(result)
        self.assertEqual(board[2][2], "X")


    # etc

    def test_is_stalemate_empty_board(self):
        token = None
        """an empty board should result in ???"""
        board = [[None, None, None], [None, None, None], [None, None, None]]
        result = tictactoe.is_stalemate(board)
        self.assertFalse(result)

    def test_is_stalemate_full_board(self):
        token = "X" or "O"
        board = [["X", "O", "X"], ["O", "X", "X"], ["X", "O", "O"]] # Tests if game is stalemate. Filled Board
        result = tictactoe.is_stalemate(board)
        self.assertTrue(result)

    # tests for has_won, one for each possible winner
    def test_is_game_won_full_board_top_row(self):
        token = "X"
        board = [["X", "X", "X"], [None, None, None], [None, None, None]] # Tests top row winner
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][0] + board[0][1] + board[0][2], "XXX")


    def test_is_game_won_full_board_middle_row(self):
        token = "O"
        board = [[None, None, None], ["O", "O", "O"], [None, None, None]]   # Tests middle row winner
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[1][0] + board[1][1] + board[1][2], "OOO")

    def test_is_game_won_full_board_left_row_down(self):
        token = "X"
        board = [["X", None, None], ["X", None, None], ["X", None, None]]   # Left row down winner
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][0] + board[1][0] + board[2][0], "XXX")

    def test_is_game_won_full_board_right_row_down(self):
        token = "O"
        board = [[None, None, "O"], [None, None, "O"], [None, None, "O"]]
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][2] + board[1][2] + board[2][2], "OOO")        #Testing if same values on right column going down

    def test_is_game_won_full_board_bottom_row(self):
        token = "X"
        board = [[None, None, None], [None, None, None], ["X", "X", "X"]]
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[2][0] + board[2][1] + board[2][2], "XXX")        #Testing if same values on bottom row will equal winner

    def test_is_game_won_full_board_diagonal_win(self):
        token = "X"
        board = [["X", None, None], [None, "X", None], [None, None, "X"]]
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][0] + board[1][1] + board[2][2], "XXX")        #Testing if same values on bottom row will equal winner

    def test_is_game_won_full_board_middle_row_down_win(self):
        token = "X"
        board = [[None, "X", None], [None, "X", None], [None, "X", None]]
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][1] + board[1][1] + board[2][1], "XXX")

    def test_is_game_won_full_board_diagonal_second_win(self):
        token = "O"
        board = [[None, None, "O"], [None, "O", None], ["O", None, None]]
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][2] + board[1][1] + board[2][0], "OOO")        #Testing if same values on bottom row will equal winner
    # other tests you can think of (think edge cases -- e.g. looking at the edges of the board (off-by-one errors))

    def test_is_stalemate_check_random(self):

        board = [["X", "O", "X"], ["O", "X", "X"], ["X", "O", "O"]] # Tests if game is stalemate. Filled Board
        row = random.randint(0,2)
        column = random.randint(0,2)
        board[row][column] = None
        result = tictactoe.is_stalemate(board)
        self.assertFalse(result)


    def test_is_game_won_full_board_four_corner_win(self):
        token = "O"
        board = [["O", None, "O"], [None, None, None], ["O", None, "O"]]
        result = tictactoe.is_game_won(board, token)
        self.assertTrue(result)
        self.assertEqual(board[0][0] + board[0][2] + board[2][0] + board[2][2], "OOOO") 




if __name__ == "__main__":
    unittest.main()
