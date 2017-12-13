'''
The characters present in beabefabea  are a, b, e    and f.
Strip it to ensure we have only two unique characters in the string
Generate output string that has characters  they are alternating within the
string.
Find the string that has the maximum length meeting the alternate criteria
and only two unique characters
Example: If we delete a and f, the resulting string is bebeeeb.
This is not a valid string  because there are three consecutive e's present.
If we e and f,bababa is acceptable as it is alternating. We need to find
all such strings and print the string/s with maximum length

Solve this problem with Recursion and ensure it scales for any number of
characters
'''



import re

def alter(tupitr):
    for i in range (0, len(tupitr) -1):
        if (tupitr[i] == tupitr[i+1]):
            return False
    return True

def findmaxstring(listop):
    dict1 = {}
    for tupitr in listop:
        if (alter(tupitr[0])):
            dict1[tupitr[0]] = len(tupitr[0])
    max =  0
    oplist = []
    for key,values in dict1.items():
        if max <= values:
            max = values
            oplist.append((key, max))
    return max

def stripstring(unqcount, setgp, listop):
    if (unqcount > 2):
        listop1 = []
        for listval in listop:
            for char in setgp:
                #strs is a tuple and first element is word to be evaluated
                if(char not in listval[1]):
                    listint = []
                    listchars = list(listval[1])
                    for charinp in listval[0]:
                        if (str(char) != charinp):
                            listint.append(charinp)
                            listchars.append(char)
                            listchars = list(set(listchars))
                    listop1.append(("".join(listint), listchars))
        unqcountl = unqcount - 1
        return stripstring(unqcountl,setgp,listop1)
    else:
        return findmaxstring(listop)

if __name__ == '__main__':
    ipstr = "beabefabcceac"
    gp = re.findall('([a-z])', ipstr)
    listop = []
    setgp = list(set(gp))
    uniquecnt = len(setgp)
    listop.append((ipstr,[]))
    print(stripstring(uniquecnt, setgp, listop))# -*- coding: utf-8 -*-
