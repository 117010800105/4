import random
a="113"
c=0
for i in range(10000):
    b=random.sample(a,1)
    if b ==['1']:
        c=c+1
d=c/10000
print("更换{}%".format(d*100))
c=0
for i in range(10000):
    b=random.sample(a,1)
    if b ==['3']:
        c=c+1
d=c/10000
print("不更换{}%".format(d*100))

    

# 判断素数
n = int(input("输入一个正整数："))
f = 1
for i in range(2,n):
    if n%i == 0:
        f = 0
        break
if f == 1:
    print("{}是素数".format(n))
else:
    print("{}不是素数".format(n))
