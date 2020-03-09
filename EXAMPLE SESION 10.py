first_indent_counter=0
second_indent_counter=0
third-indent_counter=0


for i in range (0,5):
    first_indent_counter+=1 
    print("first indentation")
    for j in range (0,3):
        print ("second indentation")
        for k in range(0,10):
            print ("Third indentation")
    print ("Forth indentation")
print("Fifth Indentation")
