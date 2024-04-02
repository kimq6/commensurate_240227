import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure(figsize=(15, 7.5))
ax0 = fig.add_subplot(111)

atom_lattice = 2
tip_lattice = 1.5
atom_limit = 100  # 그냥 radius보다 충분히 큰 숫자
radius_multiple = 14
radius = tip_lattice * radius_multiple  # tip 원 반지름

# 그래프 확대
ax_limit = (radius + atom_lattice) * 1.2
ax0.set_xlim(-ax_limit, ax_limit)
ax0.set_ylim(-ax_limit, ax_limit)
ax0.set_aspect('equal')

# atom 좌표 베이스
atom_base = [x * s for s in (1, -1) for x in np.arange(atom_lattice / 2, atom_limit, atom_lattice)]

# tip 좌표 베이스
tip_base = [x * s for s in (1, -1) for x in np.arange(tip_lattice, atom_limit, tip_lattice)]
tip_base.insert(0, 0.0)  # tip 중심

# 2D atom mesh
atom_x_mesh, atom_y_mesh = np.meshgrid(atom_base, atom_base)
ax0.scatter(atom_x_mesh, atom_y_mesh, c='k', s=3)

# 2D tip mesh
tip_x_mesh, tip_y_mesh = np.meshgrid(tip_base, tip_base)

# ax2 팁 그리기(분홍) (tip_mesh를 한번만 쓰고 변경하기 때문에 미리 그린다.)
ax0.scatter(tip_x_mesh, tip_y_mesh, c='pink', s=10, marker='o', alpha=0.5)

# 원 안의 좌표만 고르기
tip_cms_mesh_distance = np.sqrt(np.power(tip_x_mesh, 2) + np.power(tip_y_mesh, 2))  # 원점으로부터의 거리를 계산한 행렬

# 원 밖의 좌표는 NaN으로 바꾸기
for x in range(len(tip_base)):
    for y in range(len(tip_base)):
        if tip_cms_mesh_distance[x, y] > radius:
            tip_x_mesh[x][y] = np.NaN
            tip_y_mesh[x][y] = np.NaN

# ax2 팁 그리기(빨강)
ax0.scatter(tip_x_mesh, tip_y_mesh, c='r', s=10, marker='o')

tip_circle = patches.Circle((0, 0), radius, color='r', fill=False)
ax0.add_patch(tip_circle)

# 계산하는 tip원자 순서쌍으로 구하기
tip_x_list = [y for x in tip_x_mesh for y in x]
tip_y_list = [y for x in tip_y_mesh for y in x]
tip_xy_list = list(zip(tip_x_list, tip_y_list))
# NaN값 없애기
tip_xy_list_unduplicate = [x for x in tip_xy_list if not np.isnan(x[0])]  # [(x1,y1),(x2,y2),...]
print(len(tip_xy_list_unduplicate))

ax0.set_title(f'2D atom and tip\natom = {atom_lattice}, tip = {tip_lattice}, radius = {radius}, atom number = {len(tip_xy_list_unduplicate)}')

plt.show()
