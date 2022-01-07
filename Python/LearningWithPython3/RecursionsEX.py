from UnitTesting import test
# def recursive_min(nested_list) :
#     smallest = None
#     first_time = True
#     for e in nested_list :
#         if type(e) == type([]) :
#             val = recursive_min(e)

#         else :
#             val = e

#             if first_time or val < smallest :
#                 smallest = val
#                 first_time = False
#     return smallest
def r_max(nxs):
    """
      Find the maximum in a recursive structure of lists
      within other lists.
      Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val < largest:
            largest = val
            first_time = False

    return largest
# test(r_max([2, 9, [1, 13], 8, 6]) == 1)
# test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
# test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
# test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)

# print(recursive_min([2, 9, [1, 13], 8, 6]))

def count(target, nxs) :
    tot = 0
    # flag = False
    for e in nxs:
        if type(e) == type([]) :  # Recursive Call
            val = count(target,e)
        else :                  #  Base Case
            val = e
        if val == target :
            # flag = False
            tot += 1
    return tot

test(count(2, [])== 0)
test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
print(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]))
# test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2))
# test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
# test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
# test(count("a",[["this",["a",["thing","a"],"a"],"is"], ["a","easy"]]) == 4)
