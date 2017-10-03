import sys
from random import randint

loop_count = 100 if len(sys.argv) == 1 else sys.argv[1]
PRIZE_DOOR = 1

try:
    loop_count = int(loop_count)
except ValueError:
    print("Couldn't convert loop_count to an int.")
    quit()

print(f"\nRunning simulation {loop_count} times.\n")


def main(loops):
    """
    If you select the correct door to begin with, it's considered a
    `staying win` since you'll win if you don't switch. If you didn't select
    the correct door to begin with, the `goat` door is removed from the
    remaining doors, leaving the `car` door as the remaining choice, so
    it is considered a `switching win`.
    """
    staying_wins = 0
    switching_wins = 0

    for num in range(loops):
        door_choice = randint(1, 3)

        if door_choice == PRIZE_DOOR:
            staying_wins += 1
        else:
            switching_wins += 1

    print("Staying wins: " + str(staying_wins))
    print("Switching wins: " + str(switching_wins) + "\n")

    staying_odds = round((staying_wins / loops) * 100, 2)
    switching_odds = round((switching_wins / loops) * 100, 2)
    print("Your odds of winning if you stay: " + str(staying_odds) + "%")
    print("Your odds of winning if you switch: " + str(switching_odds) + "%\n")


main(loop_count)
