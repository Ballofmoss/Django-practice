
def findSmallest(arr):
    smallest = arr[0].auditions
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i].auditions < smallest :
            smallest = arr[i].auditions
            smallest_index = i
    return smallest_index


def selectionSort(arr): 
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# print(selectionSort([18, 1, 4 ,3 , 50 , 45 ,15 ,31 ,51, 10]))



class Musician:  
    def __init__(self, name, auditions):
        self.name = name
        self.auditions = auditions
        
Musicians = []
BlackSabbath = Musician('BlackSabbath', 1000)
Musicians.append(BlackSabbath)

KorolIShoot = Musician('KorolIShoot', 230)
Musicians.append(KorolIShoot)

Nirvana = Musician('Nirvana', 100)
Musicians.append(Nirvana)

Rammstein = Musician('Rammstein', 850)
Musicians.append(Rammstein)

Motorhead = Musician('Motorhead', 401)
Musicians.append(Motorhead)


# print(Musicians[0].name)
sortedMusicians = selectionSort(Musicians)

for item in sortedMusicians:
    print(item.name, item.auditions)
   