sentence = input("Please write a sentence: ")

words = sentence.split()


word_count = len(words)
print(f"Word count is: {word_count}")


word_frequency = {}
for word in words:
    word = word.lower() 
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1


print("Word frequencies:")
for word, count in word_frequency.items():
    print(f"{word} - {count}")


longest_word = max(words, key=len)
print(f"The longest word is: {longest_word}")
