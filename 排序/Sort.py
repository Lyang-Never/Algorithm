# -*- coding: utf-8 -*-
import numpy as np
import math

#插入排序
def InsertSort(array):
	n = len(array)
	for i in range(1,n):
		flag = array[i]
		key = i
		while(array[key-1]>flag) and key>0:
			array[key] = array[key-1]
			key -= 1
		array[key] = flag
	return array

def Half_insortsort(array):
	n = len(array)
	for i in range(1,n):
		flag = array[i]
		low = 0
		high = i-1
		while(low<=high):
			mid = (low+high)//2
			if array[mid]>flag:
				high = mid - 1
			else:
				low = mid + 1
        # high = low - 1 
		for j in range(i,low,-1):
		    array[j] = array[j-1]
		# j = i
		# while(j>high+1):
		#     array[j] = array[j-1]
		#     j -= 1
		array[high+1] = flag
	return array

def Shell_Sort(array):
	n = len(array)
	dk = n//2
	while (dk > 0):
		for j in range(dk,n):
			#flag = array[dk]
			while j-dk>=0 and array[j-dk]>array[j]:
				array[j],array[j-dk] = array[j-dk],array[j]
				j -= dk	
		dk = dk//2
	return array
#交换排序
def BubbleSort(array):
	n = len(array)
	for i in range(0,n):
		for j in range(0,n-1-i):
			if array[j]>array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
	return array

def QuickSort(array):
	def partition(array,low,high):
		pivot = array[low]
		while low<high:
			while low<high and array[high]>=pivot:
				high -= 1
			array[low] = array[high] # 比基准小的交换到前面
			while low<high and array[low]<=pivot:
				low += 1
			array[high] = array[low] # 比基准大交换到后面
		array[low] = pivot # 基准值的正确位置，也可以为 nums[high] = pivot
		return low
       #return low   # 返回基准值的索引，也可以为 return high

    #递归
	def qsort(array,low,high):
	    if low<high:
		    pivotpos = partition(array,low,high)
		    qsort(array,low,pivotpos-1)
		    qsort(array,pivotpos+1,high)
	    return array
        
	result = qsort(array,0,len(array)-1)
	return result
#选择排序
def SelectSort(array):
	n = len(array)
	for i in range(0,n-1):
		min = i
		for j in range(i+1,n):
			if array[j]<array[min]:
				min = j
		array[i],array[min] = array[min],array[i]
	return array

def HeapSort(array):
	def AdjustDown(array,k,end):
		flag = array[k]
		i = 2*k + 1
		while i<=end:
		    if i<end and array[i]<array[i+1]:
		        i += 1
		    if flag > array[i]:
		        break
		    else:
		        array[k] = array[i]
		        k = i
		    i = 2*i + 1
		array[k] = flag
	def BuildMaxHeap(array,length):
		i = length//2 - 1                   ###
		if length<=1:
		    return array
		while i>=0:                        ###
		 	AdjustDown(array,i,length)
		 	i -= 1

	BuildMaxHeap(array,len(array)-1)
	i = len(array) - 1
	while i >= 0:
		array[0],array[i] = array[i],array[0]
		AdjustDown(array,0,i-1)
		i -= 1
	return array
#归并排序
def MergeSort(array):
    if len(array)<=1:
        return array
    def merge(left,right):
        i = j = 0
        results = list()
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                results.append(left[i])
                i += 1
            else:
                results.append(right[j])
                j += 1
        results = results+left[i:]+right[j:]
        return results
    mid = len(array)//2
    left = MergeSort(array[:mid])
    right = MergeSort(array[mid:])
    result = merge(left,right)
    return result
#基数排序
def RadixSort(array):
    N = 10
    M = 1
    mostbit = len(str(max(array)))
    buckets = [[] for row in range(N)]
    while mostbit:
        for i in range(len(array)):
            buckets[array[i]//M % N].append(array[i])
        j = 0
        for bucket in buckets:
            while bucket:                    ###
                array[j] = bucket.pop(0)
                j += 1
        M *= 10
        mostbit -= 1 
    return array
#计数排序
def ConutingSort(array):
    bucket = [0]*(max(array)+1)
    for num in array:
        bucket[num] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j]>0:
            array[i] = j            ###
            i += 1
            bucket[j] -= 1
    return array
#桶排序
def BucketSort(array):

    n=len(array)
    big=max(array)
    num=big//10+1
    bucket=[]
    buckets=[[] for i in range(0,num)]

    for i in array:                         #划分桶
        buckets[i//10].append(i)            
    for i in buckets:                       #桶内排序
        bucket=HeapSort(i)

    arr=[]
    for i in buckets:
        if isinstance(i, list):
            for j in i:
                arr.append(j)
        else:
            arr.append(i)
    for i in range(0,n):
        array[i]=arr[i]
    return array


if __name__ == "__main__":
    input_ = np.random.randint(1,20,size = (5,))
    input = input_.tolist()
    print(input)

    output1 = Half_insortsort(input)
    print(output1)
    
