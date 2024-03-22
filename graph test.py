import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)  # 0부터 2π까지의 범위에서 100개의 값 생성
y = np.zeros_like(x)  # x와 같은 크기의 0으로 이루어진 배열 생성

# x_ = np.linspace(0, 2*np.pi, 1000)  # 0부터 2π까지의 범위에서 1000개의 값 생성
random_values = [2*np.pi*x for x in np.random.rand(1000000)]  # 생성된 값 중에서 랜덤하게 100개 선택
# print(random_values)
mean_random_values = np.mean(random_values)
print(np.mean(random_values))
print(np.std(random_values))

average_y = np.zeros_like(x)  # x와 같은 크기의 0으로 이루어진 배열 생성
# 각각의 위상에 대해 사인 함수를 계산하고 더함
for theta in random_values:  # theta는 라디안 단위
    y += np.sin(x + theta)

y_max_index = np.argmax(y)
y_min_index = np.argmin(y)

print(f'y_max : ({x[y_max_index]:.4f}, {y[y_max_index]:.4f})\ny_min : ({x[y_min_index]:.4f}, {y[y_min_index]:.4f})')
print(f'barrier : {y[y_max_index] - y[y_min_index]:.4f}')

plt.plot(x, y)
plt.title('Sum of sin(x + theta)')
plt.xlabel('x')
plt.ylabel('Sum of sin(x + theta)')
plt.grid(True)
plt.show()
