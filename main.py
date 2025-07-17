ciphertext = input("Please enter the Ciphertext: ")

from data import calc_freq
from decryption import frequency_analysis
from data import average_freq
from decryption import dec
from decryption import look_for_grams



raw_ciphertext = ciphertext.upper()

ciphertext = raw_ciphertext.replace(" ", "")

ciphertext = list(filter(lambda i:i.isalpha(), ciphertext))

frequency = calc_freq(ciphertext)

key = frequency_analysis(frequency, average_freq)

for k, v in key.items():
    print(f"{k}: {v}")

print(dec(ciphertext, key))

#print(look_for_grams(str(ciphertext), 3))
