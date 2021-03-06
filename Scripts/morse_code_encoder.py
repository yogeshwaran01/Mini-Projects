MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def encodeMorse(word: str) -> str:
    """
    >>> encodeMorse('HEY JUDE')
    '.... . -.--   .--- ..- -.. .'
    """
    list = word.strip().upper()
    ans = []
    for i in list:
        if i == " ":
            ans.append(" ")
        else:
            ans.append(MORSE_CODE[i])
    return " ".join(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    sen = input("Enter the string to Encode: ")
    print(encodeMorse(sen))
