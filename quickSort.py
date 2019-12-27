
def partition(arr,low,high):
    
    i = low - 1
    pivot = arr[high]
    
    for j in range(low,high):
        
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
           
            
    arr[i+1], arr[high] = arr[high], arr[i+1] #high is right of the last smallest item
    return i + 1



def quickSort(arr,low,high):
    count = 0
    if low < high:
        count += 1
       
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
        print(count)
    
arr = [1,2,22,11,0,99,3,45]
      
n = len(arr)-1
       
quickSort(arr,0,n)

print(arr)

