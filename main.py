"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""
<<<<<<< HEAD
import pygame
import random

WIDTH = 800
HEIGHT = 600

PLAYER_SIZE = 30
COIN_SIZE = 20
ENEMY_SIZE = 30

def move_player():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT]:
        player["x"] += player["speed"]
    if keys[pygame.K_UP]:
        player["y"] -= player["speed"]
    if keys[pygame.K_DOWN]:
        player["y"] += player["speed"]

    # Keep player on the screen
    player["x"] = max(0, min(WIDTH - PLAYER_SIZE, player["x"]))
    player["y"] = max(0, min(HEIGHT - PLAYER_SIZE, player["y"]))


def move_enemy():
    # Move horizontally toward the player
    if enemy["x"] < player["x"]:
        enemy["x"] += enemy["speed"]
    elif enemy["x"] > player["x"]:
        enemy["x"] -= enemy["speed"]

    # Move vertically toward the player
    if enemy["y"] < player["y"]:
        enemy["y"] += enemy["speed"]
    elif enemy["y"] > player["y"]:
        enemy["y"] -= enemy["speed"]


def move_collisons():
    # Check if the player touches the coin
    if (
        player["x"] < coin["x"] + COIN_SIZE
        and player["x"] + PLAYER_SIZE > coin["x"]
        and player["y"] < coin["y"] + COIN_SIZE
        and player["y"] + PLAYER_SIZE > coin["y"]
    ):
        player["score"] += 1

        # Move coin to a new random position
        coin["x"] = random.randint(0, WIDTH - COIN_SIZE)
        coin["y"] = random.randint(0, HEIGHT - COIN_SIZE)


def check_collisons():
    # Check if the enemy catches the player
    if (
        player["x"] < enemy["x"] + ENEMY_SIZE
        and player["x"] + PLAYER_SIZE > enemy["x"]
        and player["y"] < enemy["y"] + ENEMY_SIZE
        and player["y"] + PLAYER_SIZE > enemy["y"]
    ):
        return True

    return False

=======
def move_coin(game_state):
    if game_state["player"] == game_state["coin"]:
        game_state["score"] += 1
        next_index = (game_state.get("coin_index", 0) + 1) % len(game_state["coin_positions"])
        game_state["coin_index"] = next_index
        game_state["coin"] = game_state["coin_positions"][next_index]
        move_player()
    return game_state
>>>>>>> 281f17b422a79d38625291e0ed51cdb9ad5535c2

def main():
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")


if __name__ == '__main__':
    main()
