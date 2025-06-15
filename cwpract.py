"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

def accum(st:str) ->str:
    res_str = ''
    counter = 1

    for char in st:
        char = char.casefold()*counter
        res_str += f'{char.capitalize()}' if counter == 1 else f'-{char.capitalize()}'
        counter += 1
    return res_str

# Better version // enumerate - can help to give indexes in i and character in a 
# def accum(s):
#     return '-'.join((a * i).title() for i, a in enumerate(s, 1))

print(accum('ZpglnRxqenU'))