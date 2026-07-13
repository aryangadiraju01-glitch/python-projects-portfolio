from turtle import Turtle, Screen
import time


class Paddle:
    """Creates and controls a Pong paddle."""

    def __init__(self, x_pos, y_pos):
        self.width = 20
        self.height = 100
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(self.x_pos, self.y_pos)

    def move_up(self):
        """Move the paddle upward."""
        self.y_pos += 20
        self.paddle.goto(self.x_pos, self.y_pos)

    def move_down(self):
        """Move the paddle downward."""
        self.y_pos -= 20
        self.paddle.goto(self.x_pos, self.y_pos)


class Ball:
    """Creates and controls the Pong ball."""

    def __init__(self):
        self.width = 20
        self.height = 20
        self.x_pos = 0
        self.y_pos = 0
        self.x_move = 20
        self.y_move = 20
        self.ball_speed = 0.1

        self.ball = Turtle()
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.penup()

    def move_ball(self):
        """Move the ball based on its current direction."""
        self.x_pos += self.x_move
        self.y_pos += self.y_move
        self.ball.goto(self.x_pos, self.y_pos)

    def bounce_y(self):
        """Reverse the ball's vertical direction."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse the ball's horizontal direction and increase its speed."""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_pos(self):
        """Return the ball to the center after a player scores."""
        self.x_pos = 0
        self.y_pos = 0
        self.ball.goto(self.x_pos, self.y_pos)
        self.ball_speed = 0.1
        self.bounce_x()


class Scoreboard:
    """Tracks and displays the score for both players."""

    def __init__(self):
        self.board = Turtle()
        self.board.color("white")
        self.board.penup()
        self.board.hideturtle()

        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear and redraw the scores."""
        self.board.clear()

        self.board.goto(-100, 200)
        self.board.write(
            self.l_score,
            align="center",
            font=("Courier", 80, "normal"),
        )

        self.board.goto(100, 200)
        self.board.write(
            self.r_score,
            align="center",
            font=("Courier", 80, "normal"),
        )

    def l_point(self):
        """Give one point to the left player."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Give one point to the right player."""
        self.r_score += 1
        self.update_scoreboard()


# Screen setup
screen = Screen()
width = 800
height = 600

screen.setup(width=width, height=height, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Arcade Pong Game")
screen.tracer(0)

# Game objects
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
board = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

# Main game loop
game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    # Detect collision with the top or bottom wall.
    if ball.y_pos > 280 or ball.y_pos < -280:
        ball.bounce_y()

    # Detect collision with either paddle.
    hit_right_paddle = (
        ball.ball.distance(right_paddle.paddle) < 50
        and 320 < ball.x_pos < 360
    )
    hit_left_paddle = (
        ball.ball.distance(left_paddle.paddle) < 50
        and -360 < ball.x_pos < -320
    )

    if hit_right_paddle or hit_left_paddle:
        ball.bounce_x()

    # Detect when the right player misses.
    if ball.x_pos > 380:
        ball.reset_pos()
        board.l_point()

    # Detect when the left player misses.
    if ball.x_pos < -380:
        ball.reset_pos()
        board.r_point()

screen.exitonclick()
