import numpy as np
import matplotlib.pyplot as plt

# 여러 변수
lattice = 3
tip_lattice = 2

atom_base = 50
tip_base = 30

atom_N_cms = 4  # 계산할 원자개수
z_0 = 0

graph_column = int(np.ceil(atom_N_cms / 2)) + 1

plt.rcParams.update({'font.size': 15})
fig = plt.figure(figsize=(15, 7.5))

# 일단 그림
ax0 = fig.add_subplot(2, graph_column, 1, title="1D")
ax0.xaxis.set_visible(False)
ax0.yaxis.set_visible(False)
ax0.spines['left'].set_color('none')
ax0.spines['right'].set_color('none')
ax0.spines['top'].set_color('none')
ax0.spines['bottom'].set_color('none')
ax0.yaxis.tick_right()
ax0.tick_params(axis='y', colors='none')
ax0.xaxis.tick_bottom()

# 각 원자별 그래프
axes = []
for n in range(atom_N_cms):
    if n < graph_column - 1:
        ax = fig.add_subplot(2, graph_column, n + 2, title=f'{n + 1}th atom')
    else:
        ax = fig.add_subplot(2, graph_column, n + 3, title=f'{n + 1}th atom')
    ax.xaxis.set_visible(True)
    ax.yaxis.set_visible(True)
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    # ax.tick_params(axis='y', colors='none')
    ax.xaxis.tick_bottom()
    ax.grid()
    ax.set_xticks([0, lattice/3, lattice/3*2, lattice])
    ax.set_yticks([1, 0])
    axes.append(ax)

# ax_sum 그리기
ax_sum = fig.add_subplot(2, graph_column, graph_column + 1, title=f"sum graph ({1}~{atom_N_cms})")
ax_sum.xaxis.set_visible(True)
ax_sum.yaxis.set_visible(True)
ax_sum.spines['left'].set_color('none')
ax_sum.spines['right'].set_color('none')
ax_sum.spines['top'].set_color('none')
ax_sum.spines['bottom'].set_color('none')
# ax_sum.yaxis.tick_right()
# ax_sum.tick_params(axis='y', colors='none')
ax_sum.xaxis.tick_bottom()
ax_sum.grid()

# ax0 그리기
radius_tip = (atom_N_cms - 1) / 2 * tip_lattice + 0.01
ax_limit = round(radius_tip * 1.2 + lattice)
ax0.axis('equal')
ax0.set_xlim(-lattice*1.2, ax_limit * 2 - lattice*1.2)

# 좌표 베이스
atom_base = [x * s for s in (1, -1) for x in np.arange(lattice / 2, atom_base, lattice)]

# 1D 그리기
ax0.scatter(atom_base, [0 for x in atom_base], c='k', s=50)

# 팁 원자 베이스
tip_base_list = [x * s for s in (1, -1) for x in np.arange(tip_lattice, tip_base, tip_lattice)]
tip_base_list.insert(0, 0.0)

# ax0 팁 그리기
# ax0.scatter(tip_base_list, [z_0 for x in tip_base_list], c='pink', s=10, marker='o', alpha=0.5)  # 분홍
tip_base_list_in = [x for x in tip_base_list[0:atom_N_cms]]
ax0.scatter(tip_base_list_in, [z_0 for x in tip_base_list_in], c='r', s=50, marker='o')  # 빨강

# 빨간점 위치 그리기 (위에서 이동됨)
ax0.set_xticks(tip_base_list_in)
# for txt in tip_base_list_in:
#     ax0.text(txt, 1.1*z_0, f'{txt}', verticalalignment='bottom')

# 합 리스트
x_cut = 10000
ax_sum_x = [x for x in np.linspace(0, lattice, x_cut)]
ax_sum_y = [0.0 for x in np.linspace(0, lattice, x_cut)]

for n in range(atom_N_cms):
    x_ = np.linspace(0, lattice, x_cut)
    x_cal = np.array([x - lattice/4 - n*(lattice-tip_lattice) for x in x_])
    y_ = np.sin(2*np.pi/lattice * x_cal)/2+0.5
    axes[n].plot(x_, y_, linestyle='-', marker='', linewidth=5)
    ax_sum_y += y_

ax_sum.plot(ax_sum_x, ax_sum_y, linestyle='-', marker='', linewidth=5)
if max(ax_sum_y) - min(ax_sum_y) < 0.00001:
    ax_sum.set_ylim(-1, 1)
# ax_sum.text(0.0, (max(ax_sum_y) + min(ax_sum_y)) / 2, f'potential barrier\n{max(ax_sum_y) - min(ax_sum_y)}', horizontalalignment='left', verticalalignment='center')
ax_sum.set_xticks([0, lattice/3, lattice/3*2, lattice])
ax_sum.set_yticks([round(max(ax_sum_y), 2), round(min(ax_sum_y), 2)])

# plt.tight_layout()
plt.show()
