# The starting point of the application.

from SubstitutionCipher import SubstitutionCipher

# option1Answer = input('Do you want to encrypt (E) or decrypt (D)?')

# option2Answer = input('Do you want to use substitution (S) or transposition (T)?')

plain_text = input("Enter plaintext message:")

cipher = SubstitutionCipher()
print(cipher.encrypt(plain_text, 123))
