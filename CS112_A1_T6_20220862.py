#Program: Connect4 game
#Author: Richard Remo Emmanuel
#ID: 20220862
#Version: 0.6
#Date: 1/march/2024




class Connect4:
    def __init__(self):
        #initializing the game board with empty spaces
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        #defining players symbol
        self.players = ['X', 'O']
        #initilaize the index of the current player
        self.current_player = 0

    def print_board(self):
        #print the game board with separating column  and '-' rows
        for row in reversed(range(6)):
            print('|'.join(self.board[row]))
        print('-' * 13)
        #print column numbers reference
        print('  '.join(map(str, range(1, 8))))

    def drop_piece(self, col):
        #drop a piece in the specified column
        for row in range(6):
            if self.board[row][col] == ' ':
                #updates the board with current player's symbol
                self.board[row][col] = self.players[self.current_player]
                return True
                #if column is full return falsed
        return False


    def check_winner(self):
        #definedirection to check for winning combinations: right, down , diagonal down-right, diagonal down-left
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        #iterate over each cell on the board
        for row in range(6):
            for col in range(7):
                if self.board[row][col] != ' ':
                    for dr, dc in directions:
                        for i in range (1, 4):
                            #check if there's a winning  combination in any direction
                            r, c = row + i * dr, col + i * dc
                            if 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.board[row][col]:
                                if i == 3:
                                    return True
                            else:
                                break



        #if no winning combination found return false
        return False


    def Play_game(self):
        #main game loop
        while True:
            #display the current state of the board
            self.print_board()
            #prompt the current player to choose a column
            col = int(input(f"player{self.players[self.current_player]},  choose a column (1, 7)")) - 1
            if 0 <= col <= 6:
                #if column choice is valid try to drop a piece
                if self.drop_piece(col):
                    #check for a winner
                    if self.check_winner():
                        #if a player wins diplay winning message
                        self.print_board()
                        print(f"player{self.players[self.current_player]} win! ")
                        break
                    #if no winner and the board is full it's a draw
                    elif ' ' not in self.board[0]:
                        self.print_board()
                        print("it's a draw!")
                        break
                    else:
                        #switch to next the player turn
                        self.current_player = (self.current_player + 1)  % 2

                else:
                    #if column is full , prompt to try again
                     print("Column is full. Try again. ")
            else:
                #if column is invalid prompt to choose again
                print("Invalid Colunm, Please choose a column betwen 1 and 7.") 

#create an instance of the connect4 class start the game                                                
if __name__ == "__main__":
    game = Connect4()
    game.Play_game()
