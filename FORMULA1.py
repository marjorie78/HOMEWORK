
#BOOK2
unique_words=[]
fp=open("BOOK2.txt.py", "r")
punc = ".,!?-"
text=""
for each_line in fp:
    for p in punc:
        #replace punc
        each_line = each_line.replace(p,"")
        #consctruct letter by letter and do not add the punc
        for letter in each_line:
            if letter not in punc:
                text=text+letter
    words_list = each_line.split()
    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)

print(len(unique_words))
#BOOK1

unique_words=[]
fp=open("BOOK1.py.txt", "r")
punc = ".,!?-"
for each_line in fp:
    for p in punc:
        each_line = each_line.replace(p,"")
    words_list = each_line.split()
    for word in words_list:
        if word not in unique_words:
            unique_words.append(word)

print(len(unique_words))