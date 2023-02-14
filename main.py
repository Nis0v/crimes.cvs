import csv
l = list()
ls = 0
with open("Crimes.csv", "r") as f:
    read = csv.reader(f)
    for text in read:
        if "2015" in text[2]:
            l.append(text[5])
            n = list(set(l))
for n1 in n:
    g = l.count(n1)
    if g >= len(l)/2:
        ls = g
        h = n1
        break
    elif g > ls:
        ls = g
        h = n1
print(h, ls)
with open("Crimes1.csv", "w") as f:
    f.write(h)
