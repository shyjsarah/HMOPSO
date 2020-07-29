import random
import numpy as np

def vary(in_,w_now,max_,min_):
    i=random.randint(0,len(in_)-1)
    v_pos = np.random.randint(0, len(in_[0]) - 1, int(w_now * 25))
    for j in range(len(v_pos)):
        in_[i][v_pos[j]] = random.randint(int(min_[0]), int(max_[0]))
    '''
    for i in range(len(in_)):
        v_pos = np.random.randint(0, len(in_[0])-1, int(w_now*25))
        for j in range(len(v_pos)):
            in_[i][v_pos[j]]=random.randint(int(min_[0]),int(max_[0]))
    '''
    return in_

def cross(in_,archive_in,w_now):
    for i in range(len(in_)):
        in_ref=archive_in[random.randint(0,len(archive_in)-1)]
        v_pos = np.random.randint(0, len(in_[0])-1, int((1-w_now)* 25))
        for j in range(len(v_pos)):
            in_[i][v_pos[j]]=in_ref[v_pos[j]]
    return in_

