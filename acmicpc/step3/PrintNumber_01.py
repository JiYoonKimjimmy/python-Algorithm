import sys

inputArr = sys.stdin.readline().split(' ')
length = int(inputArr[0])
compare = int(inputArr[1])
tempArr = sys.stdin.readline().split(' ')
for j in range(length):
    if compare > int(tempArr[j]):
        print(tempArr[j])
