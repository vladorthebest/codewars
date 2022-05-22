
def check_word(word):
    if "'" in word:
        word = word.replace("'", '')
    if word.isalpha():
        return True
    else:
        return False

def sorter_dict(dictionary):
    list_dict = list(dictionary.items())
    list_dict.sort(key=lambda i:i[1])
    return list_dict[::-1]


def count_word(text):
    list_text = list(text.split())
    words = set(list_text)
    result = {}
    
    for word in words:
        if check_word(word):
            result[word] = list_text.count(word)
                
    return result

def replace_text(text):
    for i in text:
        if i.isalpha() or i.isalnum() or i=="'":
            pass
        else:
            text = text.replace(i, ' ') 
    return text

def top_3_words(text):
    text = text.lower()
    text = replace_text(text)
    dictionary = count_word(text)
    dict_list = sorter_dict(dictionary)
    dict_list = [x[0] for x in dict_list]
    return dict_list[:3]