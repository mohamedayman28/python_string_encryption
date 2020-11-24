#!/usr/bin/env python3.6

class SecretMessage:
    def __init__(self, msg):
        self.msg = msg

    def shift_encryption(self):
        """ Method to shift every letter by 3 letter."""
        encrypted_msg = ''

        upper_letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        lower_letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        for letter in self.msg:
            # Uppercase letter.
            if letter in upper_letters:
                # Index that character.
                index = upper_letters.index(letter)
                # Shift by 3 steps.
                crypting = (index + 3) % 26
                # Form the encrypted msg.
                encrypted_msg += upper_letters[crypting]
            # Lowercase letter.
            elif letter in lower_letters:
                index = lower_letters.index(letter)
                crypting = (index + 3) % 26
                encrypted_msg += lower_letters[crypting]
            else:
                # Add else characters as it is (ex: !!).
                encrypted_msg += letter

        return encrypted_msg
