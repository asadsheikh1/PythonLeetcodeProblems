def stringManipulation(word):
    vowels = "aeiou"
    if word[0] in vowels:
        result = word + "way"
        return result
    else:
        result = word[1:] + word[0] + "ay"
        return result


print(stringManipulation("air"))
print(stringManipulation("python"))
print(stringManipulation("asad"))
print(stringManipulation("sheikh"))
