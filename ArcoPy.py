import copy
import threading
import time

BEST_STEPS_TAKEN = []
BEST_SCORE = 300
BEST_QUANTITY = 0
NUM_OPTIONS = 10
BEST_ORBS = []
SHARED_LOCK = threading.Lock()
#eval numbers:
MOST_OF_ONE = 47
LEAST_OF_ONE = 35




def Walking (quantity, maxSteps, t_name, spheres, steps, depth, iteration):
    #global BEST_SCORE
    #if depth == 1:
    #        print(t_name,"doing a depth one operation")
    #        print("Best score is",BEST_SCORE,"for iteration",iteration)
    if depth >= maxSteps:
        score = evaluation(spheres)
        if score < 0:
            print("score less than 0, something wrong")
            return
        global BEST_SCORE
        global BEST_STEPS_TAKEN
        global BEST_ORBS
        global BEST_QUANTITY
        with SHARED_LOCK:
            if (score < BEST_SCORE):
                print("\n",t_name,"finds its score of",score,"beats the current score of", BEST_SCORE,"with:")
                BEST_SCORE = score
                BEST_STEPS_TAKEN = copy.copy(steps)
                BEST_ORBS = spheres
                BEST_QUANTITY = quantity
                print("Steps:", maxSteps," \nBest path:", BEST_STEPS_TAKEN," \nBest orbs:", BEST_ORBS," \nSize of batches:", quantity)
        return
        
    for i in range(NUM_OPTIONS):
        if depth == 0:
            print(t_name,"completion %:", (i / NUM_OPTIONS) * 100)
        if (iteration == 1) and (BEST_SCORE <= 38):
            print("Best score good enough:",BEST_SCORE,", moving to second step.")
            break
        if (iteration == 2) and (BEST_SCORE <= 15):
            print("Best score good enough:",BEST_SCORE,", moving to third step.")
            break
        if (iteration == 3) and (BEST_SCORE <= 4):
            print("Best score good enough, finishing up.")
            break
        if ((i == 0) and (spheres[4] >= quantity) and (spheres[7] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair1")
            Walking(quantity, maxSteps, t_name, pair1(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 1) and (spheres[0] >= quantity) and (spheres[5] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair2")
            Walking(quantity, maxSteps, t_name, pair2(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 2) and (spheres[2] >= quantity) and (spheres[5] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair3")
            Walking(quantity, maxSteps, t_name, pair3(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 3) and (spheres[3] >= quantity) and (spheres[4] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair4")
            Walking(quantity, maxSteps, t_name, pair4(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 4) and (spheres[1] >= quantity) and (spheres[3] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair5")
            Walking(quantity, maxSteps, t_name, pair5(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 5) and (spheres[2] >= quantity) and (spheres[6] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair6")
            Walking(quantity, maxSteps, t_name, pair6(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 6) and (spheres[0] >= quantity) and (spheres[6] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair7")
            Walking(quantity, maxSteps, t_name, pair7(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 7) and (spheres[1] >= quantity) and (spheres[7] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("pair8")
            Walking(quantity, maxSteps, t_name, pair8(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 8) and (spheres[0] >= quantity) and (spheres[2] >= quantity) and (spheres[3] >= quantity) and (spheres[7] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("set1")
            Walking(quantity, maxSteps, t_name, set1(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        if ((i == 9) and (spheres[1] >= quantity) and (spheres[4] >= quantity) and (spheres[5] >= quantity) and (spheres[6] >= quantity)):
            extrasteps = copy.copy(steps)
            extrasteps.append("set2")
            Walking(quantity, maxSteps, t_name, set2(copy.copy(spheres),quantity),extrasteps, depth + 1,iteration)
        
    if depth == 0:
        print(t_name,"completion %: 100")
    return
    
def evaluation (spheres):
    # lower is better
    # how off is the current output from the desired output?
    #desired output: between 50 and 28 spheres for each type
    score = 0
    
    for i in range(8):
        if i != 2:
            if spheres[i] > MOST_OF_ONE:
                score = score + (spheres[i] - MOST_OF_ONE)
            elif spheres[i] < LEAST_OF_ONE:
                score = score + (LEAST_OF_ONE - spheres[i])
            else:
                pass
        else:
            if spheres[i] > (MOST_OF_ONE + 10):
                score = score + (spheres[i] - MOST_OF_ONE + 10)
            elif spheres[i] < (LEAST_OF_ONE + 10):
                score = score + (LEAST_OF_ONE + 10 - spheres[i])
            else:
                pass
    '''
    for i in spheres:
        if i > MOST_OF_ONE:
            score = score + (i - MOST_OF_ONE)
        elif i < LEAST_OF_ONE:
            score = score + (LEAST_OF_ONE - i)
        else:
            pass
    '''
    return score
    
    
def pair1 (spheres, quantity): # 4,7
    spheres[4] = spheres[4] - quantity
    spheres[7] = spheres[7] - quantity
    spheres[3] = spheres[3] + quantity
    spheres[5] = spheres[5] + quantity
    return spheres

def pair2 (spheres, quantity): # 0,5
    spheres[0] = spheres[0] - quantity
    spheres[5] = spheres[5] - quantity
    spheres[2] = spheres[2] + quantity
    spheres[4] = spheres[4] + quantity
    return spheres

def pair3 (spheres, quantity): # 2,5
    spheres[2] = spheres[2] - quantity
    spheres[5] = spheres[5] - quantity
    spheres[3] = spheres[3] + quantity
    spheres[6] = spheres[6] + quantity
    return spheres

def pair4 (spheres, quantity): # 3,4
    spheres[4] = spheres[4] - quantity
    spheres[3] = spheres[3] - quantity
    spheres[1] = spheres[1] + quantity
    spheres[2] = spheres[2] + quantity
    return spheres

def pair5 (spheres, quantity): # 1,3
    spheres[1] = spheres[1] - quantity
    spheres[3] = spheres[3] - quantity
    spheres[6] = spheres[6] + quantity
    spheres[7] = spheres[7] + quantity
    return spheres

def pair6 (spheres, quantity): # 2,6
    spheres[2] = spheres[2] - quantity
    spheres[6] = spheres[6] - quantity
    spheres[0] = spheres[0] + quantity
    spheres[1] = spheres[1] + quantity
    return spheres

def pair7 (spheres, quantity): # 0,6
    spheres[0] = spheres[0] - quantity
    spheres[6] = spheres[6] - quantity
    spheres[7] = spheres[7] + quantity
    spheres[5] = spheres[5] + quantity
    return spheres    

def pair8 (spheres, quantity): # 1,7
    spheres[1] = spheres[1] - quantity
    spheres[7] = spheres[7] - quantity
    spheres[0] = spheres[0] + quantity
    spheres[4] = spheres[4] + quantity
    return spheres
#---------------------------------------
def set1 (spheres, quantity): # 0,2,3,7
    spheres[0] = spheres[0] - quantity
    spheres[2] = spheres[2] - quantity
    spheres[3] = spheres[3] - quantity
    spheres[7] = spheres[7] - quantity
    
    spheres[1] = spheres[1] + quantity
    spheres[4] = spheres[4] + quantity
    spheres[5] = spheres[5] + quantity
    spheres[6] = spheres[6] + quantity
    return spheres

def set2 (spheres, quantity): # 1,4,5,6
    spheres[1] = spheres[1] - quantity
    spheres[4] = spheres[4] - quantity
    spheres[5] = spheres[5] - quantity
    spheres[6] = spheres[6] - quantity
    
    spheres[0] = spheres[0] + quantity
    spheres[2] = spheres[2] + quantity
    spheres[3] = spheres[3] + quantity
    spheres[7] = spheres[7] + quantity
    return spheres
    
if __name__ == "__main__":
    #can only add more threads if max steps is increased as well, by the same amount.
    
    #spheres: gamma, epsilon, zeta, theta, lambda, xi, phi, omega
    spheres = [29,71,9,3,44,13,102,16]
    
    #array order: [[score],[num_steps],[steps_taken],[orb count post-steps],[fed in each step]]
    best_array = [[],[],[],[],[]]
    
    #goal: all spheres under 48 and above 30
    steps_taken = []
    depth = 0
    threadList = []
    feed_size = 9
    max_steps = 7
    print("+++++++Starting execution cycle 1+++++++")
    iteration = 1
    #------------------------------------------
    for i in range(3): 
        tname = "Thread_"+str(i+1)
        tfeed_size = feed_size-i
        t = threading.Thread(group=None,target=Walking,name=tname,args=(tfeed_size, max_steps, tname, spheres, steps_taken, depth,iteration))
        threadList.append(t)
        
    [t.start() for t in threadList]
    [t.join() for t in threadList]

    print("Best score:", BEST_SCORE)
    print("Steps:", max_steps)
    print("Best path:", BEST_STEPS_TAKEN)
    print("Best orbs:", BEST_ORBS)
    print("Size of batches:", BEST_QUANTITY)
    
    #store this cycle's best
    best_array[0].append(copy.copy(BEST_SCORE))
    best_array[1].append(copy.copy(max_steps))
    best_array[2].append(copy.copy(BEST_STEPS_TAKEN))
    best_array[3].append(copy.copy(BEST_ORBS))
    best_array[4].append(copy.copy(BEST_QUANTITY))
    
    #------------------------------------------
    print("+++++++Starting execution cycle 2+++++++")
    depth = 0
    feed_size = 9
    iteration = 2
    threadList = []
    steps_taken = []
    spheres = copy.copy(BEST_ORBS)
    print("current state of orbs is:",spheres)
    
    for i in range(3):
        tname = "Thread_"+str(i+1)
        tfeed_size = feed_size-i
        t = threading.Thread(group=None,target=Walking,name=tname,args=(tfeed_size, max_steps, tname, spheres, steps_taken, depth,iteration))
        threadList.append(t)
        
    [t.start() for t in threadList]
    [t.join() for t in threadList]

    print("Best score:", BEST_SCORE)
    print("Steps:", max_steps)
    print("Best path:", BEST_STEPS_TAKEN)
    print("Best orbs:", BEST_ORBS)
    print("Size of batches:", BEST_QUANTITY)
    
    #store this cycle's best
    best_array[0].append(copy.copy(BEST_SCORE))
    best_array[1].append(copy.copy(max_steps))
    best_array[2].append(copy.copy(BEST_STEPS_TAKEN))
    best_array[3].append(copy.copy(BEST_ORBS))
    best_array[4].append(copy.copy(BEST_QUANTITY))
    
    #------------------------------------------
    print("+++++++Starting execution cycle 3+++++++")
    depth = 0
    iteration = 3
    spheres = copy.copy(BEST_ORBS)
    feed_size = 4
    max_steps = 2
    while BEST_SCORE > 5:
        if max_steps >= 7:
            break
        threadList = []
        steps_taken = []
        max_steps = max_steps+1
        print("Trying final step with step size of", max_steps)
        
        for i in range(3):
            tname = "Thread_"+str(i+1)
            tfeed_size = feed_size-i
            t = threading.Thread(group=None,target=Walking,name=tname,args=(tfeed_size, max_steps, tname, spheres, steps_taken, depth,iteration))
            threadList.append(t)
        
        [t.start() for t in threadList]
        [t.join() for t in threadList]
        
    
    #store this cycle's best
    best_array[0].append(copy.copy(BEST_SCORE))
    best_array[1].append(copy.copy(max_steps))
    best_array[2].append(copy.copy(BEST_STEPS_TAKEN))
    best_array[3].append(copy.copy(BEST_ORBS))
    best_array[4].append(copy.copy(BEST_QUANTITY))
    
    #------------------------------------------
    '''
    print("+++++++Starting execution cycle 4+++++++")
    depth = 0
    iteration = 3
    spheres = copy.copy(BEST_ORBS)
    feed_size = 8
    max_steps = 2
    while BEST_SCORE > 5:
        if max_steps >= 7:
            break
        threadList = []
        steps_taken = []
        max_steps = max_steps+1
        print("Trying final step with step size of", max_steps)
        
        for i in range(3):
            tname = "Thread_"+str(i+1)
            tfeed_size = feed_size-i
            t = threading.Thread(group=None,target=Walking,name=tname,args=(tfeed_size, max_steps, tname, spheres, steps_taken, depth,iteration))
            threadList.append(t)
        
        [t.start() for t in threadList]
        [t.join() for t in threadList]
        
    
    #store this cycle's best
    best_array[0].append(copy.copy(BEST_SCORE))
    best_array[1].append(copy.copy(max_steps))
    best_array[2].append(copy.copy(BEST_STEPS_TAKEN))
    best_array[3].append(copy.copy(BEST_ORBS))
    best_array[4].append(copy.copy(BEST_QUANTITY))
    '''
    print("Final stats:")
    print("Score:",best_array[0])
    #print("Step amounts:",best_array[1])
    print("Step orders:",best_array[2][0])
    print("Step orders:",best_array[2][1])
    print("Step orders:",best_array[2][2])
    #print("Step orders:",best_array[2][3])
    print("Orbs at the start of each set of steps:",best_array[3])
    print("Feed sizes for each set of steps:",best_array[4])
    #end