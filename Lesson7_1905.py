# import random
#
# counter = [random.randint(-20, 20) for k in range(10)]
# sumNegative = 0
# sumPair = 0
# sumNoPair = 0
# dobytok = 1
#
# for num in counter:
#     if num < 0:
#         sumNegative += num
#     if num % 2 == 0:
#         sumPair += num
#     else:
#         sumNoPair += num
# for index in range(len(counter)):
#     if index % 3 == 0:
#         dobytok *= counter[index]
#
# print(counter)
# print(f'Сума парних дорівнює: {sumPair}')
# print(f'Сума непарних дорівнює: {sumNoPair}')
# print(f'Сума негативних дорівнює: {sumNegative}')
# print(f'добуток  дорівнює: {dobytok}')
#
# min_num = min(counter)
# max_num = max(counter)
# min_index = counter.index(min_num)
# max_index = counter.index(max_num)
#
# mul_between = 1
# if min_index < max_index:
#     for num in counter[min_index + 1: max_index]:
#         mul_between *= num
#     print(mul_between)
# else:
#     print('Not found')
#
# print('-------------')
# positiv_list = [num for num in counter if num > 0]
# print(positiv_list)
# result_pos = 0
# if len(counter) > 2:
#     first_pos = counter.index(positiv_list[0])
#     last_pos = counter.index(positiv_list[-1])
#
#     if  first_pos < last_pos:
#         result_pos = sum(counter[first_pos + 1: last_pos])
#     print(result_pos)
#



# import time
# start = time.time()
# my_list = [1, 2, 3, 4, 4, 3, 2, 1, 5, 12, 14, 10]
# unique_list = []
# for num in my_list:
#     if num not in unique_list:
#         unique_list.append(num)
#
# print(unique_list)
#
# lis2 = []
#
# for i in range(1,1000000):
#
#     lis2.append(i)
#
# print(lis2)
#
# # unique = list(set(my_list))
#
# print('Унікальні', unique_list)
# res = time.time() - start
# print(f'{res:10f}')


#Множини
x = set()
A = {1, 2, 3}
B = {2, 3, 4, 5}
print(A.intersection(B))

print(A.union(B))

print(A.difference(B))
print(B.difference(A))