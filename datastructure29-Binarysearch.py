# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 10:41:29 2021

@author: deesaw
"""


def binary_search(arr,ele):
    
    # First and last index values
    first = 0
    last = len(arr) - 1
    
    found = False
    
    
    while first <= last and not found:
        
        mid = (first+last)//2 
        
        # Match found
        if arr[mid] == ele:
            found = True
        
        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid -1
            # Set up 
            else:
                first = mid + 1
                
    return found

# list must already be sorted!
arr = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(arr,44))
print(binary_search(arr,4))

def rec_bin_search(arr,ele):
    
    # Base Case!
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:
        
        mid = len(arr)/2
        
        # If match found
        if arr[mid]==ele:
            return True
        
        else:
            
            # Call again on second half
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:],ele)
