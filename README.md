# Snake Game in Python 🐍

This is a simple implementation of the classic **Snake** game, created using Python and the `uib_inf100_graphics` library for handling graphical output. The game allows you to control a snake, collect apples, and grow in size while avoiding collisions with walls or your own body.

## Features ✨

- **Multiple Levels:** Choose between three levels: Small, Normal, and Large.
- **Snake Growth:** Each apple you collect will increase the snake's size, and your score will increase as well.
- **Game Over:** If the snake hits a wall or its own body, the game ends, and you can restart.
- **Debug Mode:** Toggle the debug mode to display the snake's position, size, and direction.
- **Keyboard Controls:**
  - 🡺 `W` to move up
  - 🡻 `S` to move down
  - 🡸 `A` to move left
  - 🡷 `D` to move right
  - 🔘 `Space` to start the game or toggle debug mode
  - ⏎ `Enter` to restart the game after game over
  - 🔢 `1`, `2`, `3` to select the level

## Game Instructions 🎮

### Starting the Game 🏁

Press `Space` to begin playing the game.

### Select a Level 🌟

You will be presented with a menu to choose a level:
- Press `1` for the **Small** level
- Press `2` for the **Normal** level
- Press `3` for the **Large** level

### Gameplay 🎯

- The snake starts at a predefined position on the board. Your goal is to collect apples, which will cause the snake to grow.
- Use the arrow keys (`W`, `S`, `A`, `D`) to control the snake's movement.

### Game Over 💥

The game ends if the snake collides with a wall or its own body. You can restart by pressing `Enter`.

### Debug Mode 🛠️

You can toggle the debug mode by pressing `Q`. When enabled, the current position, size, and direction of the snake will be displayed on the screen.

---

## How to Play 📝

- **Start the game** by pressing the `Space` key.
- **Navigate the snake** using the `W`, `S`, `A`, and `D` keys.
- **Collect apples** (represented by `-1` on the board) to increase the snake's size and score.
- **Avoid hitting walls or the snake’s own body.** If you do, the game will end. You can restart by pressing `Enter`.

---

## Acknowledgments 🙏

- This game uses the `uib_inf100_graphics` library for graphical rendering.
- The Snake game is a classic game originally created by **Gremlin Interactive** and released in **1976**.
