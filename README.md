# Python String Encryption

## Overview
The goal of this project is to implement encryption and decryption algorithms for strings. The project consists of two widely known encryption algorithms [Ceasar encryption](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/) and [Hill Cipher encryption](https://www.geeksforgeeks.org/hill-cipher/) along with their decryption.

Hill Cipher

I stack to the point of implement the Hill Cipher in Python, and since my background is within Backend it took me time to understand the Algebra behind the Algorithm, but here is my walkthrough before the stack:

Looking-up "Matrix Encryption Algorithm", it called the Hill Cipher Encryption wich base on the Matrix Algebra, the Cipher consists of 3 elements:
* Indexed English chracters, which starts from 0 to 25.
* The key, which should be a square of integer (n squared).
* Column of numbers, as each number corresponde to number of indexed English chracters e.g.a=0, b=1, ... z=25 .
* Base 24 (n mod 24).
