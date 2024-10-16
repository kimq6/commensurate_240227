import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import list_to_txt

# 변수
tip_lattice = 3.8
sample_lattice = 4.0
tip_max = 500
delta = 0.1
scan_type = 'x'  # afm, x, xy 중 선택
tip_shape = 'circle'  # square, diamond, circle 중 선택

# potential을 계산하는 함수(sample 모양 결정)
def potential_at_xy_square(x, y):
    return (np.cos(np.pi * 2 * x / sample_lattice) + np.cos(np.pi * 2 * y / sample_lattice))

# x_tip, y_tip 생성
xy_base = np.arange(tip_lattice, tip_max + tip_lattice, tip_lattice)
x_values = [-x for x in xy_base[::-1]] + [0.0] + [x for x in xy_base]
y_values = [y for y in xy_base[::-1]] + [0.0] + [-y for y in xy_base]
x_tip, y_tip = np.meshgrid(x_values, y_values)

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

# tip_boundary = 크기, move_x, move_y는 변위, potential_sum을 반환하는 함수. 조건 계산과 mask_array의 조건에 따라 모양을 바꿀 수 있다
def potential_sum(tip_boundary, move_x, move_y):
    # mask_array 생성
    mask_array = make_mask(x_tip, y_tip, tip_boundary)
    
    # move_x와 move_y를 각각 x_tip과 y_tip에 더함
    x_tip_moved = x_tip + move_x
    y_tip_moved = y_tip + move_y
    
    # mask_array가 True인 경우에만 potential 계산
    potential_values = np.zeros_like(x_tip)  # 초기화
    potential_values[mask_array] = potential_at_xy_square(x_tip_moved[mask_array], y_tip_moved[mask_array])
    
    # potential_values 배열의 모든 요소의 합을 구함
    potential_sum = np.sum(potential_values)
    return potential_sum

# 변위 목록 설정
move_range = np.arange(0.0, sample_lattice, delta)

# tip_boundary 목록 설정
tip_boundary_range = np.arange(0.0, tip_max, tip_lattice)

if scan_type == 'afm':
    # afm 방식 스캔
    import itertools
    max_min = []
    for tip_boundary in tqdm(tip_boundary_range, desc='progress bar'):
        potential_sums = []
        for move_x, move_y in itertools.product(move_range, repeat=2):
            potential_sums.append(potential_sum(tip_boundary, move_x, move_y))
        max_min.append(max(potential_sums) - min(potential_sums))
elif scan_type == 'x':
    # x방향 스캔
    max_min = []
    move_y = sample_lattice / 2
    for tip_boundary in tqdm(tip_boundary_range, desc='progress bar'):
        potential_sums = []
        for move_x in move_range:
            potential_sums.append(potential_sum(tip_boundary, move_x, move_y))
        max_min.append(max(potential_sums) - min(potential_sums))
elif scan_type == 'xy':
    # xy방향 스캔
    max_min = []
    for tip_boundary in tqdm(tip_boundary_range, desc='progress bar'):
        potential_sums = []
        for move_x in move_range:
            move_y = move_x
            potential_sums.append(potential_sum(tip_boundary, move_x, move_y))
        max_min.append(max(potential_sums) - min(potential_sums))
else:
    raise ValueError('scan_type은 afm, x, xy 중 하나여야 합니다')

list_to_txt.copy_for_excel(max_min, p=True)

# 그래프 그리기
fig, ax1 = plt.subplots(figsize=(12, 8))

x_ = range(1, len(tip_boundary_range) + 1)
ax1.plot(x_, max_min, marker='o', color='b')
ax1.set_ylabel('Max-Min', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# x축 눈금 설정
x_ticks = np.linspace(x_[0], x_[-1], 10)
ax1.set_xticks(x_ticks)
if tip_shape == 'square':
    ax1.set_xticklabels([f'{x:.0f}\n{(x - 1) * 2 * tip_lattice:.2f}' for x in x_ticks])
    ax1.set_xlabel('Tip index\nside length[Å]')
elif tip_shape == 'diamond':
    ax1.set_xticklabels([f'{x:.0f}\n{(x - 1) * np.sqrt(2) * tip_lattice:.2f}' for x in x_ticks])
    ax1.set_xlabel('Tip index\nside length[Å]')
elif tip_shape == 'circle':
    ax1.set_xticklabels([f'{x:.0f}\n{(x - 1) * 2 * tip_lattice:.2f}' for x in x_ticks])
    ax1.set_xlabel('Tip index\ndiameter[Å]')

plt.title(f'tip lattice = {tip_lattice}Å, sample lattice = {sample_lattice}Å\ndelta = {delta}Å, tip max = {tip_max}Å, scan_type = {scan_type}')
plt.grid(True)
plt.tight_layout()
plt.show()
