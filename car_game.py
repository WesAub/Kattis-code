""" #INPUT N AND M
#WORDS
#LICENSE PLACE
#CHECK IF LETTERS ARE IN LICCENSE PLATE
#CHECK IF INCORRECT ORDER
#OUTPUT WORD OR INVALID FOR M PLATES """

####
"""nm_input = input("enter values for n and m\n")
for i in nm_input:
        n = int(nm_input[0])
        m = int(nm_input[2])

#print(n)
#print(m)

word_list =[]
plateList = []
    
for i in range(n):
        word = input("")
        word_list.append(word.upper())

    
for i in range(m): 
    plates = input("")
    plateList.append(plates.upper())
#print(word_list) 
#print(plateList)"""

""" def get_comp(word_list, plateList):
    word_spell = []
    plate_Spell = []
    iter = 0
    safety = False
    for i in word_list:
        for p in i:
            word_spell.append(p)
    for j in plateList:
        for q in j:
            plate_Spell.append(q)
    for r in word_spell:
        while iter < len(plate_Spell):
            if r == plate_Spell[iter]:
                iter += 1
                if 
            elif r in plate_Spell == False:
                print("Not a valid word")
            elif r != plate_Spell[iter]:
                iter+= 1

get_comp(w_list,p_list) """


w_list = ["babco", "prop", "bwot"]
p_list = ["BBC", "PLO", "MAG"]
word_spell = []
plate_Spell = []


iter =0

for w in w_list:
    for m in w:
        word_spell. append(m)
    for i in p_list:
        for j in i:
            plate_Spell. append(j)
            count = 0
            for p in plate_Spell:
                for q in word_spell:
                    if p == word_spell[iter]:
                        count += 1
                    else:
                        iter += 1
                        break
    if count == len(plate_Spell):
        print(j)





            
            
            

            
            
            
                






                     
    

