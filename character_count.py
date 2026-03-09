#Write a function char_frequency(s) that takes a string s and returns a dictionary containing the frequency of each character in the string, ignoring spaces

def char_frequency(s):
    new_s=s.strip()
    dictionary={}
    for i in new_s:
        if i.isalpha():
            i=i.lower()
            if i in dictionary:
                dictionary[i]+=1
            else:
                dictionary[i]=1
    
    for key, value in dictionary.items():
        print(f"{key}: {value}")

char_frequency("Apple")