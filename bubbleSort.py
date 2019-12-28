
"""
bubble sort 

O(n**2)

brute force
"""    
    

def bubble(arr):
        
    stop = 0
    
    while stop < len(arr)-1: 
        
        for i in range(len(arr)-1):
            
            if arr[i] > arr[i+1]:
                
                arr[i],arr[i+1] = arr[i+1],arr[i]
            
            else:
            
                stop += 1
                
        if stop < len(arr)-1:
            
            stop = 0 #reset the stop breaker
           
            
    return arr


arr = [2,5,7,1,0,-1,-99]

print(bubble(arr))
