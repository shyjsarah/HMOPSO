#encoding: utf-8
import numpy as np
import random
import pareto
import archive
def update_v(v_,v_min,v_max,in_,in_pbest,in_gbest,w,c1,c2):
    #更新速度ٶ�ֵ
    v_temp = w*v_ + c1*random.uniform(0,1)*(in_pbest-in_) + c2*random.uniform(0,1)*(in_gbest-in_)
    #速度边界处理ֵ
    for i in range(v_temp.shape[0]):
        for j in range(v_temp.shape[1]):
            v_temp[i,j]=int(v_temp[i,j])
            if v_temp[i,j]<v_min[j]:
                v_temp[i,j] = v_min[j]
            if v_temp[i,j]>v_max[j]:
                v_temp[i,j] = v_max[j]
    return v_temp
def update_in(in_,v_,in_min,in_max):
    #更新位置
    in_temp = in_ + v_
    #越界处理ֵ
    for i in range(in_temp.shape[0]):
        for j in range(in_temp.shape[1]):
            in_temp[i,j]=int(in_temp[i,j])
            if in_temp[i,j]<in_min[j]:
                in_temp[i,j] = in_min[j]
            if in_temp[i,j]>in_max[j]:
                in_temp[i,j] = in_max[j]
    return in_temp
def compare_pbest(in_indiv,pbest_indiv):
    if(in_indiv[0]==-1):
        return False
    num_greater = 0
    num_less = 0
    for i in range(len(in_indiv)):
        if in_indiv[i] < pbest_indiv[i]:
            num_greater = num_greater +1
        if in_indiv[i] > pbest_indiv[i]:
            num_less = num_less +1
    #如果当前支配历史，更新
    if (num_greater>0 and num_less==0):
        return True
    #如果历史支配当前粒子，不更新
    elif (num_greater==0 and num_less>0):
        return False
    else:
        #如果互不支配，随机选择
        random_ = random.uniform(0.0,1.0)
        if random_ > 0.5:
            return True
        else:
            return False
def update_pbest(in_,fitness_,in_pbest,out_pbest):
    for i in range(out_pbest.shape[0]):
        #ͨ比较历史pbest和当前适应度，决定是否要更新
        if compare_pbest(fitness_[i],out_pbest[i]):
            out_pbest[i] = fitness_[i]
            in_pbest[i] = in_[i]
    return in_pbest,out_pbest
def update_archive(in_,fitness_,archive_in,archive_fitness,thresh,mesh_div,min_,max_,particals):
    ##首先，计算当前粒子群的pareto边界，将边界粒子加入到存档archiving中
    pareto_1 = pareto.Pareto_(in_,fitness_)
    curr_in,curr_fit = pareto_1.pareto()
    ##其次，在存档中根据支配关系进行第二轮筛选，将非边界粒子去除
    in_new = np.concatenate((archive_in,curr_in),axis=0)
    fitness_new = np.concatenate((archive_fitness,curr_fit),axis=0)
    pareto_2 = pareto.Pareto_(in_new,fitness_new)
    curr_archiving_in,curr_archiving_fit = pareto_2.pareto()

    return curr_archiving_in,curr_archiving_fit
def update_gbest(archiving_in,archiving_fit,particals):
    get_g = archive.get_gbest(archiving_in,archiving_fit,particals)
    return get_g.get_gbest()
