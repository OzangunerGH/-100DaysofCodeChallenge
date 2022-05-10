board_list = ["", "", "", "", "", "", "", "", ""]
turn = 1
game_over = False
 
def check_winner(board_list, mark):
    return((board_list[0] == mark and board_list[1] == mark and board_list[2] == mark) or  #for row1
 
           (board_list[3] == mark and board_list[4] == mark and board_list[5] == mark) or  #for row2
 
           (board_list[6] == mark and board_list[7] == mark and board_list[8] == mark) or  #for row3
 
           (board_list[0] == mark and board_list[3] == mark and board_list[6] == mark) or  #for Colm1
 
           (board_list[1] == mark and board_list[4] == mark and board_list[7] == mark) or  #for Colm 2
 
           (board_list[2] == mark and board_list[5] == mark and board_list[8] == mark) or  #for colm 3
 
           (board_list[0] == mark and board_list[4] == mark and board_list[8] == mark) or  #daignole 1
 
           (board_list[2] == mark and board_list[4] == mark and board_list[6] == mark))
def next_round():
  global turn
  global board_list
  allowed_entries = ["1","2","3","4","5","6","7","8","9"]
  square = input("Which square you would like to fill ? User a number from 1 to 9.\n")
  if square == "exit" or square not in allowed_entries:
      exit()
  else:
      square = int(square)
  if turn % 2 == 0:
      marker = "O"
  else:
      marker = "X"
  if board_list[square - 1] == "":
      board_list[square - 1] = marker
      board = f"{board_list[0]}         |{board_list[1]}      | {board_list[2]}\n - - - - - - - - - - -  \n" \
              f"{board_list[3]}       | {board_list[4]}     | {board_list[5]}\n - - - - - - - - - - - \n" \
              f"{board_list[6]}       | {board_list[7]}     | {board_list[8]}"
      print(board)
      turn += 1
  else:
    pass
 
def is_game_over():
    mark = "X"
    game_over = check_winner(board_list, mark)
    if game_over:
        print("Player 1 Wins!")
        exit()
    mark = "O"
    game_over = check_winner(board_list, mark)
    if game_over:
        print("Player 2 Wins!")
        exit()
    if "" not in board_list:
        print("It's a draw.")
        game_over = True
 
while not game_over:
    next_round()
    is_game_over()
 
 
