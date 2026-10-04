import os
import time


# Colors
RESET = "\033[0m"
GREEN = "\033[48;5;22m"
RED = "\033[41m"
WHITE = "\033[47m"


# Clear console
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Wait before next task
def wait():
    input("\nPress Enter...")
    clear_screen()


# TASK 1: FLAG OF BANGLADESH
def flag():
    print("TASK 1 - FLAG\n")

    for y in range(10):
        for x in range(30):

            if (x - 14) ** 2 + (y - 5) ** 2 <= 16:
                print(RED + "  ", end="")
            else:
                print(GREEN + "  ", end="")

        print(RESET)


# TASK 2: PATTERN
def pattern():
    print("TASK 2 - PATTERN\n")

    p = [
        "###########",
        "##     ####",
        "## ### ####",
        "## #   ####",
        "## # ######",
        "## #     ##",
        "###########"
    ]

    for row in p:
        for repeat in range(3):
            for x in row:

                if x == "#":
                    print(WHITE + "  ", end="")
                else:
                    print(RESET + "  ", end="")

        print(RESET)


# EXTRA TASK: GRAPH y = 2x + 3
def graph():
    width = 9
    max_y = 19

    # Clear screen and move cursor to top-left
    graph_text = "\033[2J\033[H"

    graph_text += "EXTRA TASK - GRAPH y = 2x + 3\n\n"
    graph_text += "y\n"
    graph_text += "^\n"

    for y in range(max_y, -1, -1):
        graph_text += "|"

        for x in range(width):
            value = 2 * x + 3

            if y == value:
                graph_text += " *"
            else:
                graph_text += "  "

        graph_text += "\n"

    graph_text += "+" + "--" * width + "> x\n"

    # Print whole graph at once
    print(graph_text, end="")


# TASK 3: ANIMATION
def animation():
    for x in [2, 7, 12, 17]:
        clear_screen()

        print("\033[H", end="")
        print("TASK 3 - ANIMATION\n")
        print(" " * x + "●")

        time.sleep(0.5)


# TASK 4: DIAGRAM
def diagram():
    print("TASK 4 - DIAGRAM\n")

    numbers = []

    # Read numbers from file
    with open("sequence.txt", "r") as file:
        data = file.read().split()

    # Convert text to numbers
    for x in data:
        numbers.append(float(x))

    if len(numbers) < 250:
        print("Error: sequence.txt must contain at least 250 numbers.")
        return

    # First 125 numbers
    first = 0

    for i in range(125):
        first += abs(numbers[i])

    # Second 125 numbers
    second = 0

    for i in range(125, 250):
        second += abs(numbers[i])

    total = first + second

    if total == 0:
        print("Error: total is 0.")
        return

    # Percentages
    p1 = first / total * 100
    p2 = second / total * 100

    print("First 125 :", round(p1, 1), "%")
    print("Second 125:", round(p2, 1), "%")
    print()

    # Diagram
    print("A:", "#" * int(p1 / 2))
    print("B:", "#" * int(p2 / 2))


# MAIN
flag()
wait()

pattern()
wait()

graph()
wait()

animation()
wait()

diagram()