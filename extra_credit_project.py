# import os module
import os

# Define main function
def main():
    # invoke intro
    intro()
    # invoke get_user_selection
    get_user_selection()


# Define introduction function
def intro():
    # Contains introduction to program. Mainly print statements.
    print('    ------ Cipher It ------')
    print(' -------- Encrypt or Decrypt Your Files -------')
    print()
    print('      *******CAUTION********')
    print()
    print('This is a very simple cryptography program that is only to be used for educational purposes.')
    print('This should not be used for actual encryption.')
    print()
    print('Thank you :))')


# Define user selection function
def get_user_selection():

    # Display menu
    print()
    print(' ---------- Menu----------')
    print('>>>> 1. Encrypt or Decrypt Files')
    print('>>>> 2. More Information')
    print('>>>> 3. Exit')
    print()

    # Get user input for menu selection.
    while True:
        # Get user input.
        user_option = input('Please choose an option from the menu: ')
        print()

        # Use try except statements to see if user is inputting the correct values (integer value).
        try:
            user_option = int(user_option)
        except:
            print('You must enter a number.')
            continue
        
        # Use if-elif-else statements to check user's choice.
        if user_option == 1:
            # will execute encryption function.
            encryption() 
            break
        elif user_option == 2:
            # will execute more_info function.
            more_info() 
            break
        elif user_option == 3:
            # will execute end_program function.
            end_program() 
        else:
            # will continue the while loop if user did not enter number associated with menu option.
            continue 


# Define encryption function
def encryption():
    # Display message indicating that encryption option was chosen.
    print('''You\'ve chosen to encrypt or decrypt you\'re file.

        *****NOTE*****''')
    print()
    print('In order to encrypt or decrypt your files, you must enter a text file with a .txt extension.')
    print()
    
    # Use while loop for user validation.
    while True:
        # Get user input
        get_user_file = input('Please enter the name of the file you would like encrypted or decrypted: ')

        # Check if text extension is included in user input.
        if '.txt' in get_user_file:
            print()
            print('Please wait as I retrive your file...')
            print()

            # Use try except statement to check if file exists.
            try:
                # If file is found, open file and read through it.
                with open(get_user_file, 'r') as open_user_file:
                    print('File Found! Please wait as your file is processed...')
                    print()
                    read_user_file = open_user_file.read()
                    # Assign empty string to variable that will hold the encrypted or decrypted text.
                    ciphertext = ''
                    # Define shift number.
                    SHIFT_NUM = 13
                    
                    # iterate through file and encrypt or decrypt the text.
                    for char in read_user_file:
                        # Check if the iterator variable is in the alphabet.
                        if char.isalpha():
                            # Check if the iterator variable is uppercase.
                            if char.isupper():
                                shift_letters = ord(char) + SHIFT_NUM
                                if shift_letters > ord('Z'):
                                    shift_letters -= 26
                                ciphertext += chr(shift_letters)
                            else:
                                # Else statement executes if the iterator variable is lowercase and not uppercase.
                                shift_letters = ord(char) + SHIFT_NUM
                                if shift_letters > ord('z'):
                                    shift_letters -= 26
                                ciphertext += chr(shift_letters)
                        # Check if itrator variable is a digit.
                        elif char.isdigit():
                            shift_letters = ord(char) + SHIFT_NUM
                            if shift_letters > ord('9'):
                                shift_letters -= 10
                            ciphertext += chr(shift_letters)
                        else:
                            # Else statement executes if the iterator variable is neither a letter nor a number.
                            ciphertext += char

                # Use while loop for user validation.
                while True:
                    # Display message to user that a new file will be created.
                    print('To avoid overwriting your data, I will create a new file for you! Please enter a new name for your text file.')
                    print('*****Remember to use .txt when creating your new file!*****')
                    print()

                    # Get new file name from user.
                    create_new_file = input('Enter file name here: ')
                    print()

                    # Check if file name already exists. 
                    if os.path.isfile(create_new_file):
                        print('This file already exists. Please try again.')
                        print()
                        continue
                    
                    # Check if user included text extension.
                    if '.txt' in create_new_file:   # If text extension included, a new file will be created.
                        with open(create_new_file, 'w') as write_to_file:   # Open new file and write to it.
                            write_to_file.write(ciphertext)

                        # Display message that file has been written to and created. 
                        print('Process complete!')
                        print()
                        print('You\'re new file has been created.')
                        print()
                        break
                    else:
                        # Else statement will execute if user doesn't include text extension.
                        print('You must include a .txt as your extension.')
                        print()
                        continue
                break

             # If file not found, then except statement executes. 
            except:
                print('Oops! File not found.')
                print()
                
                # Use while loop for user validation.
                while True:
                    file_not_found = input('Enter 1 to try another file or 2 to exit the program: ')
                    print()
                    # Use try except to check if user entered correct value (integer value).
                    try:
                        file_not_found = int(file_not_found)
                        break
                    except:
                        print('You must enter a number.')

                # Use while loop for user validation.
                while True:
                    if file_not_found == 1:
                        encryption()
                    elif file_not_found == 2:
                        end_program()
                    else:
                        continue
        else:
            # Else statement executes if text extension not included.
            print('You must include a .txt as your extension.')
            continue
        
    # Invoke start_over function
    start_over()

# Define more information function
def more_info():
    # Gives more information about program and the purpose of the program. Mainly print statements.

    print('You\'ve chosen to view more information about this program.')
    print()
    print('The purpose of this program is to encrypt and decrypt files.')
    print('This program uses a very basic substitution cipher called Casear Cipher, which is not very secure.')
    print('I created this program as a way to experiment with encryption.')
    print('Please use this for educational purposes and not for actual encryption.')
    print('Thank you for using my program.')
    print()

    # will invoke the start_over function
    start_over() 

# Define start over function
def start_over():
    # Ask if user would like to run the program again.
    print('Would you like to run the program again or exit the program?')
    print()

    # Use while loop for user validation
    while True:
        user_choice = input('Enter 1 to run the program again or 2 to exit the program: ') # Get user input
        print()

        # Use try except statements to check if user is inputting the correct value (integer value).
        try:
            user_choice = int(user_choice) 
        except:
            print('You must enter a number.') 
            continue

        # Use if-elif-else statements to check if user entered number from options.
        if user_choice == 1:
            print('You\'ve chosen to run the program again.')
            print()
            # Invoke main function. Will start the program over.
            main() 
            break
        elif user_choice == 2:
            # Invoke end_program function. Will exit the program.
            end_program() 
        else:
            # Continue while loop if user didn't enter a number from options.
            print('You must enter 1 to run the program again or 2 to exit.')
            print()
            continue

# Define end of program function
def end_program():
    # Prints out goodbye message
    print()

    print('''You\'ve chosen to exit the program. 
                                    
        ~~ Goodbye ~~''')
    # exits the program
    exit()


# Invoke main function
main()
