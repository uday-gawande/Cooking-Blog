def selection_sort(arr):
    # first we find the lowest element in the array 
    # put it in first position 
    # and then for the 2nd position and so on 
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
            
        arr[min], arr[i] = arr[i], arr[min]
    
    return arr

def bubble_sort(arr):
    # after the 1st pass we get the largest element on the right side
    for i in range(len(arr)-1):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            
        if swapped == False:
            return arr
    return arr

def insertion_sort(arr):
    # here we insert the elements in its correct position
    for i in range(1, len(arr)):
        x = arr[i]
        j = i-1

        while j >= 0 and x < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        
        arr[j+1] = x
    
    return arr


a = selection_sort([5,1,4,2,5,4,45,5,2,8,54,4])
b = bubble_sort([5,1,4,2,5,4,45,5,2,8,54,4])
c = insertion_sort([5,1,4,2,5,4,45,5,2,8,54,4])
print(a)
print(b) 
print(c) 
