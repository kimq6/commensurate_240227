import numpy as np
import matplotlib.pyplot as plt
import save_graph

fig = plt.figure(figsize=(15, 7.5))
ax0 = fig.add_subplot(241, title="1D commensurate")
# plt.grid(axis='x')
ax1 = fig.add_subplot(242, title="1D incommensurate")
# plt.grid(axis='x')
ax2 = fig.add_subplot(243, title="2D commensurate")
ax3 = fig.add_subplot(244, title="2D incommensurate")
ax4 = fig.add_subplot(245, title="1D commensurate")
# plt.grid()
ax5 = fig.add_subplot(246, title="1D incommensurate")
# plt.grid()
ax6 = fig.add_subplot(247, title="2D commensurate")
ax7 = fig.add_subplot(248, title="2D incommensurate")

# 여러 변수들, 단위 [Å]
lattice = 2
cms_lattice = 1.5
inc_lattice = 1.25
atom_limit = 100
create_base_cms = 10  # 팁 원자를 얼마나 생성, 계산할지(cms)
create_base_inc = 10  # 팁 원자를 얼마나 생성, 계산할지(inc)

# 코드 실행 여부 결정
do_1D_cms = 0
do_1D_inc = 0
do_2D_cms = 1

# 시그마 값
sigma_2d = 7
sigma_3d = 3.5

ax_limit = 15  # 그래프 확대 (보여주기)
radius_cms = 10  # tip 원 반지름(cms) (보여주기)
radius_inc = 10  # tip 원 반지름(inc) (보여주기)

for n in range(0,4):
    exec(f'ax{n}.set_xlim(-ax_limit, ax_limit)')
    exec(f'ax{n}.set_ylim(-ax_limit, ax_limit)')
    exec(f'ax{n}.set_aspect("equal")')

# 격자 그리기 (파악하기 쉽게)
ax0.set_xticks([x * s for s in (1, -1) for x in np.arange(0, ax_limit, cms_lattice)])
ax1.set_xticks([x * s for s in (1, -1) for x in np.arange(0, ax_limit, inc_lattice)])

# 좌표 베이스
atom_base = [x * s for s in (1, -1) for x in np.arange(lattice / 2, atom_limit, lattice)]

# 1D 그리기
ax0.scatter(atom_base, [0 for x in atom_base], c='k', s=3)
# ax0.axis('off')

ax1.scatter(atom_base, [0 for x in atom_base], c='k', s=3)
# ax1.axis('off')

# 2D 그리기
atom_x_mesh, atom_y_mesh = np.meshgrid(atom_base, atom_base)

ax2.scatter(atom_x_mesh, atom_y_mesh, c='k', s=3)
# ax2.axis('off')

ax3.scatter(atom_x_mesh, atom_y_mesh, c='k', s=3)
# ax3.axis('off')

# 팁 원자 베이스(commensurate)
tip_base_cms = [x * s for x in np.arange(cms_lattice, create_base_cms, cms_lattice) for s in (1, -1)]
tip_base_cms.insert(0, 0.0)

# 팁 원자 베이스(incommensurate)
tip_base_inc = [x * s for x in np.arange(inc_lattice, create_base_inc, inc_lattice) for s in (1, -1)]
tip_base_inc.insert(0, 0.0)

# ax0 팁 그리기
ax0.scatter(tip_base_cms, [0 for x in tip_base_cms], c='pink', s=10, marker='o', alpha=0.5)  # 분홍
tip_base_cms_in = [x for x in tip_base_cms if abs(x) < radius_cms]
ax0.scatter(tip_base_cms_in, [0 for x in tip_base_cms_in], c='r', s=10, marker='o')  # 빨강

# ax1 팁 그리기
ax1.scatter(tip_base_inc, [0 for x in tip_base_inc], c='pink', s=10, marker='o', alpha=0.5)  # 분홍
tip_base_inc_in = [x for x in tip_base_inc if abs(x) < radius_inc]
ax1.scatter(tip_base_inc_in, [0 for x in tip_base_inc_in], c='r', s=10, marker='o')  # 빨강

# 2D mesh생성(commensurate)
tip_x_cms_mesh, tip_y_cms_mesh = np.meshgrid(tip_base_cms, tip_base_cms)
# 변형이 편한 list 형태로 바꾸기
# tip_x_cms_mesh = [list(x) for x in tip_x_cms_mesh]
# tip_y_cms_mesh = [list(x) for x in tip_y_cms_mesh]

# ax2 팁 그리기(분홍) (tip_mesh를 한번만 쓰고 변경하기 때문에 미리 그린다.)
ax2.scatter(tip_x_cms_mesh, tip_y_cms_mesh, c='pink', s=10, marker='o', alpha=0.5)

# 원 안의 좌표만 고르기
tip_cms_mesh_distance = np.sqrt(np.power(tip_x_cms_mesh, 2) + np.power(tip_y_cms_mesh, 2))
tip_cms_mesh_in = tip_cms_mesh_distance.copy()
tip_cms_mesh_out = tip_cms_mesh_distance.copy()

for x in range(len(tip_base_cms)):
    for y in range(len(tip_base_cms)):
        if tip_cms_mesh_distance[x, y] > radius_cms:
            tip_x_cms_mesh[x][y] = np.NaN
            tip_y_cms_mesh[x][y] = np.NaN

# ax2 팁 그리기(빨강)
ax2.scatter(tip_x_cms_mesh, tip_y_cms_mesh, c='r', s=10, marker='o')

# 2D mesh 생성(incommensurate)
tip_x_inc_mesh, tip_y_inc_mesh = np.meshgrid(tip_base_inc, tip_base_inc)
# 변형이 편한 list 형태로 바꾸기
# tip_x_inc_mesh = [list(x) for x in tip_x_inc_mesh]
# tip_y_inc_mesh = [list(x) for x in tip_y_inc_mesh]

# ax3 팁 그리기(분홍) (tip_mesh를 한번만 쓰고 변경하기 때문에 미리 그린다.)
ax3.scatter(tip_x_inc_mesh, tip_y_inc_mesh, c='pink', s=10, marker='o', alpha=0.5)

# 원 안의 좌표만 고르기
tip_inc_mesh_distance = np.sqrt(np.power(tip_x_inc_mesh, 2) + np.power(tip_y_inc_mesh, 2))

for x in range(len(tip_base_inc)):
    for y in range(len(tip_base_inc)):
        if tip_inc_mesh_distance[x, y] > radius_inc:
            tip_x_inc_mesh[x][y] = np.NaN
            tip_y_inc_mesh[x][y] = np.NaN

# ax3 팁 그리기(빨강)
ax3.scatter(tip_x_inc_mesh, tip_y_inc_mesh, c='r', s=10, marker='o')

# mesh한 원자 좌표 보기 편하게(순서쌍으로) 바꾸기(1D)
atom_x = []  # 원자 좌표가 보기 편한 [(x1,0), (x2,0), ...]형태로 되어있음
for x in atom_base:
    atom_x.append((x, 0))

# mesh한 원자 좌표 보기 편하게(순서쌍으로) 바꾸기(2D)
atom_xy = []  # 원자 좌표가 보기 편한 [(x1,y1), (x2,y2), ...]형태로 되어있음
for x in atom_base:
    for y in atom_base:
        atom_xy.append((x, y))

# 계산하는 tip원자 순서쌍으로 구하기(2D cms)
tip_x_cms_list = [y for x in tip_x_cms_mesh for y in x]
tip_y_cms_list = [y for x in tip_y_cms_mesh for y in x]
tip_xy_cms_list = list(zip(tip_x_cms_list, tip_y_cms_list))
# NaN값 없애기
tip_xy_cms_list_unduplicate = [x for x in tip_xy_cms_list if not np.isnan(x[0])]  # [(x1,y1),(x2,y2),...]
# scatter 가능한 형태로 tip_x_y_cms_list[0]이 x좌표 모음, tip_x_y_cms_list[1]이 y좌표 모음이다.
tip_x_y_cms_list = list(zip(*tip_xy_cms_list_unduplicate))  # [(x1,x2,x3,...)(y1,y2,y3,...)]

# 계산하는 tip원자 순서쌍으로 구하기(2D inc)
tip_x_inc_list = [y for x in tip_x_inc_mesh for y in x]
tip_y_inc_list = [y for x in tip_y_inc_mesh for y in x]
tip_xy_inc_list = list(zip(tip_x_inc_list, tip_y_inc_list))
# NaN값 없애기
tip_xy_inc_list_unduplicate = [x for x in tip_xy_inc_list if not np.isnan(x[0])]  # [(x1,y1),(x2,y2),...]
# scatter 가능한 형태로 tip_x_y_inc_list[0]이 x좌표 모음, tip_x_y_inc_list[1]이 y좌표 모음이다.
tip_x_y_inc_list = list(zip(*tip_xy_inc_list_unduplicate))  # [(x1,x2,x3,...)(y1,y2,y3,...)]


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

if do_1D_cms == 1:
    # 아니 이걸 반복하라고?
    print(f'1D commensurate', end=" >> ")
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

    ax4_x = []
    ax4_y = []
    for atom_n in range(1, len(tip_base_cms) + 1, 1):
        tip_cms_in = tip_base_cms[0:atom_n]  # 안에 있는 원자들만 고르기
        potential_sums = []
        for x_move in np.arange(0, lattice, 0.01):  # 옆으로 조금씩 움직이면서 반복
            potential_sum = 0  # potential 합 초기화
            for tip in tip_cms_in:  # tip의 좌표들
                for x_ in atom_base:  # 원자의 좌표들
                    potential_sum += potential_2d((x_, 0), (tip + x_move, z_0_1D_cms))  # i번째 그래핀 원자와 팁원자(0, 0, z)간의 potential을 함수로 구해서 누적
            potential_sums.append(potential_sum)
        difference = max(potential_sums) - min(potential_sums)
        max_index = np.argmax(potential_sums)
        min_index = np.argmin(potential_sums)
        ax4_x.append(atom_n)
        ax4_y.append(difference)
        print(f"atom number = {atom_n}, max = {max(potential_sums)}, {max_index}, min = {min(potential_sums)}, {min_index}, difference = {difference}")
    ax4.plot(ax4_x, ax4_y, linestyle = '--', marker = 'o')
    ax4.set_xticks([round(x, 3) for x in ax4_x])
    ax4.set_yticks([round(x, 3) for x in ax4_y])
    # ax4.yaxis.set_tick_params(horizontalalignment='center')
    print(ax4_x)
    print(ax4_y)

print()

if do_1D_inc == 1:
    # inc
    print(f'1D incommensurate', end=" >> ")
    z_0_1D_inc = 0  # potential 합이 최소일 때 z값 저장할곳
    potential_0_1D_inc = 100000
    for z_ in np.arange(3.5, 3.7, 0.001):  # 이 범위에서 z반복
        potential_sum = 0
        for tip in tip_base_inc:
            for x_ in atom_base:
                potential_sum += potential_2d((x_, 0), (tip, z_))
        if potential_0_1D_inc > potential_sum:
            z_0_1D_inc = z_
            potential_0_1D_inc = potential_sum
    print(f'z0 = {z_0_1D_inc}')

    ax5_x = []
    ax5_y = []
    for atom_n in range(1, len(tip_base_inc) + 1):
        tip_inc_in = tip_base_inc[0:atom_n]  # 안에 있는 원자들만 고르기
        potential_sums = []
        for x_move in np.arange(0, lattice, 0.01):  # 옆으로 조금씩 움직이면서 반복
            potential_sum = 0.0  # potential 합 초기화
            for tip in tip_inc_in:  # tip의 좌표들
                for x_ in atom_base:  # 원자의 좌표들
                    potential_sum += potential_2d((x_, 0), (tip + x_move, z_0_1D_inc))  # i번째 그래핀 원자와 팁원자(0, 0, z)간의 potential을 함수로 구해서 누적
            potential_sums.append(potential_sum)
        difference = max(potential_sums) - min(potential_sums)
        max_index = np.argmax(potential_sums)
        min_index = np.argmin(potential_sums)
        ax5_x.append(atom_n)
        ax5_y.append(difference)
        print(f"atom number = {atom_n}, max = {max(potential_sums)}, {max_index}, min = {min(potential_sums)}, {min_index}, difference = {difference}")
    ax5.plot(ax5_x, ax5_y, linestyle = '--', marker = 'o')
    ax5.set_xticks([round(x, 3) for x in ax5_x])
    ax5.set_yticks([round(x, 3) for x in set(ax5_y)])
    print(ax5_x)
    print(ax5_y)

print()

# 2D 그래프
if do_2D_cms == 1:
    # 2D commensurate
    ax6_x = []  # 반지름
    ax6_y = []  # barrier
    z_0_2D_cms = 0  # z0 저장
    potential_0_2D_cms = 100000  # potential 저장
    # 일단 최대 반지름에 대해 z0
    for z_ in np.arange(3.42, 3.44, 0.001):
        print(round(z_, 4))
        potential_sum = 0  # potential 초기화
        # mesh 생성
        tip_x_mesh, tip_y_mesh = np.meshgrid(tip_base_cms, tip_base_cms)
        # 원 안의 좌표 거리
        tip_mesh_distance = np.sqrt(np.power(tip_x_mesh, 2) + np.power(tip_y_mesh, 2))
        # 원 밖의 좌표는 0으로
        tip_x_mesh[tip_mesh_distance > create_base_cms] = 0
        tip_y_mesh[tip_mesh_distance > create_base_cms] = 0
        for x_ in range(len(tip_x_mesh)):
            for y_ in range(len(tip_y_mesh)):
                for atom in atom_xy:
                    potential_sum += potential_3d((atom[0], atom[1], 0), (tip_x_mesh[x_, y_], tip_y_mesh[x_, y_], z_))
        if potential_0_2D_cms > potential_sum:
            z_0_2D_cms = z_
            potential_0_2D_cms = potential_sum
    print(f"z_0_2D_cms = {z_0_2D_cms}, potential = {potential_0_2D_cms}")

    # 나눌 정도
    div = 10
    # 이동할 격자(2x2)
    tip_move = np.linspace(0, lattice, div)
    tip_move_x, tip_move_y = np.meshgrid(tip_move, tip_move)
    
    # 반지름에 대해 tip 안의 원자만 고르고
    for radius in range(1, create_base_cms, 1):
        # mesh 생성
        tip_x_mesh, tip_y_mesh = np.meshgrid(tip_base_cms, tip_base_cms)
        # 원 안의 좌표 거리
        tip_mesh_distance = np.sqrt(np.power(tip_x_mesh, 2) + np.power(tip_y_mesh, 2))
        # 원 밖의 좌표는 0으로
        tip_x_mesh[tip_mesh_distance > radius] = 0
        tip_y_mesh[tip_mesh_distance > radius] = 0
        for x_ in range(len(tip_x_mesh)):
            for y_ in range(len(tip_y_mesh)):
                if tip_x_mesh[x_, y_] and tip_y_mesh[x_, y_] != 0:
                    potential_3d


# lattice 정사각형만큼 움직였을 때에 대해 퍼텐셜을 구하기
# tip 좌표에 대해, xy좌표에 대해 합을 저장
# 값을 저장
# 그래프 그리기

fig.tight_layout()
save_graph.save_graph(f'main_{sigma_2d}σ, {lattice}-{inc_lattice}')
plt.show()
