"""
Compresses a string based on it's repeating characters, case sensitive, and works for alphabetical characters only.

Time Complexity: O(n)
- The compression process iterates through the string once.

Space Complexity: O(n)
- A new 'compressed' string is created, which can be up to 2*n characters long.
"""

def string_compression(s: str) -> str:
    """
    Compresses a string based on it's repeating characters, 
    case sensitive, and works for alphabetical characters only.

    Args:
        s (str): Input string to compress.

    Returns:
        str: Compressed string.
    
    Example:
        >>> string_compression("paaaaallllkddjdjkkkkklsp")
        1p5a4l1k2d1j1d1j5k1l1s1p
    """

    # If string is of size 0
    if not s:
        return ""
    
    #Initialize helper variables
    l, h, count=0, 0, 1
    res = ""

    # Loop to move through string, with help of 2 pointers
    while(h<len(s)):
        if(s[h] == s[l]):
            h = h+1
            count = count+1
        else:
            res = res + str(h-l)
            res = res + s[l]
            l = h
    
    # Need to add last character before ending the function
    res = res + str(h-l)
    res = res + s[l]
    
    return res


# ------------------ RUNNABLE EXAMPLE ------------------
x = 'paaaaallllkddjdjkkkkklsp'
print(string_compression(x))