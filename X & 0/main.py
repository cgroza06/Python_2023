import pygame
import sys
import random

pygame.init()

size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4
size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tac-Toe")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
font = pygame.font.SysFont('stxingkai', 35)
game_over = False
player_score = 0
AI_score = 0
winner = None


def display_message(message_lines, color):
    screen.fill(black)

    for i, line in enumerate(message_lines):
        text = font.render(line, True, color)
        text_rect = text.get_rect(center=(width // 2, height // 3 + i * font.get_linesize()))
        screen.blit(text, text_rect)

    pygame.display.update()


def difficulty_selection():
    screen.fill(black)
    display_message(["Select Difficulty", "1. Easy", "3. Hard"], white)
    pygame.display.update()
    waiting_for_selection = True
    while waiting_for_selection:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode == '1':
                    screen.fill(black)
                    return 1
                elif event.unicode == '3':
                    screen.fill(black)
                    return 3
    screen.fill(black)
    pygame.display.update()


def check_win(matrix, sign):
    for row in matrix:
        if row.count(sign) == 3:
            return True
    for col in range(3):
        if matrix[0][col] == sign and matrix[1][col] == sign and matrix[2][col] == sign:
            return True
    if matrix[0][0] == sign and matrix[1][1] == sign and matrix[2][2] == sign:
        return True
    if matrix[0][2] == sign and matrix[1][1] == sign and matrix[2][0] == sign:
        return True
    return False


def check_draw(matrix):
    return all(cell != 0 for row in matrix for cell in row)


def computer_random_move(matrix):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if matrix[row][col] == 0]
    return random.choice(empty_cells) if empty_cells else None


def computer_best_move(matrix):
    # Verifica daca AI-ul castiga in urmatoarea miscare
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == 0:
                matrix[row][col] = 'O'
                if check_win(matrix, 'O'):
                    return row, col
                else:
                    matrix[row][col] = 0

    # Verifica daca jucatorul castiga in urmatoarea miscare
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == 0:
                matrix[row][col] = 'X'
                if check_win(matrix, 'X'):
                    matrix[row][col] = 'O'
                    return row, col
                else:
                    matrix[row][col] = 0

    # Verifica daca poate ocupa unul din colturi
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    empty_corners = [(row, col) for row, col in corners if matrix[row][col] == 0]
    if empty_corners:
        return random.choice(empty_corners)

    # Verifaca daca poate ocupa centrul
    if matrix[1][1] == 0:
        return 1, 1

    # Ia orice colt
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    empty_edges = [(row, col) for row, col in edges if matrix[row][col] == 0]
    if empty_edges:
        return random.choice(empty_edges)


def computer_move(matrix):
    if difficulty_level == 1:
        return computer_random_move(matrix)
    elif difficulty_level == 3:
        return computer_best_move(matrix)


def reset_game():
    return [[0] * 3 for _ in range(3)]


def draw_board():
    for row in range(3):
        for col in range(3):
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, white, (x, y, size_block, size_block))
            if matrix[row][col] == 'X':
                pygame.draw.line(screen, red, (x + 20, y + 20), (size_block - 20 + x, size_block - 20 + y), 3)
                pygame.draw.line(screen, red, (x + size_block - 20, y + 20), (x + 20, size_block - 20 + y), 3)
            elif matrix[row][col] == 'O':
                pygame.draw.circle(screen, green, (x + size_block // 2, y + size_block // 2), size_block // 3 - 4, 3)


difficulty_level = difficulty_selection()
pygame.display.set_caption(f"Tic-Tac-Toe (Difficulty: {difficulty_level})")

matrix = reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if matrix[row][col] == 0:
                matrix[row][col] = 'X'
                if check_win(matrix, 'X'):
                    winner = "You win"
                    player_score += 1
                    game_over = True
                else:
                    computer_move_result = computer_move(matrix)
                    if computer_move_result:
                        computer_row, computer_col = computer_move_result
                        matrix[computer_row][computer_col] = 'O'
                        if check_win(matrix, 'O'):
                            winner = "AI wins"
                            AI_score += 1
                            game_over = True
                    if check_draw(matrix):
                        winner = "Draw"
                        game_over = True

    draw_board()

    if game_over:
        screen.fill(black)
        display_message(
            [f"{winner}!", f"YOU: {player_score}", f"AI: {AI_score}", "", "Do you want to play again?", "(Y/N)"],
            white)

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.lower() == 'y':
                        matrix = reset_game()
                        game_over = False
                        waiting_for_input = False
                        winner = None
                        screen.fill(black)
                    elif event.unicode.lower() == 'n':
                        pygame.quit()
                        sys.exit()

    pygame.display.update()
