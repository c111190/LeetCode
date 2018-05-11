#794. Valid Tic-Tac-Toe State
'''
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
'''
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        
        char = ''.join(board)
        diff = char.count('X')-char.count('O')
        
        
        if diff > 1 or diff < 0:
            return False
        winner = win(board)
        #print '1', winner, diff
        if winner == 'winwin':
            return False
        
        if winner == 'X' and diff == 0:
            return False
        
        if winner == 'O' and diff != 0:
            return False
        
        
        trans_board = [ ''.join([board[j][i] for j in range(3)]) for i in range(3) ]
        winner = win(trans_board)
        
        #print '2', winner, diff
        if winner == 'winwin':
            return False
        
        if winner == 'X' and diff == 0:
            return False
        
        if winner == 'O' and diff != 0:
            return False
        
        return True
    
def win(board):
    if 'XXX' in board and 'OOO' in board:
        return 'winwin'

    if 'XXX' in board:
        return 'X'
    
    if 'OOO' in board:
        return 'O'

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    return 'none'
