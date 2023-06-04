import os
import argparse

banner = """
┬─┐┌─┐┬  ┬┌─┐┬─┐┌─┐┌─┐  ┌─┐┬┌─┐┬ ┬┌─┐┬─┐
├┬┘├┤ └┐┌┘├┤ ├┬┘└─┐├┤   │  │├─┘├─┤├┤ ├┬┘
┴└─└─┘ └┘ └─┘┴└─└─┘└─┘  └─┘┴┴  ┴ ┴└─┘┴└─
"""

def reverse_cipher(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                cipher_char = chr(155 - ord(char))
            else:
                cipher_char = chr(219 - ord(char))
        else:
            cipher_char = char
        ciphertext += cipher_char
    return ciphertext

def encrypt_text(plaintext):
    return reverse_cipher(plaintext)

def decrypt_text(ciphertext):
    return reverse_cipher(ciphertext)

# Print banner
os.system("clear")
print(banner)

# Command-line argument parser
parser = argparse.ArgumentParser(description='Reverse Cipher - A simple tool that allows you to encrypt or decrypt text using a basic substitution cipher.')

# Encryption argument
parser.add_argument('-e', '--enc', action='store_true', help='Encrypt the text')

# Decryption argument
parser.add_argument('-d', '--dec', action='store_true', help='Decrypt the text')

# Text argument
parser.add_argument('-t', '--text', type=str, help='Text to be processed')

# File argument
parser.add_argument('-f', '--file', type=str, help='Path to the input file')

# Output argument
parser.add_argument('-o', '--output', type=str, help='Path to the output file')

args = parser.parse_args()

if args.enc and args.dec:
    print("Error: Please specify either encryption (-e/--enc) or decryption (-d/--dec), not both.")
elif not args.enc and not args.dec:
    print("Error: Please specify either encryption (-e/--enc) or decryption (-d/--dec).")
elif args.text is None and args.file is None:
    parser.print_help()
    print("Error: Please provide the text to be processed (-t/--text) or specify a file (-f/--file).")
else:
    if args.text:
        if args.enc:
            result = encrypt_text(args.text)
            print("Encrypted Text:", result)
        elif args.dec:
            result = decrypt_text(args.text)
            print("Decrypted Text:", result)
    elif args.file:
        try:
            with open(args.file, 'r') as file:
                text = file.read().strip()
                if args.enc:
                    result = encrypt_text(text)
                    if args.output:
                        with open(args.output, 'w') as output_file:
                            output_file.write(result)
                            print("Encryption result written to", args.output)
                    else:
                        print("Encrypted Text:", result)
                elif args.dec:
                    result = decrypt_text(text)
                    if args.output:
                        with open(args.output, 'w') as output_file:
                            output_file.write(result)
                            print("Decryption result written to", args.output)
                    else:
                        print("Decrypted Text:", result)
        except FileNotFoundError:
            print("Error: The specified file does not exist.")

# Check if no arguments are provided
if not any(vars(args).values()):
    parser.print_help()
