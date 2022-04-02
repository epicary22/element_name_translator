import random

twoLettersList = ["He", "Li", "Be", "Ne", "Na", "Mg", "Al", "Si", "Cl", "Ar", "Ca", "Sc", "Ti", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
oneLetterList = ["H", "B", "C", "N", "O", "F", "P", "S", "K", "V", "Y", "I", "W", "U"]
characterList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", ",", ".", "/", "!", "?", "(", ")", " ", "'", ";"]

builderCount = 0
myTranslatedWord = ""
xList = []
toggleSimpleMode = True # Toggle this for simplified (and more chaotic) mode

while True:

    myWord = input()
    myWord = myWord.lower()
    if myWord == "":
        continue


    if myWord[0] == "!":
        if myWord[1:] == "simple":
            toggleSimpleMode = not toggleSimpleMode
            print("Simple mode:", toggleSimpleMode)
        else:
            print("Function not recongnized. List of functions:\n'!simple'")
        continue

    builderCount = 0
    myTranslatedWord = ""

    while builderCount < len(myWord):

        changedWord = 0
        myCurrentWordChunk = myWord[builderCount:builderCount+2]
        #print(myCurrentWordChunk)

        if changedWord != 1:
            for x in twoLettersList:
                if myCurrentWordChunk == x.lower():
                    myTranslatedWord = myTranslatedWord + x
                    builderCount += 1
                    changedWord = 1
                    continue

        if changedWord != 1:
            for y in oneLetterList:
                if myCurrentWordChunk[0] == y.lower():
                    myTranslatedWord = myTranslatedWord + y
                    changedWord = 1
                    continue

        if changedWord != 1:
            for z in characterList:
                if myCurrentWordChunk[0] == z.lower():
                    myTranslatedWord = myTranslatedWord + z
                    changedWord = 1
                    continue

        if changedWord != 1:
            xList = []
            for x in twoLettersList:
                if myCurrentWordChunk[0] == x[0].lower():
                    xList.append(x)
                    #print("appended", x)
            #print(xList)
            if xList != []:
                randomBit = xList[random.randint(0, len(xList) - 1)]
                myTranslatedWord = myTranslatedWord + randomBit
                changedWord = 1
                if myCurrentWordChunk[-1] in characterList and len(myCurrentWordChunk) >= 1:
                    myTranslatedWord = myTranslatedWord + myCurrentWordChunk[-1]
                if toggleSimpleMode == True:
                    builderCount += 1 # Toggle this on and off

        builderCount += 1

    print("my word:", myTranslatedWord)


# This thing should translate a normal word to element symbols (diamond -> [Di] Am O Nd)
# Use list scanning to do this (take out first 2 characters of lower(string), check [2 letter symbols], check [1 letter symbols], replace)
