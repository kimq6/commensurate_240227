import matplotlib.pyplot as plt

plt.figure(figsize=(15, 7.5))

# 임의의 리스트 생성
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 그래프 그리기
plt.plot(x, y)
plt.title('omo')  # 그래프 제목 설정
plt.xlabel('x')  # x축 레이블 설정
plt.ylabel('y')  # y축 레이블 설정
plt.xticks(x)  # x축 눈금 설정
plt.yticks(y)  # y축 눈금 설정
plt.grid(True)  # 그리드 표시
plt.show()  # 그래프 보여주기
