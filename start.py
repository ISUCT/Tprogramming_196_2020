import math

def calc(x):
    y = (math.fabs(x**2 - 2.5))**(1/4) + (math.log10(x**2))**(1/3)
    return y

def task_a(xn,xk,dx):
    x = xn
    res = []
    while x<=xk:
        y = calc(x)
        res.append((x, y))
        x += dx
    return res

def task_b(x):
    res = []
    for x_item in x:
        y = calc(x_item)
        res.append((x_item, y))
    return res

def print_res(res):
    for item in res:
        x,y = item
        print(f"x={x} y={y}")


if __name__ == "__main__":
    res = task_a(1.1,3.6,0.5)
    print("Task A ------------")
    print_res(res)

    x_lst = [1.2, 1.28, 1.36, 1.46, 2.35]
    res = task_b(x_lst)

    print("Task B ------------")
    print_res(res)