def longest_word(text):
    words = text.split()
    if not words:
        return ""
    longest = words[0]
    for word in words[1:]:
        if len(word) > len(longest):
            longest = word
    return longest