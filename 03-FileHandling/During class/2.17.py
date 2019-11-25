import re
txt='To be, or not to be, that is the question'
pattern = re.compile(r'[^\s\daeoiyu,.]')
matches = pattern.findall(txt)
print(matches)