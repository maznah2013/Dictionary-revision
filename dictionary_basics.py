#CREATE A DICTIONARY
countries={"UAE":"Dubai", "India":"Delhi", "UK":"England", "USA":"Washington", "France":"Paris"}
print(countries)

#ACCESS A VALUE FROM THE DICTIONARY
place=countries["UK"]
print(f"I want to visit {place}")

#ADD A NEW KEY VALUE TO THE DICTIONARY
countries["Pakistan"]="Lahore"
print(countries)

#ACCESS ALL THE KEYS FROM THE DICTIONARY
print("The keys in this dictionary are:")
for key in countries:
    print(key)
    
