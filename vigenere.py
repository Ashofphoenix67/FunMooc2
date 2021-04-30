import string
import itertools

def cesar(clear, key, encode=True):
    if clear not in string.ascii_letters:
        return clear
    offset = ord(key.lower())-ord('a') + 1
    if not encode:
        offset *= -1
    firstl = ord('a')
    letter = chr((firstl + (ord(clear.lower()) - firstl + offset) % 26))
    if (clear.isupper()):
        return (letter.upper())
    return letter

def vigenere(clear, key, encode=True):
    return "".join(cesar(c, k, encode) for c, k in zip(clear, itertools.cycle(key)))

print(vigenere(
  'que nous vîmes',
  'baudelaire'))


