import numpy as np
import matplotlib.pyplot as plt
import list_to_txt

# 변수
tip_lattice = 3.8
sample_lattice = 4.0
tip_max = 25
delta = 0.1
scan_type = 'x'  # afm, x, xy 중 선택

# 서브플롯 설정
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# potential을 계산하는 함수(sample 모양 결정)
def potential_at_xy_square(x, y):
    return (np.cos(np.pi * 2 * x / sample_lattice) + np.cos(np.pi * 2 * y / sample_lattice))

# x_tip, y_tip 생성
xy_base = np.arange(tip_lattice, tip_max + tip_lattice, tip_lattice)
x_values = [-x for x in xy_base[::-1]] + [0.0] + [x for x in xy_base]
y_values = [y for y in xy_base[::-1]] + [0.0] + [-y for y in xy_base]
x_tip, y_tip = np.meshgrid(x_values, y_values)

# 조건 계산식(tip 모양 결정)
def make_mask_square(x_, y_):
    mask_array = np.ones_like(x_, dtype=bool)
    return mask_array

def make_mask_diamond(x_, y_, boundary):
    condition_array = np.abs(x_) + np.abs(y_)
    mask_array = condition_array <= boundary + 0.0001
    return mask_array

def make_mask_circle(x_, y_, boundary):
    condition_array = x_**2 + y_**2
    mask_array = condition_array <= boundary ** 2 + 0.0001
    return mask_array

# mask_array 생성. make_mask_circle, make_mask_square, make_mask_diamond 중 선택
# mask_array = make_mask_square(x_tip, y_tip)
mask_array = make_mask_diamond(x_tip, y_tip, tip_max)
# mask_array = make_mask_circle(x_tip, y_tip, tip_max)

# 변위 목록 설정
move_range = np.arange(0.0, sample_lattice, delta)

x_ = []
y_ = []

if scan_type == 'afm':
    # 데이터 생성 (move_x를 x로 하고 result를 y로 설정)
    for move_x in move_range:
        for move_y in move_range:
            # move_x와 move_y를 각각 x_tip과 y_tip에 더함
            x_tip_moved = x_tip + move_x
            y_tip_moved = y_tip + move_y
            
            # mask_array가 True인 경우에만 potential 계산
            potential_values = np.zeros_like(x_tip)  # 초기화
            potential_values[mask_array] = potential_at_xy_square(x_tip_moved[mask_array], y_tip_moved[mask_array])
            
            # potential_values 배열의 모든 요소의 합을 구함
            potential_sum = np.sum(potential_values)
            y_.append(potential_sum)
    from matplotlib.patches import Rectangle
    rect = Rectangle((0, 0), move_range[-1], move_range[-1], facecolor='b', alpha=0.5)
    ax2.add_patch(rect)

elif scan_type == 'x':
    move_y = sample_lattice / 2
    for move_x in move_range:
        # move_x와 move_y를 각각 x_tip과 y_tip에 더함
        x_tip_moved = x_tip + move_x
        y_tip_moved = y_tip + move_y
        
        # mask_array가 True인 경우에만 potential 계산
        potential_values = np.zeros_like(x_tip)  # 초기화
        potential_values[mask_array] = potential_at_xy_square(x_tip_moved[mask_array], y_tip_moved[mask_array])
        
        # potential_values 배열의 모든 요소의 합을 구함
        potential_sum = np.sum(potential_values)
        x_.append(move_x)
        y_.append(potential_sum)
    ax2.annotate('', xy=(move_range[-1], 0), xytext=(move_range[0], 0), arrowprops=dict(facecolor='b'))

elif scan_type == 'xy':
    for move_x in move_range:
        move_y = move_x
        # move_x와 move_y를 각각 x_tip과 y_tip에 더함
        x_tip_moved = x_tip + move_x
        y_tip_moved = y_tip + move_y
        
        # mask_array가 True인 경우에만 potential 계산
        potential_values = np.zeros_like(x_tip)  # 초기화
        potential_values[mask_array] = potential_at_xy_square(x_tip_moved[mask_array], y_tip_moved[mask_array])
        
        # potential_values 배열의 모든 요소의 합을 구함
        potential_sum = np.sum(potential_values)
        x_.append(move_x)
        y_.append(potential_sum)
    ax2.annotate('', xy=(move_range[-1], move_range[-1]), xytext=(move_range[0], move_range[0]), arrowprops=dict(facecolor='b'))


# potential sum - index 그래프
ax1.plot(y_, c='b', marker='o', markersize=2)
ax1.set_title(f'Potential Sum - Index\nTip boundary = {tip_max}, lattice = {tip_lattice}, scan type = {scan_type}')
ax1.set_xlabel('Index')
ax1.set_ylabel('Potential Sum')

# 팁 모양
ax2.scatter(x_tip[mask_array], y_tip[mask_array], label='tip', c='b')
ax2.set_title('tip shape')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
# x축과 y축 비율을 동일하게 설정
ax2.set_aspect('equal', adjustable='box')

list_to_txt.copy_for_excel(y_)

# 플롯 표시
plt.tight_layout()
plt.show()
