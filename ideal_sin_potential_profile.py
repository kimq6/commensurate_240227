import numpy as np
import matplotlib.pyplot as plt

# 여러 변수
lattice = 2
tip_lattice = 1.5
atom_N_cms = 1  # 계산할 원자개수

graph_column = int(np.ceil(atom_N_cms / 2)) + 1
print(f'asdf {graph_column}')

fig = plt.figure(figsize=(15, 7.5))
# 일단 그림
ax0 = fig.add_subplot(2, graph_column, 1, title="1D")

# 각 원자별 그래프
axes = []
for n in range(atom_N_cms):
    if n < graph_column - 1:
        ax = fig.add_subplot(2, graph_column, n + 2, title=f'{n + 1}th atom')
    else:
        ax = fig.add_subplot(2, graph_column, n + 3, title=f'{n + 1}th atom')
    axes.append(ax)

# axes[0] sin 만들기
x_1 = np.linspace(0, 2, 100)
y_1 = np.sin(np.pi*x_1)

axes[0].plot(x_1, y_1, linestyle=' ', marker='.')
axes[0].set_xlabel('x')
axes[0].set_ylabel('sin(x)')
axes[0].set_title('Sine Function')

plt.show()
