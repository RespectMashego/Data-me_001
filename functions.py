# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    return lst[::-1]

# print(reverse_list([1,2,3,4,5,6,7,8,9]))

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    
    """
    counter=0
    for lst_item in lst:
        if element==lst_item:
            counter+=1
    return counter

# print(count_occurrences([1,2,3,4,5,6,7,7,7,8,9],7))

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    
   
    keys=[]
    for key in dct:
        if dct[key]==value:
            
            keys.append(key)
    return keys
        
# print(get_keys_with_value({"age":10,"old":10,"stop":8},10))

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    return  lst1 + lst2

# print(merge_sorted_lists([1,2,3],[4,5,6]))
    
    
   

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    counter=0
    if len(str1)==len(str2):   
        for l in str1:
            for k in str2:
                if l==k:
                    counter+=1
                    break;
        if counter==len(str1):
            return True
        else:
            return False
    else:
        return False
    
print(is_anagram("listen","silint"))
                
        
        


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    return set(lst)
   

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this