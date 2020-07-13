# author：wuziwei   
# @time:2020-07-05 16:58
# coding:-*- utf-8 -*-

# 将字符转换为整数表示,只能转换一个字符
a = ord('吴')
# 将整数转换为字符表示，只能转换一个字符
b = chr(21556)
print(a, b)

# 字符串类型
c = 'abc'
# bytes类型,仅能转换ASCII编码
d = b'adc'
print(type(d), type(c))

c1 = '会当凌绝顶，一览众山小'
# str转换成bytes,解码需对应编码
d1 = c1.encode('utf8')
c2 = b'\xe4\xbc\x9a\xe5\xbd\x93\xe5\x87\x8c\xe7\xbb\x9d\xe9\xa1\xb6\xef\xbc\x8c\xe4\xb8\x80\xe8\xa7\x88\xe4\xbc\x97\xe5\xb1\xb1\xe5\xb0\x8f'
# bytes转换成str,解码需对应编码
d2 = c2.decode('utf8')
print(d1, d2)
