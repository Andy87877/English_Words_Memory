# https://replit.com/@andy8787main/EnglishWordsMemory
''' test
# 輸入
path = 'test.txt'
f = open(path, 'w') # w寫入 a加入
f.write('Hello World\n')
f.write('123\n')
f.write('123.45\n')
f.close()
# 讀取
f = open(path)
l = []
for line in f.readlines():
    l.append(line)
print(l)
f.close()
'''
ask = input()
print("輸入請打1 輸出請打2")

if (ask == '1'): #輸入  
    path = 'all.txt'
    f = open(path, 'a') # w寫入 a加入 
    while(True):
        st = input() + '\n'
        f.write(st)
elif (ask == '2'):
    path = 'all.txt'
    f = open(path)
    l = []
    for line in f.readlines():
        l.append(line)
