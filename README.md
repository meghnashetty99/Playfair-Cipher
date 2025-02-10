# Playfair-Cipher
Description

This project is an implementation of the Playfair Cipher in Python. The Playfair Cipher is a digraph substitution cipher that encrypts pairs of letters in a given text using a 5x5 matrix generated from a keyword. The same matrix is used for decryption.

Features

Generates a Playfair Cipher 5x5 matrix based on a keyword.

Encrypts plaintext using the Playfair Cipher method.

Decrypts ciphertext back to the original plaintext.

Handles duplicate letters and spaces efficiently.

Usage

Encryption

The plaintext is converted to uppercase, and the letter 'J' is replaced with 'I'.

The text is split into pairs, adding 'X' if necessary to avoid duplicate letter pairs.

The Playfair matrix is used to encrypt the pairs based on the Playfair Cipher rules.

Decryption

The ciphertext is split into pairs.

The Playfair matrix is used to decrypt the pairs based on the Playfair Cipher rules.
