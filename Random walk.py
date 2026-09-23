import copy, math
import numpy as np
import matplotlib.pyplot as plt
import random

m=1000
s=0.5
mu=1
n=np.sqrt(m)

list1=[-1/n,1/n]

list2=[]
list3=[]
M=0
list2.append(M)
#list3.append()

#x=random.choice(list1)
#print(x)

for i in range(m):
    res=random.choices(list1, weights=[1, 1], k=1)
    x_i=res[0]
    M=M+x_i
    list2.append(M)
    #a=s*M-(mu-0.5*s*s)*i
    S1=(1+s/np.sqrt(m))**(0.5*(mu*i+M))
    S2 = (1 - s / np.sqrt(m)) ** (0.5 * (mu*i - M))
    S=S1*S2
    list3.append(S)

#plt.plot(list2, marker="o", color="blue",linestyle="-")
#plt.plot(list2, color="blue",linestyle="-")
#plt.plot(list3, color="red",linestyle="-")
#plt.title("random walk")
#plt.xlabel("n")
#plt.ylabel("height")
#plt.grid(True)
#plt.show()

fig, ax1 = plt.subplots()

# Левая ось Y для List2
ax1.plot(list2, color="blue", label="Random Walk")
ax1.set_xlabel("n")
ax1.set_ylabel("walk", color="blue")

# Правая ось Y для list3
ax2 = ax1.twinx()
ax2.plot(list3, color="red", label="Geometric process")
ax2.set_ylabel("binomial", color="red")

plt.title("random walk + binomial")
plt.show()








