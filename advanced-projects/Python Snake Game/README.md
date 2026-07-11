# Pygame Snake Game

A classic Snake game built with Python and Pygame.

The player controls a continuously moving snake, collects fruit, earns points, and loses when the snake hits a wall or its own body.

This project was created to practice:

- Python object-oriented programming
- Classes and objects
- Constructors
- Instance attributes
- Instance methods
- Lists and list slicing
- Loops and conditionals
- Pygame graphics
- Pygame events
- Keyboard input
- Collision detection
- Timed game updates
- Two-dimensional coordinates
- Basic game-state management

---

## Table of Contents

1. [Project Preview](#project-preview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Running the Game](#running-the-game)
6. [Controls](#controls)
7. [How the Game Works](#how-the-game-works)
8. [Detailed Code Explanation](#detailed-code-explanation)
9. [Important Python Syntax](#important-python-syntax)
10. [Important Pygame Concepts](#important-pygame-concepts)
11. [Possible Improvements](#possible-improvements)
12. [What I Learned](#what-i-learned)

---

## Project Preview

The game window is divided into a grid.

Each grid square is 40 pixels wide and 40 pixels tall. The board contains 20 rows and 20 columns, producing an 800-by-800-pixel game window.

The snake and fruit are stored using grid coordinates rather than raw pixel coordinates.

For example:

```python
Vector2(5, 10)
```

means:

- Column 5
- Row 10

When the object is drawn, those grid coordinates are multiplied by the size of one cell:

```python
block.x * cell_pixel_size
block.y * cell_pixel_size
```

Therefore, the grid position `(5, 10)` becomes the pixel position `(200, 400)` when each cell is 40 pixels wide.

---

## Features

- Snake movement on a grid
- Arrow-key controls
- Prevention of immediate 180-degree turns
- Random fruit placement
- Snake growth after eating fruit
- Score tracking
- Wall-collision detection
- Self-collision detection
- Fruit-placement protection so fruit does not spawn inside the snake
- Object-oriented project structure

---

## Project Structure

```text
pygame-snake-game/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `main.py`

Contains the full game, including:

- Snake class
- Fruit class
- Score class
- Main game-controller class
- Pygame setup
- Event loop
- Drawing loop

### `README.md`

Explains the project, installation process, game logic, Python syntax, and Pygame concepts.

### `requirements.txt`

Lists the external Python packages required to run the project.

### `.gitignore`

Prevents unnecessary files such as virtual environments, cache folders, and IDE settings from being uploaded to GitHub.

---

## Installation

### 1. Install Python

Install Python 3 from the official Python website.

Confirm that Python is installed:

```bash
python --version
```

On some computers, the command may be:

```bash
py --version
```

### 2. Download or clone this repository

Using Git:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project folder:

```bash
cd pygame-snake-game
```

### 3. Create a virtual environment

Windows:

```bash
py -m venv .venv
```

Activate it in Command Prompt:

```bash
.venv\Scripts\activate
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install the required package

```bash
pip install -r requirements.txt
```

---

## Running the Game

Run:

```bash
python main.py
```

On Windows, this may also work:

```bash
py main.py
```

---

## Controls

| Key | Action |
|---|---|
| Up Arrow | Move upward |
| Down Arrow | Move downward |
| Left Arrow | Move left |
| Right Arrow | Move right |
| Close Window | Exit the game |

The program prevents the snake from instantly reversing direction.

For example, the snake cannot move directly left while it is currently moving right because that would cause the head to immediately collide with the second segment.

---

# How the Game Works

The project uses four classes:

```python
SNAKE
FRUIT
SCORE
MAIN
```

Each class has one main responsibility.

- `SNAKE` stores, moves, grows, and draws the snake.
- `FRUIT` stores, randomizes, and draws the fruit.
- `SCORE` stores and displays the score.
- `MAIN` connects the other objects and controls the game rules.

This is an example of separation of responsibilities. Instead of placing all code inside one large loop, related behavior is grouped into classes.

---

# Detailed Code Explanation

## Imports

```python
import pygame
import sys
import random
from pygame.math import Vector2
```

### `import pygame`

Imports the Pygame library.

Pygame provides tools for:

- Creating a game window
- Drawing shapes
- Reading keyboard input
- Handling events
- Managing time
- Rendering text

### `import sys`

Imports Python's built-in `sys` module.

This project uses:

```python
sys.exit()
```

to completely stop the Python program.

### `import random`

Imports Python's random-number tools.

The game uses:

```python
random.randint()
```

to choose random grid coordinates for the fruit.

### `from pygame.math import Vector2`

Imports Pygame's two-dimensional vector class.

A `Vector2` object stores an `x` value and a `y` value.

Example:

```python
Vector2(5, 10)
```

represents the coordinate:

```text
x = 5
y = 10
```

Vectors are useful because they can be added together:

```python
Vector2(5, 10) + Vector2(1, 0)
```

produces:

```python
Vector2(6, 10)
```

This makes snake movement easier to calculate.

---

# The `SNAKE` Class

```python
class SNAKE:
```

The `class` keyword creates a class.

A class is a blueprint that defines the data and behavior its objects will have.

Later, the program creates a snake object with:

```python
self.snake = SNAKE()
```

The parentheses call the class constructor.

---

## Snake Constructor

```python
def __init__(self):
```

`__init__` is the constructor method.

It runs automatically whenever a new object is created from the class.

`self` refers to the specific object being created or used.

For example:

```python
self.body
```

means the `body` attribute belonging to this particular snake object.

---

## Snake Body

```python
self.body = [
    Vector2(5, 10),
    Vector2(4, 10),
    Vector2(3, 10)
]
```

The snake body is stored as a list of `Vector2` objects.

Each vector represents one snake segment.

The first item is the head:

```python
self.body[0]
```

The remaining items are body segments.

Initial positions:

```text
Head:       (5, 10)
Second:     (4, 10)
Tail:       (3, 10)
```

Because the coordinates move from left to right, the snake starts facing right.

### List indexing

```python
self.body[0]
```

returns the first item.

```python
self.body[1]
```

returns the second item.

Python list indexes begin at zero.

---

## Snake Direction

```python
self.direction = Vector2(1, 0)
```

The direction vector controls how the head position changes.

```text
Vector2(1, 0)   = move right
Vector2(-1, 0)  = move left
Vector2(0, -1)  = move up
Vector2(0, 1)   = move down
```

Pygame's coordinate system begins in the top-left corner.

Therefore:

- Increasing `x` moves right.
- Decreasing `x` moves left.
- Increasing `y` moves down.
- Decreasing `y` moves up.

---

## Growth Flag

```python
self.new_block = False
```

This Boolean variable records whether the snake should grow during its next movement.

A Boolean can contain:

```python
True
False
```

When the snake eats fruit, this value becomes `True`.

During the next move, the tail is kept instead of removed, causing the snake to become one segment longer.

---

## Drawing the Snake

```python
def draw_snake(self):
```

This method draws every body segment.

```python
for block in self.body:
```

The `for` loop visits each vector in the snake's body list.

During each iteration, `block` refers to one body segment.

---

### Creating a Rectangle

```python
block_rect = pygame.Rect(
    block.x * cell_pixel_size,
    block.y * cell_pixel_size,
    cell_pixel_size,
    cell_pixel_size
)
```

`pygame.Rect()` creates a rectangle.

Its four values represent:

```python
pygame.Rect(x_position, y_position, width, height)
```

The snake coordinates are grid coordinates, so they are multiplied by the cell size.

For a block at:

```python
Vector2(5, 10)
```

the pixel location becomes:

```text
x = 5 × 40 = 200
y = 10 × 40 = 400
```

The width and height are both 40 pixels.

---

### Drawing the Rectangle

```python
pygame.draw.rect(screen, (183, 111, 122), block_rect)
```

This draws a filled rectangle.

Arguments:

1. `screen` — the surface on which the rectangle is drawn
2. `(183, 111, 122)` — the RGB color
3. `block_rect` — the rectangle's position and dimensions

RGB means red, green, and blue.

Each value normally ranges from 0 to 255.

---

## Adding a Block

```python
def add_block(self):
    self.new_block = True
```

This method does not immediately modify the body list.

Instead, it sets the growth flag.

The next time `move_snake()` runs, the method notices the flag and keeps the tail.

---

## Moving the Snake

```python
def move_snake(self):
```

The snake moves by:

1. Creating a copy of its body
2. Calculating a new head
3. Inserting that head at index `0`
4. Usually removing the old tail

---

### Movement While Growing

```python
if self.new_block:
```

This is equivalent to:

```python
if self.new_block == True:
```

The shorter form is considered more natural Python syntax.

```python
body_copy = self.body[:]
```

`[:]` creates a shallow copy of the full list.

The original tail is kept.

```python
body_copy.insert(0, body_copy[0] + self.direction)
```

This line:

1. Gets the current head with `body_copy[0]`
2. Adds the direction vector
3. Inserts the new coordinate at index `0`

Example:

```text
Current head: (5, 10)
Direction:    (1, 0)
New head:     (6, 10)
```

```python
self.body = body_copy
```

Replaces the old body list with the updated list.

```python
self.new_block = False
```

Resets the flag so the snake does not continue growing every frame.

---

### Normal Movement

```python
else:
    body_copy = self.body[:-1]
```

`[:-1]` copies every list element except the final one.

The final element is the tail.

Removing the tail prevents the snake from becoming longer during normal movement.

Suppose the body is:

```python
[(5, 10), (4, 10), (3, 10)]
```

The slice:

```python
self.body[:-1]
```

produces:

```python
[(5, 10), (4, 10)]
```

A new head is inserted:

```python
body_copy.insert(0, body_copy[0] + self.direction)
```

The result becomes:

```python
[(6, 10), (5, 10), (4, 10)]
```

The snake appears to have moved right by one cell.

---

# The `FRUIT` Class

```python
class FRUIT:
```

This class controls the fruit's position and appearance.

---

## Fruit Constructor

```python
def __init__(self):
    self.randomize()
```

When a fruit object is created, the constructor immediately calls `randomize()`.

This ensures the fruit receives a random starting position.

---

## Drawing the Fruit

```python
fruit_rect = pygame.Rect(
    self.position.x * cell_pixel_size,
    self.position.y * cell_pixel_size,
    cell_pixel_size,
    cell_pixel_size
)
```

This converts the fruit's grid coordinate into a pixel rectangle.

```python
pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
```

This draws the fruit rectangle onto the screen.

---

## Randomizing the Fruit

```python
self.x = random.randint(0, number_of_cells - 1)
self.y = random.randint(0, number_of_cells - 1)
```

`random.randint(a, b)` returns a random integer between `a` and `b`, including both endpoints.

Because the board has 20 cells, valid coordinates are:

```text
0 through 19
```

That is why the maximum is:

```python
number_of_cells - 1
```

Then the two values are combined:

```python
self.position = Vector2(self.x, self.y)
```

---

# The `SCORE` Class

```python
class SCORE:
```

This class stores the current score and draws it on the screen.

---

## Score Constructor

```python
self.value = 0
```

The score begins at zero.

```python
self.font = pygame.font.Font(None, 40)
```

Creates a Pygame font object.

Arguments:

1. `None` — use Pygame's default font
2. `40` — font size

---

## Increasing the Score

```python
def increase(self):
    self.value += 1
```

`+= 1` adds one to the existing value.

It is equivalent to:

```python
self.value = self.value + 1
```

---

## Rendering the Score

```python
score_surface = self.font.render(
    f"Score: {self.value}",
    True,
    (56, 74, 12)
)
```

The `render()` method converts text into a drawable Pygame surface.

Arguments:

1. The text
2. Whether anti-aliasing is enabled
3. The text color

The text uses an f-string:

```python
f"Score: {self.value}"
```

An f-string allows variables or expressions to be placed inside braces.

If `self.value` is `3`, the result is:

```text
Score: 3
```

---

## Positioning the Score

```python
score_rect = score_surface.get_rect(
    topright=(
        number_of_cells * cell_pixel_size - 20,
        20
    )
)
```

Every Pygame surface can create a rectangle matching its size using `get_rect()`.

The `topright` argument positions the top-right corner of that rectangle.

The x-coordinate is:

```python
number_of_cells * cell_pixel_size - 20
```

The full window width is:

```text
20 × 40 = 800 pixels
```

Subtracting 20 creates a 20-pixel margin from the right edge.

The y-coordinate is `20`, creating a 20-pixel margin from the top.

```python
screen.blit(score_surface, score_rect)
```

`blit()` places one surface onto another.

It places the rendered score surface onto the main screen.

---

# The `MAIN` Class

```python
class MAIN:
```

This class acts as the game controller.

It owns the snake, fruit, and score objects and handles the interactions between them.

---

## Main Constructor

```python
self.snake = SNAKE()
self.fruit = FRUIT()
self.score = SCORE()
```

These lines create one object from each class.

This relationship can be described as composition:

- The main game has a snake.
- The main game has a fruit.
- The main game has a score.

---

## Updating the Game

```python
def update(self):
    self.snake.move_snake()
    self.check_collision()
    self.check_fail()
```

This method performs one logical game update.

The order is important:

1. Move the snake
2. Check whether it ate the fruit
3. Check whether it hit a wall or itself

---

## Drawing All Elements

```python
def draw_elements(self):
    self.fruit.draw_fruit()
    self.snake.draw_snake()
    self.score.draw_score()
```

This method tells each object to draw itself.

The `MAIN` class does not need to know every drawing detail. Each individual class handles its own drawing behavior.

---

## Fruit Collision

```python
if self.fruit.position == self.snake.body[0]:
```

The fruit is eaten when its coordinate equals the snake head's coordinate.

Remember:

```python
self.snake.body[0]
```

is the head.

When a collision occurs:

```python
self.fruit.randomize()
self.snake.add_block()
self.score.increase()
```

The game:

1. Moves the fruit
2. Tells the snake to grow
3. Adds one point

---

## Preventing Fruit from Spawning Inside the Snake

```python
while self.fruit.position in self.snake.body:
    self.fruit.randomize()
```

The `in` operator checks whether a value exists inside a collection.

This loop means:

> While the fruit coordinate is one of the snake's body coordinates, generate another coordinate.

A `while` loop continues as long as its condition remains true.

---

## Failure Detection

```python
snake_head = self.snake.body[0]
```

Stores the head coordinate in a local variable.

This avoids repeatedly writing the longer expression.

---

### Wall Collision

```python
if not 0 <= snake_head.x < number_of_cells:
    self.game_over()
```

Python allows chained comparisons.

```python
0 <= snake_head.x < number_of_cells
```

means:

```python
0 <= snake_head.x and snake_head.x < number_of_cells
```

The `not` operator reverses the Boolean result.

Therefore, game over occurs when the x-coordinate is outside the valid range.

The same logic checks the y-coordinate:

```python
if not 0 <= snake_head.y < number_of_cells:
    self.game_over()
```

---

### Self-Collision

```python
for block in self.snake.body[1:]:
```

The slice `[1:]` returns every segment except the head.

The code compares each body segment with the head:

```python
if block == snake_head:
    self.game_over()
```

If any body segment occupies the same coordinate as the head, the snake collided with itself.

---

## Ending the Game

```python
pygame.quit()
sys.exit()
```

`pygame.quit()` shuts down Pygame's initialized modules.

`sys.exit()` stops the Python program.

Using both ensures that the window and process close cleanly.

---

# Pygame Setup

## Initialize Pygame

```python
pygame.init()
```

Initializes Pygame's modules.

This should run before creating the window or using Pygame fonts.

---

## Grid Constants

```python
cell_pixel_size = 40
number_of_cells = 20
```

The game uses:

- 40 pixels per grid cell
- 20 cells per row and column

Window size:

```text
40 × 20 = 800 pixels
```

---

## Creating the Window

```python
screen = pygame.display.set_mode(
    (
        number_of_cells * cell_pixel_size,
        number_of_cells * cell_pixel_size
    )
)
```

`set_mode()` creates the game window.

The window dimensions are passed as a tuple:

```python
(width, height)
```

The resulting window is 800 by 800 pixels.

---

## Window Caption

```python
pygame.display.set_caption("Snake Game")
```

Sets the title displayed on the window.

---

## Clock Object

```python
clock = pygame.time.Clock()
```

Creates a clock used to control the maximum frame rate.

Later:

```python
clock.tick(60)
```

limits the drawing loop to approximately 60 frames per second.

---

# Timed Snake Movement

```python
SCREEN_UPDATE = pygame.USEREVENT
```

Pygame includes a range of event values reserved for custom events.

This line creates a custom event identifier.

```python
pygame.time.set_timer(SCREEN_UPDATE, 150)
```

This asks Pygame to place a `SCREEN_UPDATE` event into the event queue every 150 milliseconds.

Because there are 1,000 milliseconds in one second, the snake moves approximately:

```text
1000 ÷ 150 = 6.67 times per second
```

The drawing loop still runs up to 60 times per second, but the snake only changes grid position when the timer event occurs.

This separation makes movement consistent.

---

# Creating the Main Game Object

```python
main_game = MAIN()
```

Creates the central game-controller object.

Its constructor automatically creates the snake, fruit, and score objects.

---

# The Main Game Loop

```python
while True:
```

This creates an infinite loop.

The game continues running until `sys.exit()` stops the program.

Each loop performs three broad jobs:

1. Process events
2. Draw the current game state
3. Update the visible display

---

# Event Processing

```python
for event in pygame.event.get():
```

Pygame stores events in an event queue.

`pygame.event.get()` retrieves the pending events.

Examples include:

- Closing the window
- Pressing a key
- Custom timer events

The loop handles each event one at a time.

---

## Closing the Window

```python
if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()
```

When the user clicks the window's close button, Pygame creates a `QUIT` event.

The program then closes cleanly.

---

## Moving on Timer Events

```python
if event.type == SCREEN_UPDATE:
    main_game.update()
```

Every 150 milliseconds, the custom timer event triggers one game update.

That causes the snake to move and collision checks to run.

---

# Keyboard Input

```python
if event.type == pygame.KEYDOWN:
```

A `KEYDOWN` event occurs when a keyboard key is pressed.

The program then checks which key was pressed.

---

## Down Arrow

```python
if event.key == pygame.K_DOWN:
```

Checks whether the pressed key was the down arrow.

```python
if main_game.snake.direction.y != -1:
```

A y-direction of `-1` means the snake is moving upward.

The snake is only allowed to move down when it is not already moving up.

```python
main_game.snake.direction = Vector2(0, 1)
```

Sets the direction to downward movement.

---

## Up Arrow

```python
elif event.key == pygame.K_UP:
```

`elif` means "else if."

This condition is only checked if the earlier key condition was false.

```python
if main_game.snake.direction.y != 1:
```

A y-direction of `1` means the snake is moving down.

The direction changes to up only when the snake is not moving down.

---

## Left Arrow

```python
if main_game.snake.direction.x != 1:
```

An x-direction of `1` means the snake is moving right.

The direction changes to left only if it is not moving right.

---

## Right Arrow

```python
if main_game.snake.direction.x != -1:
```

An x-direction of `-1` means the snake is moving left.

The direction changes to right only if it is not moving left.

---

# Drawing Each Frame

## Clear the Previous Frame

```python
screen.fill((175, 215, 70))
```

Fills the entire window with the background color.

This clears the old snake and fruit drawings before the new frame is drawn.

Without clearing the screen, old positions would remain visible and create trails.

---

## Draw Current Objects

```python
main_game.draw_elements()
```

Draws the fruit, snake, and score based on their current state.

---

## Display the New Frame

```python
pygame.display.update()
```

Updates the visible window with everything drawn during the current loop.

Drawing commands modify the screen surface in memory. `pygame.display.update()` makes those changes visible.

---

## Limit the Frame Rate

```python
clock.tick(60)
```

Limits the loop to approximately 60 iterations per second.

This reduces unnecessary CPU usage and creates a stable rendering rate.

---

# Important Python Syntax

## Dot Notation

```python
main_game.snake.direction
```

Dot notation accesses data or behavior belonging to an object.

This expression means:

1. Access the `main_game` object
2. Access its `snake` object
3. Access that snake object's `direction` attribute

---

## Method Calls

```python
self.fruit.randomize()
```

The parentheses call a method.

Without parentheses:

```python
self.fruit.randomize
```

Python refers to the method itself but does not execute it.

---

## Assignment

```python
self.value = 0
```

The assignment operator stores the value on the right inside the variable or attribute on the left.

---

## Equality Comparison

```python
self.fruit.position == self.snake.body[0]
```

`==` compares two values.

It does not assign a value.

Difference:

```python
=   assignment
==  comparison
```

---

## Membership Operator

```python
self.fruit.position in self.snake.body
```

Checks whether the fruit coordinate exists in the body list.

---

## List Slicing

```python
self.body[:]
```

Copies the entire list.

```python
self.body[:-1]
```

Copies everything except the final item.

```python
self.body[1:]
```

Copies everything except the first item.

---

## Boolean Negation

```python
not 0 <= snake_head.x < number_of_cells
```

`not` reverses a Boolean value.

```text
not True  -> False
not False -> True
```

---

## Local Variables and Instance Attributes

Local variable:

```python
snake_head = self.snake.body[0]
```

This variable exists only inside the method.

Instance attribute:

```python
self.value = 0
```

This belongs to an object and can be accessed by other methods through `self`.

---

# Important Pygame Concepts

## Surfaces

A surface is an image-like area that can be drawn on.

The main display surface is:

```python
screen
```

Rendered text is also stored as a surface:

```python
score_surface
```

---

## Rectangles

A `pygame.Rect` stores:

- Position
- Width
- Height

It is frequently used for drawing and collision detection.

---

## Events

Events represent things that happen during the program.

Examples:

```python
pygame.QUIT
pygame.KEYDOWN
SCREEN_UPDATE
```

---

## Rendering Versus Updating Logic

The project separates:

- Logical updates
- Visual rendering

Logical update:

```python
main_game.update()
```

Rendering:

```python
main_game.draw_elements()
pygame.display.update()
```

This is a standard game-development pattern.

---

# Object-Oriented Programming Concepts Used

## Class

A blueprint for creating objects.

Example:

```python
class SNAKE:
```

## Object

A specific instance of a class.

Example:

```python
self.snake = SNAKE()
```

## Constructor

The method that initializes an object.

Example:

```python
def __init__(self):
```

## Attribute

Data stored inside an object.

Examples:

```python
self.body
self.direction
self.value
```

## Method

A function defined inside a class.

Examples:

```python
move_snake()
draw_fruit()
increase()
```

## Encapsulation

Each class groups related data and behavior.

For example, the `SCORE` class stores both:

- The score value
- The logic used to render that value

## Composition

The `MAIN` object contains objects of other classes.

```python
self.snake = SNAKE()
self.fruit = FRUIT()
self.score = SCORE()
```

---

# Possible Improvements

Future versions could include:

- A restart screen instead of immediately closing
- A visible game-over message
- A high-score system
- Sound effects
- Background music
- Snake-head and tail graphics
- Rounded snake segments
- Difficulty levels
- Increasing speed as the score grows
- A pause feature
- A start menu
- Saving scores to a file
- Unit tests for movement and collision logic
- PEP 8 class names such as `Snake`, `Fruit`, `Score`, and `Game`
- Moving constants into a settings section
- Separating classes into multiple Python files

---

# What I Learned

This project demonstrates how a game can be divided into smaller systems rather than written as one large block of code.

Key lessons include:

- Representing game objects with classes
- Using vectors for position and direction
- Moving a multi-segment object using list slicing
- Converting grid coordinates into pixels
- Processing Pygame events
- Preventing invalid direction changes
- Detecting collisions using coordinates
- Separating game logic from rendering
- Managing relationships between multiple objects

---

## Requirements

- Python 3
- Pygame

Install Pygame manually with:

```bash
pip install pygame
```

---

## Author

Created by Aryan Gadiraju as a Python and object-oriented programming practice project.
