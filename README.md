# Star Wars - Jedi vs Dark Side

A Space Invaders-style arcade game built with Python and Pygame, set in the Star Wars universe. Battle waves of Tie Fighters and a Jedi x-wing starfighter across three difficulty modes.

---

## Features

- **3 difficulty modes** — Easy, Medium, and Hard with increasing enemy rows and behaviours
- **Hard mode** — Tie Bombers fire back at the player from the front line of the fleet
- **Collision detection** — Per-pixel rect-based hit detection with explosion animations
- **Score tracking** — Score persists across rounds within a session
- **Lives system** — 3 lives with per-life respawn and game over screen
- **Replay loop** — Replay without restarting the application

---

## Project Structure

```
space_invader_app/
├── README.md                # about the app
├── main.py                  # Entry point, pygame init, asset preloading
├── config.py                # Screen dimensions, shared font config
├── screen.py                # GameScreen class, background rendering
├── start_screen.py          # Difficulty selection UI
├── game_control.py          # Main game loop, round and replay logic
├── jedi.py                  # Player starfighter — movement, shooting, rendering
├── dark_side.py             # Base enemy class — fleet layout, movement, rendering
├── dark_side_hard.py        # DarkSideHard subclass — adds enemy shooting behaviour
├── collision_detector.py    # Bullet hit detection, explosion rendering
├── image_cropping.py        # Cropping images to suit the game
├── .gitignore               # prevent certain file types from being uploaded to Github
└── static/                  # Game assets (images, fonts)
```

---

## Architecture

- `DarkSideHard` extends `DarkSide` via inheritance, overriding `shoot()`, `update_bullets()`, and `draw()` to add enemy bullet behaviour
- Enemy fleet positions are stored as a flat list of `[x, y]` coordinates; collision detection uses `pygame.Rect`
- Class-level assets (e.g. `droid`, `darthvader`, `tie-fighter`) are loaded once via `load_class_assets()` before the game loop to avoid per-frame I/O
- `CollisionDetector` is fully static — no instantiation needed; explosions are tracked in a class-level list with timestamps for duration-based rendering
- Hard mode bullets are fired only from the bottom-most enemy in each column, determined by grouping fleet positions by x coordinate each frame
- Player shooting is preprogrammed — the starfighter fires automatically on a fixed interval each frame rather than requiring manual input, keeping focus on movement and survival

---

## Requirements

- Python 3.10+
- Pygame

```bash
pip install pygame
```

---

## Installation & Run

```bash
git clone https://github.com/LegradiK/space_invader_app.git
cd space_invader_app

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

pip install pygame
python3 main.py
```

---

## Controls

| Key | Action |
|-----|--------|
| Left / Right arrow | Move starfighter |
| Space / Enter | Confirm / Replay |
| Escape | Quit to menu |

---

## Difficulty Modes

| Mode | Enemy Rows | Enemy Speed | Hard Behaviour |
|------|-----------|-------------|----------------|
| Easy | 3 | 1.6 | — |
| Medium | 5 | 2.0 | — |
| Hard | 5 | 3.0 | Tie Fighters shoot back |

---

## Credits

### Background
- Background photo by [cottonbro studio](https://www.pexels.com/photo/stars-in-night-sky-6138036/) from [Pexels](https://www.pexels.com)

### Icons & Images

- [Caza X (Starfighter)](https://thenounproject.com/icon/caza-x-2202282/) icon by [Linker](https://thenounproject.com/creator/linker/) from [The Noun Project](https://thenounproject.com), licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Tie Fighter](https://thenounproject.com/icon/tie-fighter-42403/) icon by [Jonas Nullens](https://thenounproject.com/creator/jonas.nullens/) from [The Noun Project](https://thenounproject.com), licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Storm Trooper (Droid) icon](https://www.flaticon.com/free-icon/droid_16170237) created by egorpolyakov from [Flaticon](https://www.flaticon.com)
- [Darth Vader icon](https://www.flaticon.com/free-icon/dark_16177406) created by egorpolyakov from [Flaticon](https://www.flaticon.com)
- [Light Saber icon](https://www.flaticon.com/free-icon/light-saber_3873296) created by Freepik from [Flaticon](https://www.flaticon.com)
- [Leia icon](https://www.flaticon.com/free-icon/people_15458676) created by pocike from [Flaticon](https://www.flaticon.com)
- [Luke Skywalker icon](https://icon-icons.com/icon/luke-skywalker-star-wars/76939) by Sensible World from [Icon-Icons.com](https://icon-icons.com)
- [Explosion icon](https://www.flaticon.com/free-icon/explode_7445310) created by Umeicon from [Flaticon](https://www.flaticon.com)

### Font
- [Star Jedi Font](https://www.dafont.com/star-jedi.font) by Boba Fonts