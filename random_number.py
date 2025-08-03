def print_board(board):
    """Print the Sudoku board in a readable format"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Find an empty cell (represented by 0)"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, column
    return None

def is_valid(board, num, pos):
    """Check if a number is valid in a given position"""
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    """Solve the Sudoku using backtracking"""
    find = find_empty(board)
    if not find:
        return True  # Puzzle is solved
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # Backtrack if solution not found

    return False

def input_board():
    """Take input for the Sudoku board"""
    print("Enter the Sudoku board (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            row = input(f"Row {i+1} (9 numbers separated by spaces): ").split()
            if len(row) != 9:
                print("Please enter exactly 9 numbers.")
                continue
            try:
                row = [int(num) for num in row]
                board.append(row)
                break
            except ValueError:
                print("Please enter numbers only (0-9).")
    return board

def main():
    """Main function to run the Sudoku solver"""
    print("SUDOKU SOLVER")
    board = input_board()
    
    print("\nInput Sudoku:")
    print_board(board)
    
    if solve(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("\nNo solution exists for this Sudoku.")

if __name__ == "__main__":
    main()