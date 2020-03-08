unique_words=[]
fp=open("BOOK1.py", "r")
punct = ".,!?-"
for each_line in fp:
    for p in punct:
        each_line=each_line.replace(p,"")
            for each_line in fp:
                each_line=each_line.split("")

for word in each_line:
    if word==word:
        word = unique_words.remove(word)
            if not word in unique_words:
                word = unique_words.append(word)

number_words=0
for word in unique_words:
        number_words=word+1
            print("there are",number_words,"words")
