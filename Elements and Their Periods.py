                                ### ELEMENTS AND THEIR PERIODS
            
liste = [1,3,4,5,7,8,3,1,5,2,4,5,5,6,5,3,6,6,3]

for x in [1,2,3,4,5,6,7,8,9,0] :
    repeat = 0
    for i in range(len(liste)):
        if liste[i] == x:
            repeat +=1
    print(x,repeat)
    
# I am going to do research about elements in a list to print elements for once
