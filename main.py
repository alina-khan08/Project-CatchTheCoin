"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""
def move_coin(game_state):
    if game_state["player"] == game_state["coin"]:
        game_state["score"] += 1
        next_index = (game_state.get("coin_index", 0) + 1) % len(game_state["coin_positions"])
        game_state["coin_index"] = next_index
        game_state["coin"] = game_state["coin_positions"][next_index]
        move_player()
    return game_state

def main():
    print("CSCI 1030U group project - not built yet.")
    print("Replace main() with your core loop. See MILESTONES.md for what is due when.")


if __name__ == '__main__':
    main()
