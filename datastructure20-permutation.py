# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:08:54 2021

@author: deesaw
"""


def permute(s):
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                print(f'permute {s[:i]} + {s[i+1:]}')
                # Add it to output
                out += [let + perm]
                print(i,"........",s,"......",let,".......",perm,"......",out)

    return out

print(permute('abc'))