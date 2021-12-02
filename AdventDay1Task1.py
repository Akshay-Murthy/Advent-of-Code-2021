import sys
sys.stdin = open("AoCDec1.txt", "r")
count = 0
Numbers = []
for i in range(2000):
    Numbers.append(int(input()))
print(len(Numbers))
for j in range(len(Numbers)):
    if j > 0:
        if Numbers[j] > Numbers[j - 1]:
            count += 1 
print(count)
