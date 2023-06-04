### Tool Name: Reverse Cipher

Description:
The Reverse Cipher tool allows you to encrypt or decrypt text using a basic substitution cipher. In this cipher, each alphabetic character is replaced with its corresponding character from the opposite end of the alphabet. The tool provides an easy way to apply this cipher to text either from the command line or from a file.

### Features:

- Encryption: You can encrypt plain text by running the tool with the -e or --enc option. The tool will apply the reverse cipher and provide the encrypted result.
- Decryption: You can decrypt encrypted text by running the tool with the -d or --dec option. The tool will reverse the reverse cipher and provide the decrypted result.
- Text Input: You can directly input the text to be processed using the -t or --text option.
- File Input: You can specify a file containing the text to be processed using the -f or --file option.
- Output to File: You can save the encryption or decryption result to a file by providing the -o or --output option along with the desired output file path.

### Installation 
```
git clone https://github.com/mkdirlove/ReverseCipher.git
```
```
cd ReverseCipher
```
```
python3 ReverseCipher.py -h

┬─┐┌─┐┬  ┬┌─┐┬─┐┌─┐┌─┐  ┌─┐┬┌─┐┬ ┬┌─┐┬─┐
├┬┘├┤ └┐┌┘├┤ ├┬┘└─┐├┤   │  │├─┘├─┤├┤ ├┬┘
┴└─└─┘ └┘ └─┘┴└─└─┘└─┘  └─┘┴┴  ┴ ┴└─┘┴└─

usage: ReverseCipher.py [-h] [-e] [-d] [-t TEXT] [-f FILE] [-o OUTPUT]

Reverse Cipher - A simple tool that allows you to encrypt or decrypt text using a basic substitution cipher.

options:
  -h, --help            show this help message and exit
  -e, --enc             Encrypt the text
  -d, --dec             Decrypt the text
  -t TEXT, --text TEXT  Text to be processed
  -f FILE, --file FILE  Path to the input file
  -o OUTPUT, --output OUTPUT
                        Path to the output file
                        
```

### Sample Usage:
To encrypt or decrypt text from the command line:
```
python3 ReverseCipher.py -e/-d -t "Text to be processed"
```
To encrypt or decrypt text from a file and save the result to another file:
```
python3 ReverseCipher.py -e/-d -f input.txt -o output.txt
```
Please note that the reverse cipher is a simple encryption method and should not be used for sensitive or critical information. It is primarily intended for educational or basic encoding purposes.

Feel free to customize and enhance the tool based on your requirements. Let me know if you have any further questions!
