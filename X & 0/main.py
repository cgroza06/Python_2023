import pygame
import sys


def ckeck_win(matrix, sign):
    zeros = 0
    for row in matrix:
        zeros += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if matrix[0][col] == sign and matrix[1][col] == sign and matrix[2][col] == sign:
            return sign
    if matrix[0][0] == sign and matrix[1][1] == sign and matrix[2][2] == sign:
        return sign
    if matrix[0][2] == sign and matrix[1][1] == sign and matrix[2][0] == sign:
        return sign
    if zeros == 0:
        return 'Piece'
    return False


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
matrix = [[0] * 3 for i in range(3)]
query = 0
game_over = False

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
                if query % 2 == 0:
                    matrix[row][col] = 'x'
                else:
                    matrix[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            query = 0
            matrix = [[0] * 3 for i in range(3)]
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if matrix[row][col] == 'x':
                    color = red
                elif matrix[row][col] == 'o':
                    color = green
                else:
                    color = white

                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 20, y + 20), (size_block - 20 + x, size_block - 20 + y), 3)
                    pygame.draw.line(screen, white, (x + size_block - 20, y + 20), (x + 20, size_block - 20 + y), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 3 - 4,
                                       3)
        if (query - 1) % 2 == 0:
            game_over = ckeck_win(matrix, 'x')
        else:
            game_over = ckeck_win(matrix, 'o')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('stxingkai', 80)
            if game_over == 'x':
                text = font.render("X wins", True, red)
            elif game_over == 'o':
                text = font.render("O wins", True, green)
            else:
                text = font.render("Draw", True, white)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])

    pygame.display.update()