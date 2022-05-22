def duplicate_count(text):
    text = list(text.lower())
    text1 = text[:]
    n = 0
    print(text)
    
    for item in text:
        print(item, text1)
        try:
            text1.remove(item)
        except:
            pass
        if item in text1:
            n+=1
            while item in text1:
                text1.remove(item)

    return n