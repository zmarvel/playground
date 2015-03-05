#!/usr/bin/env python

# I'll finish this later.

def find_reps(rep):
    new_reps = {rep}
    left, mid, right = rep.rpartition('10')
    if mid:
        for r_l in find_reps(left):
            new_reps.add(('%s%s%s' % (r_l, mid, right)).lstrip('0'))
            new_reps.add(('%s%s%s' % (r_l, '02', right)).lstrip('0'))
        new = ('%s02%s' % (left, right)).lstrip('0')
        new_reps |= {new} | find_reps(new)

    left, mid, right = rep.rpartition('20')
    if mid:
        for r_l in find_reps(left):
            new_reps.add(('%s%s%s' % (r_l, mid, right)).lstrip('0'))
            new_reps.add(('%s%s%s' % (r_l, '12', right)).lstrip('0'))
        new = ('%s12%s' % (left, right)).lstrip('0')
        new_reps |= {new} | find_reps(new)

    return new_reps
        


# 
#     left, mid, right = rep.rpartition('10')
#     if mid:
#         new = ('%s02%s' % (left, right)).lstrip('0')
#         print(new)
#         new_reps.add(new)
#         for r in find_reps(left):
#             new_reps.add('%s%s%s' % (r, mid, right))
#             new_reps.add('%s%s%s' % (r, '02', right))
# 
#     left, mid, right = rep.rpartition('20')
#     if mid:
#         new = ('%s12%s' % (left, right)).lstrip('0')
#         print(new)
#         new_reps.add(new)
#         for r in find_reps(left):
#             new = '%s%s%s' % (r, mid, right)
#             new_reps.add(new)
#             new = '%s%s%s' % (r, '12', right)
#             new_reps.add(new)
# 
#     return new_reps

user_in = input('>')
while user_in != ':q':
    dec = int(user_in)
    # Make the decimal into a binary number represented as a string.
    bits = bin(dec).replace('0b', '')
    print('{} -> {}'.format(dec, bits))

    print(find_reps(bits))
    user_in = input('>')
