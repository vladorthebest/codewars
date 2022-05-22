def anagrams(word, words):
    all = []
    for w in words:
        if set(word) == set(w) and len(word) == len(w):
            all.append(w)
    
    return all