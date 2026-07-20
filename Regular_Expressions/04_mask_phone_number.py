import re
text = "Call me at 9876543210"
print(re.sub(r"\d","*",text))