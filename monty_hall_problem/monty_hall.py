import sys
from random import randint

loop_count = 100 if len(sys.argv) == 1 else sys.argv[1]

try:
    loop_count = int(loop_count)
except ValueError:
    print("Couldn't convert loop_count to an int.")
    quit()

print(f"Running simulation {loop_count} times.")


def main(loops):
    for num in range(loops):
        prize_door = randint(1, 3)
        door_choice = randint(1, 3)
        print(f"Prize door: {prize_door}")
        print(f"Door choice: {door_choice}")


main(loop_count)
