import random
import helper


#This module is collection of simple programs that can be done on a list.
def exchange(a, b, c):
    "Helper method to exchange elements in an array."
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

#This module is collection of simple functions that can be perfomed on a list.

def isPrime(n):
    """
    Takes an integer and determines if it is a prime or not. Use this
    to determine if an integer in list is prime or not.
    """
    for m in range(2, int(n**0.5)+1):
        if not n % m:
            return False
    return True


def reverse(a):
    "Reverses a list in place."
    for i in range(len(a) / 2):
        temp = a[i]
        a[i] = a[-i - 1]
        a[-i - 1] = temp
    return a


def shuffle(a):
    """
    Shuffles the contents of a list in place.
    """
    for i in range(len(a)):
        b = random.randrange(len(a))
        temp = a[i]
        a[i] = a[b]
        a[b] = temp
    return a


def kDistinct(a):
    "Takes in a list and returns number of distinct values."
    copy = []
    for i in a:
        if i not in copy:
            copy.append(i)
    return len(copy)


def SetDistinct(a):
    """
    Takes in a list and returns number of distinct values. Computation is done
    using a set.
    """
    return len(set(a))


def kDuplicates(a):
    "Computes number of duplicates in an list."
    a = sorted(a)
    count = 0
    seen = False
    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            seen = False
        if a[i - 1] == a[i] and seen == False:
            count += 1
            seen = True
        if a[i - 1] == a[i] and seen == True:
            seen = True
    return count

def HardKdistinct(a):
    """
    Computes number of distinct values in a list without using a set or
    allocating extra space.
    """
    if len(a) == 0:
        return 0
    a = sorted(a)
    count = 1
    seen = False
    for i in range(1, len(a)):
        if a[i - 1] != a[i]:
            seen = False
            count += 1
        if a[i - 1] == a[i] and seen == False:
            seen = True
        if a[i - 1] == a[i] and seen == True:
            seen = True
    return count

def removeDupInPlace(a):
    # Work in progress, does not work properly.
    "Removes duplicates in an array without allocating extra memory."
    a = sorted(a)
    print a
    seen = False
    count = 0
    l = len(a) - 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1] and seen == True:
            seen = False
            l -= 1
        if a[i] == a[i - 1] and seen == False and a[i - 1] != a[l]:
            exchange(a, l, i - 1)
            seen = True
            count += 1
            l -= 1
        if a[i] == a[i - 1] and seen == True:
            seen = True
    print a
    return a[:len(a) - count]


def removeDuplicates(a):
    """
    Takes in an array and removes all the duplicates, by allocating extra
    memory.
    """
    copy = []
    for i in a:
        if i not in copy:
            copy.append(i)
    return copy


def KSmallest(a, k):
    """
    Returns k smallest integers in the list, and excludes
    duplicates. If the array consists ten 2's  and one 5, and k is
    it will return an array consisting of 2 and 5. This is not ideal for large
    data input as more memory is used to store the distinct values.
    """
    a = removeDuplicates(a)
    for i in range(len(a) - k):
        a.remove(max(a))
    return a


def addsum(list1, list2):
    """
    Takes two lists as input and adds the values at each position together.
    If one array is larger than the other, the rest of the output of that array
    is simply added to the end of the ouput array.
    """
    if len(a) >= len(b):
	    for i in range(len(b)):
	        a[i] = a[i]+ b[i]
	    return a
    else:
        for i in range(len(a)):
            b[i] = a[i] + b[i]
	    return b


def longest_repeat(a):
    "Takes in a list and finds the longest continuous sequence of an item."
    count = 0
    reset = 0
    element = a[0]
    for i in a:
        if element == i:
            count += 1
        else:
            element = i
            count = 1
        if count > reset:
            reset = count
    return reset


def make1D(a):
    "Takes a 2D list and returns a 1D version of it."
    for i in range(1, len(a)):
        for j in range(len(a[i])):
            a[0].append(a[i][j])
    del(a[1:])
    return a[0]


def main():
    a = [1, 2, 3, 4, 5, -1, -1, -1]
    #print(removeDupInPlace(a))
    #print(HKdistinct(a))
    #print(KSmallest(array, 99))
    print("\n")
    print("Removed in Place " + str(removeDupInPlace(a)))
    print("There are " + str(kDuplicates(a)) + " duplicates.")
    print("There are " + str(kDistinct(a)) + " distinct values.")

if __name__ == '__main__':
    main()
