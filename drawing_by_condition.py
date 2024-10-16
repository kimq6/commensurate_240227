import numpy as np
import matplotlib.pyplot as plt

# 변수
tip_boundary_index = 3
tip_lattice = 3.9
tip_boundary = tip_boundary_index * tip_lattice

# 1차원 x좌표와 y좌표 배열 생성
x_values = np.arange(-tip_boundary, tip_boundary + tip_lattice, tip_lattice)
y_values = np.arange(tip_boundary, -tip_boundary - tip_lattice, -tip_lattice)

# 2차원 격자 형태의 x좌표와 y좌표 배열 생성
x_tip, y_tip = np.meshgrid(x_values, y_values)

# 조건 계산
# condition_array = np.sqrt(x_tip**2 + y_tip**2)  # 원
condition_array = np.abs(x_tip) + np.abs(y_tip)  # 마름모

# mask_array: 조건에 맞으면 True, 아니면 False
mask_array = condition_array <= tip_boundary + 0.01  # 원이나 마름모
# mask_array = np.ones_like(x_tip, dtype=bool)  # 네모

# 그래프 그리기
plt.figure(figsize=(8, 8))
plt.scatter(x_tip[mask_array], y_tip[mask_array], c='b', marker='o')

# 축 레이블 설정
plt.xlabel('X Tip')
plt.ylabel('Y Tip')
plt.title(f'tip_max = {tip_boundary}, lattice = {tip_lattice}')

# x축과 y축의 범위 설정
axes_limit = 20
plt.xlim(-axes_limit, axes_limit)
plt.ylim(-axes_limit, axes_limit)

# 축의 비율을 동일하게 설정하여 정사각형 모양의 그래프를 생성
plt.gca().set_aspect('equal', adjustable='box')

# 그래프 보여주기
plt.show()
