# Flappy Bird Game

Welcome to the Flappy Bird game built with Pygame! This README will guide you through the key aspects of the project.

## Features

- **Smooth Gameplay**: Enjoy a seamless gaming experience with smooth animations and controls.
- **Realistic Physics**: Experience realistic bird movements and collisions.
- **Scoring System**: Keep track of your score as you navigate through the pipes.
- **Sound Effects**: Engaging sound effects to enhance the gameplay experience.
- **Attractive Graphics**: High-quality sprites for the bird, background, pipes, and base.

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/My_Projects.git
    cd My_Projects
    ```

2. **Install Pygame**:
    ```bash
    pip install pygame
    ```

3. **Run the game**:
    ```bash
    python flappy_bird.py
    ```

## How to Play

- **Start the Game**: Press the spacebar or the up arrow key to start the game.
- **Control the Bird**: Use the spacebar or the up arrow key to flap the bird's wings and navigate through the pipes.
- **Avoid Collisions**: Avoid hitting the pipes and the ground to keep the bird flying.
- **Score Points**: Pass through the pipes to score points.

## Code Overview

- **Global Variables**: Constants for screen dimensions, game sprites, and sounds.
- **welcomeScreen()**: Displays the welcome screen with the game logo and instructions.
- **mainGame()**: Core game loop handling bird movement, pipe generation, collision detection, and scoring.
- **isCollide()**: Checks for collisions between the bird and pipes or ground.
- **getRandomPipe()**: Generates random positions for the upper and lower pipes.

## Game Assets

- **Sprites**: Located in the `gallery/sprites` directory (bird, background, pipes, base, and numbers).
- **Sounds**: Located in the `gallery/audio` directory (wing, hit, point, die, and swoosh).

## Credits

- **Developer**: S.Prabha
- **Inspiration**: Classic Flappy Bird game

Enjoy playing Flappy Bird! Feel free to contribute and improve the game.
