# Move the first letter of each word to the end of it, then add
# "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    output = ""
    words = text.split(' ')
    for word in words:
        if word not in ['!', '.', ',', '?']:
            output += (word[1:] + word[0] + "ay ")
        else:
            output += word + " "
    return output[:-1]


def better_pig_it(text):
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
