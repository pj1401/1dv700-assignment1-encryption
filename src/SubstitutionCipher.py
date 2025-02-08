import random
import copy

class SubstitutionCipher:
  standard_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def encrypt (self, plain_text, key):
    cipher_key = self.get_cipher_alphabet(key)
    # The encrypted letters will be added to a list.
    cipher_text = []

    for letter in plain_text:
      # Find the index of the letter in the standard alphabet,
      # and replace it with the cipher Alphabet.
      index = self.standard_alphabet.find(letter.upper())
      if (index != -1):
        cipher_text.append(cipher_key[index])
      else:
        cipher_text.append(letter.upper())
    return "".join(cipher_text)

  def get_cipher_alphabet (self, key):
    # Use the key as a seed when shuffling the alphabet.
    random.seed(key)
    alphabet_to_shuffle = list(copy.deepcopy(self.standard_alphabet))
    random.shuffle(alphabet_to_shuffle)
    return "".join(alphabet_to_shuffle)
