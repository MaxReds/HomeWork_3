str1 = str(input("Eneter a word: ").replace(' ','').lower())
str2 = str(input("Enter a word: ").replace(' ','').lower())
str1_list = sorted(str1)
str2_list = sorted(str2)
if str1_list == str2_list:
        print("Yes")
else:
        print("No")



