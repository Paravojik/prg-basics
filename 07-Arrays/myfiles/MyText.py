def numberOfWords(text):
    for sep in ".!":
        text = text.replace(sep, " ")
    words = text.split()
    return len(words)
def orderedWords(text):
    for sep in ".!":
        text = text.replace(sep, " ")
    words = text.split()
    words.sort(reverse=True, key=lambda x:len(x))
    return words

def alpWords(text):
    for sep in ".!":
        text = text.replace(sep, " ")
    words = text.split()
    return sorted(words,key=lambda x:x.lower())