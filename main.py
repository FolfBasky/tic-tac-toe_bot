import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.board = [' ' for _ in range(9)]
        self.current_player = "X"

        self.buttons = [tk.Button(self.window, text=" ", width=10, height=5, command=lambda i=i: self.make_move(i), bg='black', fg='red', font=('Helvetica','20', 'bold')) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.buttons[position]['text'] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Победа!", f"Победил игрок {self.current_player}")
                self.window.quit()
            elif ' ' not in self.board:
                messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
                self.window.quit()
                exit()
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.current_player == "O":
                self.bot_move()

    def check_win(self, player):
        win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for pos in win_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] == player:
                return True
        return False

    def bot_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.make_move(best_move)

    def minimax(self, board, depth, is_maximizing):
        if self.check_win('O'):
            return 1
        elif self.check_win('X'):
            return -1
        elif ' ' not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()
