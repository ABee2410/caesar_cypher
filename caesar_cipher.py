def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value < 32:
        new = 31 - unicode_value
        new_value = 126 - new
        
    elif unicode_value > 126:
        new = unicode_value - 126
        new_value = 31 + new

    else:
        new_value = ord(letter) + shift_amount
        
    
    new_letter = chr(new_value)

    return new_letter

def encrypt(message, shift_amount):
    encryption = ""
    for letter in message:
        encryption += shift(letter, shift_amount)
        
    return encryption

def decrypt(encrypted_message, shift_amount):
    decryption = ""
    for letter in encrypted_message:
        decryption += shift(letter, shift_amount)
        
    return decryption

secret_message = "A well-set paragraph of text is not supposed to wow the reader; the wowing should be left to the idea or observation for which the paragraph is a vehicle. In fact, the perfect paragraph is unassuming to the point of near invisibility."
encrypted_message = encrypt(secret_message, 3)


print(secret_message)
print(encrypted_message)
print(decrypt(encrypted_message, -3))
