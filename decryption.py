
# Todo: Tune up probabilities


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

def frequency_analysis(cipher_freq, eng_freq, conflict=dict(), **limiter):
    closest_match = {}
    if len(conflict) == 0:
        for cc, cf in cipher_freq.items():
            eng_freq = dict(eng_freq)
            cm = list(sorted(eng_freq.items(), key=lambda i: abs(i[1] - cf)))
            eng_freq = list(sorted(eng_freq.items(), key=lambda i: abs(i[1] - cf)))
            cm = cm.pop(0)
            #eng_freq.pop(0)
            closest_match[cc] = cm[0]
        confs = find_conflicts(closest_match)
        return closest_match

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
            if len(ciphertext) - index != 3:
                continue
            storage[ciphertext[index: index + 3]] = storage.get(ciphertext[index:index + 3], 0) + 1
            storage = dict(filter(lambda i:i[1] > 1, storage.items()))
            return storage
        storage[ciphertext[index: index + 3]] = storage.get(ciphertext[index:index + 3], 0) + 1


def look_for_digrams(ciphertext:str):
    storage = dict()
    for index, letter in enumerate(ciphertext):
        if index == len(ciphertext) - 2:
            if len(ciphertext) - index != 2:
                continue
            storage[ciphertext[index: index + 2]] = storage.get(ciphertext[index:index + 2], 0) + 1
            storage = dict(filter(lambda i:i[1] > 1, storage.items()))
            return storage
        storage[ciphertext[index: index + 2]] = storage.get(ciphertext[index:index + 2], 0) + 1


def find_max_in(dictionary:dict):
    largest = 0
    for keys, values in dictionary.items():
        if values > largest:
            largest = keys
    return largest