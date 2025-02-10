# The starting point of the application.

from SubstitutionCipher import SubstitutionCipher

# option2Answer = input('Do you want to use substitution (S) or transposition (T)?')

try:
  option1_answer = input("Do you want to encrypt (E) or decrypt (D)? ")

  if (option1_answer.upper() == "E"):
    plain_text = input("Enter plaintext message: ")
    key = int(input("Enter the secret key: "))

    cipher = SubstitutionCipher()
    print(cipher.encrypt(plain_text, key))
  else:
    cipher_text = input("Enter text to decipher: ")
    key_known_answer = input("Is the key known? Yes (Y) No (N) ")
    if (key_known_answer.upper() == "Y"):
      key = int(input("Enter the key: "))

      cipher = SubstitutionCipher()
      print(cipher.decrypt_with_key(cipher_text, key))
    else:
      cipher = SubstitutionCipher()
      print(cipher.decrypt(cipher_text))
except TypeError as t:
  print(t)
except Exception as e:
  print(e)
