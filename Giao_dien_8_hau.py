import pygame

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("8 Queens Puzzle")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Kích thước ô vuông
square_size = screen_width // 8

# Vẽ bàn cờ
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            pygame.draw.rect(screen, WHITE, [col * square_size, row * square_size, square_size, square_size])
        else:
            pygame.draw.rect(screen, BLACK, [col * square_size, row * square_size, square_size, square_size])
solution = [0, 4, 7, 5, 2, 6, 1, 3]
# Vẽ các quân hậu
for col, row in enumerate (solution):
    pygame.draw.circle(screen, RED, [col * square_size + square_size // 2, row * square_size + square_size // 2], square_size // 2 - 10)

# Hiển thị lên màn hình
pygame.display.flip()

# Vòng lặp game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Kết thúc game
pygame.quit()
