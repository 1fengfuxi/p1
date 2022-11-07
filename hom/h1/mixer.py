
count=0
newnoun=[]
newadverb=[]
newadjactive=[]
pluralnoun=False
while count<4:

    noun=input("please enter your noun")
    newnoun.append(noun)
    if pluralnoun==False:
        noun=input("please enter a plural noun ")
        newnoun.append(noun)
        pluralnoun=True
    if count<3:
        adverb=input("please enter a adverb ")
        newadverb.append(adverb)
    if count<4:
        adjactive=input("please enter a adjactive")
        newadjactive.append(adjactive)

    count+=1


story=(f"alebert einstein ,the son of {newnoun[0]} and noun {newnoun[1]} was borned in ulm, germanany\n"
       f"in 1879 and 1902,he had a job as {newnoun[2]} {newnoun[3]} in the Swiss patent office and attended\n"
       f"the University of Zurich. There he began studying atoms, molecules,\n"
       f"and  {newnoun[4]}. he won a noble price whixh are located at sweaden\n"
       f"Sweden occupies the {newadjactive[0]} part of the Scandinavian Peninsula, which it shares\n "
       f"with Norway. The land slopes {newadverb[0]} from the high mountains along the Norwegian frontier\n "
       f"eastward to the Baltic Sea. {newadverb[1]}, it is one of the {newadjactive[1]} and most {newadjactive[2]} parts of the Earth’\n"
       f"s crust. Its surface formations and soils were altered by the receding glaciers of the Pleistocene Epoch "
       f"(about 2,600,000 to 11,700 years ago\n"
       f" Sweden has a {newadjactive[3]} favourable climate relative to its northerly latitude owing to moderate {newadverb[2]} \n"
       f"winds and the warm North Atlantic Current.")
print(story)