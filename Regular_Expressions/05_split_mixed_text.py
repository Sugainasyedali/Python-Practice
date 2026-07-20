import re

text = "Apple, Banana; Mango Orange"

result = re.split(r"[,; ]+", text)

print(result)