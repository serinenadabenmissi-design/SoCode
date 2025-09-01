math= ["charlie", "kevin","alise", "bob", "leo"]
physics= ["jack","paolo","alex","bob","charlie"]

math.append(input("enter a new student in math: "))

physics.insert(2,input("enter a new student in physics: "))
math.sort()
physics.sort()
print(math)
print(physics)
name=input("enter a student name to remove: ")

for student in physics:
    if name==student:
        physics.remove(student)

print(physics)
print(math)
