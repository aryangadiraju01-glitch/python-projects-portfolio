import pygame
import sys
import random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [
            Vector2(5, 10),
            Vector2(4, 10),
            Vector2(3, 10)
        ]

        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * cell_pixel_size,
                block.y * cell_pixel_size,
                cell_pixel_size,
                cell_pixel_size
            )

            pygame.draw.rect(screen, (183, 111, 122), block_rect)

    def add_block(self):
        self.new_block = True

    def move_snake(self):
        if self.new_block:
            # Keep the tail so the snake grows by one block.
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False

        else:
            # Remove the tail and add a new head.
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            self.position.x * cell_pixel_size,
            self.position.y * cell_pixel_size,
            cell_pixel_size,
            cell_pixel_size
        )

        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, number_of_cells - 1)
        self.y = random.randint(0, number_of_cells - 1)
        self.position = Vector2(self.x, self.y)


class SCORE:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 40)

    def increase(self):
        self.value += 1

    def draw_score(self):
        score_surface = self.font.render(
            f"Score: {self.value}",
            True,
            (56, 74, 12)
        )

        score_rect = score_surface.get_rect(
            topright=(
                number_of_cells * cell_pixel_size - 20,
                20
            )
        )

        screen.blit(score_surface, score_rect)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.score = SCORE()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.score.draw_score()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.score.increase()

            # Prevent fruit from appearing inside the snake.
            while self.fruit.position in self.snake.body:
                self.fruit.randomize()

    def check_fail(self):
        snake_head = self.snake.body[0]

        # Wall collision.
        if not 0 <= snake_head.x < number_of_cells:
            self.game_over()

        if not 0 <= snake_head.y < number_of_cells:
            self.game_over()

        # Self-collision.
        for block in self.snake.body[1:]:
            if block == snake_head:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()

cell_pixel_size = 40
number_of_cells = 20

screen = pygame.display.set_mode(
    (
        number_of_cells * cell_pixel_size,
        number_of_cells * cell_pixel_size
    )
)

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                # Do not move down if currently moving up.
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            elif event.key == pygame.K_UP:
                # Do not move up if currently moving down.
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)

            elif event.key == pygame.K_LEFT:
                # Do not move left if currently moving right.
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

            elif event.key == pygame.K_RIGHT:
                # Do not move right if currently moving left.
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))

    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)
