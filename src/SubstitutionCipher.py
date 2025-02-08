import random
import copy

class SubstitutionCipher:
  standard_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def encrypt (self, plain_text, key):
    cipher_alphabet = self.get_cipher_alphabet(key)

    return self.substitute_text(plain_text, self.standard_alphabet, cipher_alphabet)

  def get_cipher_alphabet (self, key):
    # Use the key as a seed when shuffling the alphabet.
    random.seed(key)
    alphabet_to_shuffle = list(copy.deepcopy(self.standard_alphabet))
    random.shuffle(alphabet_to_shuffle)
    return "".join(alphabet_to_shuffle)

  def substitute_text (self, origin_text, origin_alphabet, substitute_alphabet):
    # The encrypted letters will be added to a list.
    substituted_text = []

    for letter in origin_text:
      # Find the index of the letter in the standard alphabet,
      # and replace it with the cipher Alphabet.
      index = origin_alphabet.find(letter.upper())
      if (index != -1):
        substituted_text.append(substitute_alphabet[index])
      else:
        substituted_text.append(letter.upper())
    return "".join(substituted_text)

  def decrypt (self, cipher_text):
    return self.decrypt_with_key(cipher_text, 120)

  def decrypt_with_key (self, cipher_text, key):
    cipher_alphabet = self.get_cipher_alphabet(key)

    return self.substitute_text(cipher_text, cipher_alphabet, self.standard_alphabet)
