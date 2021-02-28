def reverse(s):
    return (s[::-1])
def complement(s):
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 
'g': 'c', 't': 'a', 'M': 'K', 'K': 'M', 'R': 'Y', 'Y': 'R', 'W': 'W', 'S': 'S', 
'V': 'B', 'B': 'V', 'H': 'D', 'D': 'H', 'N': 'N', '-': '-' }
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)
def revcom(s):
    return complement(s[::-1])
