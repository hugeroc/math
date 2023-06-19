from pynverse import inversefunc
import math
def KDratio2ddg(ratio):
    # ratio = KDmt/KDwt   
    return math.log(1/ratio)*1.987*298/1000
def ddg2KDratio(ddg):
    inv_f = inversefunc(KDratio2ddg,y_values=ddg,domain=[0.00001,100000],# domain 表示原函数自变量区间，
                        open_domain=[True, True])
    return inv_f
  
print('KDwt/KDmt=10,ddg= '+str(KDratio2ddg(10)))
print('KDwt/KDmt=10,ddg= '+str(KDratio2ddg(100)))
print('ddg=-1,KDwt/KDmt= '+str(ddg2KDratio(-1)))
print('ddg=-2,KDwt/KDmt= '+str(ddg2KDratio(-2)))
