def countVowCons(string):
    numvowels = 0;
    numcons = 0
    for char in string:
        if char in "AEIOUaeiou":
            numvowels = numvowels + 1
        elif char in "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm":
            numcons = numcons + 1
    return numvowels,numcons

phrase = input("Enter a phrase:")
[numvowels,numcons] = countVowCons(phrase)
print("There are "+str(numvowels)+" vowels and "+str(numcons)+" consonants in your string.")

exit()