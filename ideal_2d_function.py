import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# 격자 potential을 계산하는 함수
def potential_at_xy(x, y, λ):
    return (np.cos(np.pi * 2 * x / λ) + np.cos(np.pi * 2 * y / λ))

# tip_boundary = 크기, move_x, move_y는 변위, potential_sum을 반환하는 함수 where 안의 조건에 따라 모양을 바꿀 수 있다
def potential_sum(tip_boundary, move_x, move_y):
    # 간격 변수 (tip_lattice)
    tip_lattice = 3.83
    sample_lattice = 4.0

    # 1차원 x좌표와 y좌표 배열 생성
    x_values = np.arange(-tip_boundary, tip_boundary + 1) * tip_lattice
    y_values = np.arange(tip_boundary, -tip_boundary - 1, -1) * tip_lattice

    # 2차원 격자 형태의 x좌표와 y좌표 배열 생성
    x_tip, y_tip = np.meshgrid(x_values, y_values)

    # move_x와 move_y를 각각 x_tip과 y_tip에 더함
    x_tip = x_tip + move_x
    y_tip = y_tip + move_y

    # 원점으로부터 거리를 계산하여 tip_boundary보다 큰 좌표는 값을 0으로 설정
    condition_array = np.sqrt(x_tip**2 + y_tip**2)

    # condition_array가 tip_boundary보다 작은 경우 계산
    potential_values = np.where(condition_array <= tip_boundary,
                                potential_at_xy(x_tip, y_tip, sample_lattice), 0)

    # potential_values 배열의 모든 요소의 합을 구함
    total_potential_sum = np.sum(potential_values)
    
    return total_potential_sum

# move_x, move_y 범위를 설정
move_range = np.arange(0.0, 4.1, 0.01)

# tip_boundary 범위를 설정
tip_boundary_range = np.arange(0.1, 100, 4)

max_min = []
for tip_boundary in tqdm(tip_boundary_range, desc='progress bar'):
    potential_sums = []
    for move_x in move_range:
        for move_y in move_range:
            potential_sums.append(potential_sum(tip_boundary, move_x, move_y))
    max_min.append(max(potential_sums) - min(potential_sums))

print(max_min)

# 그래프 그리기
plt.figure() 
plt.plot(tip_boundary_range, max_min, marker='o')
plt.xlabel('Tip Boundary')
plt.ylabel('Max-Min Potential Sum')
plt.title('Max-Min Potential Sum vs Tip Boundary')
plt.grid(True)
plt.show()
