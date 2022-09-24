col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':  # matrix요소값이 *일 경우, 지뢰이므로 통과
            continue
        else:
            matrix[i][j] = 0   # 각 요소 자리 별로 카운트 초기값 세팅
            for y in range(i - 1, i + 2):  # 윗 행과 아랫 행을 검색
                for x in range(j - 1, j + 2): # 왼쪽 열과 오른쪽 열을 검색
                    if y < 0 or x < 0 or y >= row or x >= col: # 정해준 행렬 범위 벗어 나면 통과
                        continue
                    elif matrix[y][x] == '*':
                        matrix[i][j] += 1

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='')
    print()


