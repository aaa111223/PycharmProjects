import numpy as np 
import matplotlib.pyplot as plt 

# �������������ϵ�� x �� y ����
x = np.arange(0,  3  * np.pi,  0.1) 
y = np.sin(x)
plt.title("sine wave form")  
# ʹ�� matplotlib �����Ƶ�
plt.plot(x, y) 
plt.show()