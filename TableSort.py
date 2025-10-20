def getNthLargest(array, n):
    for element in array:
        if type(element) != int:
            return "Niewłaściwe dane wejściowe"
    if type(n) != int:
        return "Niewłaściwe dane wejściowe"
    array = QuickSort(array, 0, len(array) - 1)
    print(array)
    return array[len(array) - n]

def QuickSort (array, left, right):
    middleVal = array[(right + left) // 2]
    array[(right + left) // 2], array[right] = array[right], array[(right + left) // 2]
    j = left
    for i in range(left, right):
        if array[i] < middleVal:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[j], array[right] = array[right], array[j]
    if j > left:
        QuickSort(array, left, j - 1)
    if j + 1 < right:
        QuickSort(array, j + 1, right)
    return array



print(getNthLargest([1,5,3,4,8,6,4,99,8,77,5,3,22], 6))
print("6\n")
print(getNthLargest("es", 2))
print("Niewłaściwe dane wejściowe\n")
print(getNthLargest([1,2,3,45,6,7,9,3,4,55,6,77,9,0], 2))
print("55\n")