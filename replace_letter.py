def replace(word, letter_to_replace, replacement):
    new_word = ""
    for letter in word:
        if letter == letter_to_replace:
            new_word += replacement
        else:
            new_word += letter
    return new_word


# Test            
new_word = replace("hollar", "h", "d")
print(new_word)
