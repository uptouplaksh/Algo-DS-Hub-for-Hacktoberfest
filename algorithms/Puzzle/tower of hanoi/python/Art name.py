def ascii_banner(text):
    """
    Print a simple ASCII art banner for the given text.
    """
    banner = {
        "A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
        "B": ["BBBB ", "B   B", "BBBB ", "B   B", "BBBB "],
        "C": [" CCC ", "C   C", "C    ", "C   C", " CCC "],
        "D": ["DDD  ", "D  D ", "D   D", "D  D ", "DDD  "],
        "E": ["EEEEE", "E    ", "EEE  ", "E    ", "EEEEE"],
        " ": ["     ", "     ", "     ", "     ", "     "]
    }

    # Convert to uppercase
    text = text.upper()
    
    for i in range(5):  # Each character is 5 lines high
        line = ""
        for char in text:
            line += banner.get(char, ["?????"]*5)[i] + "  "
        print(line)

if __name__ == "__main__":
    name = input("Enter your name: ")
    print("\nHere’s your ASCII art banner:\n")
    ascii_banner(name)
