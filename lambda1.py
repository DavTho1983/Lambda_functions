#Standard function
def f(x):
    return 3*x + 1

#Anonymous function
g = lambda x: 3*x + 1
print(g(2))

#Combine first and last name
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("   leonard", "EULER"))

#lambda x1, x2, ..., xn: <expression>
#no multiline lambda functions

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
