class Solution:
  def __init__(self):
    pass


  def numOfTrailingZeros(self, n):
      count = 0
      while n > 0 and n % 5 == 0:
        count += 1
        n //= 5
      return count


  def getMinimumTrailingZeros(self, mat):
      if not isinstance(mat, list):
        raise Exception("Could not process the data passed")
      
      foundZero = False
      matLen = len(mat)

      if matLen == 0:
        return -1

      dp = [[0] * matLen for _ in range(matLen)]
      dp[0][0] = self.numOfTrailingZeros(mat[0][0])

      for i in range(1, matLen):
        dp[i][0] = dp[i - 1][0] + self.numOfTrailingZeros(mat[i][0])
        dp[0][i] = dp[0][i - 1] + self.numOfTrailingZeros(mat[0][i])
          
      for i in range(1, matLen):
        for j in range(1, matLen):
          if (mat[i][j] == 0 or mat[j][i] == 0):
            foundZero = True
          from_top = dp[i - 1][j] + self.numOfTrailingZeros(mat[i][j])
          from_left = dp[i][j - 1] + self.numOfTrailingZeros(mat[j][i])
          dp[i][j] = min(from_top, from_left)
      
      return dp[matLen - 1][matLen - 1] if not foundZero else 1
  

  def getMinimumTrailingZerosPath(self, mat):
    pass



# Test case 1 ==> Expected result/answer is 1
# matrix = [
#     [2, 10, 1, 3],
#     [10, 5, 4, 5],
#     [2, 10, 2, 1],
#     [25, 2, 5, 1],
# ]

# Test case 2 ==> Expected result/answer is 2
# matrix = [
#     [10, 1, 10, 1],
#     [1, 1, 1, 10],
#     [10, 1, 10, 1],
#     [1, 10, 1, 1],
# ]

# Test case 3 ==> Expected result/answer is 1
# matrix = [
#   [10, 10, 10],
#   [10, 0, 10],
#   [10, 10, 10],
# ]

# Test case 4 ==> Expected result/answer is -1
matrix = []

classInstance = Solution()
print("the solution value is", classInstance.getMinimumTrailingZeros(matrix))