d={"eng-spa":{"yes":"si"},"eng-ger": {"yes":"ja"}}
print (d["eng-ger"]["yes"])
print(d["eng-spa"]["yes"])

#common words

punctuation2 = ",.;:!?\"'()[]{}-*<>"

def common_words(file_name):

    fd = open(file_name, "r")
    d = {}
    for line in fd:
        #"line"="I,can; see a cat."
        for c in punctuation2:
            line = line.replace(c, " ")
            # "line"="I can see a cat"
        words = line.split()
        #words= ["I","can","see""a""cat"]
        for word in words:
            # word= ["I",then "can",then see" then "a""cat"]
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
                #d={"harry":100, "potter":50, "the":20}
    #get the values from the dictionary
    values = list(d.values())
    values.sort(reverse=True)
    #values = [200,100,50] what are the keys matching???
    #now need to find the words that match to these values
    common = []
    for numbers in values[:10]:
        for keys in d:
            if d[keys] == numbers:
                common.append((keys, numbers))
    print("the most common words are:")

    for i in common:
        print(i[0], i[1], "times")


common_words("BOOK2.txt.py")
common_words("BOOK1.py.txt")