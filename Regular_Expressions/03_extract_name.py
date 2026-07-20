import re
name = "Ali, Sugaina"
element = re.search(r"^(.+),(.+)$",name)
print(element.group(1))
print(element.group(2))