fruit_count={}

for i in range(5):
    fruit=input("Enter your favorite fruit: ")

    if fruit in fruit_count:
        fruit_count[fruit]+=1
    else:
        fruit_count[fruit]=1

for key, value in fruit_count.items():
    print(key,":",value)