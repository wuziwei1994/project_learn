def fileData(str):
    file = './log.txt'
    jpeg = []#用列表的方式存储jpeg的文件大小
    sum = 0#初始化sum值为0
    f = open(file,'r').readlines()
    for one in f:
        a = one.split('\t')[0:2]
        if str in a[0]:
            jpeg.append(a[1])
    for i in jpeg:
        sum = sum + int(i)
    return sum
print(fileData('png'))
print(fileData('jpeg'))
print(fileData('json'))

