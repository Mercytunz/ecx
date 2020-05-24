"""
Create a function string_test that accepts a sentence(s) in string form as a
parameter and calculates the number of uppercase letters and lowercase in the
string.
"""
def string_test(sentence):
    n = 0
    m = 0
    for i in sentence:
        if i.isupper() is True:
            n += 1

        elif i.islower() is True:
            m += 1
    return f"Number of lowercase letters is {m}\n Number of upper case letters is {n}"
letter = string_test("The quick Brown Fox")
letter1 = string_test("My name is Nwosu Itinuoluwawa Mercy, a Student of 30daysofcode")

print(letter)
print(letter1)
            
