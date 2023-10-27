# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE

# print the data
str_data = {
    "Length": len(test_str),
    "digits": len(list(num for num in test_str if num.isnumeric())),
    "Punctuation": len(
        list(punc for punc in test_str if punc in string.punctuation)
    ),
    "Unique Letters": (
        unique_letters := set(i for i in test_str if i.isalpha())
    ),
    "Unique Count": len(unique_letters),
}
pprint.pp(str_data)
