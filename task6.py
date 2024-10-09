def check(s:str, file:str):
    list_n = s.lower().split()
    un_words = sorted(set(list_n))
    for i in range(len(un_words)):
        if un_words[i] in list_n:
            w_c = {word:list_n.count(word) for word in un_words}
    filename = open(file, 'w')
    for word in un_words:
        filename.write(f"{word} {w_c[word]}\n")
        
