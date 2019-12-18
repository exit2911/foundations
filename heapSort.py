
def heapify(arr,n,i):
    
    largest = i
    
    l = 2*i + 1
    r = 2*i + 2
    
    
    if l < n and arr[i] < arr[l]: #anchor using l
        largest = l
        
            
    if r < n and arr[largest] < arr[r]: #anchor using largest as index to account of the max children 
        largest = r
        
    if largest != i:
        
        arr[i], arr[largest] =  arr[largest], arr[i]

        
def heapSort(arr): #min to max
    
    n = len(arr)
    
    for i in range(n,-1,-1): #max vs. min will be different. this iteration is based on binary tree structure.
        
        heapify(arr,n,i)
        
    
  
    for i in range(n-1,0,-1):
        
        arr[i], arr[0]= arr[0], arr[i]
        
        heapify(arr,i,0)
        

arr = [99,1,5,56,2]
n = len(arr)

heapSort(arr)

print("final",arr)

