# https://replit.com/@andy8787main/EnglishWordsMemory
print("輸入單字請打1")
ask = input()

if (ask == '1'): #輸入  
    print("如果要退出 請輸入0")
    while(True):
        #  英文
        print("請輸入英文")
        st = input() + '\n'
        if (st == '0\n'):
            quit()
        f = open('English.txt', 'a') # w寫入 a加入
        f.write(st)
        f.close

        #  中文
        print("請輸入中文")
        st = input() + '\n'
        f = open('Chinese.txt', 'a') # w寫入 a加入
        f.write(st)
        f.close

        #  詞性
        print("請輸入詞性")
        st = input() + '\n'
        f = open('Part.txt', 'a') # w寫入 a加入
        f.write(st)
        f.close
else: #放到list上面
    #  英文
    f = open('English.txt')
    English = []
    for line in f.readlines():
        English.append(line)
    f.close()

    #  中文
    f = open('Chinese.txt')
    Chinese = []
    for line in f.readlines():
        Chinese.append(line)
    f.close()

    #  詞性
    f = open('Part.txt')
    Part = []
    for line in f.readlines():
        Part.append(line)
    f.close()
    
print(English)
print(Chinese)
print(Part)




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
