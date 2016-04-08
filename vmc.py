import numpy
import math
numsteps=50
storage=[]

def psi(coords,ions):
    mod1=numpy.linalg.norm(coords[0])
    mod2=numpy.linalg.norm(coords[1])
    mod1=mod1**2
    mod2=mod2**2
    val=math.exp((-0.5)*(mod1 + mod2))
    return val

def calcenergy(coords):
    mod1=numpy.linalg.norm(coords[0])
    mod2=numpy.linalg.norm(coords[1])
    mod1=mod1**2
    mod2=mod2**2
    val=math.exp((-0.5)*(mod1 + mod2))
    del1=(coords[0,0] + coords[1,0])*val
    del2=(coords[1,0] + coords[1,1])*val
    ans=(-(del1+del2)/2)
    return ans

def VMC(WF,ions,numSteps):
    R=numpy.zeros((2,2),float)
    movesAttempted=0.0
    movesAccepted=0.0
    for step in xrange(0,numSteps):
        for ptcl in xrange(0,len(R)):
            a=5
            accept=0
            test=R.copy()
            xsubzerowave=psi(R,R)
            randomgen=(numpy.random.rand()-0.5)*3
            test[ptcl]=numpy.add(test[ptcl],randomgen)
            xsub1=psi(test,test) # make your move for particle "ptcl"
            prob0=xsubzerowave**2
            prob1=xsub1**2 
            
            lamp=min(1,(numpy.float64(prob0)/prob1))
            dice=numpy.random.rand()
            
            if dice<=lamp: # decide if you accepted or rejected
                accept=1
            else:
                accept=0

            movesAttempted+=1

            global counter
            global storage

            if accept==1:
                movesAccepted+=1
                R = test
                answer=calcenergy(R)
                storage.append(answer)

            # updated movesAttempted and movesAccepted
            # here you will compute other things in the next steps
    print "Acceptance ratio: ", movesAccepted/movesAttempted
    return

def WaveFunction1_test1(wavefunction):
    coords=numpy.array([[1.0,0.5,0.3],[-0.2,0.1,-0.1]])
    ions=numpy.array([[-0.7,0.0,0.0],[0.7,0.0,0.0]])
    if numpy.abs(wavefunction(coords,ions)-0.496585)<1e-5:
        return True
    else:
        return False

#if (WaveFunction1_test1(psi)):
#    print 'Wavefunction Test passed'
#else:
#    print 'Wavefunction Test Failed'

ions=numpy.array([[0,0],[0,0]])
temp=5

VMC(temp,ions,numsteps)

print numpy.mean(storage)
print numpy.std(storage)

