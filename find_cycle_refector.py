import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 여러 변수들, 단위 [Å]
lattice = 2
cms_lattice = 1.25
atom_limit = 100
create_base_cms = 70  # 팁 원자를 얼마나 생성, 계산할지(cms) (네모꼴) (atom_N_cms 보다 크게)

# 시그마 값
sigma_2d = 4.5
sigma_3d = 3.5

radius_cms = 10  # tip 원 반지름(cms) (보여주기)

cycle = 8

atom_N_cms = 7  # 보여줄 원자개수(1D)
graph_column = int(np.ceil(cycle / 2)) + 1
print(f'graph_column {graph_column}')

ax_limit = round(radius_cms * 1.2 + lattice)  # 그래프 확대 (보여주기)

fig = plt.figure(figsize=(15, 7.5))
# 일단 그림
ax0 = fig.add_subplot(2, graph_column, 1, title="1D")
ax0.set_xticks([x * s for s in (1, -1) for x in np.arange(0, ax_limit, cms_lattice)])

# 각 원자별 그래프
axes = []
for n in range(cycle):
    if n < graph_column - 1:
        ax = fig.add_subplot(2, graph_column, n + 2, title=f'atom / {cycle} remain ... {n}')
    else:
        ax = fig.add_subplot(2, graph_column, n + 3, title=f'atom / {cycle} remain ... {n}')
    axes.append(ax)

# 앞에 보이게 하려고 뒤에만듦
ax_sum = fig.add_subplot(2, graph_column, graph_column + 1, title=f"sum of {atom_N_cms} graph")


print(f'atom_N_cms = {atom_N_cms}')


ax0.set_xlim(-ax_limit, ax_limit)
ax0.set_ylim(-ax_limit, ax_limit)
# ax0.set_aspect("equal")

# 격자 그리기 (파악하기 쉽게)
ax0.set_xticks([x * s for s in (1, -1) for x in np.arange(0, ax_limit, cms_lattice)])
# ax1.set_xticks([x * s for s in (1, -1) for x in np.arange(0, ax_limit, inc_lattice)])

# 좌표 베이스
atom_base = [x * s for s in (1, -1) for x in np.arange(lattice / 2, atom_limit, lattice)]

# 1D 그리기
ax0.scatter(atom_base, [0 for x in atom_base], c='k', s=3)
# ax0.axis('off')

# ax1.scatter(atom_base, [0 for x in atom_base], c='k', s=3)
# ax1.axis('off')

# 2D 그리기
# atom_x_mesh, atom_y_mesh = np.meshgrid(atom_base, atom_base)

# ax2.scatter(atom_x_mesh, atom_y_mesh, c='k', s=3)
# ax2.axis('off')

# ax3.scatter(atom_x_mesh, atom_y_mesh, c='k', s=3)
# ax3.axis('off')

# 팁 원자 베이스(commensurate)
tip_base_cms = [x * s for x in np.arange(cms_lattice, create_base_cms, cms_lattice) for s in (1, -1)]
tip_base_cms.insert(0, 0.0)

# 팁 원자 베이스(incommensurate)
# tip_base_inc = [x * s for x in np.arange(inc_lattice, create_base_inc, inc_lattice) for s in (1, -1)]
# tip_base_inc.insert(0, 0.0)

# ax0 팁 그리기
ax0.scatter(tip_base_cms, [3.647 for x in tip_base_cms], c='pink', s=10, marker='o', alpha=0.5)  # 분홍
tip_base_cms_in = [x for x in tip_base_cms if abs(x) < radius_cms]
ax0.scatter(tip_base_cms_in, [3.647 for x in tip_base_cms_in], c='r', s=10, marker='o')  # 빨강

def distance_2d(cor1, cor2):
    return np.sqrt(np.power((cor1[0]-cor2[0]), 2) + np.power((cor1[1]-cor2[1]), 2))


def distance_3d(cor1, cor2):
    return np.sqrt(np.power((cor1[0]-cor2[0]), 2) + np.power((cor1[1]-cor2[1]), 2) + np.power((cor1[2]-cor2[2]), 2))


# 퍼텐셜값 찾기
def potential_2d(cor1, cor2, d_ij=0.105, x_ij=3.851, sigma=sigma_2d):
    distance = distance_2d(cor1, cor2)
    if distance < sigma * np.power(2, -1/6) * x_ij:  # 시그마 안의 거리에 있는 원자는 그냥 포텐셜 값 구하기
        return d_ij * (np.power((x_ij/distance), 12) - 2 * np.power((x_ij/distance), 6))
    else:  # 시그마 값 넘는 원자는 potential 0 으로 취급
        return 0


def potential_3d(cor1, cor2, d_ij=0.105, x_ij=3.851, sigma=sigma_3d):  # cor1, cor2: 3차원 좌표 2개, d: DIJ, x: xIJ, sigma: 몇 시그마까지 할지
    distance = distance_3d(cor1, cor2)
    if distance < sigma * np.power(2, -1/6) * x_ij:  # 시그마 안의 거리에 있는 원자는 그냥 포텐셜 값 구하기
        return d_ij * (np.power((x_ij/distance), 12) - 2 * np.power((x_ij/distance), 6))
    else:  # 시그마 값 넘는 원자는 potential 0 으로 취급
        return 0


# 아니 이걸 반복하라고?
print(f'1D', end=" >> ")
z_0_1D_cms = 0  # potential 합이 최소일 때 z값 저장할곳
potential_0_1D_cms = 100000
for z_ in np.arange(3.5, 3.7, 0.001):  # 이 범위에서 z반복
    potential_sum = 0
    for tip in tip_base_cms:
        for x_ in atom_base:
            potential_sum += potential_2d((x_, 0), (tip, z_))
    if potential_0_1D_cms > potential_sum:
        z_0_1D_cms = z_
        potential_0_1D_cms = potential_sum
print(f'z0 = {z_0_1D_cms}')

for remain in range(cycle):
    ax_sum_x = []
    ax_sum_y = []
    color = cm.jet(remain / cycle)
    for atom_n in [x for x in range(1, len(tip_base_cms) + 1) if x % cycle == remain]:
        tip_inc_in = tip_base_cms[0:atom_n]  # 안에 있는 원자들만 고르기
        potential_sums = []
        for x_move in np.arange(0, lattice, 0.1):  # 옆으로 조금씩 움직이면서 반복
            potential_sum = 0.0  # potential 합 초기화
            for tip in tip_inc_in:  # tip의 좌표들
                for x_ in atom_base:  # 원자의 좌표들
                    potential_sum += potential_2d((x_, 0), (tip + x_move, z_0_1D_cms))  # i번째 그래핀 원자와 팁원자(0, 0, z)간의 potential을 함수로 구해서 누적
            potential_sums.append(potential_sum)
        difference = max(potential_sums) - min(potential_sums)
        max_index = np.argmax(potential_sums)
        min_index = np.argmin(potential_sums)
        ax_sum_x.append(atom_n)
        ax_sum_y.append(difference)
        print(f"atom number = {atom_n}, max = {max(potential_sums)}, {max_index}, min = {min(potential_sums)}, {min_index}, difference = {difference}")
    ax_sum.plot(ax_sum_x, ax_sum_y, linestyle = '--', marker = 'o', color=color)
    ax_sum.set_xticks([round(x, 3) for x in ax_sum_x])
    axes[remain].plot(ax_sum_x, ax_sum_y, linestyle = '--', marker = 'o', color=color)
    axes[remain].set_xticks([round(x, 3) for x in ax_sum_x])
    axes[remain].set_yticks([round(x, 5) for x in set(ax_sum_y)])

print()

fig.tight_layout()
plt.show()
