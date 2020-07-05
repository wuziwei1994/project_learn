file=open(r'./file1.txt').readlines()
file_2=open(r'./file2.txt','w')
for i in file:
    salary= i.replace(' ','').replace('\n','').split(':')[-1]
    name= i.replace(' ','').replace('\n','').split(':')[1].split(';')[0]
    tax = int(int(salary)*0.1)
    income = int(salary)-tax
    file2='name:{:<10};salary:{:>10};tax:{:>10};income:{:>10}\n'.format(name,salary,tax,income)
    file_2.write(file2)
    print(file2)
file_2.close()






