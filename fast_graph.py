import matplotlib.pyplot as plt
import numpy as np

# 임의의 xlist와 ylist 생성
xlist = [0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5]
xlist = [np.power(x, 2) for x in xlist]
ylist = [0.0554768005404096, 0.16636343946809706, 0.16636343946811216, 0.16643040162116307, 0.16629647731510744, 0.3881367173186163, 0.38827064162532565, 0.1664304016234439]
# 그래프 그리기
plt.plot(xlist, ylist, marker='o', linestyle='-', color='r', label='y = x^2')
plt.title('y = x^2')
plt.xticks(xlist)
plt.yticks(ylist)

# 그래프 표시
plt.show()
