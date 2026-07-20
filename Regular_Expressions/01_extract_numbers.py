import re
text = "I scored 85 in Math, 91 in Science and 78 in English."
print(re.findall(r"\d+",text))