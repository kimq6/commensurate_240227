import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# 변수 (tip_lattice)
tip_lattice = 3.8
sample_lattice = 4.0
tip_max = 300
delta = 0.1

# potential을 계산 함수
def potential_at_xy(x, y, λ):
    return (np.cos(np.pi * 2 * x / λ) + np.cos(np.pi * 2 * y / λ))

# tip_boundary = 크기, move_x, move_y는 변위, potential_sum을 반환하는 함수. 조건 계산과 mask_array의 조건에 따라 모양을 바꿀 수 있다
def potential_sum(tip_boundary, move_x, move_y):
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

    # move_x와 move_y를 각각 x_tip과 y_tip에 더함
    x_tip = x_tip + move_x
    y_tip = y_tip + move_y

    # mask_array가 True인 경우에만 potential 계산
    potential_values = np.zeros_like(x_tip)  # 초기화
    potential_values[mask_array] = potential_at_xy(x_tip[mask_array], y_tip[mask_array], sample_lattice)

    # potential_values 배열의 모든 요소의 합을 구함
    total_potential_sum = np.sum(potential_values)
    
    return total_potential_sum

# move_x, move_y 범위를 설정
move_range = np.arange(0.0, sample_lattice, delta)

# tip_boundary 범위를 설정
tip_boundary_range = np.arange(0.0, tip_max, tip_lattice)

max_min = []
for tip_boundary in tqdm(tip_boundary_range, desc='progress bar'):
    potential_sums = []
    for move_x in move_range:
        for move_y in move_range:
            potential_sums.append(potential_sum(tip_boundary, move_x, move_y))
    max_min.append(max(potential_sums) - min(potential_sums))

print(max_min)

# 그래프 그리기
fig, ax1 = plt.subplots()

x_ = range(1, len(tip_boundary_range) + 1)
ax1.plot(range(1, len(tip_boundary_range) + 1), max_min, marker='o', color='b')
ax1.set_xlabel('Tip index\nTip boundary')
ax1.set_ylabel('Max-Min Potential Sum', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# x축 눈금과 레이블 설정
x_ticks = np.linspace(x_[0], x_[-1], 10)
ax1.set_xticks(x_ticks)
ax1.set_xticklabels([f'{x:.0f}\n{x * tip_lattice:.2f}' for x in x_ticks])

plt.title(f'tip lattice = {tip_lattice}Å, sample lattice = {sample_lattice}Å\ndelta = {delta}Å, tip max = {tip_max}Å')
plt.grid(True)
plt.tight_layout()
plt.show()
