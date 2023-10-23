import sys

is_x_turn = True


def print_board(board):
    """
    Board has pipes on the sides of each cell, dashes on top and bottom.
    Print the top dashes, then print each line of the board (first contents, then separator line)
    Last separator line will act as the bottom dashes
    -------------
    | X | O |   |
     ---
    """
    print("-------------")  # top dashes

    for row in board:  # loop through each row
        output = "|"  # start with the leftmost pipe
        for cell in row:  # loop through each cell
            if cell is None:
                output += "   |"
            else:
                output += f" {cell} |"

        # outside `for cell ...`
        print(output)  # this is the row we just assembled
        print("-------------")  # this is the division between this row and the following


def prompt_user_for_input():
    # ask the user to type something
    user_input = input(f"Choose a cell: ")

    # we can do some cleanup of the user input, like removing extra leading/trailing spaces (strip()) and making everything lowercase (lower())
    # we can make a new variable, and/or reuse it
    user_input_clean = user_input.strip()
    user_input_clean = user_input_clean.lower()  # we reused user_input_clean here

    return user_input_clean

# TODO implement me!
# all the "do" methods should:
#   - verify if the move is legal (if not, return False)
#   - if legal, put the correct token (X or O) in the correct place in the board
#   - if a token was placed, return True, otherwise return False
def do_top_left(board):
    while is_x_turn or not is_x_turn:
        board[0][0] = token
        return True
        

def do_top_middle(board):
    while is_x_turn or not is_x_turn:
        board[0][1] = token
        return True
    # print("'do_top_middle' needs to be implemented!")
    # return False

def do_top_right(board):
    while is_x_turn or not is_x_turn:
        board[0][2] = token
    # print("'do_top_right' needs to be implemented!")
        return True

def do_middle_left(board):
    while is_x_turn or not is_x_turn:
        board[1][0] = token
    # print("'do_middle_left' needs to be implemented!")
        return True

def do_center(board):
    while is_x_turn or not is_x_turn:
        board[1][1] = token
    # print("'do_center' needs to be implemented!")
        return True

def do_middle_right(board):
    while is_x_turn or not is_x_turn:
        board[1][2] = token
    # print("'do_middle_right' needs to be implemented!")
        return True

def do_bottom_left(board):
    while is_x_turn or not is_x_turn:
        board[2][0] = token
    # print("'do_bottom_left' needs to be implemented!")
        return True

def do_bottom_middle(board):
    while is_x_turn or not is_x_turn:
        board[2][1] = token
    # print("'do_bottom_middle' needs to be implemented!")
        return True

def do_bottom_right(board):
    while is_x_turn or not is_x_turn:
        board[2][2] = token
    # print("'do_bottom_right' needs to be implemented!")
        return True

def is_game_won(board):

    if board[0][0] != None and board[0][0] == board[0][1] and board[0][0] == board[0][2]: # Top Row
        return True
    elif board[0][0] != None and board[0][0] == board[1][0] and board[0][0] == board[2][0]: #Left Row Down
        return True
    elif board[0][0] != None and board[0][0] == board[1][1] == board[0][0] == board[2][2]: # Diagonal
       return True
    elif board[2][0] != None and board[2][0] == board[1][1] and board[2][0] == board[0][2]: #Diagonal
        return True
    elif board[0][2] != None and board[0][2] == board[1][2] and board[0][2] == board[2][2]: #Right Row Down
        return True
    elif board[2][0] != None and board[2][0] == board[2][1] and board[2][0] == board[2][2]: # Bottom Row
        return True
    elif board[1][0] != None and board[1][0] == board[1][1] and board[1][0] == board[1][2]: # Middle Row
        return True
    elif board[0][1] != None and board[0][1] == board[1][1] and board[0][1] == board[2][2]: #Middle Row Down
        return True
    
    else:
      return False

    # if (board[0][0] == board[0][1] == board[0][2]) or (board[1][0] == board[1][1] == board[1][2]) or (board[2][0] == board[2][1] == board[2][2]) or (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board [2][0]):
        #  print(f"{token} is the winner!")
    #     # sys.exit()


    

    # winning_combinations = [[]]
    # if board[][] == board[][]:
    #     print(has_won)

    # print("'is_game_won' needs to be implemented!")
    # return False


def board_checker(board):
    for row in board:
        for cell in row:
            if cell is not None and board is not None:
                return False
            else:
                return True

def is_stalemate(board):
    return board_checker(board)
    # checker = len(board)

    # for row in board:
    #     for cell in row:
    
    
    
    
    
    # for row in board:
    #     if is_game_won:
    #         return False
    #     else:
    #         return True



    # idx = board[index]        
    # for row in board:
    #     if board[idx][idx] 

    

    # for x in board:
    #     x != x
    # return True
    # index = board[]

    # if index != index:
    #     return True

   

    # while True:
    #     if board[0][0] != None and board[0][0] != board[0][1] and board[0][0] != board[0][2] and
        
    #     elif board[1][0] != None  and board[1][0] != board[1][1] and board[1][0] != board[1][2] and #Middle Row
            
    #     elif board[2][0] != None and board[2][0] != board[2][1] and board[2][0] != board[2][2] and # Bottom Row
           
    #     elif board[0][0] != None and board[0][0] != board[1][0] and board[0][0] == board[2][0] and #Left Row Down
            
    #     elif board[0][2] != None and board[0][2] != board[1][2] and board[0][2] == board[2][2] and #Right Row Down
            
    #     elif board[0][0] != None and board[0][0] != board[1][1] and board[0][0] != board[2][2] and # Diagonal
            
    #     elif board[2][0] != None and board[2][0] != board[1][1] and board[2][0] != board[0][2] and #Diagonal
    #         return True
    #     else:
    #         return False
   

    # # print("'is_stalemate' needs to be implemented!")
    # # return False


valid_spaces = {"top left": do_top_left, 
                 "top middle": do_top_middle, 
                 "top right": do_top_right, 
                 "middle left": do_middle_left, 
                 "center": do_center, 
                 "middle right": do_middle_right, 
                 "bottom left": do_bottom_left, 
                 "bottom middle": do_bottom_middle, 
                 "bottom right": do_bottom_right}



# def used_spaces():
    


def validate_and_route(user_input, board):
    global is_x_turn
    if user_input in ("quit", "exit"):
        print("See ya!")
        sys.exit()
    elif user_input in valid_spaces.keys():
        success = valid_spaces[user_input](board)  # this is where the correct function gets called
        if success:  # if a turn was successfully played
            is_x_turn = not is_x_turn  # it's the other person's turn now
        else:
            print(f"Uh-oh, looks like '{user_input}' is an illegal move!")
    else:
        print(f"Unknown command: '{user_input}'")


def game_loop():
    print("~* Tic Tac Toe *~")  # this is outside the loop, so only gets printed once
    
    # this is our board -- the capital letters are only for visual distinction
    # note this is what is called a 2-dimensional array -- an array (list) where each
    # element is another array (list)
    #
    # items can be accessed as such:
    #   board[0]      this is the first row of the board
    #   board[0][0]   this is the first cell of the first row
    #   board[2][1]   this is the second cell of the third row
    #   etc
    BOARD = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]

    # our loop where we look for user input
    while True:
        global token
        print_board(BOARD)  # print the board first
        token = "X" if is_x_turn else "O"
        print(f"It's {token}'s turn!")
        user_input = prompt_user_for_input()  # get the input from the user
        validate_and_route(user_input, BOARD) # interpret the input and (try to) do the move

        # look for a winner
        has_won = is_game_won(BOARD)
        if has_won:
            print(f"{token} is the winner!")
            sys.exit()

        # look for a stalemate
        if is_stalemate(BOARD):   # a function that returns a boolean can be used as an 'if' condition
            print(f"Stalemate -- bummer!")
            sys.exit()


# our classic (if ugly) Python entry point
if __name__ == "__main__":
    game_loop()






 # winner = board[[2][0] == [0][1] ==[0][2]] == [[2][0], [2][1] == [2][2] == token]
    # for x in winner:
    #     if is_x_turn or not is_x_turn and x in winner:
    #         return is_game_won