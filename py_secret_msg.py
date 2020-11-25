class MessageEncryption:
    """ Allow user to encrypt their messages or decrypt it on demand. Along as,
    allow them to choice between to kind of algorithms Shift and Matrix.

    Note: The Matrix algorithm in progress, more on that in the README.md.
    """

    # User inputs along with help messages.
    msg = input('Your Message: ')

    # Select encryption type.
    help_msg = 'Shift Algorithm type "s".\nMatrix Algorithm type "m".\nNumbers and empty choice will be considered as "s".'
    print('\n' + help_msg)
    encryption_type = input('\n' + 'Encryption Type: ')

    # Select to decrypt or encrypt message.
    help_msg = 'To encrypt your message type "e", for decryption type "d", numbers and empty choice will be considered as "e".'
    print('\n' + help_msg)
    decrypt_or_encrypt = input('\n' + 'Your choice goes here: ')
    # On decrypt option.
    if decrypt_or_encrypt == 'd':
        encrypted = True
    else:
        encrypted = False

    def shift_encryption(self, msg=msg, encrypted=encrypted):
        """ Shift every letter by 3 letters.
        args:
            * msg: The user input message.
            * encrypted: Check if message is encrypted(default=True).
        """
        encrypted_msg = ''

        upper_letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        lower_letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        for letter in msg:
            steps = 3
            # If user select to decrypt.
            if encrypted:
                # decrypt it.
                steps = -3

            # Uppercase letter.
            if letter in upper_letters:
                # Index that character.
                index = upper_letters.index(letter)
                # Shift by steps.
                crypting = (index + steps) % 26
                # Form the encrypted msg.
                encrypted_msg += upper_letters[crypting]
            # Lowercase letter.
            elif letter in lower_letters:
                index = lower_letters.index(letter)
                crypting = (index + steps) % 26
                encrypted_msg += lower_letters[crypting]
            else:
                # Add else characters as it is (ex: !!, ' ').
                encrypted_msg += letter

        print('\n' + f'Here is your secret message {encrypted_msg}')

    def matrix_encryption(self):
        print('\n' + 'Sorry, the Matrix Algorithm is in progress.')

    # If user select the matrix algorithm.
    if encryption_type == 'm':
        matrix_encryption(None)
    # For shift algorithm encryption_type == 's'.
    else:
        shift_encryption(None)
