
def quicksort(array):
    
    less = []
    equal = []
    greater = []
    
    if len(array) > 1:
        pivot = array[0]
        
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
                
        return sorted(less) + equal + sorted(greater)
    else: #for when array has only 1 element
        return array

array = [1,5,7,3,8]

result = quicksort(array)

print(result)
