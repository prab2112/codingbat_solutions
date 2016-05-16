def sum67(nums):
  sum = 0
  check = True
  for i in range(len(nums)):
    if(nums[i]==6):
      check = False
    #i=i+1
    if(check):
      sum += nums[i]
    if(nums[i]==7):
      check = True
  return sum
