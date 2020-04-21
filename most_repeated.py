'''a program to display most repeated letter in a sentence'''
word = "This is a common interview question"
word_frequency = {}
for character in word:
    if character in word_frequency:
        word_frequency[character] += 1
    else:
        word_frequency[character] = 1


sorted_char = sorted(word_frequency.items(),
                     key=lambda kv: kv[1], reverse=True)
print(sorted_char[0])
