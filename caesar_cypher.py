import sys

def input_error_handling():
    print("You have entered an invalid response. You can type 'exit' (case-insensitive) to exit the program.")
    user_action = input("Enter 1 to continue or type 'exit' to quit: ").strip().lower()
    if user_action == "1":
        user_input()
    elif user_action == "exit":
        print("Exiting the program...")
        sys.exit()
    else:
        print("Invalid input. Exiting the program...")
        sys.exit()

def user_input():
    def display_option():
        print("You can type 'exit' (case-insensitive) to exit the program.")
        action = input("Enter 1 to encrypt text or Enter 2 to decrypt text: ").strip().lower()
        return action

    action = display_option()

    if action in ['1', '2']:
        text = input("Enter the text to be processed: ").strip()
        try:
            shift = int(input("Enter shift value (only positive integers): ").strip())
            if action == '2':  # For decryption, make the shift negative
                shift = -shift
        except ValueError:
            print("Invalid shift value. Exiting the program...")
            sys.exit()
    elif action == "exit":
        print("Exiting the program...")
        sys.exit()
    else:
        input_error_handling()

    return text, shift, action

def cipher_encryptor_decryptor(text, shift):
    output_text = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            offset = ord('A') if char.isupper() else ord('a')
            output_char = chr((ord(char) - offset + shift) % 26 + offset)
            output_text += output_char
        else:
            output_text += char  # Keep non-alphabetic characters as they are
    return output_text

def main():
    text, shift, action = user_input()
    result_text = cipher_encryptor_decryptor(text, shift)
    if action == '1':
        print(f"Encrypted text: {result_text}")
    elif action == '2':
        print(f"Decrypted text: {result_text}")

# Start the program
main()
