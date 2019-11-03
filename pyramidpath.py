#! python

 
x = '75' +\
'95 64' +\
'17 47 82' +\
'18 35 87 10' +\
'20 04 82 47 65' +\
'19 01 23 75 03 34' +\
'88 02 77 73 07 63 67' +\
'99 65 04 28 06 16 70 92' +\
'41 41 26 56 83 40 80 70 33' +\
'41 48 72 33 47 32 37 16 94 29' +\
'53 71 44 65 25 43 91 52 97 51 14' +\
'70 11 33 28 77 73 17 78 39 68 17 57' +\
'91 71 52 38 17 14 91 43 58 50 27 29 48' +\
'63 66 04 68 89 53 67 30 73 16 69 87 40 31' +\
'04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

pyramid = x.split(' ')
listPyramid = []
for idx, val in enumerate(pyramid):
    if len(val) == 4:
        splitval = val[2:]
        pyramid[idx] = val[:2]
        pyramid.insert(idx + 1, splitval)

# mylist = []
index = 0
limit = 1
num = 1

# while num <= 100:
#     mylist.append([])

#     while len(mylist[index]) < limit and num <= 100:
#         mylist[index].append(num)
#         num += 1

#     index += 1
#     limit += 1

PyraVal = pyramid[0]
while index < len(pyramid):
    listPyramid.append([])

    while len(listPyramid[index]) < limit and index < len(pyramid):
        listPyramid[index].append(PyraVal)
        if num > idx:
            break
        PyraVal = pyramid[num]
        num += 1
    if num > idx:
        break

    index += 1
    limit += 1
c = len(listPyramid) - 1

previous_sums = []
for row in range(c, -1, -1):
    current_sums = []
    for position, value in enumerate(listPyramid[row]):
        if position >= len(previous_sums):  # only necessary for first line
            add_from_left = 0
        else:
            add_from_left = previous_sums[position]
        if position <= len(previous_sums) and row != c:
            add_from_right = previous_sums[position + 1]
        else:
            add_from_right = 0
        current_sums.append(max(add_from_right + int(value), add_from_left + int(value)))

    previous_sums = current_sums
    
print(f'Max sum is: {max(previous_sums)}')

# Explanation of above:
''' 'c' keeps Indexerror from happening in initial loop without hardcoding,
   Initial loop iterates from bottom to top, row captures index of list to be iterated.
   Enumerate of listPyramid[row] will iterate through row list and produce position value
   of value and the value itself, since first line has no previous sums the first line is
   necessary (could also probably use try/except). Pyramid is 'Left-justified' so the same
   position corresponds to the bottom left value, +1 corresponds to bottom right. Once both
   values have been created we max the value and save it to our current list. This eventually
   whittles itself down and finds the max path sum.'''
