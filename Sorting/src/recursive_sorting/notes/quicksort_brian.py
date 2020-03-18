# quick sort
[ 5  9  3  7  2  8  1  6]

# pick first mumber

# append all smaller to new array left
# append all bigger to new array right

[3 2 1]  [5]  [9 7 8 6]

# recurse left

[2 1 ][3][]     [5]  [9 7 8 6]

#recurse left

[1][2][][3][]     [5]  [9 7 8 6]

#recurse left
# 1 is sorted,  base case

#recurse right
# empty array base case

#recurse right
# empty array, base case

#recurse right
[1][2][][3][]     [5]  [9 7 8 6]

[1][2][][3][]     [5] [7 8 6][9][]

#recurse left 

[1][2][][3][]     [5] [6][7][8][  ][9][]

[1, 2] [3]
[1, 2,  3]

# plan
def quicksort(data):
# base case:  if array length 0 or 1
    if len(data) < 2:
        #  return array
        return data

# else:
    else:
# pick pivot might as well pick first because its unsorted, none are better
    pivot = data[0]
    left  = []
    right = []
# put anything smaller into left array
# put anything bigger into right array
    for value in data[1:]:
        if value <= pivot:
            left.append(value)
        else:
            right.append(value)
# return quicksort(left) + pivot + quicksort(right)
    return quicksort(left) + [pivot] + quicksort(right)
# 