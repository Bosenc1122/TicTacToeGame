import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Initialize Window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Board Representation
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Function to draw the grid
def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(window, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for i in range(1, BOARD_COLS):
        pygame.draw.line(window, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw the X's and O's
def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            symbol = board[row][col]
            if symbol == 'X':
                draw_x(row, col)
            elif symbol == 'O':
                draw_o(row, col)

# Function to draw X
def draw_x(row, col):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    offset = SQUARE_SIZE // 4

    pygame.draw.line(window, BLACK, (x - offset, y - offset), (x + offset, y + offset), LINE_WIDTH)
    pygame.draw.line(window, BLACK, (x + offset, y - offset), (x - offset, y + offset), LINE_WIDTH)

# Function to draw O
def draw_o(row, col):
    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 4

    pygame.draw.circle(window, BLACK, (x, y), radius, LINE_WIDTH)

# Function to check if a player has won
def check_winner(symbol):
    # Check rows
    for row in range(BOARD_ROWS):
        if all(board[row][col] == symbol for col in range(BOARD_COLS)):
            return True
    # Check columns
    for col in range(BOARD_COLS):
        if all(board[row][col] == symbol for row in range(BOARD_ROWS)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(BOARD_ROWS)) or \
       all(board[i][BOARD_COLS - i - 1] == symbol for i in range(BOARD_ROWS)):
        return True
    return False

# Function to check if the board is full
def board_full():
    return all(board[row][col] != '' for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

# Main function
def main():
    current_player = 'X'
    running = True

    while running:
        window.fill(WHITE)
        draw_grid()
        draw_symbols()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not check_winner('X') and not check_winner('O') and not board_full():
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
                if board[row][col] == '':
                    board[row][col] = current_player
                    if check_winner(current_player):
                        print(f"Player {current_player} wins!")
                    elif board_full():
                        print("It's a tie!")
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
