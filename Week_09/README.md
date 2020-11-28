学习笔记

不同路径2
> 因为机器人每次只能向下或者向右移动一步，因此从坐标 (0,0) 到坐标 (i,j) 的
>路径总数的值取决于从坐标 (0,0) 到坐标 (i - 1, j) 的路径总数和从坐标 (0, 0) 到坐标
>(i, j - 1) 的路径总数，即 f(i, j) 只能通过 f(i - 1, j) 和 f(i, j - 1) 转移得到。

>状态转移方程:
> 1. 如果 u(i, j) = 0, 那么 f(i, j) = 0
> 2. 如果 u(i, j) != 0, 那么 f(i, j) = f(i - 1, j) + f(i, j - 1)

```python

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    width = len(obstacleGrid[0])
    dp = [0 for _ in range(width)]
    dp[0] = 1

    for i in obstacleGrid:
        for j in range(width):
            if i[j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
    return dp[width - 1]

``` 