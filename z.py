import matplotlib.pyplot as plt

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# ddd
plt.plot(x, y)

# 그래프 제목 및 축 레이블 추가
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 그래프 보이기
plt.show()
