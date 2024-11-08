import sys

number = int(sys.argv[1])

for i in range(1, number + 1):  # 1부터 number까지 반복
    if number % i == 0:  # 나머지가 0이면
        print(i, end=" ")  # 약수 출력
print()  # 마지막에 줄 바꿈 추가
