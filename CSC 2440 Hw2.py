#Question 1: Sorting list in descending order

A = [2,5,3,1,4,7,6]
for i in range(len(A) - 1):
    max_index = i #The largest value is set equal to i
    for j in range(i + 1, len(A)): #This part of the loop finds the largest index
        if A[j] > A[max_index]:
            max_index = j

    A[i], A[max_index] = A[max_index], A[i] #This part swaps the largest index with the first index

    print("Sorted array in descending order", A)


# Question 2: Sorted by the average value of even elements
"""
A = [2,5,3,1,4,7,6]

def average(A):
    even = [2,4,6] #Just the even numbers of the list
    return sum(even) / len(even) # Calculates and returns the average

# Calculates the average of even elements
average_even = average(A)
print("The average of even numbers:", average_even)
"""