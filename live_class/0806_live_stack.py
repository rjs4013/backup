# 스택의 구현
# def push(item, size):
#     global top
#     top += 1
#     if top == size:
#         print('overflow!')
#     else:
#         stack[top] = item
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10,size)
# top += 1            # push(20)
# stack [top] = 20    #
# -----------------------------
# def pop():
#     global top
#     if top == -1:
#         print('underflow')
#         return 0
#     else:
#         top -= 1
#         return  stack[top+1]
# print(pop())
# ------------------------------
# if top > -1: # pop()
#     top -= 1
#     print(stack[top+1])
# ------------------------------
# stack = []
# stack.append(1) # push(1)
# stack.append(2) # push(2)
# stack.append(3) # push(3)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# ------------------------------
# STACK_SIZE = 10
# stack = [0] * 10
# top = -1
#
# top += 1    # push(1)
# stack[top] = 1
# top += 1    # push(2)
# stack[top] = 2
# top += 1    # push(3)
# stack[top] = 3
#
# top -= 1
# print(stack[top+1])
# print(stack[top])
# top -= 1
# print(stack[top])
# top -= 1
# --------------------------------
# def f2(c,d):
#     return c-d
#
# def f1(a,b):
#     c = a+b
#     d = 10
#     return f2(c,d)
# a = 10
# b = 20
# print(f1(a,b))
# --------------------------
# f(n)
# if n == 1:
#     return 1
# else:
#     return n*f(n-1)
# --------------------------
# def fibo(n):
#     if n < 2:
#         return n
#     else :
#         return  fibo(n-1) + fibo(n-2)
# ----------------------------
# # 모든 배열 원소에 접근하기
# def f(i,N):  # i: 접근할 원소 인덱스, N: 크기
#     if i == N:
#         return
#     else :
#         print(arr[i])
#         f(i+1, N)
#
# arr = [1,2,3]
# f(0,3)
# ----------------------------
### 배열에 v가 있으면 1, 없으면 0을 리턴
# def f(i,N,v):
#     if i == N:
#         return 0
#     if arr[i] == v:
#         return 1
#     else:
#         return f(i+1, N, v)
# arr = [1, 2, 3, 4, 5]
# print(f(0,5,5))

