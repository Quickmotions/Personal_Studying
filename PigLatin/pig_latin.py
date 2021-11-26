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
