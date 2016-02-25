#
# goal: understand how lists work in Python.
#
# You are given a non-empty list of integers (X). For this task, you should return a list consisting
# of only the non-unique elements in this list. To do soou  ywill need to remove all unique elements
#  (elements which are contained in a given list only once). When solving this task, do not change the
# order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
#
# The result must be a list, it should be coded in 1 function.
#
# Test lists:
#
print("_________________________________________________________________________________________________")

task_list1 = [1, 2, 3, 1, 3]
task_list2 = [1, 2, 3, 4, 5]
task_list3 = [5, 5, 5, 5, 5]
task_list4 = [10, 9, 10, 10, 9, 8]
ss = []
def non_unuique_list_argument(mass):
    ununique_list = []

    for list_arg in mass:
        counter = 0
        for check_arg in mass:
            if(list_arg == check_arg):
                counter += 1
            else:
                pass
        if(counter >= 2):
            ununique_list.append(list_arg)
        else:
            pass;
    return ununique_list

print (non_unuique_list_argument(task_list1))
print (non_unuique_list_argument(task_list2))
print (non_unuique_list_argument(task_list3))
print (non_unuique_list_argument(task_list4))

# =====Task 2=====
#
# Goal: understand how strings in Python work
#
# You are given a text, which contains different english letters and punctuation symbols. You should find the most
#  frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
#  Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
#
# If you have two or more letters with the same frequency, then return the letter which comes first in the latin
#  alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
#
# Input: A text for analysis as a string (unicode for py2.7).
#
# Output: The most frequent letter in lower case as a string.
#
# Example:
#
# most_frequent_letter("Hello World!") == "l"
# most_frequent_letter("How do you do?") == "o"
# most_frequent_letter("One") == "e"
# most_frequent_letter("Oops!") == "o"
# most_frequent_letter("AAaooo!!!!") == "a"
# most_frequent_letter("abe") == "a"
print("_________________________________________________________________________________________________")

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def most_frequent_letter(word):
    word = word.lower()
    frequent_counter_arr = []
    for ALetters in alphabet:
        counter = 0
        for WLetters in word:
            if(ALetters == WLetters):
                counter +=1
            else:
                pass
        frequent_counter_arr.append(counter)
    max_frequent_number = max(frequent_counter_arr)
    letter_index = frequent_counter_arr.index(max_frequent_number)
    our_letter = alphabet[letter_index]
    return our_letter

print(most_frequent_letter("Hello World!"))
print(most_frequent_letter("How do you do?"))
print(most_frequent_letter("One"))
print(most_frequent_letter("Oops!"))
print(most_frequent_letter("AAaooo!!!!"))
print(most_frequent_letter("abe"))

# ====Task 3====
#
# You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...)
#  then multiply this summed number and the final element of the array together. Don't forget that the first element
#  has an index of 0.
#
# For an empty array, the result will always be 0 (zero).
#
# Input: A list of integers.
#
# Output: The number as an integer.
#
# Example:
#
# your_function([0, 1, 2, 3, 4, 5]) == 30
# your_function([1, 3, 5]) == 30
# your_function([6]) == 36
# your_function([]) == 0
print("_________________________________________________________________________________________________")

def number_operations(arr):
    sum = 0
    for n in range(0,len(arr)):
        if(n == 0 or n%2==0):
            sum =sum + arr[n]
        else:
            pass

    if(len(arr)>0):
        last_number = arr[len(arr)-1]
        result = sum * last_number
    else:
        result = 0

    return result

print(str(number_operations([0, 1, 2, 3, 4, 5])))
print(str(number_operations([1, 3, 5])))
print(str(number_operations([6])))
print(str(number_operations([])))


