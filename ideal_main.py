import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 여러 변수
lattice = 2
tip_lattice = np.sqrt(2)

atom_N_cms = 100  # 계산할 원자개수(어디까지)

ax1_option = 0  # 0: 그냥 그리기, 1: 색상별로 그리기
cycle = 4  # ax1_option = 1일 때 색상 개수. 잘 나누면 일정한 값이 됨

plt.rcParams.update({'font.size': 24})
fig = plt.figure(figsize=(15, 7.5))
# 일단 그림
ax1 = fig.add_subplot(1, 1, 1, title=f"potential barrier - atom number / {lattice} : {tip_lattice}")

x_cut = 10000
ax1_x = []
ax1_y = []

print(lattice-tip_lattice)

for N_ in range(atom_N_cms):  # 계산할 원자수 인덱스 0, 1, 2, 3, 4에 대해
    sum_y = np.zeros(x_cut)  # potential profile 초기화
    for n in range(N_):  # 원자 1번에 대해 / 1, 2번에 대해 / 1, 2, 3번에 대해 / ...
        x_ = np.linspace(0, lattice, x_cut)  # [0, 0.01, 0.02, 0.03, ..., 2]
        x_cal = np.array([x - lattice/4 - n*(lattice-tip_lattice) for x in x_])  # [-1, -0.09, -0.08, ..., 1] 평행이동한거
        y_ = np.sin(2*np.pi/lattice * x_cal)/2  # [f(-1), f(-0.09), f(-0.08), ..., f(1)]
        sum_y += y_  # potential profile 누적
    potential_barrier = max(sum_y) - min(sum_y)
    ax1_x.append(N_)
    ax1_y.append(potential_barrier)
    print(f'{N_}th atom, potential barrier = {round(potential_barrier, 4)}')

if ax1_option == 1:
    cmap = cm.get_cmap('viridis', cycle)  # 7개의 색상을 가진 'viridis' colormap을 가져옵니다.
    for c in range(cycle):
        ax_x = [x for i, x in enumerate(ax1_x) if i % cycle == c]
        ax_y = [y for i, y in enumerate(ax1_y) if i % cycle == c]
        ax1.plot(ax_x, ax_y, linestyle='--', marker='.', color=cmap(c % cycle))
else:
    ax1.plot(ax1_x[1:], ax1_y[1:], linestyle='--', marker='o', markersize=10)

ax1.set_xlabel('atom number')
ax1.set_ylabel('potential barrier')
ax1.set_xticks(ax1_x)
ax1.set_yticks(ax1_y)

plt.tight_layout()
plt.show()
