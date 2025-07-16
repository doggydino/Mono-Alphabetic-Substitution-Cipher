import math
import data

# Could use is close for comparison of values
plaintext = ''

def frequency_analysis(cipher_freq, eng_freq):
    closest_match = {}
    for cc, cf in cipher_freq.items():
        cm = list(sorted(eng_freq.items(), key=lambda i: abs(i[1] - cf))).pop(0)[1]
        closest_match[cc] = cm
    return closest_match




