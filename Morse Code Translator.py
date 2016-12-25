# Morse Code Translator
# by Raphael Gutierrez (https://facebook.com/raphael.gutierrez.17)
# Licensed under MIT (https://github.com/ralphgutz/Morse-Code-Translator/blob/master/LICENSE)

print('=' * 37)
print("= WELCOME TO MORSE CODE TRANSLATOR! =")
print('=' * 37)

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
              'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
              'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
              'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
              '0': '-----', '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '..--.', 
              ':': '---...', '\"': '.-..-.', '\'': '.----.', '=': '-...-'}

morse_code_rev = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
              '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
              '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
              '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
              '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
              '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
              '-----': '0', '.-.-.-': '.', '--..--': ',', '..--..': '?', '..--.': '!', 
              '---...': ':', '.-..-.': '\"', '.----.': '\'', '-...-': '='}

def main():
    while True:
        print("\nPress 1 for Text-to-Morse Converter.")
        print("Press 2 for Morse-to-Text Converter.")
        print("Press 'X' to exit.")
        chc_input = input("Input: ")
        if chc_input == '1':
            morse()
        elif chc_input == '2':
            morse_rev()
        elif chc_input == 'X' or chc_input == 'x':
            break
        else:
            print("\nInvalid Input!")

def morse():
    print("\nYou've chosen the TEXT-TO-MORSE CONVERTER.")
    user_input = input("\n Your text: ")
    print("")
    for char in user_input:
        print(' ', char, '>', morse_code[char.upper()])
    main()

def morse_rev():
    print("\nYou've chosen the MORSE-TO-TEXT CONVERTER.")
    user_input = input("\n Your code: ")
    print("")
    print(' ', user_input, '>', morse_code_rev[user_input])
    main()

if __name__ == '__main__':
    main()