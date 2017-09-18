def flatten(arr1):
    ans = []
  def helper(arr):
    for i in arr:
      if isinstance(i, list):
        helper(i)
      else:
        ans.append(i)
  helper(arr1)
  return ans
