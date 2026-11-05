def analyze_text(text):
    words_list = text.split()
   
    if not words_list:
        return None

    words_count = len(words_list)

    letters_count = 0
    for a in text:
        if a != " ":
            letters_count += 1

    longest = words_list[0]
    for word in words_list:
        if len(word) > len(longest):
            longest = word

    shortest = words_list[0]
    for word in words_list:
        if len(word) < len(shortest):
            shortest = word

    seen = set()
    for word in words_list:
        seen.add(word.lower())
    unique_count = len(seen)

    return {
        "words": words_count,
        "letters": letters_count,
        "longest_word": longest,
        "shortest_word": shortest,
        "unique_words": unique_count
    }

text = input("Введите предложение: ")
result = analyze_text(text)
print(result)