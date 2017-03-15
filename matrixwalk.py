from readfiles import *
from sklearn.preprocessing import normalize
from numpy import *
fromyears =2016

def compute(vals):
    scorediff = (int(vals[3]) - int(vals[5]))
    return (scorediff),0.

def winner(t1,t2,X):
    score1 = X[keyToEnum[t1]][keyToEnum[t2]]
    score2 = X[keyToEnum[t2]][keyToEnum[t1]]
    if score1>score2:
        return t1
    return t2

teams = readteams()
incidencematrix = readresults(teams,fromyears,compute)
bracket = readbrackets()

mininc = incidencematrix.min()
X = incidencematrix #- mininc
diff = False
while not diff:
    tmp = normalize(dot(X,X))
    diff = allclose(tmp,X)
    X = tmp

rounds = 6
for i in range(rounds):
    print [teams[ids] for ids in bracket]
    newround = []
    print "---------------"
    for ididx in xrange(0,len(bracket),2):
        ids1,ids2 = bracket[ididx],bracket[ididx+1]
        wid = winner(ids1,ids2,X)
        newround.append(wid)
    bracket = newround
print [teams[ids] for ids in bracket]

