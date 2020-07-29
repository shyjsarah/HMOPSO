#encoding: utf-8
import random
import numpy as np
import archive
import pareto
#
def init_designparams(particals,in_min,in_max, pm , vm):
    in_dim = len(in_max)     #输入参数维度
    in_temp = np.zeros((particals,in_dim))

    for i in range(particals):
        pm_tmp=pm.copy()
        for j in range(in_dim):
            index = random.randint(0, len(pm) - 1)
            while(((vm[j][0] + pm_tmp[index][0]) > 1) or ((vm[j][1] +pm_tmp[index][1]) > 1)):
                index = random.randint(0, len(pm) - 1)
            in_temp[i,j]=index
            pm_tmp[index][0] += vm[j][0]
            pm_tmp[index][1] += vm[j][1]

    return in_temp

def init_v(particals,v_max,v_min):
    v_dim = len(v_max)     #输入参数维度
    v_ = np.zeros((particals,v_dim))
    return v_
def init_pbest(in_,fitness_):
    return in_,fitness_
def init_archive(in_,fitness_):
    pareto_c = pareto.Pareto_(in_,fitness_)
    curr_archiving_in,curr_archiving_fit = pareto_c.pareto()
    return curr_archiving_in,curr_archiving_fit
def init_gbest(curr_archiving_in,curr_archiving_fit,particals):
    get_g = archive.get_gbest(curr_archiving_in,curr_archiving_fit,particals)
    return get_g.get_gbest()
