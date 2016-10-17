import os

a = (11, 33, 44, 55)


for i in a:
    for j in range(10):
        fpath = r"C:\Users\ashanker9\Desktop\Molecular_Dynamics_Data\%d\hop%d" % (i,j)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        print(fpath)
