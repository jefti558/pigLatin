def vowelTranslate(word):
    return (word + "yay")


def findFirstVowel(word):
    for i in range(len(word)):
        if word[i] in vowels or word[i] == 'y':
            return i

def consonantTranslate(word):
    vowelPos = findFirstVowel(word)
    if vowelPos:
        end = word[0:vowelPos]
        begin = word[vowelPos:]
        return begin + end + "ay"
    else:
        return word + "ay"



def translate(english):
    words = english.lower().split()
    result = []
    for word in words:
        firstChar = word[0]
        if (firstChar.isalpha()):
            if (firstChar in vowels):
                translated = vowelTranslate(word)
                result.append(translated)
            else:
                translated = consonantTranslate(word)
                result.append(translated)
        else:
            result.append(translated)

    for word in result:
        print(word, end = " ")
    print("\n")



vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    translate(input("Enter english: "))