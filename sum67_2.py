def sum67(nums):
	s=i=0
	while i < len(nums):
		if nums[i]!=6:
			s+=nums[i]
			i+=1
		else:
			while(nums[i]!=7):
				i+=1
			i+=1
	return s

print "sum67([1, 2, 2]) = ",sum67([1, 2, 2])
print "sum67([1, 2, 2, 6, 99, 99, 7])",sum67([1, 2, 2, 6, 99, 99, 7])
print "sum67([1, 1, 6, 7, 2])",sum67([1, 1, 6, 7, 2])
print "sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])",sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
print "sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])",sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])
print "sum67([2, 7, 6, 2, 6, 7, 2, 7])",sum67([2, 7, 6, 2, 6, 7, 2, 7])
print "sum67([2, 7, 6, 2, 6, 2, 7])",sum67([2, 7, 6, 2, 6, 2, 7])
print "sum67([1, 6, 7, 7])",sum67([1, 6, 7, 7])
print "sum67([6, 7, 1, 6, 7, 7])",sum67([6, 7, 1, 6, 7, 7])
print "sum67([6, 8, 1, 6, 7])",sum67([6, 8, 1, 6, 7])
print "sum67([])",sum67([])
print "sum67([6, 7, 11])",sum67([6, 7, 11])
print "sum67([11, 6, 7, 11])",sum67([11, 6, 7, 11])
print "sum67([2, 2, 6, 7, 7])",sum67([2, 2, 6, 7, 7])