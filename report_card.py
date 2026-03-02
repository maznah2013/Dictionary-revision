marks={"English":78, "Math":65, "Hindi":68, "Science":72}
total=0
for key in marks:
    total+=marks[key]
print(f"The total mark you have gotten is {total}")

avg=total//4
print(f"Your average is {avg}")