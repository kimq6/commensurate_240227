import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# 초기 설정
atom_lattice = 4  # atom_lattice 값 수정
tip_lattice = 3.839 # tip_lattice 값 수정
atom_limit = 200  # radius_multiple와 tip_lattice 곱보다 큰 숫자
radiuses = np.arange(0, atom_limit, tip_lattice)  # 반지름을 1부터 n까지 변화시킬 예정, 원하는 반지름은 수정가능

# 함수 정의
def potential_at_xy(x, y, B, λ):
    return B * (np.cos(np.pi * 2 * x / λ) + np.cos(np.pi * 2 * y / λ))


B = 1/4  # 적절한 B 값 설정
λ = atom_lattice

potential_barrier = []  # 각 반경에서의 최대-최소 잠재 에너지를 저장할 리스트

# tip 좌표 베이스 계산
base = [x * s for x in np.arange(tip_lattice, atom_limit, tip_lattice) for s in (1, -1)]
base.insert(0, 0.0)  # tip 중심 추가
tip_base = [(x, y) for x in base for y in base]

# 반지름별 최대-최소 잠재 에너지 계산
for radius in tqdm(radiuses, desc='Calculating max-min potentials'):
    max_z_value_sum = 0.0  # 최대값 초기화
    min_z_value_sum = 0.0  # 최소값 초기화

    # potential_sum을 저장하기 위한 리스트. 이 리스트의 값들 중에서 최대값과 최소값을 구한다. 이 리스트의 요소는 tip이 (x_move, y_move)만큼 이동했을 때의 tip potential의 합이다.
    potential_sums = []  # 초기화
    for x_move in np.arange(0, atom_lattice, 0.1):
        for y_move in np.arange(0, atom_lattice, 0.1):
            # radius 안에 속해 있는 원자에 대해 중심이 (0,0)에서 potential 합 구하고 초기화, (0,0.1)에서 합 구하고 초기화, ... (atom_lattice,atom_lattice)에서 합 구하고 초기화 용도
            potential_sum = 0.0
            for x, y in tip_base:
                limit = radius + 0.01
                if np.abs(x) <= limit and np.abs(y) <= limit:  # 만약 tip 원자가 사각형 변의 반 안에 속해 있다면
                    potential_sum += potential_at_xy(x + x_move, y + y_move, B, λ)  # potential_sum에 해당 tip 원자의 potential을 더한다.
            potential_sums.append(potential_sum)  # potential_sums에 potential_sum을 추가한다.
    
    # 최댓값과 최솟값을 계산합니다.
    max_z_value_sum = max(potential_sums)  # potential_sums의 최대값을 max_z_value_sum에 저장
    min_z_value_sum = min(potential_sums)  # potential_sums의 최소값을 min_z_value_sum에 저장

    potential_barrier.append(max_z_value_sum - min_z_value_sum)  # potential_barrier에 max_z_value_sum과 min_z_value_sum의 차이를 저장

# x축 깔끔하게 표시하기
# potential_barrier의 변화를 계산
changes = np.abs(np.diff(potential_barrier))
# 변화가 큰 임계값 설정
threshold = 0.02  # 이 값보다 더 큰 변화인 경우
# 변화가 임계값보다 큰 경우의 인덱스 찾기
large_change_indices = np.where(changes > threshold)[0]
# 해당하는 radiuses 값 추출
large_change_radiuses = [radiuses[i+1] for i in large_change_indices]
print(potential_barrier)
print(large_change_radiuses)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(radiuses, potential_barrier, marker='o')
plt.xlabel('Radius')
plt.ylabel('Max-Min Potential')
plt.xticks(large_change_radiuses)
plt.yticks(potential_barrier)
plt.title('Radius vs. Max-Min Potential')
plt.grid(True)
plt.show()


