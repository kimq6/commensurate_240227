import numpy as np
import matplotlib.pyplot as plt

# 변수
tip_boundary_index = 2
tip_lattice = 3.8
tip_max = tip_boundary_index * tip_lattice
tip_shape = 'circle'  # square, diamond, circle 중 선택

# x_tip, y_tip 생성
xy_base = np.arange(tip_lattice, tip_max + tip_lattice, tip_lattice)
x_values = [-x for x in xy_base[::-1]] + [0.0] + [x for x in xy_base]
y_values = [y for y in xy_base[::-1]] + [0.0] + [-y for y in xy_base]
x_tip, y_tip = np.meshgrid(x_values, y_values)

# 조건 계산식(tip 모양 결정)
if tip_shape == 'square':
    def make_mask(x_, y_, boundary):
        mask_array = np.ones_like(x_, dtype=bool)
        return mask_array
elif tip_shape == 'diamond':
    def make_mask(x_, y_, boundary):
        condition_array = np.abs(x_) + np.abs(y_)
        mask_array = condition_array <= boundary + 0.0001
        return mask_array
elif tip_shape == 'circle':
    def make_mask(x_, y_, boundary):
        condition_array = x_**2 + y_**2
        mask_array = condition_array <= boundary ** 2 + 0.0001
        return mask_array

mask_array = make_mask(x_tip, y_tip, tip_max)

# 그래프 그리기
plt.figure(figsize=(8, 8))
plt.scatter(x_tip[mask_array], y_tip[mask_array], c='b', marker='o')

# 축 레이블 설정
plt.xlabel('X Tip')
plt.ylabel('Y Tip')
plt.title(f'tip_max = {tip_max}, lattice = {tip_lattice}')

# x축과 y축의 범위 설정
axes_limit = 20
plt.xlim(-axes_limit, axes_limit)
plt.ylim(-axes_limit, axes_limit)

# 축의 비율을 동일하게 설정하여 정사각형 모양의 그래프를 생성
plt.gca().set_aspect('equal', adjustable='box')

# 그래프 보여주기
plt.show()
