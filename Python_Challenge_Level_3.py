import re

text = open('challenge3.txt').read()
pattern = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text)
for patterns in pattern:
    print(patterns, end='')