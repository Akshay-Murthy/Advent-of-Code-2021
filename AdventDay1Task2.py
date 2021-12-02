import sys
Numbers = []
Sums = [] 
Start = 0
End = 3
sys.stdin = open("AoCDec1+.txt", "r")
for i in range(2000):
   Numbers.append(int(input()))
for j in range(len(Numbers)):
    Sums.append(sum(Numbers[Start:End]))
    Start += 1 
    End += 1
Sums.pop(-1)
Sums.pop(len(Sums) - 1)
count = 0 
for urmom in range(len(Sums)):
    if urmom > 0:
        if Sums[urmom] > Sums[urmom - 1]:
            count += 1
print(count)
