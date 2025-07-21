# Could use is close for comparison of values

# Todo: Tune up probabilities
def frequency_analysis(cipher_freq, eng_freq, **limiter):
    original = eng_freq
    closest_match = {}
    if len(limiter) == 0:
        for cc, cf in cipher_freq.items():
            eng_freq = dict(eng_freq)
            cm = list(sorted(eng_freq.items(), key=lambda i: abs(i[1] - cf)))
            eng_freq = list(sorted(eng_freq.items(), key=lambda i: abs(i[1] - cf)))
            cm = cm.pop(0)
            eng_freq.pop(0)
            closest_match[cc] = cm[0]
        return closest_match


def find_conflicts(freq_dict):
    counts = dict()
    uniques = dict()
    conflicts = dict()
    for v in freq_dict.values():
        counts[v] = counts.get(v, 0) + 1
    for k, v in freq_dict.items():
        if counts[v] > 1:
            conflicts[k] = v
        else:
            uniques[k] = v
    return conflicts


def resolve_conflicts(func, key):
    for i in func:
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

# Todo: Fix look for trigrams and finish it
# look for trigrams, digrams etc
def look_for_trigrams(ciphertext:str):
    storage = dict()
    for index, letter in enumerate(ciphertext):
        if index == len(ciphertext) - 3:
            storage[ciphertext[index: index + 4]] = storage.get(ciphertext[index:index + 4], 0) + 1
            return storage
        storage[ciphertext[index: index + 4]] = storage.get(ciphertext[index:index + 4], 0) + 1