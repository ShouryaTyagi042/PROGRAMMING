import sys
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter in "OQ" :
        print(letter+"u" + suffix)
    else :
        print(letter + suffix)

def count_letters(s,l) :
    count = 0
    for ch in s :
        if ch == l :
            count += 1
    return count

def reverse(s) :
    return s[::-1]

def mirror(s) :
    return s + reverse(s)

def remove_letter(l,s) :
    ans = ""
    for ch in s :
        if ch == l :
            continue
        else :
            ans += ch
    return ans

def is_palindrome(s):
    if s == reverse(s):
        return True

def count(sub,st) :
    step = 0
    c = 0
    while True :
        s = st[step:].find(sub)
        if s != -1 :
            c += 1
            step += s + 1
        else :
            break
    return c
# print(count("is", "Mississippi"))

def remove(sub,string) :
    r = string.find(sub)
    if r!= -1 :
        l_r = len(sub)
        return string[:r] + string[r+l_r:]
    else :
        return string

def remove_all(sub,string) :
    l = string.split(sub)
    ans = ""
    for ch in l :
        if ch != "" :
            ans += ch
    return ans





def test(did_pass) :
    """ Print the result of the case"""
    linenum = sys._getframe(1).f_lineno
    if did_pass :
        msg = "Test at line {} ok.".format(linenum)
    else :
        msg = "Test at line {} FAILED.".format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """

    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")


test_suite()




"""
layout = "{0:>8}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}" \
         "{7:>4}{8:>4}{9:>5}{10:>5}{11:>5}"

layout2 = "{0:>3}{1:>6}{2:>4}{3:>4}{4:>4}{5:>4}" \
          "{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}{12:>4}"

print(layout.format(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
print(" :-----------------------------------------------------")

for i in range(1, 13):
    print(layout2.format(str(i) + ":", i*1, i*2, i*3, i*4, i*5, i*6,
                         i*7, i*8, i*9, i*10, i*11, i*12))
"""

