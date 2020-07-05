import pprint
def putInfoToDict(fileName):
    fileName1 = open(fileName,'r').readlines()
    stu = []
    stu_map = {}
    for i in fileName1:
        stu.append(i.replace(' ','').replace('\t','').replace("'",'').replace(';','').replace('\n',''))
    for one in stu:
        if one == '':
            break
        name = one.replace('(','').replace(')','').split(',')[-2]
        lessonid = one.replace('(','').replace(')','').split(',')[1]
        checkintime = one.replace('(','').replace(')','').split(',')[0]
        stu_map.update({name:[{'lessonid':lessonid,'checkintime':checkintime}]})
    return stu_map
pprint.pprint(putInfoToDict('0005_1.txt'))