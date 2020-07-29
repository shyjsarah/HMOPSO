
#encoding: utf-8
import numpy as np
import random
 

class get_gbest():
    def __init__(self,curr_archiving_in,curr_archiving_fit,particals):
        self.curr_archiving_in = curr_archiving_in  # 存档中所有粒子坐标
        self.curr_archiving_fit = curr_archiving_fit  # 所有粒子适应度值
        self.particals = particals  # 粒子群数量
        self.gbest_in = np.zeros((self.particals, self.curr_archiving_in.shape[1]))  # 初始化gbest坐标
        self.gbest_fit = np.zeros((self.particals, self.curr_archiving_fit.shape[1]))  # 初始化gbest适应度ֵ

    def get_gbest_index(self):
        return random.randint(0, len(self.curr_archiving_in) - 1)
 
    def get_gbest(self):
        for i in range(self.particals):
            gbest_index = self.get_gbest_index()
            self.gbest_in[i] = self.curr_archiving_in[gbest_index] #gbest坐标
            self.gbest_fit[i] = self.curr_archiving_fit[gbest_index] #gbest适应度ֵ
        return self.gbest_in,self.gbest_fit
 

