print("Welcome to Railfence Technique") #welcome message

plain_text = input("Enter plaintext:   ")             #plaintext is taken from user
ciphertext = plain_text[::2] + plain_text[1::2]       #ciphertext is combination of odd values and even values of plaintext
print("The cipherText is:",ciphertext)                #ciphertext is printed out.