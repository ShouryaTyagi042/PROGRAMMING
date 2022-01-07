def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

print(r_sum([1,24,[4,[5]]]))

# def r_max(nested_list) :
#     largest = None
#     first_time = True
#     for e in nested_list :
#         if type(e) == type([]) :
#             val = r_max(e)

#         else :
#             val = e

#             if first_time or val > largest :
#                 largest = val
#                 first_time = False
#     return largest
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

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest
print(r_max([34,45,[78,[89]]]))


import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)                    # Print the line
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname, prefix + "| ")


print_files("C:\\Users\\rajni tyagi\\Desktop\\Shourya Tyagi\\GitHub\\PROGRAMMING\\Python\\LearningWithPython3")
