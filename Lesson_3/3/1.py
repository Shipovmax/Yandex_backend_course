class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row, col):
        # Проверка валидности хода
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False, "Координаты должны быть от 0 до 2"

        if self.board[row][col] != " ":
            return False, "Клетка уже занята"

        # Делаем ход
        self.board[row][col] = self.current_player

        # Проверяем победу
        if self.check_winner():
            return True, f"Игрок {self.current_player} победил!"

        # Проверяем ничью
        if self.is_board_full():
            return True, "Ничья!"

        # Меняем игрока
        self.current_player = "O" if self.current_player == "X" else "X"
        return True, "Ход принят"

    def check_winner(self):
        # Проверка строк
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def display(self):
        print("\n  0 1 2")
        for i, row in enumerate(self.board):
            print(f"{i} {'|'.join(row)}")
            if i < 2:
                print("  -----")


# Тестирование
if __name__ == "__main__":
    game = Board()

    # Пример игры
    moves = [(1, 1), (0, 0), (0, 1), (2, 0), (2, 1)]  # X побеждает

    for move in moves:
        game.display()
        print(f"\nХод игрока {game.current_player}: {move}")
        success, message = game.make_move(move[0], move[1])
        print(message)

        if "победил" in message or "Ничья" in message:
            game.display()
            break

print(print.__doc__)
