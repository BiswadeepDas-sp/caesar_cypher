# caesar_cypher
This Python program encrypts and decrypts text using a Caesar cipher algorithm. Users can choose to encrypt or decrypt text with a specified shift value. It includes error handling for invalid inputs and allows users to exit the program at any prompt by typing "exit" (case-insensitive). Simple, intuitive, and easy to use.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Error Handling](#error-handling)
- [License](#license)

## Features
- Encrypts text using a specified shift value.
- Decrypts text using the reverse of the specified shift value.
- Provides an option to exit the program at any input prompt by typing "exit" (case-insensitive).
- Handles invalid input gracefully with error messages.

## Prerequisites
This program requires Python 3.x to run. Make sure you have Python installed on your system. You can download it from the official website: [Python.org](https://www.python.org/).

## Usage
1. Run the program from the command line or terminal:
   ```bash
   python your_program_name.py
   ```

2. The program will prompt you to select one of the following options:
   - Enter `1` to encrypt text.
   - Enter `2` to decrypt text.
   - Enter `exit` to exit the program at any prompt.

3. If you choose to encrypt or decrypt:
   - Enter the text you wish to process.
   - Enter the shift value (positive integer for encryption). For decryption, the shift will be applied in reverse.

4. The program will display the encrypted or decrypted text as output.

## How It Works
- **Caesar Cipher Algorithm:** This program uses a Caesar cipher to encrypt or decrypt text by shifting each letter by a specified number of positions in the alphabet.
- **Encryption:** Each letter in the input text is shifted to the right by the specified number of positions.
- **Decryption:** Each letter in the input text is shifted to the left by the specified number of positions.

### Example
- **Input for Encryption:** `HELLO` with a shift of `3` produces `KHOOR`.
- **Input for Decryption:** `KHOOR` with a shift of `3` produces `HELLO`.

## Error Handling
- The program provides clear instructions when an invalid input is detected.
- If an invalid shift value is entered, the program exits with an error message.
- To continue after an error, the program prompts the user to try again or exit.

## License
This project is open-source and available for personal or educational use. Feel free to modify or distribute it under your requirements.

---
