# Python String Encryption

![image](https://raw.githubusercontent.com/mohamedayman28/python_string_encryption/main/github_cover_4_python_secret_message_repo.jpg)

## How to run the project
* I use Python version 3.6
* so run **python3.6**

## Overview
The goal of this project is to implement encryption and decryption algorithms for strings. The project consists of two widely known encryption algorithms [Ceasar encryption](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/) and [Hill Cipher encryption](https://www.geeksforgeeks.org/hill-cipher/) along with their decryption.

### Ceasar(shift) Encryption
I use this [code](https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-25.php) from w3school as the base code for the shift algorithm.

### Hill Cipher(matrix) Encryption

My mathematical background not behind the basics which took me much time to understand the Algebra behind this Cipher.
Now, I do understand how to solve the Matrix Algebras but I get stuck at the task implementation point, anyway, here is how I managed to solve the Hill Cipher Algorithm before getting to the stuck point:

**Look up.**
It's named the Hill Cipher Encryption which bases on the Matrix Algebra.
  
**Understand.**
* The Algorithm consists of 4 aspects:
  * Indexed English characters, which starts from 0 to 25.
  * Key (password), which should be a square of integer (n squared).
  * A column of numbers, each number corresponds to the indexed English characters.
  * Base 24 (n mod 24).
    
* **Implement.**
  * I use this GeeksForGeeks [example](https://www.geeksforgeeks.org/hill-cipher/).
  * Along with the old-school way, paper and pen.
  * I came a cross a question which consumes more time:
  
    **Q**: What if the length of the colum elements shorter or longer that the virtical length.
    
    **A**: The last element of the column will be repeated to match the Matrix virticallyso if Key is 'GYBNQKURP'(matrix of 3) and Text is 'AC'(column of 2), Text will be 'ACC'(column of 3).
