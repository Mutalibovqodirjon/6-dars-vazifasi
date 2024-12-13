# 1 misol
# a= range(11)
# a_iter=a.__iter__()
# for i in a_iter:
#     print(i)


# 2 misol
# a = ["olma","nok","anor","banan","o'rik"]
# a_iter = a.__iter__()
# for  i in a_iter:
#     print(i)


#  3 misol
# a = ["olma","nok","anor","banan","o'rik"]
# a_iter = a[::-1].__iter__()
# for  i in a_iter:
#     print(i)


# 4 misol
# a= "olma"
# b=a.__iter__()
# for i in b :
#     print(i)


#  5 misol
# l =[]
# for i in range(1,21):
#     if i %2 == 0:
#         l.append(i)
# l.__iter__()
# for a in l:
#     print(a)


# 6 misol
# a= [3,6,2,9,7,5,3,68,4,5,5,4,4]
# a_iter = a.__iter__()
# b= sum(a_iter)
# print(b)


#  7  misol
# a = ["olma","nok","anor","banan","o'rik","ananas","madarin","gilos","shaftoli","mango"]
# a_iter = a.__iter__()
# b= input("Mevani nomini kiritng: ")
# if b in a_iter:
#     print("bor")
# else:
#     print("yuq")


#=====================================
#======GENERATORGA OID VAZIFALAR======
#=====================================




# 1 misol
# def generator():
#     for num in range(1, 20):
#         yield num
#
# for i in generator():
#     print(i)


#  2 misol

# def uzunlik(matn):
#     sozlar = matn.split()
#     for i in sozlar:
#         yield len(i)
#
# matn = "olma nok anor banan o'rik ananas madarin gilos shaftoli mango"
# uzunliklar = uzunlik(matn)
#
# for uzunlik in uzunliklar:
#     print(uzunlik)


#  3 misol
# def generator():
#     for num in range(1, 20):
#         if num % 2 ==0:
#             yield num
#
# for i in generator():
#     print(i)


#  4 misol
# def generator():
#     for num in range(1, 16):
#         if num % 2 ==1:
#             yield num
#
# for i in generator():
#     print(i)

#  5 misol
# from time import sleep
# def generator():
#     a = 0
#     while True:
#         a += 1
#         sleep(0.5)
#         yield a
#
# for i in generator():
#     print(i)


#  6 misol
# def generator(x):
#     yield pow(x,2)
#
# for i in generator(int(input("son kiriting: "))):
#     print(i)


#  7 misol
# def generrator(son):
#     a = 0
#     for i in  son:
#         a += i
#         yield a
#
# b = [ 1,2,3,4,5,6,7,8,9]
# for i in generrator(b):
#     print(i)

#  8 misol
# def generator(son):
#     for i in son:
#         if i > 0:
#             yield i
#
#
# l = [-1,-2,-5,-6,-3,2,3,5,-5,-3,5,4,3,2,-5,-958]
# for i in generator(l):
#     print(i)


#  9 misol
# import random
#
# def generator(s):
#     for _ in range(s):
#         yield random.randint(1, 1000)
# a = random.randint(1, 10)
# for i in generator(a):
#     print(i)

# #  10 misol
# def tubmi(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# son = int(input("son kiriting: "))
# if tubmi(son):
#     print(f"{son} tub son.")
# else:
#     print(f"{son} tub son emas.")


#  11 misol
# def generator(a):
#     yield a[::-1]
#
# b= "Hello"
# for i in generator(b):
#     print(i)

 # 12 misol
# def generator(x):
#     a = 1
#     for i in range(1,x+1):
#         a = i * x
#     yield a
# b= int(input("son kiriting: "))
# for i in generator(b):
#     print(i)