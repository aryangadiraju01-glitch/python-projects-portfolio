# Python Pong Game

A two-player Pong game built with Python's built-in `turtle` graphics module.

This project uses object-oriented programming to organize the paddles, ball, and scoreboard into separate classes while keeping the entire game inside one `main.py` file.

## Features

- Two-player keyboard controls
- Paddle and wall collision detection
- Score tracking
- Ball reset after a player scores
- Increasing ball speed after paddle collisions
- Object-oriented structure
- No external packages required

## Controls

### Left Player

- `W` — Move up
- `S` — Move down

### Right Player

- `Up Arrow` — Move up
- `Down Arrow` — Move down

## Project Structure

```text
Python-Pong-Game/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

All classes are located inside `main.py`:

- `Paddle`
- `Ball`
- `Scoreboard`

## How the Game Works

### Paddle Class

The `Paddle` class creates a paddle at a supplied x and y position. Each paddle stores its current position and contains methods for moving up and down.

### Ball Class

The `Ball` class controls the ball's position, movement direction, speed, wall bouncing, paddle bouncing, and reset behavior.

The ball moves by adding `x_move` and `y_move` to its current coordinates during every loop iteration.

### Scoreboard Class

The `Scoreboard` class stores the scores for the left and right players. It clears and redraws the scoreboard whenever either player earns a point.

### Main Game Loop

The game loop repeatedly:

1. Pauses based on the current ball speed.
2. Updates the screen.
3. Moves the ball.
4. Checks for wall collisions.
5. Checks for paddle collisions.
6. Checks whether a player missed the ball.
7. Updates the score and resets the ball when necessary.

## Running the Project

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal inside the project folder.
4. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Requirements

This project only uses Python standard-library modules:

- `turtle`
- `time`

No `pip install` command is required.

## Concepts Practiced

- Classes and objects
- Constructors
- Instance attributes
- Instance methods
- Object interaction
- Event listeners
- Collision detection
- Game loops
- Coordinate systems
