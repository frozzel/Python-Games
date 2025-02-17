with open("caesar.txt") as file:
    print(f"\033[35m {file.read()}\033[0m")  
    
run = True
while run:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("\033[0mType 'encode' to encrypt, type 'decode' to decrypt:\n \033[35m").lower()
    text = input("\033[0mType your message:\n \033[35m").lower()
    shift = int(input("\033[0mType the shift number:\n \033[35m"))

    def caesar(text, shift, direction):
        if direction == "decode":
            shift *= -1
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift
                if new_position > 25:
                    new_position = new_position - 26
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += letter
        print(f"\033[0mThe {direction}d text is \033[35m{cipher_text}\033[0m")
        run_again = input("Would you like to go again? Type 'yes' or 'no'  \033[35m").lower()
        if run_again == "no":
            global run
            run = False
            print("\033[0m 👋 Goodbye, have a great day! 👋")
        
        

    if direction == "encode" or direction == "decode":
        caesar(text, shift, direction)
    else:
        print("Invalid input")