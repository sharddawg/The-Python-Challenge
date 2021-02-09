text = open('challenge2.txt').read()
output = {}
for i in text:
    if i in output:
        output[i] = output[i] + 1
    else:
        output[i] = 1

for key, value in output.items():
    print(key, " : ", value)


# OR

# Terrible time complexity
for i in text:
    num = text.count(i)
    if num < 50:
        print(i, end='')
