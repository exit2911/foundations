
def insertSort(arr):
    
    for key in range(len(arr)):
        
        for i in range(key):
          
          if arr[i] > arr[key]:
              arr.insert(i,arr[key])
              del arr[key+1]


    return arr
              

arr = [2,8,0,-1,-9,11]

print(insertSort(arr))
