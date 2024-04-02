
## main.py

1차원 commensurate, 1차원 incommensurate, 2차원 commensurate, 2차원 incommensurate 할 때의 원자 배치 그림과 원자 개수(반지름)(x축), potential barrier(y축)의 그래프를 그림
(2d incommensurate는 2d commensurate로 대체 가능해서 그래프 기능이 없다)

#### 변수 설명

+ lattice = 원자 lattice constant
+ cms_lattice = commensurate할 때의 tip lattice constant
+ inc_lattice = incommensurate할 때의 tip lattice constant
(사실상 cms나 inc나 계산은 똑같다. 이 값만 다를뿐.)
따라서 cms_lattice에 incommensurate한 값을 넣으면 incommensurate 결과를 얻을 수 있다.
+ atom_limit = 원자 생성 한계, 50이면 100*100 만큼의 네모 안에 원자를 생성한다는 소리
+ create_base_cms = tip 생성 한계(commensurate)
+ create_base_inc = tip 생성 한계(incommensurate)
+ x_cc = LJpotential에서 sigma랑 관련 있는 상수. 탄소-탄소끼리
+ d_cc = LJpotential에서 epsilon과 관련 있는 상수. 탄소-탄소끼리
+ sigma_2d, sigma_3d = cutoff, 계산할 원자로부터 관련된 거리보다 멀면 계산을 안 한다.
+ radius_cms, radius_inc = 보여주기용 tip 원 반지름
+ **cms_1D, inc_1D, cms_2D, inc_2D** = 각각의 코드를 실행할지 여부를 결정

- - - 

## profile_at_x+sum.py
sample lattice와 tip lattice를 설정해서 원자의 개수에 따른 potential profile을 원자 하나하나를 더해서 보여준다.

#### 변수
+ atom_lattice = sample 간격
+ tip_lattice = tip 간격
+ atom_limit = sample 생성 반경
+ create_base = tip 생성 반경
+ atom_N = tip 원자 개수

- - -

## draw_by_radius.py
sample lattice와 tip lattice를 설정하고, radius(원 반지름)안에 있는 tip 원자를 시각화해준다.

#### 변수
+ atom_lattice = sample 간격
+ tip_lattice = tip 간격
+ radius_multiple = lattice의 배수역할... radius 식을 보면 이해됨
+ radius = 원 반지름

- - -

## ideal_main.py
ideal한 sin함수의 합으로 1차원 potential barrier를 구해서 표시한 것.

#### 변수
+ lattice = sample lattice
+ tip_lattice = tip lattice
+ atom_N_cms = 계산할 원자 개수
+ ax1_option = 0이면 원자 개수에 따라 그리기, 1이면 cycle마다 건너뛰어서 색상 다르게 해서 연결하기. cycle이 적당한 배수면 각 색상 그래프는 일자로 그려진다.
+ cycle 원자 개수를 나누는 정도, 4인 경우 원자 개수가 (1,5,9,13...), (2,6,10,14...), (3,7,11,15...), (4.8.12.16...)끼리 묶는다

- - -

## ideal_sin_potential_profile.py
profile_at_x+sum.py의 ideal한 버전. 원자 배치와 각 atom의 profile이 나오고 그것의 합이 왼쪽아래 그래프에 있다.

#### 변수
+ lattice = sample lattice
+ tip_lattice = tip lattice
+ atom_N_cms = 계산할 원자 개수
+ z_0 = 왼쪽 위의 그림 보기 좋게 하려고 넣은거

- - -

## draw.py
main.py의 그림에서 원자 배치를 그린 부분만 따온것.