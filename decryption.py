# Could use is close for comparison of values
# plaintext = ''

# Todo: Tune up probabilities
def frequency_analysis(cipher_freq, eng_freq):
    closest_match = {}
    for cc, cf in cipher_freq.items():
        cm = list(sorted(eng_freq.items(), key=lambda i: abs(i[1] - cf)))
        cm = cm.pop(0)
        closest_match[cc] = cm[0]
    return closest_match

# Todo: Clean up output
def conflict_analysis(dictionary):
    test = dict()
    conflicts = dict()
    for k, v in dictionary.items():
        if v in test.values():
            conflicts[k] = v
        else:
            test[k] = v
    return conflicts
# Todo: Write conflict resolution function
def conflict_resolution():
    pass

# Todo: NOT MY CODE DELETE AND REMAKE LATER
def dec(ciphertext, key):
  plaintext = ""
  for letter in ciphertext:
    val = key.get(letter, None)
    if (val != None):
      plaintext += val
    else:
      plaintext += letter
  return plaintext

# Todo: Fix look for grams and finish it
def look_for_grams(ciphertext:str, gram_amount:int):
    storage = dict()
    for i in ciphertext:
        a = ciphertext.index(i)
        storage[a:a+gram_amount + 1] = storage.get(storage[a:a+gram_amount+1])
    return storage




