from nltk.corpus import words

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
    # Try every key, check if the result is readable, and
    # save readable solutions in a list.
    possible_solutions = []

    for key in range(256):
      text = self.decrypt_with_key(cipher_text, key)
      if (self.is_readable(text)):
        possible_solutions.append(text)
    return possible_solutions

  def decrypt_with_key (self, cipher_text, key):
    cipher_alphabet = self.get_cipher_alphabet(key)

    return self.substitute_text(
      cipher_text, cipher_alphabet, self.standard_alphabet).capitalize()

  def is_readable (self, text):
    word_list = map(str.lower, words.words())
    words_to_test = text.split()

    return all(word.lower() in word_list for word in words_to_test)
