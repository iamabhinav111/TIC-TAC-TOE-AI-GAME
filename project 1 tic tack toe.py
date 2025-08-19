"""
Tic-Tac-Toe AI Game
-------------------
This project demonstrates an AI agent that plays Tic-Tac-Toe against a human player.
The AI uses the Minimax algorithm with Alpha-Beta pruning, making it unbeatable.

Author: Abhinav Kumar (Internship Project)
"""

import math

class TicTacToe:
    def __init__(self):
        """Initialize the game board."""
        self.board = [" " for _ in range(9)]

    def print_board(self):
        """Display the current game board."""
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("|".join(row))
            print("-" * 5)

    def available_moves(self):
        """Return list of available moves."""
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def is_full(self):
        """Check if the board is full."""
        return " " not in self.board

    def winner(self):
        """Check if there is a winner."""
        win_combos = [
            (0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # cols
            (0,4,8), (2,4,6)            # diagonals
        ]
        for (a, b, c) in win_combos:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                return self.board[a]
        return None

    def minimax(self, depth, alpha, beta, is_maximizing):
        """Minimax algorithm with Alpha-Beta pruning."""
        win = self.winner()
        if win == "O":
            return 1
        elif win == "X":
            return -1
        elif self.is_full():
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for move in self.available_moves():
                self.board[move] = "O"
                eval = self.minimax(depth+1, alpha, beta, False)
                self.board[move] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.available_moves():
                self.board[move] = "X"
                eval = self.minimax(depth+1, alpha, beta, True)
                self.board[move] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def best_move(self):
        """Determine the AI's best move using Minimax."""
        best_val = -math.inf
        move = None
        for i in self.available_moves():
            self.board[i] = "O"
            move_val = self.minimax(0, -math.inf, math.inf, False)
            self.board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
        return move

    def play_game(self):
        """Run the main game loop where human plays against AI."""
        print("Welcome to Tic Tac Toe (Internship Project)")
        self.print_board()

        while True:
            # Human turn
            try:
                human_move = int(input("Enter your move (0-8): "))
            except ValueError:
                print("Invalid input. Please enter a number between 0-8.")
                continue

            if 0 <= human_move <= 8 and self.board[human_move] == " ":
                self.board[human_move] = "X"
            else:
                print("Invalid move. Try again.")
                continue

            self.print_board()
            if self.winner():
                print("Player X wins!")
                break
            if self.is_full():
                print("It's a draw!")
                break

            # AI turn
            ai_move = self.best_move()
            self.board[ai_move] = "O"
            print("AI chose position", ai_move)
            self.print_board()

            if self.winner():
                print("Player O (AI) wins!")
                break
            if self.is_full():
                print("It's a draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
