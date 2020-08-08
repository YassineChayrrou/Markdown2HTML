import re

text = "this is my **text** ok i hop**e** this works __well__"
match = re.findall('\*\*.*?\*\*', text)
for i in match:
      text = text.replace(i, "<em>" + i[2:-2] + "</em>")
print(text)
