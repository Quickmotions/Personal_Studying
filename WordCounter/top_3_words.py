# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
# 26/08/2022 - Fergus Haak - Most frequent words in text finder

def top_3_words(text):
    top3 = []
    word_occurrences = {}
    text = [*text]
    new_text = ""
    for index in range(len(text)):

        if not text[index].isalpha():
            if not text[index - 1].isalpha() and not text[index + 1].isalpha() and index != 0:
                new_text += " "
                continue
        new_text += text[index]
    print(new_text)
    words = new_text.lower().split(" ")
    for word in words:
        if word == "":
            continue
        if word not in word_occurrences:
            word_occurrences[word] = 0
        word_occurrences[word] += 1
    word_occurrences = dict(sorted(word_occurrences.items(), key=lambda item: item[1], reverse=True))
    for i in range(3):
        if len(word_occurrences) >= i + 1:
            top3.append(list(word_occurrences.keys())[i])
    return top3


print(top_3_words("  //wont won't won't"))
print(" ".isalpha())
