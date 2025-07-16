
average_freq = {
    "A": .0757,
    "B": .0184,
    "C": .0409,
    "D": .0338,
    "E": .1151, # Most common
    "F": .0123,
    "G": .0270,
    "H": .0232,
    "I": .0901,
    "J": .0016, # Least Common
    "K": .0085,
    "L": .0531,
    "M": .0284,
    "N": .0685,
    "O": .0659,
    "P": .0294,
    "Q": .0016,
    "R": .0707,
    "S": .0952,
    "T": .0668,
    "U": .0327,
    "V": .0098,
    "W": .0074,
    "X": .0029,
    "Y": .0163,
    "Z": .0047,
}


def calc_freq(ciphertext):
    freq = dict()
    for letter in ciphertext:
        freq[letter] = round((freq.get(letter, 0) + 1) / len(ciphertext), 4)
    for letter in freq:
        print(f"Letter: {letter} Frequency: {freq[letter]}")
    return freq

