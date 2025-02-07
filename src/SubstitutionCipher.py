class SubstitutionCipher:
  def encrypt (self, plain_text, key):
    self.get_cipher_alphabet(key)
    return plain_text

  def get_cipher_alphabet (self, key):
    # TODO: This is only a temporary shifted key.
    return 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
