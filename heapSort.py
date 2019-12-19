
def heapify(arr,n,i):
    
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[i]: # if left is larger than parent
        largest = l
    if r < n and arr[r] > arr[largest]: #if right is larger than largest
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] #swap to make parent the largest

def heapSort(arr):
    
    n = len(arr)
    
    for i in range(n,-1,-1): #gives us the counts of the elements backwards including 0
        heapify(arr,n,i)

    for i in range(n-1,0,-1): #give the index backwards except 0
    
        arr[i],arr[0] = arr[0],arr[i]              
        
        heapify(arr,i,0)
        
arr=[4,5,2,8,9]

heapSort(arr)
print(arr)
        
    
                  
    
    
                 
    
                      
        
        
