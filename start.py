import math

def calc(a,b,x):
    y = 1 + math.log10(x/a)**2/(b - math.exp(x/a))
    return y

def task_a(a,b,xn,xk,dx):
    x = xn
    res = []
    while x<=xk:
        y=calc(a,b,x) 
        res.append((x,y))
        x += dx
    return res 
def print_res(res):
  for item in res:
    x,y = item
    print(f"x={x} y={y}")

res = task_a(a,b,1.1,3.6,0.5)   
for item in res:
    x,y = item
    print(f"x={x} y={y}")

def task_b(a,b,i):
    res = [] 
    for x_item in i:
        y=calc(a,b,x_item)
        res.append ((x_item, y))
    return res
if __name__ == "__main__":
    a = 2.5
    b = 4.6
    res = task_a(a,b,1.1,3.6,0.5)
    print("Task A ------------")
    print_res(res)

    x_lst = [1.2, 1.28, 1.36, 1.46, 2.35] 
    res = task_b(a,b,x_lst)  

    print("Task B ------------")
    print_res(res)

    









