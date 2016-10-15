def chinesePuzzle(heads, legs):

    rabbit = 0
    chicken =0
    for rabbit in range(1, heads):
        chicken = heads - rabbit
        if((2*chicken + 4*rabbit) == legs):
            return chicken, rabbit

    return None, None

def chinesePuzzleRec(current, heads, legs):

    if(current>heads):
        return None, None
    chicken = current
    rabbit = heads - current
    if((2*chicken + 4*rabbit) == legs):
        return chicken, rabbit
    else:
        return chinesePuzzleRec(current+1, heads, legs)

    return None, None

numofheads = int(input("Number of heads: "))
numoflegs = int(input("Number of legs: "))



result = chinesePuzzleRec(0, numofheads, numoflegs)
print ("Recursion: Number of chickens are %d and rabbits are %d." % result)


result = chinesePuzzle(numofheads, numoflegs)
print ("Loop: Number of chickens are %d and rabbits are %d." % result)