# def replace_exclamation(s):
#     vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
#     # str = s.lower()
#     # for ch in vowels:
#     #     str = str.replace(ch, "!")
#     # return str
#     str = s.upper()
#     for ch in vowels:
#         str = str.replace(ch, "!")
#     return (str)
# s = "vaeyde"
# print(replace_exclamation(s))


# 将所有元音字母大写
# vowels = ['a', 'e', 'i', 'o', 'u']
# str = str(input('Please enter a string: '))
# str = str.lower()
# for ch in vowels:
#     str = str.replace(ch, ch.upper())
# print(str)
# vowels = ['a', 'e', 'i', 'o', 'u']
# str = str(input('Please enter a string: '))
# str = str.lower()
# for ch in vowels:
#     str = str.replace(ch, "!")
# print(str)

# 纠错501为soi
# def correct(string):
#     lists = [5, 0, 1]
#     string = string
#     for ch in lists:
#         if ch == 5:
#             string = string.replace(str(ch), "S")
#         if ch == 0:
#             string = string.replace(str(ch), "O")
#         if ch == 1:
#             string = string.replace(str(ch), "I")
#     return string
# string = "5o1"
# correct(string)
# 循环并且返回值
# def update_light(current):
#     print("开始")
#     yield 'yellow'
#     print("回车之后，再开始")
#     yield 'red'
#     print("回车之后，再次开始")
#     yield 'green'
# for i in update_light("green"):
#     print(i)
#     str = input("enter")
# def update_light(current):
#     if current.__eq__("green"):
#         return 'yellow'
#     if current.__eq__("yellow"):
#         return 'red'
#     if current.__eq__("red"):
#         return 'green'
# update_light("green")

# 四则运算获取最大值
import math
# def expression_matter(a, b, c):
#
#     d = a * (b + c)
#     e = a * b * c
#     f = a + b * c
#     g = (a + b) * c
#     h = a + b + c
#     return max(d,e,f,g,h)
# print(expression_matter(1,1,1))
# import math
# # def circle_circumference():
# #     cricle = 30
# #     c = 2 * math.pi * cricle
# #     return round(c,6)
# #
# # print(circle_circumference())
# 只取正数的和
# def positive_sum(arr):
#     # Your code here
#     count = 0
#     if len(arr) == 0:
#         return 0
#     for lists in arr:
#         if lists>=0:
#             count += lists
#     return count
# arr = [0,0,-1,0]
# print(positive_sum(arr))
# 含数字的字符串大小写转换
# def to_alternating_case(string):
#     number = (1,2,3,4,5,6,7,8,9,0)
#     str = ""
#     for s in string:
#         if s in number:
#            str += s
#         else:
#            str += s.swapcase()
#     return str
# string = "12dfaAdSDFD"
# print(to_alternating_case(string))
# def abbrevName(name):
#     # ['yang', 'han']
#     print(name.split())
#     # 使用join进行连接
#     return '.'.join(map(lambda x: x[0].upper(), name.split()))
# print(abbrevName("yang han"))
# 数字判断
# def isDigit(string):
#     import re
#     string = string.strip()
#     return bool(re.match("^[+-]?\d*\.{0,1}\d+$",string))
#
# print(isDigit(" -234.4 "))
# def two_sort(array):
#
#     # print(list(map(lambda x:x.istitle(),array)))#返回首字母大小写真假
#     #sorted可以直接对数组中的元素进行排序，如果要对对象进行排序操作，就可以使用lambda函数
#     print("***".join(sorted(array)[0]))
# two_sort(["all", "go", "on", "holiday", "somewhere", "very", "cold","Lets"])
# 108000
# 1.08
from decimal import Decimal


#
# def cockroach_speed(s):
#     return (int(s*100000/3600))
# cockroach_speed(1.09)
# def count_sheep(n):
#     # your code
#     # str = ""
#     # i = 1
#     # while i<=n:
#     #     str += "{} sheep...".format(i)
#     #     i += 1
#     # return str
#     return "".join("{} sheep...".format(i) for i in range(1,n+1))
# print(count_sheep(3))
# def switch_it_up(number):
#     #your code here
#     number_0_10 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
#     return number_0_10[number]
# print(switch_it_up(3))
# def bool_to_word(boolean):
#     # if boolean == True:
#     #     return "Yes"
#     # else:
#     #     return "No"
#     return "Yes" if boolean else "No"
# print(bool_to_word(False))
# def find_average(array):
#     if len(array)>0:
#         return sum(array)/len(array)
#     return 0
# array = [ 1, 2, 3 ]
# print(find_average(array))
# def opposite(number):
#     return abs(number) if number<0 else -number
# print(opposite(-23))
# def square_sum(numbers):
#     #your code here
#     # s = 0
#     # for x in numbers:
#     #     s += x**2
#     # return s
#     return sum(map(lambda x:x**2,numbers))
# print(square_sum([0, 3, 4, 5]))
# 返回负数
# def make_negative( number ):
#     # ...
#     return -number if number>0 else number or 0
# print(make_negative(3))
# def count_red_beads(N_blue):
#     # if N_blue>=2:
#     #     red_beads = 2*N_blue-2
#     #     return red_beads
#     # return 0
#     return 2*N_blue-2 if N_blue>=2 else 0
# print(count_red_beads(5))
# def solve(s):
#     print(list(map(str.isupper,s)))
#     return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()
# print(solve("CCce"))
# def binary_array_to_number(arr):
#     # string = ""
#     # for a in arr:
#     #     string += str(a)
#     # print(string)
#     # return str(int(string, 2))
# # 通过将遍历出来的str通过join将值传递到字符串中，然后以int("",2)整数输出
#     print("".join(map(str,arr)))
#     return int("".join(map(str, arr)), 2)
# print(binary_array_to_number([0, 0, 0, 1]))
# def predict_age(arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8):
#     # your code
#     arr = [arr1,arr2,arr3,arr4,arr5,arr6,arr7,arr8]
#     sumnum = 0
#     for a in arr:
#         sumnum += a**2
#     return int((sumnum**0.5)/2)
# predict_age(65, 60, 75, 55, 60, 63, 64, 45)
# 去重 但是顺序有问题
# def remove_duplicate_words(s):
#     s = s.split(" ")
#     sf = set()
#     for string in s:
#         if s.count(string) == 1:
#             sf.add(string)
#     return sf
# print(remove_duplicate_words("my cat is my cat fat"))

# def projectPartners(n):
#   '''Return combination'''
#   from functools import reduce
#   m = 2
#   m1 = reduce(lambda x, y: x * y, range(1, m + 1))
#   n1 = reduce(lambda x, y: x * y, range(1, n + 1))
#   b = n - m
#   if n-m == 0:
#       return 1
#   a =  reduce(lambda x, y: x * y, range(1, b + 1))
#   return int(n1/(m1*a))
# 替换其中不需要的字符串（下面涉及到的知识点有将列表中的数据转为字符串，然后使用replace进行替换，全部小写
# 然后将整体的字符串使用split(",")拆分为单个字符串并且以列表的形式返回并且需要判断输入的值是否为None或者[]）
# def remove_rotten(bag_of_fruits):
#     if bag_of_fruits==None:
#         return []
#     return " ".join(bag_of_fruits).replace("rotten", "").lower().split(",") if len(bag_of_fruits)!=0 else []
# print(remove_rotten(["rottenadsf,rottenaopoad"]))

# 取最小值
# def find_smallest_int(arr):
#     # Code here
#     return (min(arr))
# find_smallest_int([0, 1-2**64, 2**64])

# 国外车牌号
# def driver(data):
#     # Start driving here!
#     string = ""
#     if len(data[2]) < 5:
#         i = 5-len(data[2])
#         name = ""
#         while i>0:
#             name += "9"
#             i-=1
#         string += data[2]+name
#     else:
#         string += data[2][0:5]
#     string += data[3].split("-")[2][2]
#
#     mon = data[3].split("-")[1][0:3]
#     number_0_10 = ['Zero', 'Jan', 'Feb', 'Mar', 'Apr',
#                    'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     # 返回其索引
#     if number_0_10.index(mon)<10:
#         mon = "0"+str(number_0_10.index(mon))
#     else:
#         mon = str(number_0_10.index(mon))
#     if data[4].__eq__("F"):
#         m = int(mon)+50
#         string += str(m)
#     else:
#         string += mon
#     day = data[3].split("-")[0]
#     string += day
#     year = data[3].split("-")[2][3]
#     string += year
#     if data[1].__eq__(""):
#         string += data[0][0]+"9"
#     else:
#         string += data[0][0] + data[1][0]
#     string += "9AA"
#     return string.upper()
# # data = ["John", "James", "Smith", "01-Jan-2000", "M"]
# data = ["Andrew", "Robert", "Lee", "02-September-1981", "M"]
# print(driver(data))
# 列表遍历
# def work_needed(projectMinutes, freeLancers):
#     h = 0
#     m = 0
#     for lists in freeLancers:
#         h += lists[0]*60
#         m += lists[1]
#     result = projectMinutes - h - m
#     if result >= 60:
#         return "I need to work {} hour(s) and {} minute(s)".format(result // 60, result % 60)
#     if result <= 0:
#         return "Easy Money!"
#     else:
#         return "I need to work {} hour(s) and {} minute(s)".format(0, result)
# print(work_needed(0, [(0,20),(0,20),(0,20)]))
# 多种字母组合
# def scrolling_text(text):
#     lists = []
#     for s in range(len(text)):
#         lists.append(text.upper())
#         text = text[1:len(text)] + text[0:1]
#     return lists
# def scrolling_text(text):
#     text = text.upper()
#     return [ text[i:] + text[:i] for i in range(len(text)) ]
# print(scrolling_text("abc"))
# def str_replace(str, x, y):
#     if x == y:
#         return str
#     x_val = str[x:x+1]
#     y_val = str[y:y+1]
#     if x < y:
#         str = str[0:x] + y_val + str[x+1:y] + x_val + str[y+1:len(str)]
#     else:
#         str = str[0:y] + x_val + str[y+1:x] + y_val + str[x+1:len(str)]
#     return str
# #递归求结果
# def str_sort(str,x):
#
#     if x == len(str):               #当x为字符串的最大长度时返回当前字符交换的结果
#         global str_list
#         str_list.append(str)
#         return
#     for i in range(x,len(str)):
#         if str[i] not in str[x:i]:
#             str = str_replace(str,i,x)  #递归遍历第i个字符，
#             str_sort(str,x+1)
#             str = str_replace(str,x,i)  #恢复字符串原来的顺序，便于下次遍历
#         else:
#             return
# s = 'abc'
# global str_list
# str_list = []
# str_sort(s,0)
#
# print(len(str_list), str_list)
# def scrolling_text(text):
#     # lists = []
#     # for i in range(len(text)):
#     #     for j in range(len(text)):
#     #         lists.append(i)
#     # return lists  #返回值[0, 0, 0, 1, 1, 1, 2, 2, 2]
#     return [ i for i in range(len(text)) for j in range(len(text))]  #[0, 0, 0, 1, 1, 1, 2, 2, 2]
# print(scrolling_text("abc"))
# 遥控器
# 词= codewars
# c=a-b-c-OK=3  (2,0)
# o=c-d-e-j-o-OK=5  (4,2)
# d=o-j-e-d-OK=4 (3,0)
# e=d-e-OK=2 (4,0)
# w=e-j-o-t-y-x-w-OK=7 (2,4)
# a=w-r-m-h-c-b-a-OK=7 (0,0)
# r=a-f-k-p-q-r-OK=6 (2,3)
# s=r-s-OK=2 (3,3)
# 先给定每个单词一个坐标，每次的移动长度等于上一个坐标减去下一个坐标的绝对值再加上1，最初始坐标a(0,0)
# def tv_remote(word):
#     d = {
#         "a": [0, 0], "b": [1, 0], "c": [2, 0], "d": [3, 0], "e": [4, 0], "1": [5, 0], "2": [6, 0], "3": [7, 0],
#         "f": [0, 1], "g": [1, 1], "h": [2, 1], "i": [3, 1], "j": [4, 1], "4": [5, 1], "5": [6, 1], "6": [7, 1],
#         "k": [0, 2], "l": [1, 2], "m": [2, 2], "n": [3, 2], "o": [4, 2], "7": [5, 2], "8": [6, 2], "9": [7, 2],
#         "p": [0, 3], "q": [1, 3], "r": [2, 3], "s": [3, 3], "t": [4, 3], ".": [5, 3], "@": [6, 3], "0": [7, 3],
#         "u": [0, 4], "v": [1, 4], "w": [2, 4], "x": [3, 4], "y": [4, 4], "z": [5, 4], "_": [6, 4], "/": [7, 4],
#
#     }
#     count = abs(sum(map(lambda x: x[0] - x[1], zip(d["a"], d[word[0]]))))
#     x = 0
#     y = 0
#     for s in range(len(word)-1):
#         x += abs(d[word[s]][0]-d[word[s+1]][0])
#         y += abs(d[word[s]][1]-d[word[s+1]][1])
#     return x+y+count+len(word)
# print(tv_remote("a/a/a/a/"))
# print(tv_remote("."))
# def sort_my_string(S):
#     String = ""
#     string = ""
#     for s in range(len(S)):
#         if s % 2 != 0:
#             String += S[s]
#         else:
#             string += S[s]
#     return string + " " + String
#
# print(sort_my_string("YCOLUE'VREER"))
# 自己做的边境测试没有通过，4-8位是FFFF的情况有问题
# def communication_module(packet):
#     String = ""
#     String += packet[0:4] + "FFFF"
#     result = 0
#     if packet[4:8] == "0F12":
#         result = int(packet[8:12]) + int(packet[12:16])
#     if packet[4:8] == "B7A2":
#         result = int(packet[8:12]) - int(packet[12:16])
#     if packet[4:8] == "C3D9":
#         result = int(packet[8:12]) * int(packet[12:16])
#     if packet[4:8] == "":
#         result = -1
# 这时候即便是结果输出是对的但是没有将边境考虑进入，所以报错（总体来说还没有将加减乘三种边境考虑进入出错）
#     if packet[4:8] == "FFFF":
#         result = 10000000
#     result = str(result)
#     if int(result) < 0:
#         String.ljust(8, "0")
#     elif int(result) > 9999:
#         String.ljust(4, "9") + "0000"
#     else:
#         String += result.rjust(4, "0") + "0000"
#     String += packet[-4:]
#
#     return String
#

# def communication_module(packet):
#     header = packet[:4]
#     instruction = packet[4:8]
#     data1 = packet[8:12]
#     data2 = packet[12:16]
#     footer = packet[-4:]
#
#     if instruction == "0F12":
#         result = min(int(data1) + int(data2), 9999)
#     elif instruction == "B7A2":
#         result = max(int(data1) - int(data2), 0)
#     elif instruction == "C3D9":
#         result = min(int(data1) * int(data2), 9999)
#     else:
#         result = 0
#     result = str(result).zfill(4)
#     return header + 'FFFF' + result + '0000' + footer
# 完全看不懂的，但是看起来好简便，值得研究
# INSTRUCTIONS = {"0F12": int.__add__, "B7A2": int.__sub__, "C3D9": int.__mul__}
#
#
# def communication_module(packet):
#     header, inst, d1, d2, footer = (packet[i:i + 4] for i in range(0, 20, 4))
#     res = max(0, min(9999, INSTRUCTIONS[inst](int(d1), int(d2))))
#
#     return f"{header}FFFF{res:0>4}0000{footer}"
# print(communication_module("E4E4FFFFZ3Z3"))
# class Dictionary(dict):
#     def newentry(self,word,definition):
#         self[word]=definition
#     def look(self, key):
#         return self[key] if key in self else "Can't find entry for {}".format(key)
# if __name__ == '__main__':
#     # import time, datetime
#     # whatday = datetime.datetime(2018, 6, 17).strftime("%w")
#     # print(whatday)
#     d = Dictionary()
#     # d.newentry('Soccer', 'A sport')
#     d.newentry("Apple", "A fruit")
#     print(d.look("Soccer"))
# 单词出现的次数
# def sum_of_a_beach(beach):
#     # your code
#     lists = ["Sand","Water","Fish","Sun"]
#     b = beach.lower()
#     num = 0
#     for ls in lists:
#         if ls.lower() in b:
#             num += b.count(ls.lower())
#     return num
# print(sum_of_a_beach("123FISH321"))
# def potatoes(p0, w0, p1):
#     print(3/4)
#     print(3//4)
# print(potatoes(93, 129, 91))
# def is_smooth(arr):
#     # python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
#     d, m = divmod(len(arr), 2)
#     # 简单说True值等于1，False值为0
#     print(False + 1)  #1
#     print(True+1)  # 2
#     print(True*3) #3
#     print(False*3) #0
#     print(False/3)  #0
#     print(True*True) #1
#     # print(3/False)  #报错
#     # print(m == 0)。可作奇偶性的判断
#     print( arr[0] == arr[-1] == arr[d] + arr[d - 1] * (m == 0))
#     return arr[0] == arr[-1] == arr[d] + arr[d - 1] * (m == 0)
# print(is_smooth([7, 2, 2, 5, 10]))
# # 结尾填词
# def covfefe(s):
#     #covfefe !
#     # if "coverage" in s:
#     #     return s.replace("coverage","covfefe")
#     # else:
#     #     return s.__add__(" covfefe")
#     return s.replace("coverage","covfefe") if "coverage" in s else s.__add__(" covfefe")
# print(covfefe("double space "))

# def bear_fur(bears):
#     b = ['black', 'brown', 'white', 'dark brown', 'grey', 'light brown']
#     if bears[0] == bears[1] and bears[0] in b:
#         return bears[0]
#     elif "black" in bears and "brown" in bears:
#         return "dark brown"
#     elif "black" in bears and "white" in bears:
#         return "grey"
#     elif "brown" in bears and "white" in bears:
#         return 'light brown'
#     elif bears[0] not in b or bears[1] not in b:
#         return 'unknown'
# print(bear_fur(['black', 'black']))
# bear_fur(['black', 'brown']), 'dark brown'
# test.assert_equals(bear_fur(['black', 'white']), 'grey')
# test.assert_equals(bear_fur(['brown', 'white']), 'light brown')
#
# test.assert_equals(bear_fur(['green', 'brown']), 'unknown')
# def draw_stairs(n):
#     return "\n".join(" "*i+'I' for i in range(n))
#真真则为假，一假一真则为真
# print(draw_stairs(3))
# def xor(a,b):
#     return a!=b
# print(xor(xor(False, False), xor(False, False)))
# 几倍字符串输出
# def boolean_to_string(b):
#     return str(b)+""
# print(boolean_to_string(True))
# def repeat_str(repeat, string):
#     return string*repeat
# print(repeat_str(3, 'hello '))
# 将含有的元音字母使用！替换
# def replace_exclamation(s):
#     return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)
# print(replace_exclamation("sdfasdfa"))
# def expect(a,b):
#     a = str(a)
#     name = ""
#     name += a + b
#     return name
# print(expect(True,"sd"))
# 此处是圆类中对象半径属性的传递
# import math
# def circle_circumference(circle):
#     result =2 * circle.radius * math.pi
#     return round(result, 6)
# def feast(beast, dish):
#     return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False
# print(feast("brown bear", "bear claw"))
# def split_and_merge(string, sp):
#     string = string.split(" ")
#     result = ""
#     for i in string:
#         # 使单词组之间空格连接
#         result += "{}".format(sp).join(i)+" "
#     #     去掉出最后一个空格元素
#     return result.rstrip(" ")
# print(split_and_merge("My name is John","-"))
# def reverseseq(n):
#     return [x for x in range(n,0,-1)]
# def reverseseq(n):
#     return list(range(n, 0, -1))
# print(reverseseq(5)) #[5, 4, 3, 2, 1]

# 待解决

#
# def L(n, L0, L1, add):
#         if n == 1:
#             return L1
#         if n == 0:
#             return L0
#         else:
#             for i in range(n):
#                 print (L(n - 1,L0,L1,add) + L(n - 2,L0,L1,add) + add)
# L(5, 0, 0, 2)


# def insert_missing_letters(st):
# #     string = "abcdefghijklmnopqrstuvwxz"
# #     letter = ""
# #     for l in range(len(string)):
# #         for s in range(len(st)):
# #             letter += string[l]
# #             if st[s]==(string[l]):
# #                 string[l].__add__("")
# #     return letter
# #
# # print(insert_missing_letters("hello"))
# from math import sqrt
# def not_primes(a, b):
#     p = [p for p in range(a, b) if 0 not in [p % d for d in range(2, int(sqrt(p)) + 1)]]
#     lists =""
#     for i in range(a, b):
#         if i not in p:
#             lists += str(i)+" "
#     l = ['1','4','6','8','9','0']
# not_primes(2, 222)