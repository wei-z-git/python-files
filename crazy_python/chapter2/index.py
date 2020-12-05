# s = 'crazyit.org is good site'
x = open('1.txt', 'r')
s = x.read()
x.close()
# # print('内容是：%s' %d)
# # print('mantou在 %s  个位置：' % (d.find('mantou')-1))
#
# print(s.split(None, 2))
# print(s.split('.'))
#
# s2 = s
# print(s2)
# print(s+', '+s2)
#
# # print((s.startswith('craz')))
# # print(s.endswith('org'))
# # print(s.find('org'))
# # help(str.startswith)

print(not False)

Name = 'mantou'
price = 0
version = 2.0
if Name.endswith('mantou') and price < 10 or version == 1.0 :
    print('buy it')
else:
    print('not buy')
