import random
import docx

from builtins import PendingDeprecationWarning


def generate_sudoku():
    # Generate a sudoku puzzle
    puzzle = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(choices)
            for choice in choices:
                if is_valid(puzzle, i, j, choice):
                    puzzle[i][j] = choice
                    break
    return puzzle

def is_valid(puzzle, i, j, val):
    # Check row
    if val in puzzle[i]:
        return False

    # Check column
    if val in [puzzle[x][j] for x in range(9)]:
        return False

    # Check 3x3 grid
    start_row = i // 3 * 3
    start_col = j // 3 * 3
    for x in range(3):
        for y in range(3):
            if puzzle[start_row + x][start_col + y] == val:
                return False
    return True

def solve_sudoku(puzzle):
    # Solve the sudoku puzzle using backtracking
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for val in range(1, 10):
                    if is_valid(puzzle, i, j, val):
                        puzzle[i][j] = val
                        if solve_sudoku(puzzle):
                            return True
                        puzzle[i][j] = 0
                return False
    return True

def create_doc(num_puzzles):
    # Create a docx file with the sudoku puzzles and solutions
    doc = docx.Document()
    for _ in range(num_puzzles):
        puzzle = generate_sudoku()
        solve_sudoku(puzzle)
        for row in puzzle:
            doc.add_row([cell for cell in row])
        doc.add_page_break()
    doc.save('sudoku.docx')

# Generate 5 sudoku puzzles
create_doc(5)
