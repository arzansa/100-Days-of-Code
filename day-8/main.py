from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

restart = True

while(restart):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'e':
        direction = 'encode'
    if direction == 'd':
        direction = 'decode'

    while direction != 'encode' and direction != 'decode':
        print('please enter only encode or decode')
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction == 'e':
            direction = 'encode'
        if direction == 'd':
            direction = 'decode'

    text = input("Type your message:\n").lower()

    while not text.replace(' ','').isalnum:
        print('please enter only letters and numbers')
        text = input("Type your message:\n").lower()


    shift = input("Type the shift number:\n")

    while not shift.isnumeric():
        print('please enter only numbers')
        shift = input("Type the shift number:\n")

    shift = int(shift)
    if shift > 26:
        shift = shift % 26



    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        #e.g. 
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

    def caesar(text, shift, direction):
        encrypted_text = ''
        for i in range(0, len(text)):

            try:
                if (direction == 'encode'):
                    try:
                        encrypted_text += alphabet[alphabet.index(text[i])+int(shift)]       
                    except IndexError as e:
                        encrypted_text += alphabet[alphabet.index(text[i])-(26-int(shift))]
                if (direction == 'decode'):
                    try:
                        encrypted_text += alphabet[alphabet.index(text[i])-int(shift)]       
                    except IndexError as e:
                        encrypted_text += alphabet[alphabet.index(text[i])+(26-int(shift))]
            except ValueError:
                encrypted_text += str(text[i])

        return encrypted_text


    print("Here's your result: " + caesar(text, shift, direction))

    again = ''
    while again != 'y' and again != 'n':
        again = input('Would you like to go again? (y/n)\n').lower()
        if again != 'y' and again != 'n':
            print('Only y or n please')

    if again == 'n':
        restart = False

print('Adios')