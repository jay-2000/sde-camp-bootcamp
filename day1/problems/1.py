#integer input
n = int(input())

#string input
n = input()

#float input
n = float(input())

# no double data type exists in python

#array input in one line
arr = list(map(int,input().split().strip()))

#array input using for loop
arr = [] #declare array
for _ in range(n): #if n=size of array is given then we loop over the size of the array to get array values
  arr.append(int(input()))
  
