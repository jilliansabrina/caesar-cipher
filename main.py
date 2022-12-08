import os
from caesar_art import logo
from caesar_art import end

# Caesar cipher encrypting or decrypting, depending on the direction.
def caesar(text, shift, direction):
  output = ''
  for char in text:
    # If the character is not a letter, no modifications are made.
    if not (ord(char) >= 97 and ord(char) <= 122):
      output += char
    # If the shift makes the ASCII character < 97, it loops around the end of the alphabet.
    elif ord(char) + shift * direction < 97:
      char_dif = 97 - (ord(char) + shift * direction)
      output += chr(123 - char_dif)
    # If the shift makes the ASCII character > 122, it loops around the start of the alphabet.
    elif ord(char) + shift  * direction > 122:
      char_dif = ord(char) + shift * direction - 122
      output += chr(96 + char_dif)
    else:
      output += chr(ord(char) + shift * direction)
  print(f'\nThe {"encrypted" if direction == 1 else "decrypted"} text is \'{output}\'.\n')

def main():
  # Welcome message
  print(f'Welcome to the Caesar Cipher!\n\n{logo}\n\n')
  
  direction = int(input("Type '-1' to decrypt, type '1' to encrypt: "))
  # If the direction entered is invalid, ask the user again.
  while direction != 1 and direction != -1:
    direction = int(input('The value entered is invalid. Please try again: '))
  
  text = input("Type your message: ").lower()
  shift = int(input("Type the shift number: "))

  # Validates that the shift entered isn't out of bounds.
  if shift > 26:
    shift %= 26

  # Invokes the cipher.
  caesar(text, shift, direction)

  # Asks if the user would like to continue using the cipher.
  answer = input('Type \'yes\' if you want to go again. Otherwise type \'no\'. ').lower()
  os.system('clear')

  while answer != 'yes' and answer != 'no':
    answer = input(f'\'{answer}\' is not a valid answer. Please try again: ')
  if answer == 'yes':
    return main()
  elif answer == 'no':
    print(f'\n\n{end}')

if __name__ == "__main__":
    main()