import sys
import re

#Creates an unique set of alphabets in the word
def checknonrepeat(strm):
    for i in range(0,len(strm)-1):
        if (strm[i] == strm[i+1]):
            return False
    return True

#This function is going to pick the largest and return the str.
def checklargest(liststrs):
    s = sorted(liststrs, key = lambda x: len(x[0]))
    return s[0]

#This is for continuous iteration of the stuff - to make this work for more than one removal
def findstring(unqcount, setgp, listop):
    while (unqcount > 2):
        for listval in listop:
            for char in setgp:
                #strs is a tuple and first element is word to be evaluated
                if(char not in listval[1]):
                    for charinp in listval[0]:
                        if (str(char) != charinp):
                            listint.append(charinp)
                    listchars = strs[1]
                    listchars.append(char)
                    listchars = list(set(listchars))
                    listop1.append("".join(listint), listchars)
        unqcount = unqcount - 1
        return findstring(unqcount,setgp,listop1)
    return checklargest(listop1)

# Creates the first clean up done
if __name__ == '__main__':
    gp = re.findall('([a-z])', "beabeefeab")
    setgp = list(set(gp))
    unqcount = len(setgp) -1
    listop = []
    listint = []
    for char in setgp:
        for charinp in "beabeefeab":
            if (str(char) != charinp):
                listint.append(charinp)
#char is being maintained to ensure, we don run the clean up again on the character

    print(2)
