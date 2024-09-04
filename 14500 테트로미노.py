
block = [ 
    [ (0,0), (0,1), (0,2), (0,3) ], # 길쭉한 가로.
    [ (0,0), (1,0), (2,0), (3,0) ], # 길쭉한 세로. 
    [ (0,0), (0,1), (1,0), (1,1) ], # 정사각형.
    [ (0,0), (1,0), (2,0), (2,1) ], # ㄴ자 1.
    [ (0,0), (1,0), (1,1), (1,2) ], # ㄴ자 2.
    [ (0,0), (1,0), (0,1), (0,2) ], # 역ㄱ자 1.
    [ (0,0), (1,0), (2,0), (0,1) ], # 역ㄱ자 2.
    [ (0,0), (0,1), (0,2), (1,2) ], # ㄱ자 1.
    [ (0,0), (0,1), (1,1), (2,1) ], # ㄱ자 2.
    [ (1,0), (1,1), (1,2), (0,2) ], # 역ㄴ자 1.
    [ (0,1), (1,1), (2,1), (2,0) ], # 역ㄴ자 2.
    [ (0,0), (1,0), (1,1), (2,1) ], # ㅢㅡ 모양.
    [ (0,1), (1,0), (1,1), (2,0) ], # ㅢㅡ 모양 반전.
    [ (0,1), (0,2), (1,0), (1,1) ], # ㅢㅡ 모양 90도.
    [ (0,0), (0,1), (1,1), (1,2) ], # ㅢㅡ 모양 90도 반전.
    [ (0,0), (0,1), (0,2), (1,1) ], # ㅜ 모양.
    [ (0,0), (1,0), (2,0), (1,1) ], # ㅏ 모양.
    [ (0,1), (1,0), (1,1), (1,2) ], # ㅗ 모양.
    [ (0,1), (1,1), (2,1), (1,0) ] # ㅓ 모양.
    ]

def BlockScan(grid, N, M, y, x):
  score = 0
  for bl in block: # 블럭 모양 총 19개. O(19)
    cnt = 0
    for ny, nx in bl: # 총 4칸 확인 O(4)
      ny = ny + y
      nx = nx + x
      if not (0 <= ny < N and 0 <= nx < M): 
        cnt = 0
        break
      cnt += grid[ny][nx]

    if cnt >= score:
      score = cnt
  
  return score


# 종이의 세로N 가로M. (4 ≤ N, M ≤ 500)
N, M = map(int, input().split())

grid = []
for _ in range(N):
  grid.append(list(map(int, input().split())))

max_score = 0
# O(N * M * 13 * 4)
for i in range(N):
  for j in range(M):
    block_score = BlockScan(grid, N, M, i, j)
    if max_score <= block_score:
      max_score = block_score

print(max_score)

# O(N * M)
