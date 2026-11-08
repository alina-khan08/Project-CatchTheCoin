import argparse
import json
import os
import tkinter as tk 
import random


# -----------------------------
# GAME SETTINGS
# -----------------------------

WIDTH = 700
HEIGHT = 500

PLAYER_SIZE = 30
COIN_SIZE = 20
ENEMY_SIZE = 30

PLAYER_SPEED = 20
ENEMY_SPEED = 5

BACKGROUND_COLOR = "white"

# Object oriented programming for high score
class HighScoreTracker:
    #Reads and writes the highscore onto the disk
    def __init__(self, filename="highscore.json"):
        self.filename = filename

    def load(self):
        #Reads the highscore from JSON
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f).get("high_score", 0)
            except (json.JSONDecodeError, IOError):
                return 0
        return 0

    def save(self, score):
        #Write the high score to JSON
        with open(self.filename, "w") as f:
            json.dump({"high_score": score}, f, indent=4)

# -----------------------------
# GAME OBJECT DICTIONARIES
# -----------------------------

player = {
    "x": 50,
    "y": 50,
    "speed": PLAYER_SPEED,
    "score": 0
}

coin = {
    "x": 300,
    "y": 200
}

enemy = {
    "x": 600,
    "y": 400,
    "speed": ENEMY_SPEED
}


# -----------------------------
# GAME VARIABLES
# -----------------------------

root = None
canvas = None

game_over = False

#Global tracker for highscores and bonus calculations
tracker = HighScoreTracker()
high_score = tracker.load()
point_multiplier = 1



# -----------------------------
# MOVE PLAYER
# -----------------------------

def move_player(event):

    if game_over:
        return

    # Move player using arrow keys

    if event.keysym == "Up":
        player["y"] -= player["speed"]

    elif event.keysym == "Down":
        player["y"] += player["speed"]

    elif event.keysym == "Left":
        player["x"] -= player["speed"]

    elif event.keysym == "Right":
        player["x"] += player["speed"]

    # Prevent player from leaving the screen

    player["x"] = max(0, min(player["x"], WIDTH - PLAYER_SIZE))
    player["y"] = max(0, min(player["y"], HEIGHT - PLAYER_SIZE))

    check_collisions()
    draw_game()


# -----------------------------
# MOVE COIN
# -----------------------------

def move_coin():

    # Generate a new random coin position

    coin["x"] = random.randint(0, WIDTH - COIN_SIZE)
    coin["y"] = random.randint(0, HEIGHT - COIN_SIZE)

    draw_game()


# -----------------------------
# MOVE ENEMY (BASIC AI)
# -----------------------------

def move_enemy():

    if game_over:
        return

    # Enemy moves toward the player's x position

    if enemy["x"] < player["x"]:
        enemy["x"] += enemy["speed"]

    elif enemy["x"] > player["x"]:
        enemy["x"] -= enemy["speed"]

    # Enemy moves toward the player's y position

    if enemy["y"] < player["y"]:
        enemy["y"] += enemy["speed"]

    elif enemy["y"] > player["y"]:
        enemy["y"] -= enemy["speed"]

    # Keep enemy inside the screen

    enemy["x"] = max(0, min(enemy["x"], WIDTH - ENEMY_SIZE))
    enemy["y"] = max(0, min(enemy["y"], HEIGHT - ENEMY_SIZE))


# -----------------------------
# CHECK COLLISIONS
# -----------------------------

def check_collisions():

    global game_over, high_score

    # Check if player touches coin

    if (
        player["x"] < coin["x"] + COIN_SIZE
        and player["x"] + PLAYER_SIZE > coin["x"]
        and player["y"] < coin["y"] + COIN_SIZE
        and player["y"] + PLAYER_SIZE > coin["y"]
    ):

        # Increase score

        player["score"] += 1

        # Save high score to file using the object oriented programming tracker if the record is broken
        if player["score"] > high_score:
            high_score = player["score"]
            tracker.save(high_sco

        # Generate another coin



        move_coin()

    # Check if enemy catches player

    if (
        player["x"] < enemy["x"] + ENEMY_SIZE
        and player["x"] + PLAYER_SIZE > enemy["x"]
        and player["y"] < enemy["y"] + ENEMY_SIZE
        and player["y"] + PLAYER_SIZE > enemy["y"]
    ):

        game_over = True


# -----------------------------
# DRAW GAME
# -----------------------------

def draw_game():

    canvas.delete("all")

    # Draw player (blue square)

    canvas.create_rectangle(
        player["x"],
        player["y"],
        player["x"] + PLAYER_SIZE,
        player["y"] + PLAYER_SIZE,
        fill="blue"
    )

    # Draw coin (yellow circle)

    canvas.create_oval(
        coin["x"],
        coin["y"],
        coin["x"] + COIN_SIZE,
        coin["y"] + COIN_SIZE,
        fill="gold",
        outline="orange"
    )

    # Draw enemy (red square)

    canvas.create_rectangle(
        enemy["x"],
        enemy["y"],
        enemy["x"] + ENEMY_SIZE,
        enemy["y"] + ENEMY_SIZE,
        fill="red"
    )

    # Display score

    canvas.create_text(
        70,
        20,
        text="Score: " + str(player["score"]),
        fill="black",
        font=("Arial", 14, "bold")
    )

    canvas.create_text(
    WIDTH - 90,
    20,
    text="High Score: " + str(high_score),
    fill="black",
    font=("Arial", 14, "bold")
    )

    # Display game over message

    if game_over:

        canvas.create_text(
            WIDTH / 2,
            HEIGHT / 2,
            text="GAME OVER!",
            fill="red",
            font=("Arial", 32, "bold")
        )

        canvas.create_text(
            WIDTH / 2,
            HEIGHT / 2 + 45,
            text="Final Score: " + str(player["score"]),
            fill="black",
            font=("Arial", 18)
        )


# -----------------------------
# RESET GAME
# -----------------------------

def reset_game():

    global game_over

    # Reset player

    player["x"] = 50
    player["y"] = 50
    player["score"] = 0

    # Reset enemy

    enemy["x"] = WIDTH - ENEMY_SIZE
    enemy["y"] = HEIGHT - ENEMY_SIZE
    enemy["speed"] = ENEMY_SPEED

    # Reset coin

    move_coin()

    # Restart game

    game_over = False

    draw_game()


# -----------------------------
# MAIN GAME LOOP
# -----------------------------

def game_loop():

    if game_over:
        draw_game()
        return

    # Move enemy

    move_enemy()

    # Check collisions

    check_collisions()

    # Draw updated game

    draw_game()

    # Repeat game loop every 100 milliseconds

    root.after(100, game_loop)


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def main():

    global root, canvas, point_multiplier

    # Command-line arguments
    parser = argparse.ArgumentParser(description="Catch the Coin")
    parser.add_argument("--difficulty", type=int, default=1, choices=[1, 2, 3, 4, 5])
    args = parser.parse_args()

    # Calculates the bonus score using the recursive function
    point_multiplier = calculate_bonus(args.difficulty)
    enemy["speed"] = ENEMY_SPEED + (args.difficulty - 1) * 2

   
    # Create game window

    root = tk.Tk()

    root.title("Catch the Coin")

    root.resizable(False, False)

    # Create canvas

    canvas = tk.Canvas(
        root,
        width=WIDTH,
        height=HEIGHT,
        bg=BACKGROUND_COLOR
    )

    canvas.pack()

    # Instructions

    instructions = tk.Label(
        root,
        text=f"Difficulty: Level {args.difficulty} (+{point_multiplier} pts/coin) |Use the arrow keys to collect coins and avoid the enemy!",
        font=("Arial", 12)
    )

    instructions.pack(pady=5)

    # Restart button

    restart_button = tk.Button(
        root,
        text="Restart Game",
        command=reset_game
    )

    restart_button.pack(pady=5)

    # Keyboard controls

    root.bind("<Up>", move_player)
    root.bind("<Down>", move_player)
    root.bind("<Left>", move_player)
    root.bind("<Right>", move_player)

    # Draw initial game

    draw_game()

    # Start game loop

    root.after(100, game_loop)

    # Keep window running

    root.mainloop()


# -----------------------------
# RUN GAME
# -----------------------------

if __name__ == "__main__":
    main()
