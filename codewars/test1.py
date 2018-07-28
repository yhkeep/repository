# lists = [2,0]
# list1 = [4,2]
# print(abs(lists[0]-list1[0])+abs(lists[1]-list1[1])+len(lists))
# print(lists[3])
#v = v2 - v1 # Error: TypeError: unsupported operand type(s) for -: 'list' and 'list'
# 遍历存在值差问题
v1 = [2,0]
v2 = [3,2]
v3 = [4,2]
lists = [v1,v2,v3]
count = 0
for s in range(0,len(lists)-1):
    count += abs(sum(map(lambda x: x[0] - x[1], zip(lists[s],lists[s+1]))))
# 绝对值之和
v = abs(sum(map(lambda x: x[0]-x[1], zip(v2, v1))))
print(count+len(lists)+2)
# 算列表之和
import numpy
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a_array = numpy.array(a)
b_array = numpy.array(b)
c_array = a_array + b_array
d_array = a_array - b_array
print (c_array)
print (d_array)