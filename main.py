# encoding: utf-8
from HMopso import *
import datetime

def main(a,path_s):
    # 虚拟机参数
    pm = np.zeros((25, 2))
    vm = np.loadtxt("./data/vm_" + str(a + 1) + ".txt")

    #参数
    w = 0.1  # 惯性因子
    c1 = 0.49  # 局部速度因子
    c2 = 1.49  # 全局速度因子
    particals = 100  # 粒子群的数量
    cycle_ = 200  # 迭代次数
    mesh_div = 10  # 网格等分数量
    thresh = 300  # 外部存档阀值

    min_ = np.zeros((len(vm)))  # 粒子坐标的最小值
    max_ = np.full(len(vm),len(pm)-1)  # 粒子坐标的最大值

    w_start=1
    w_end=0

    mopso_ = HMopso(particals, w, c1, c2, max_, min_, thresh, pm , vm, w_start,w_end,mesh_div)  # 粒子群实例化

    pareto_in,pareto_fitness =mopso_.test(cycle_,path_s)
    return pareto_in,pareto_fitness

if __name__ == "__main__":

    path='./HMOPSO/'
    start = datetime.datetime.now()
    a = 51
    ans, std = main(a, path + 'data' + str(a + 1))
    np.savetxt(path + 'data' + str(a + 1) + '/pareto_ans', ans)  # 保存pareto边界粒子的坐标
    np.savetxt(path + 'data' + str(a + 1) + '/pareto_std', std)  # 打印pareto边界粒子的适应值
    end = datetime.datetime.now()
    print(end-start)
