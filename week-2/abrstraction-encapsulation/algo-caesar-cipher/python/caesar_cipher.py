def caesar_cipher(string_to_encrypt: str, shift_amount: int) -> None:
    #making const-like variables to indicate the bounds for the letter ranges
    LOWERCASE_UPPER_BOUND = 122
    LOWERCASE_LOWER_BOUND = 97
    
    UPPERCASE_UPPER_BOUND = 90
    UPPERCASE_LOWER_BOUND = 65
    
    NUMBER_OF_LETTERS_IN_ALPHABET = 26
    
    encrypted_message = ""# initialized as an empty string to append to
    #for loop to iterate thru the string and check the ascii values of the characters
    for char in string_to_encrypt:
        
    #using conditional statments to check if it is a capital letter, lowercase, or if we should skip and just append
    #lowercase in regular instances will be most common therefor it is checked for first    
        # if LOWERCASE_LOWER_BOUND <= ord(char) <= LOWERCASE_UPPER_BOUND:
        if char.islower():
            ###is alpha[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
            
            if (ord(char) + shift_amount) > LOWERCASE_UPPER_BOUND: 
                char = chr((ord(char) + shift_amount) - NUMBER_OF_LETTERS_IN_ALPHABET)
            elif (ord(char) + shift_amount) < LOWERCASE_LOWER_BOUND:
                char = chr((ord(char) + shift_amount) + NUMBER_OF_LETTERS_IN_ALPHABET)
            else:
                char = chr(ord(char) + shift_amount)

        # elif UPPERCASE_LOWER_BOUND <= ord(char) <= UPPERCASE_UPPER_BOUND:
        if char.isupper():

            if (ord(char) + shift_amount) > UPPERCASE_UPPER_BOUND: 
                char = chr((ord(char) + shift_amount) - NUMBER_OF_LETTERS_IN_ALPHABET)
            elif (ord(char) + shift_amount) < UPPERCASE_LOWER_BOUND:
                char = chr((ord(char) + shift_amount) + NUMBER_OF_LETTERS_IN_ALPHABET)
            else:
                char = chr(ord(char) + shift_amount)
            
        encrypted_message += char
    return encrypted_message
    