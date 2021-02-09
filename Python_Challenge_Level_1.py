text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
output = ''
for i in text:
    if i == ' ':
        output = output + ' '
    elif i == "'":
        output = output + "'"
    elif i == '.':
        output = output + '.'
    else:
        x = alphabets.find(i)
        y = x + 2
        output = output + alphabets[y % 26]
        y = 0

print(output)
