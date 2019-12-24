
def partition(arr,begin,end):
    
   
           
    for i in range(begin,end):
       
        if arr[i] > arr[end]:
            arr.insert(end+1,arr[i])
            del arr[i]
            
            
    return arr    

def quick(arr):
    
    pivot = None
    
    if pivot is None:
        
       
        begin = 0
        end = len(arr)-1
        pivot = arr[end]
        
        while len(arr[begin:end+1])> 1:  
            
            
         
            
            partition(arr,0,end)
            
            
            
                    
    
             
             
    

    return arr
