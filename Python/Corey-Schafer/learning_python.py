courses = ["history", "civics", "Geography"]
print(courses[0:2])
# ['history', 'civics']
courses.append("Art")
courses.insert(1, "physics")
courses_2 = ["chem", "bio", "maths"]
# inserts whole lists as an item in the list same for append
courses.insert(0, courses_2)
courses.extend(courses_2)  # adds the list to the initial list
popped = courses.pop()  # by default remove last value

courses.remove("history")
courses.reverse()  # reverse the list
courses_2.sort(reverse=True)  # sort method
# function to return sorted list , without altering the original list
sort_course_2 = sorted(courses_2)


print('Geography' in courses)
print(courses.index("civics"))
print(sort_course_2)
print(popped)  # returns removed value
print(courses)


# True
# 4
# ['bio', 'chem', 'maths']
# maths
# ['bio', 'chem', 'Art', 'Geography', 'civics', 'physics', ['maths', 'chem', 'bio']]


for index, courses_2 in enumerate(courses_2, start=1):
    print(index, courses_2)

# 1 maths
# 2 chem
# 3 bio

courses_s = ["chem", "bio", "maths"]
courses_string = " ".join(courses_s)
new_list = courses_string.split(" ")

print(new_list)
print(courses_string)

# ['chem', 'bio', 'maths']
# chem bio maths

courses_sa = ["chem", "bio", "maths"]
courses_sa[0] = "art"
print(courses_sa)

# ['art', 'bio', 'maths']

# Tuples

tuple_1 = ("history", "Math", "physics", "COMPSCI")

# Set

set_1 = {"history", "Math", "physics", "COMPSCI", "history"}
print(set_1)  # Removes duplicates , order is not important

# {'Math', 'history', 'COMPSCI', 'physics'}

set_2 = {'Math', 'history', 'COMPSCI', 'chem', }

print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))

# {'COMPSCI', 'history', 'Math'}
# {'physics'}
# {'Math', 'physics', 'chem', 'history', 'COMPSCI'}

# Creating empty set >>

empty_set = set{}
