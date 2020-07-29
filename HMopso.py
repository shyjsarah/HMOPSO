#encoding: utf-8
import numpy as np
from fitness_funs import *
import init
import update
import random
import plot
import plot_test
import inheritance
class HMopso:
    def __init__(self,particals,w,c1,c2,max_,min_,thresh,pm,vm,w_start,w_end,mesh_div=10):
        self.w,self.c1,self.c2 = w,c1,c2
        self.mesh_div = mesh_div
        self.particals = particals
        self.thresh = thresh
        self.max_ = max_
        self.min_ = min_
        self.max_v=max_
        self.min_v=-max_
        self.w_start_=w_start
        self.w_end_=w_end
        #self.max_v = (max_-min_)*0.05  #速度上限
        #self.min_v = (max_-min_)*0.05*(-1) #速度下限
        self.plot_ = plot_test.Plot_pareto()
        self.pm_=pm
        self.vm_=vm
    def evaluation_fitness(self,pm,vm):
        #计算适应度值ֵ
        fitness_curr = []
        for i in range((self.in_).shape[0]):
            fitness_curr.append(fitness_(self.in_[i],pm,vm))
        self.fitness_ = np.array(fitness_curr)
    def inherit(self,i,max_ite):
        w_now=self.w_start_-(self.w_start_-self.w_end_)*(i/max_ite)
        rand=random.uniform(0,1)
        if(w_now>rand):
            self.in_=inheritance.vary(self.in_,w_now,self.max_,self.min_)
        else:
            self.in_=inheritance.cross(self.in_,self.archive_in,w_now)
    def initialize(self):
        #初始化粒子位置
        self.in_ = init.init_designparams(self.particals,self.min_,self.max_,self.pm_,self.vm_)
        #初始化粒子速度
        self.v_ = init.init_v(self.particals,self.min_v,self.max_v)
        #计算适应度ֵ
        self.evaluation_fitness(self.pm_,self.vm_)
        #初始化个体最优
        self.in_p,self.fitness_p = init.init_pbest(self.in_,self.fitness_)
        #初始化外部存档
        self.archive_in,self.archive_fitness = init.init_archive(self.in_,self.fitness_)
        #初始化全局最优
        self.in_g,self.fitness_g = init.init_gbest(self.archive_in,self.archive_fitness,self.particals)
    def update_(self,i,max_ite):
        #更新粒子速度、位置、适应度、个体最优、外部存档、全局最优
        self.v_ = update.update_v(self.v_,self.min_v,self.max_v,self.in_,self.in_p,self.in_g,self.w,self.c1,self.c2)
        self.in_ = update.update_in(self.in_,self.v_,self.min_,self.max_)
        self.inherit(i,max_ite)
        self.evaluation_fitness(self.pm_,self.vm_)
        self.in_p,self.fitness_p = update.update_pbest(self.in_,self.fitness_,self.in_p,self.fitness_p)
        self.archive_in,self.archive_fitness = update.update_archive(self.in_,self.fitness_,self.archive_in,self.archive_fitness,self.thresh,self.mesh_div,self.min_,self.max_,self.particals)
        self.in_g,self.fitness_g = update.update_gbest(self.archive_in,self.archive_fitness,self.particals)
    def test(self,max_ite,path_s):
        self.initialize()
        self.plot_.show(self.in_, self.fitness_, self.archive_in, self.archive_fitness,0,path_s)
        for i in range(max_ite):
            self.update_(i,max_ite)
            self.plot_.show(self.in_, self.fitness_, self.archive_in, self.archive_fitness,i+1,path_s)
        return self.archive_in, self.archive_fitness
