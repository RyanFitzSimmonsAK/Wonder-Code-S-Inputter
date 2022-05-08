import pydirectinput
import time

# 0.0175 is about the fastest that EoS will accept inputs.
pydirectinput.PAUSE = 0.0175

"""
 * This is where the keyboard input is executed.  Start the script on the Wonder Mail S password input screen, with the cursor on 'N'.
 * This script assumes that you have "A" bound to "S" on your keyboard, and are using the arrow keys for directional inputs.
"""


def outputCode(code):
    # Gives time for the user to switch their tab to their emulator.
    time.sleep(1)

    # The game defaults to 'N', so we start at (1, 0).
    row = 1;
    column = 0;

    # This is the keyboard layout of EoS.
    keyboard = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
        ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '.', '&'],
        ['-', '_', '#', '$', '%', ':', ';', '*', '+', '<', '=', '>', '?']
    ]

    # Empty list that will eventually contain the list of inputs that create the code.
    sequence = []

    # Iterating through each character of the code, and adding the inputs to the sequence.
    for char in code:

        # Calculating where the target character is in relation to the current position.
        xMod = findCharacterIndex(keyboard, char)[1] - column
        yMod = findCharacterIndex(keyboard, char)[0] - row

        # Adds the input to the sequence, and adjusts the column / row counter.
        if xMod > 0:
            for _ in range(xMod):
                sequence.append("right")
            column += xMod
        elif xMod < 0:
            for _ in range(-1 * xMod):
                sequence.append("left")
            column += xMod

        if yMod > 0:
            for _ in range(yMod):
                sequence.append("down")
            row += yMod
        elif yMod < 0:
            for _ in range(-1 * yMod):
                sequence.append("up")
            row += yMod

        sequence.append("s")

    # Plays back the sequence with pydirectinput.
    for input in sequence:
        if input == "s":
            pydirectinput.press("s")
        else:
            inputDirection(input, 1)

    # Presses "END".
    pydirectinput.press("s")


# Used for directional inputs.
def inputDirection(direction, times):
    for _ in range(times):
        pydirectinput.press(direction)


# Used to quickly find the position of a target character.
def findCharacterIndex(keyboard, target):
    for i in range(len(keyboard)):
        for j in range(len(keyboard[0])):
            if keyboard[i][j] == target:
                return i, j
