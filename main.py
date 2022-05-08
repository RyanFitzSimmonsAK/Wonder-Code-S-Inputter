from Output import *

"""
This is a useful tool for people playing Pokémon Mystery Dungeon: Explorers of Sky (EoS) on an emulator.  
Wonder Code S is a mechanic that allows players to make themselves missions to complete.  
However, these "Wonder Codes" used to create the missions are time-consuming and tedious to input.  
This tool does the inputs for the user extremely quickly, and has functionality to input multiple codes at once.
"""

def main():

    file = open("code.txt", "r")
    codes = getCodesList(file)

    for code in codes:
        outputCode(code)


def getCodesList(file):
    """
    A function to read the text file containing the codes, and return those codes as a list.
    :return: A list containing every code to be inputted.
    :param file: File containing the codes to input.
    """

    codes = []
    currentCode = ""

    for line in file:
        # If the line is empty, then it's a new code.  In that case, add the old code to the list, and start again.
        if line == "":
            # Empty spaces and newline characters need to be removed.
            currentCode = currentCode.replace(" ", "")
            currentCode = currentCode.replace("\n", "")
            codes.append(currentCode)
            currentCode = ""
        # If the line is not empty, then it should be added to the current code.
        else:
            currentCode += line

    # Adds the last code in the file to the list.
    # Empty spaces and newline characters need to be removed.
    currentCode = currentCode.replace(" ", "")
    currentCode = currentCode.replace("\n", "")
    codes.append(currentCode)

    return codes


main()