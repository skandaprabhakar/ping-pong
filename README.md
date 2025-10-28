# 🏓 Ping Pong Game (Python + Pygame)

A classic **Ping Pong / Pong** clone built by **Skanda Prabhakar** using **Python and Pygame**, featuring:

* ⚡ Smooth ball and paddle movement
* 🧠 AI opponent
* 💥 Realistic collision and bounce physics
* 🎵 Sound effects for hits, wall bounces, and scoring
* 🏁 Game-over screen and replay menu (Best of 3 / 5 / 7)

---

## 🎮 Gameplay

Two paddles face off:

* **Left Paddle (Player):** Move using `W` (up) and `S` (down)
* **Right Paddle (AI):** Automatically tracks the ball

Score a point when the ball passes your opponent’s paddle.
The first player to reach the **target score** wins the match.

After a match ends, you can replay or exit using the on-screen options.

---

## 🧩 Repository Structure

```
ping-pong/
│
├── main.py               # Main entry point, handles game loop and replay logic
├── nall.py               # Ball movement, collision detection, and scoring
├── paddle.py             # Player and AI paddle behavior
├── game_engin.py         # Rendering, text, and game-over display
│
├── paddle_hit.wav        # (Optional) Sound: paddle hit
├── wall_bounce.wav       # (Optional) Sound: wall bounce
├── score.wav             # (Optional) Sound: scoring
│
└── README.md             # Project documentation
```

> 💡 You can rename `nall.py` → `ball.py` and `game_engin.py` → `game_engine.py` if you prefer — just update the imports in `main.py`.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/skandaprabhakar/ping-pong.git
cd ping-pong
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install pygame
```

### 4. Add sound files *(optional)*

Place these `.wav` files in the same folder as `main.py`:

* `paddle_hit.wav`
* `wall_bounce.wav`
* `score.wav`

If they’re missing, the game will still run — sounds will just be skipped.

---

## ▶️ Running the Game

```bash
python main.py
```

---

## 🔁 Replay Menu

After a player wins (reaches the target score):

| Key   | Mode      | Meaning           |
| ----- | --------- | ----------------- |
| `3`   | Best of 3 | First to 2 points |
| `5`   | Best of 5 | First to 3 points |
| `7`   | Best of 7 | First to 4 points |
| `ESC` | Exit      | Close the game    |

---

## 🔊 Sound Effects

| Event       | File              | Description                    |
| ----------- | ----------------- | ------------------------------ |
| Paddle hit  | `paddle_hit.wav`  | When ball hits paddle          |
| Wall bounce | `wall_bounce.wav` | When ball hits top/bottom wall |
| Score       | `score.wav`       | When a player scores           |

All sounds are handled by `pygame.mixer.Sound()` and played automatically during gameplay.

---

## 🧠 Code Overview

* **`Ball` (`nall.py`)** – Handles movement, wall/paddle collisions, and scoring.
* **`Paddle` (`paddle.py`)** – Manages player input and AI tracking.
* **`Game Engine` (`game_engin.py`)** – Handles drawing text, scores, and game-over screens.
* **`Main` (`main.py`)** – Initializes Pygame, runs the game loop, and manages replay logic.

---

## 🛠️ Customization

You can tweak gameplay easily:

| Feature       | Where                                   | Example                                |
| ------------- | --------------------------------------- | -------------------------------------- |
| Ball speed    | `main.py` → `Ball()`                    | Change `velocity_x` and `velocity_y`   |
| AI difficulty | `main.py`                               | Adjust `right_paddle.speed`            |
| Win target    | Replay menu or `winning_score` variable | Change match length                    |
| Volume        | In `main.py`                            | `sounds["paddle_hit"].set_volume(0.5)` |

---

## 🧑‍💻 Author

**Skanda Prabhakar**
GitHub: [@skandaprabhakar](https://github.com/skandaprabhakar)

Built with ❤️ using Python and Pygame.
Feel free to fork, modify, and contribute!

---

## 📜 License

This project is open-source and available under the **MIT License**.
