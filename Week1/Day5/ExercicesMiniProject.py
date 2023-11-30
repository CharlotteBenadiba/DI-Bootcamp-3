# Mini-Project - Tic Tac Toe
# What You Will Create
# Create a TicTacToe game in python, where two users can play together.
# tic tac toe

# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, 
# or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.
# Hint
# To do this project, you basically need to create four functions:
# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.
# Tips : Consider The Following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!


#def display_board(board):
   
#    print("*" * 29)
#    for row in board:
#        print("*", end=" ")
#        print(" | ".join(row), end=" ")
#        print("*")
#        print("*" * 29)

#def player_input(player):
    
#    while True:
#        try:
#            position = int(input(f"Player {player}, enter your position (1-9): "))
#            if 1 <= position <= 9:
#                return position
#            else:
#                print("Please enter a number between 1 and 9.")
#        except ValueError:
#            print("Invalid input. Please enter a number.")

#def check_win(board):
    
    # Check rows
#    for i in range(0, 3):
#        if board[i][0] == board[i][1] == board[i][2] != ' ':
#            return True

    # Check columns
#    for i in range(0, 3):
#        if board[0][i] == board[1][i] == board[2][i] != ' ':
#            return True

    # Check diagonals
#    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
#        return True

#    return False


#def play():
    
#    board = [[' ' for _ in range(3)] for _ in range(3)]

#    players = ['X', 'O']
#    turn = 0

#    while True:
#        display_board(board)
#        current_player = players[turn % 2]
#        position = player_input(current_player)

#        row = (position - 1) // 3
#        col = (position - 1) % 3

#        if board[row][col] == ' ':
#            board[row][col] = current_player
#            if check_win(board):
#                display_board(board)
#                print(f"Player {current_player} wins!")
#                break
#            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
#                display_board(board)
#                print("It's a tie!")
#                break
#            else:
#                turn += 1
#        else:
#            print("That position is already taken. Try again.")

# play()
 

