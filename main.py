ciphertext = input("Please enter the Ciphertext: ")
print()

from data import calc_freq
from decryption import *
from data import average_freq

raw_ciphertext = ciphertext.upper()

ciphertext = raw_ciphertext.replace(" ", "")

ciphertext = "".join((filter(lambda i:i.isalpha(), ciphertext)))

frequency = calc_freq(ciphertext)

key = frequency_analysis(frequency, average_freq)

for k, v in key.items():
    print(f"{k}: {v}")

#print(look_for_trigrams(ciphertext))

print(dec(ciphertext, key))
