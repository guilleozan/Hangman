""" Exercise sticks"""

from random import shuffle
print('Its really easy, who ever get the shortest stick loses')
# lista inicial
sticks=['-','--','---','----']

# shuffle Sticks
def shuffleSticks(list):
    shuffle(list)
    return(list)
print(shuffleSticks(sticks))

#Ask the user to pick a stick
def tryLuck():
    try1= ''
    
    while try1 not in ['1','2','3','4']:
        try1= input(' chose a number betwen 1 to 4: \n')
    
    return int(try1)



# comprobar el intento
def check_try(list, try1):
    if list[try1 -1] == '-':
        print ('you lose, so you have to do the dishes')
        
    else:
        print('you save, next one')
        
    print(f'you had {list[try1 -1]}')

sticksshuffle= shuffleSticks(sticks)
select= tryLuck()
check_try(sticksshuffle, select)