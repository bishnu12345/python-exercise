def is_vowel(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if alphabet in vowels:
        return True
    else:
        return False


alphabets = ['p', 'q', 'i', 's', 'e']
results = filter(is_vowel, alphabets)
print(list(results))  # results object is typecast into list
