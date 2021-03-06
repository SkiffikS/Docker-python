# -*- coding: utf-8 -*-

import random
from rich import print
import time
from tabulate import tabulate

print("[bold yellow]Программа для визначення найкращого алгоритму сортування масивів[/bold yellow]")

print("[bold red]Алгоритми: [/bold red]")


def Bubble_Sort(list):
    print("[italic green]Bubble Sort (Бульбашковий алгоритм)[/italic green]")
    start_time = time.time()
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return time.time() - start_time

def merge_sort(unsorted_list):
    start_time = time.time()
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    #resul = list(merge(left_list, right_list))
    return time.time() - start_time

# Merge the sorted halves
def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


def insertion_sort(InputList):
    print("[italic green]Insertion sort (Сортування вставкою)[/italic green]")
    start_time = time.time()
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
    while (InputList[j] > nxt_element) and (j >= 0):
        InputList[j+1] = InputList[j]
        j=j-1
    InputList[j+1] = nxt_element
    return time.time() - start_time


def shellSort(array, n):

    print("[italic green]Shell sort (Сортування оболонкою)[/italic green]")
    start_time = time.time()
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    return time.time() - start_time

def selection_sort(input_list):
    print("[italic green]Selection sort (Видільне Сортування)[/italic green]")
    start_time = time.time()
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value
    input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
    return time.time() - start_time

if __name__ == "__main__":

    array = []
    for i in range(1, 5000):
        n = random.randint(0, 1000000)
        array.append(n)
    a1 = Bubble_Sort(array)
    a1 = float('{:.5f}'.format(a1))
    a1t = "Bubble Sort"
    print("[italic green]Merge sort (Сортування злиттям)[/italic green]")
    a2 = merge_sort(array)
    a2 = float('{:.5f}'.format(a2))
    a2t = "Merge sort"
    a3 = insertion_sort(array)
    a3 = float('{:.5f}'.format(a3))
    a3t = "Insertion sort"
    a4 = shellSort(array, len(array))
    a4 = float('{:.5f}'.format(a4))
    a4t = "Shell sort"
    a5 = selection_sort(array)
    a5 = float('{:.5f}'.format(a5))
    a5t = "Selection sort"
    print("[red](Тест проводиться на рандомних масивах довжиною 5 000 елементів)[red]")
    result_time = [a1, a2, a3, a4, a5]
    result_name = [a1t, a2t, a3t, a4t, a5t]

    top_time = []
    top_name = []
    
    for i in range(len(result_time)):
        index_min = min(range(len(result_time)), key=result_time.__getitem__)
        top_time.append(result_time[index_min])
        top_name.append(result_name[index_min])
        del result_time[index_min]
        del result_name[index_min]

    #print(top_name)
    #print(top_time)
    top_time1 = ["Час виконання: "] + top_time
    top_name1 = ["Алгоритм: "] + top_name

    data = [
        top_name1,
        top_time1
    ]

    print("[bold blue]Таблиця лідерів[/bold blue]")
    print(tabulate(data, tablefmt="grid"))

    print(f"[bold green]Найкращий алгоритм сортування - {top_name[0]}[/bold green]")
