# import  sys
# a = ''
# b = 'a'
# c = 'ab'
# d = 'abc'
# ----------------------------
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))
# ----------------------------
# s1 = list(input())
# s2 = input()
# print(s1) # ['a','b','c']
# print(s2) # abc
# ----------------------------
# s = input() # abc
# print(s[0]) # a
# print(s[1]) # b # 스트링 형태임에도 리스트를 뽑아낼 수 있다. -> iterable
# s[0] = 'A' # TypeError: 'str' object does not support item assignment
# ----------------------------
# def strlen(a): # '\0'을 만나면 '\0'을 제외한 글자수를 리턴
#     i = 0
#     while a[i] != '\0':
#         i += 1
#     return i

# a = ['a', 'b', 'c', '\0']
# print(strlen(a))
# ----------------------------
# a = 'tired'
# arr = list(a)
# N = len(arr)
#
# for i in range(N//2):
#     arr[i], arr[N-1-i] = arr[N-1-i], arr[i]
# print(arr)
# ----------------------------


