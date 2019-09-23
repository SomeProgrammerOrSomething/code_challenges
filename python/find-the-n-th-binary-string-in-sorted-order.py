"""This is my Python Implementation for the problem here:
https://www.geeksforgeeks.org/find-the-n-th-binary-string-in-sorted-order/"""

"""Given a positive integer n,
the task is to find the nth string in the following infinite list of all possible strings over two symbols a and b sorted lexicographically.

    a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb, aaaa, … 

For example:
Input:	6
Output:	bb

Input: 	11
Output: baa
"""
import math

n = int(input("What is the nth value you want to check up to: "))

# First, we want to determine how long our string needs to be.
## For string of length k, we have "exausted" search on 2, 2^2, 2^3, ..., 2^(k-1)
## Because we are saying the string 'a' is at index 1 and not index 0, we are doing
## log2(n+1) and not log2(n)

length_of_string = math.floor(math.log2(n+1))

# Recognize that as the strings are binary strings, so we may represent their values in binary.
## The given ordering has a listed first, so a maps to 0 and b maps to 1.
## We can construct our desired string by adjusting it's element values to match the corresponding binary rep.

a_string = "a"*length_of_string

# With this a_string, we recognize our desired string is integral "distance" from this one.
## We may want to calculate that "distance" by basically having a relative index between our desired string and this one.
## In other words, we want to constrict our search for our string by looking at all strings that have the same length as our target string.
rel_index = n + 1 - pow(2,length_of_string)

# Now, we just add in the binary values accordingly.
goal_ind = len(a_string)-1
target = list(a_string)

while rel_index > 0:
	if rel_index % 2 == 1:
		target[goal_ind] = 'b'
	else:
		target[goal_ind] = 'a'
	rel_index //= 2
	goal_ind -=1

print("".join(target))