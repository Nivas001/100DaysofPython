import array as arr

#values = arr.array('i',[5,8,6,9,3,1,4])
values = [5,8,6,9,3,1,4]
swapped = 0

def printing():
    for i in range(len(values)):
        print(values[i])

print("Before sorting:-")
printing()

n = len(values)

def bubblesort():
    global swapped
    for i in range(n):
        for j in range(0, n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped+=1
                #time complexity = O(n²) Auxilary space = O(1)

def selectionsort():
    global swapped
    for i in range (n-1):
        min_index = i
        for j in range(i+1, n):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
        swapped +=1
        # time complexity = O(n²) Auxilary space = O(1)

def insertionsort():
    global swapped
    for i in range(1, n):
        key = values[i]
        j = i-1
        while j>=0 and values[j]>key:
            values[j+1] = values[j]
            swapped +=1
            j -=1
        values[j+1] = key


#bubblesort()
#selectionsort()
insertionsort()
print("After Sorting:")
printing()
print("Times sorted: ",swapped)

