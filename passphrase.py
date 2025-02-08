import random


def generate_passphrase(wordlist_file):
    """
    Generates a 4-word passphrase using the given Diceware word list.

    Args:
        wordlist_file: Path to the Diceware word list file.

    Returns:
        A string containing the 4-word passphrase.
    """
    try:
        with open(wordlist_file, 'r') as f:
            wordlist = f.read().splitlines()

        passphrase = []
        for _ in range(4):
            # Generate a random 5-digit number (representing 5 dice rolls)
            dice_rolls = ''.join(str(random.randint(1, 6)) for _ in range(5))
            # Find the corresponding word in the word list
            word_index = int(dice_rolls) - 1  # Adjust for 0-based indexing
            passphrase.append(wordlist[word_index])

        return ' '.join(passphrase)

    except FileNotFoundError:
        print(f"Error: Word list file '{wordlist_file}' not found.")
        return None


if __name__ == "__main__":
    wordlist_file = 'eff_large_wordlist.txt'  # Replace with the path to your Diceware word list file
    passphrase = generate_passphrase(wordlist_file)

    if passphrase:
        print("Generated passphrase:", passphrase)
