ciphertext = input("Please enter the Ciphertext: ")

from data import calc_freq
from decryption import frequency_analysis
from data import average_freq

raw_ciphertext = ciphertext.upper()
ciphertext = raw_ciphertext.replace(" ", "")
frequency = calc_freq(ciphertext)
print(frequency_analysis(frequency, average_freq))


