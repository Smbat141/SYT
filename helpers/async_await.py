# def binary_search(arr, search_number, middle):
#     print(2)
#     if not arr:
#         return False
#
#     if arr[middle] == search_number:
#         return True
#
#     if search_number > arr[middle]:
#         start = middle + 1
#         new_arr = arr[start:]
#         middle = len(new_arr) // 2
#
#         return binary_search(new_arr, search_number, middle)
#     else:
#         start = 0
#         end = middle
#         new_arr = arr[start:end]
#         middle = len(new_arr) // 2
#         return binary_search(new_arr, search_number, middle)
#
#
# l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# item = 3
# mid = len(l1) // 2
#
# x = binary_search(l1, item, mid)
#
# print(x)


import logging
import threading
import time
import concurrent.futures
import dis
# import threading
#
# l = threading.RLock()
# print("before first acquire")
# l.acquire()
# print("before second acquire")
# l.acquire()
# print("acquired lock twice")

# def guess_number(beg, end):
#     low = beg
#     high = end
#     while low <= high:
#         mid = (low + high) // 2
#         print(mid)
#         pose = int(input())
#         if pose == "yes":
#             print("great, we are done")
#             return True
#         if pose == -1:
#             print("low")
#             high = mid - 1
#         elif pose == 1:
#             print("high")
#             low = mid + 1
#     return "something is wrong"
#
# guess_number(1, 100)

import keyboard  # using module keyboard


