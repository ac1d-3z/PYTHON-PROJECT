c = input("Enter an Alphabet Character:")

lo_c = c.lower()

if lo_c in ['a','e','i','o','u']:
    print(c,"is a vowel")
elif lo_c.isalpha():
    print(c,"is a consonant")
else:
    print("Invalid Input please enter an alphabet....")