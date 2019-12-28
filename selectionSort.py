

def selectionSort(arr):
    
    
    n = len(arr)
    
    for i in range(n):
        
        min_key = i #need to reset min_key every time we run
        
        for k in range(i,n):
            
            if arr[k] < arr[min_key]: #in search of minimum item
                min_key = k
                
        arr[i],arr[min_key] = arr[min_key],arr[i]
        
    return arr
    
arr = [3,1,5,2,0,-9]

print(selectionSort(arr))
    
                
           
            
