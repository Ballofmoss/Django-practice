


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while  low <= high:
        mid = (low + high)
        guess =  list[mid]
        
        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else: 
            low = mid + 1
    return None

my_numbers = [1 ,15 , 17, 19, 20 , 21, 22 , 55, 72, 78, 82, 87, 90, 91, 100]

print(binary_search(my_numbers, 100))