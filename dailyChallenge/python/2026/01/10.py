# Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

#     Each element in the given matrix is either an "X" or "O".

# A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

# Return:

#     "X wins" if player X has three in a row.
#     "O wins" if player O has three in a row.
#     "Draw" if no player has three in a row.

# 1. tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]) should return "X wins".
# 2. tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]) should return "O wins".
# 3. tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]) should return "Draw".
# 4. tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]) should return "O wins".
# 5. tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]) should return "X wins".
# 6. tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]) should return "Draw".

def tic_tac_toe(board):
    for row in board:
        if row.count(row[0]) == 3: return f"{row[0]} wins" 
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col]: return f"{board[0][col]} wins"
    if board[0][0] == board[1][1] == board[2][2]: return f"{board[0][0]} wins"
    if board[2][0] == board[1][1] == board[0][2]: return f"{board[2][0]} wins"
    return "Draw"

print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]))
print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))
print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))