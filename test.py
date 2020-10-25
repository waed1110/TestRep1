inp = input('Enter file name: ')
fopen = open(inp)
dic = dict()

for lines in fopen:
    lines = lines.rstrip()
    line = lines.split()
    if len(line) < 3: continue
    if line[0] == 'From':
        dic[line[1]] = dic.get(line[1],0) + 1
bigcount = None
bigword = None
for email,count in dic.items():
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count
print(bigword, bigcount)
