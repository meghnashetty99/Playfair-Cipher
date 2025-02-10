# Playfair-Cipher
"""
This repository contains an implementation of the **Monoalphabetic Cipher** that generates a random substitution key every time it runs. It is a simple but effective encryption method where each letter in the plaintext is replaced with a randomly shuffled version of the alphabet.

##Features
✅Generates a Playfair Cipher 5x5 matrix based on a keyword.
✅Encrypts plaintext using the Playfair Cipher method.
✅Decrypts ciphertext back to the original plaintext
✅Handles duplicate letters and spaces efficiently.

##Usage

##Encryption
1.The plaintext is converted to uppercase, and the letter 'J' is replaced with 'I'.
2.The text is split into pairs, adding 'X' if necessary to avoid duplicate letter pairs.
3.The Playfair matrix is used to encrypt the pairs based on the Playfair Cipher rules.

##Decryption
1.The ciphertext is split into pairs.
2.The Playfair matrix is used to decrypt the pairs based on the Playfair Cipher rules.
