#encoding: utf-8
import numpy as np
#为了便于图示观察，试验测试函数为二维输入、二维输出
#适应值函数：实际使用时请根据具体应用背景自定义
def fitness_(in_,pm,vm):
    pm_tmp=pm.copy()
    for i in range(len(in_)):
        pm_tmp[int(in_[i])][0] += vm[i][0]
        pm_tmp[int(in_[i])][1] += vm[i][1]
    if(len(pm_tmp[pm_tmp>1])==0):
        return np.std(pm_tmp,axis=0)
    else:
        return [-1,-1]
