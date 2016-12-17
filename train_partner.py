#!/usr/bin/python
# By Arup Ghosh (17th Dec 2016)
# Problem : https://www.codechef.com/problems/ANKTRAIN
t = int(input())
ber = ["LB","MB","UB","LB","MB","UB","SL","SU"]
for i in range(t):
	n = int(input())
	x = (n-1)%8
	if 2 < x < 6:
		print str(n-3)+ber[x]
	if -1 < x < 3:
		print str(n+3)+ber[x]
	if x == 6:
		print str(n+1)+ber[-1]
	if x == 7:
		print str(n-1)+ber[-2]